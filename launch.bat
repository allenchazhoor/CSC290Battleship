echo off

set p=python

%p% -V 2>NUL

if errorlevel 1 goto nopython

%p% setup.py

if errorlevel 1 goto eof

goto launch

:nopython

echo "Python isnt installed or isnt on your path! Going to attempt looking for Python automatically..."

for /r %LOCALAPPDATA%\Programs\Python %%a in (*) do if "%%~nxa"=="python3.dll" set p=%%~dpnxa
if defined p (
echo %p%
) else (
echo "Couldn't find Python. Exiting."
)

set p=%p:python3.dll=python.exe%

:launch

cd src

echo "Launching Dreadnought"

%p% main.py

:eof