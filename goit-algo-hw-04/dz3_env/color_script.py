import sys
import sys
from pathlib import PurePath, Path
from colorama import init, Fore, Back, Style

init()


def main(start_path, indent=' ' * 1):
    
    path = Path(start_path)

    # Проходимося по папці
    for item in path.iterdir():
        if item.is_file(): 
            print(indent, Back.LIGHTBLACK_EX + Fore.LIGHTYELLOW_EX + str(item.name) + Style.RESET_ALL)
        elif item.is_dir():
            print(indent, Back.LIGHTBLACK_EX + Fore.LIGHTCYAN_EX + str(item.name) + ' ↴' + Style.RESET_ALL)
            main(item, indent * 2 )

if __name__ == '__main__':
    main(str(sys.argv[1]))


