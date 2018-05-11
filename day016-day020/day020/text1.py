import subprocess
import os


def main():
    print(os.getpid())
    subprocess.call('notepad')
    subprocess.call('calc')
    subprocess.call(r'C:\Program Files\Microsoft Games\Minesweeper\Minesweeper.exe')


if __name__ == '__main__':
    main()
