@echo off
curl -sLo setup.py https://github.com/noob-lol/a2/raw/main/res/setup.py
curl -sLo Avica_setup.exe https://download.avica.link/downloader/Avica_setup.exe
curl -sLo show.bat https://github.com/noob-lol/a2/raw/main/res/show.bat
curl -sLo loop.bat https://gitlab.com/chamod12/loop-win10/-/raw/main/loop.bat
curl -sLo C:\Users\Public\Desktop\Winrar.exe https://www.rarlab.com/rar/winrar-x64-701.exe
curl -sLo C:\Users\Public\Desktop\VMQuickConfig.exe https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe
@REM curl -sLo tesseract-setup.exe https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe
@REM if exist tesseract-setup.exe (
@REM     tesseract-setup.exe /SILENT
@REM     setx /M PATH "%PATH%;C:\Program Files\Tesseract-OCR"
@REM     echo Tesseract was installed and added to PATH.
@REM ) else (
@REM     echo Failed to download Tesseract OCR setup.
@REM )
pip install requests pyautogui pytesseract --quiet
C:\Users\Public\Desktop\Winrar.exe /S
del C:\Users\Public\Desktop\Winrar.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk"
del /f "C:\Users\Public\Desktop\Unity Hub.lnk"
net user runneradmin NoobPass1
python -c "import pyautogui as pag; pag.click(897, 64, duration=2)"
start "" "Avica_setup.exe"
