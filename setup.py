import sys
from subprocess import Popen, PIPE

if not (sys.version_info.major >= 3 and sys.version_info.minor >= 4):

    print(f'Python version is too old! Your version is {sys.version.split()[0]} and a version newer than 3.4.0 is required')

    sys.exit(1)

print(f'You are using Python version {sys.version.split()[0]}!')

#old = sys.stdout

with open('requirements.txt') as f:

    lines = [x for x in f.readlines() if x]

process = Popen([sys.executable, '-m', 'pip', 'install', *lines], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

sys.exit(0)