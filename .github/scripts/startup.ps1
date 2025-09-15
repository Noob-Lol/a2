param(
    [string]$User,
    [string]$Pass,
    [string]$TsAuthKey,
    [string]$Hostname,
    [int]$RuntimeMinutes = 355
)

function Enable-RdpUser {
    param([string]$User,[string]$Pass)
    $sec = ConvertTo-SecureString $Pass -AsPlainText -Force
    if (-not (Get-LocalUser -Name $User -ErrorAction SilentlyContinue)) {
        New-LocalUser -Name $User -Password $sec -AccountNeverExpires
        Add-LocalGroupMember -Group Administrators -Member $User
        Add-LocalGroupMember -Group "Remote Desktop Users" -Member $User
    } else {
        Set-LocalUser -Name $User -Password $sec -AccountNeverExpires
        Enable-LocalUser -Name $User
    }
    Set-ItemProperty "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name fDenyTSConnections -Value 0
    Enable-NetFirewallRule -DisplayGroup "Remote Desktop" | Out-Null
}

function Enable-Audio {
    Start-Service -Name "Audiosrv" -ErrorAction SilentlyContinue
    Start-Service -Name "AudioEndpointBuilder" -ErrorAction SilentlyContinue
}

function Start-Tailscale {
    param([string]$AuthKey,[string]$Hostname)
    $ts = "C:\Program Files\Tailscale\tailscale.exe"
    if (-not (Test-Path $ts)) {
        $dst = "$env:TEMP\tailscale-setup.exe"
        Invoke-WebRequest 'https://pkgs.tailscale.com/stable/tailscale-setup-latest.exe' -OutFile $dst
        Start-Process -FilePath $dst -ArgumentList "/quiet" -Wait
    }
    Start-Service -Name Tailscale -ErrorAction SilentlyContinue
    & $ts logout | Out-Null
    & $ts up --authkey $AuthKey --hostname $Hostname --accept-routes --accept-dns=false
    Start-Sleep -Seconds 2
}

function Keep-Alive {
    param([int]$Minutes)
    $end=(Get-Date).AddMinutes($Minutes)
    while((Get-Date) -lt $end){
        $left=[int]([math]::Ceiling(($end-(Get-Date)).TotalMinutes))
        Write-Host "RDP alive... ($left min left)"
        Start-Sleep -Seconds 60
    }
}

Write-Host "=== Startup script running ==="
Enable-RdpUser -User $User -Pass $Pass
Enable-Audio
Start-Tailscale -AuthKey $TsAuthKey -Hostname $Hostname
Keep-Alive -Minutes $RuntimeMinutes
