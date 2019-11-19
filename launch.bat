echo off

set p=python

%p% -V 2>NUL

if errorlevel 1 goto nopython

goto setup

:setup

echo We're going to check that you have the right packages installed, sit tight it might take a few minutes the first time

%p% setup.py

if errorlevel 1 goto eof

goto launch

:nopython

echo Python isnt installed or isnt on your path! Going to attempt looking for Python automatically, this may take a minute.

for /r %LOCALAPPDATA%\Programs\Python %%a in (*) do if "%%~nxa"=="python3.dll" set p=%%~dpnxa
if defined p (
    echo Found Python!
) else (
echo Couldn't find Python. Exiting.
)

set p=%p:python3.dll=python.exe%

goto setup

:launch

cd src

echo Launching Dreadnought

%p% main.py

:eof