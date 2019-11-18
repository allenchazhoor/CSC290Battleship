import sys, pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if (sys.version_info.major >= 3 and sys.version_info.minor >= 4):

    print(f'Python version is too old! Your version is {sys.version.split()[0]} and a version newer than 3.4.0 is required')

    sys.exit(1)

with open('requirements.txt') as f:
    for line in f:
        install(f)

sys.exit(0)