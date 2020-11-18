import subprocess
import sys

if __name__ == '__main__':
    packages = ['Tensorflow == 2.3.1', 'pyqt5 == 5.15.1','numpy == 1.18.5','pillow == 8.0.1','matplotlib == 3.2.2', 'scipy == 1.5.4']
    for package in packages:
        install(package)

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])