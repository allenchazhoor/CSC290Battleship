/usr/bin/env python3 setup.py

if [ $? != 0 ];
then exit;
fi;

cd src

echo "Launching Dreadnought"

/usr/bin/env python3 main.py