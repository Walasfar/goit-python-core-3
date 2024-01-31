import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

init()

# Стилі
folder_back = Back.YELLOW
folder_color = Fore.BLACK
item_back = Back.LIGHTCYAN_EX
item_color = Fore.BLACK
clear = Style.RESET_ALL

def main(user_path, indent=' ' * 1):
    """
    user_path - початковий путь
    indent - параметер за замовчуванням, кількість відступів - рекурсія
    """
    path = Path(user_path)

    if path.exists():
        # Проходимося по папці
        
        for item in path.iterdir():    
            if item.is_file(): 
                print(indent, item_back + item_color + str(item.name) + clear)
                
            elif item.is_dir():
                print(indent, folder_back + folder_color + str(item.name) + ' ↴' + Style.RESET_ALL)
                main(item, indent * 2 )
    else:
        print("File or direction is not exists.")
        


if __name__ == '__main__':
    main(str(sys.argv[1]))
