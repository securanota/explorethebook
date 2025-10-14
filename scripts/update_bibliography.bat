@echo off
REM Update Bibliography from Zotero Export
REM This script converts Zotero Better BibTeX JSON export to Hugo simple JSON format

echo 📚 Updating bibliography from Zotero export...

REM Set paths (adjust these to match your setup)
set ZOTERO_EXPORT="%USERPROFILE%\Desktop\zotero_export.json"
set BIBLIOGRAPHY_JSON="data\bibliography.json"
set CONVERTER_SCRIPT="scripts\convert_zotero_simple.py"

REM Check if Zotero export exists
if not exist %ZOTERO_EXPORT% (
    echo ❌ Error: Zotero export file not found at %ZOTERO_EXPORT%
    echo.
    echo 📋 Please export your Zotero collection first:
    echo    1. Right-click your Zotero collection
    echo    2. Choose "Export Collection"
    echo    3. Select "Better BibTeX JSON" format
    echo    4. Check "Keep updated" for automatic updates
    echo    5. Save as "zotero_export.json" on your Desktop
    echo.
    pause
    exit /b 1
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo    Please install Python 3.x from https://python.org
    pause
    exit /b 1
)

REM Convert the export
echo 🔄 Converting Zotero export to Hugo JSON format...
python %CONVERTER_SCRIPT% %ZOTERO_EXPORT% %BIBLIOGRAPHY_JSON%

if errorlevel 1 (
    echo ❌ Error: Conversion failed!
    pause
    exit /b 1
)

echo.
echo ✅ Bibliography updated successfully!
echo 📄 File: %BIBLIOGRAPHY_JSON%
echo.

REM Optional: Restart Hugo development server to see changes
set /p restart_hugo="🔄 Restart Hugo development server to see changes? (y/n): "
if /i "%restart_hugo%"=="y" (
    echo 🚀 Restarting Hugo...
    docker-compose restart
)

pause