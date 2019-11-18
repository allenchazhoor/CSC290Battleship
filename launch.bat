python -V 2>NUL

if errorlevel 1 goto nopython

python setup.py

if errorlevel 1 goto eof

cd src

python main.py

goto eof

:nopython

echo "Python isnt installed or isnt on your path! Exiting..."

:eof