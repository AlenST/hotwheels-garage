@echo off
title Hot Wheels Data Converter
echo ======================================
echo Converting Excel to JSON...
echo ======================================

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python and ensure 'python' is available.
    pause
    exit /b 1
)

REM Run the script
python generate_cars_data.py

if %errorlevel% equ 0 (
    echo.
    echo ======================================
    echo Success! cars_data.js has been updated.
    echo You can now open index.html.
    echo ======================================
) else (
    echo.
    echo ======================================
    echo Error: Could not generate data.
    echo Make sure generate_cars_data.py and List.xlsx exist.
    echo ======================================
)

pause