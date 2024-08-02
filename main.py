import json
import os

def save_language(language):
    with open('config.json', 'w') as config_file:
        json.dump({'language': language}, config_file)

def load_language():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config.get('language', None)
    return None

def choose_language():
    print("Select language / Wybierz język:")
    print("1. English")
    print("2. Polski")
    
    choice = input("Enter the number of your choice / Wprowadź numer wyboru: ")
    
    if choice == '1':
        return 'en'
    elif choice == '2':
        return 'pl'
    else:
        print("Invalid choice / Nieprawidłowy wybór. Defaulting to English.")
        return 'en'

def load_translations(language):
    with open(f'{language}.json', 'r') as file:
        return json.load(file)

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Sprawdź, czy plik konfiguracyjny istnieje i czy zawiera ustawiony język
    language = load_language()
    
    if language is None:
        # Jeśli język nie jest ustawiony, zapytaj użytkownika o wybór
        language = choose_language()
        save_language(language)
    
    translations = load_translations(language)
    print(translations['greeting'])
    
    while True:
        print()
        print(translations['options'])
        print()
        print(translations['file_manager'])
        print(translations['upgrade'])
        print(translations['package'])
        print(translations['exit'])
        print()
        choice = input(translations['choice'])
        
        if choice == '1':
            file_manager(translations)
        elif choice == '2':
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
        elif choice == '3':
            name_p = input(translations['name_package'])
            os.system(f"sudo apt-get install {name_p}")
        elif choice == '4':
            print(translations['farewell'])
            break
        else:
            print(translations['invalid_choice'])

def file_manager(translations):
    while True:
        print()
        os.system("pwd")
        print()
        print(translations['file_manager'])
        print()
        print(translations['options'])
        print()
        print(translations['ls'])
        print(translations['cd'])
        print(translations['mkdir'])
        print(translations['mkfile'])
        print(translations['rm'])
        print(translations['sudo_rm'])
        print(translations['exit2'])
        print()
        choice = input(translations['choice'])
        print()
    
        if choice == '1':
            ls()
        elif choice == '2':
            cd(translations)
        elif choice == '3':
            mkdir(translations)
        elif choice == '4':
            mkfile(translations)
        elif choice == '5':
            rm(translations)
        elif choice == '6':
            sudo_rm(translations)
        elif choice == '7':
            break
        else:
            print(translations['invalid_choice'])

def ls():
    os.system("ls")

def cd(translations):
    name = input(translations['name_dir'])
    try:
        os.chdir(name)
    except Exception as e:
        print(f"{e}")

def mkdir(translations):
    name = input(translations['name_dir'])
    os.system(f"mkdir {name}")

def mkfile(translations):
    name = input(translations['name_file'])
    os.system(f"nano {name}")

def rm(translations):
    name = input(translations['name_dir_file'])
    os.system(f"rm -r {name}")

def sudo_rm(translations):
    name = input(translations['name_dir_file'])
    os.system(f"sudo rm -r {name}")

if __name__ == '__main__':
    main()