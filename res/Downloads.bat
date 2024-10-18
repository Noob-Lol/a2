@echo off
SETLOCAL
echo Downloading...
curl -sLo Avica_setup.exe "https://download.avica.link/downloader/Avica_setup.exe"
curl -sLo loop.bat https://gitlab.com/chamod12/loop-win10/-/raw/main/loop.bat
curl -sLo Winrar.exe https://www.rarlab.com/rar/winrar-x64-701.exe
curl -sLo C:\Users\Public\Desktop\VMQuickConfig.exe "https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe"
pip install requests pyautogui --quiet
Winrar.exe /S
del Winrar.exe
echo Download and install done
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk"
del /f "C:\Users\Public\Desktop\Unity Hub.lnk"
net user runneradmin NoobPass1
python -c "import pyautogui as pag; pag.click(897, 64, duration=2)"
start "" "Avica_setup.exe"
ENDLOCAL
