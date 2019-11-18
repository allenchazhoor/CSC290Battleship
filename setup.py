import sys
from pip._internal import main as pipmain

def install(package):
    pipmain(['install', package])

if not (sys.version_info.major >= 3 and sys.version_info.minor >= 4):

    print(f'Python version is too old! Your version is {sys.version.split()[0]} and a version newer than 3.4.0 is required')

    sys.exit(1)

#old = sys.stdout

#sys.stdout = None

with open('requirements.txt') as f:
    for line in f:
        if line:
            install(line)

sys.exit(0)