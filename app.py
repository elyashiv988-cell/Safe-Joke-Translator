from joke_service import *
from translation_service import *
from file_manager import *

def display_menu():
    lang = input(f"Choose a translation language:\n\n1. Hebrew\n2. Spanish\n3. French\n4. Italian\n")
    return lang

def choose_language(lang):

    if lang.lower() == "hebrew" or lang == "1":
        return "HE"
    elif lang.lower() == "spanish" or lang == "2":
        return "ES"
    elif lang.lower() == "french" or lang == "3":
        return "FR"
    elif lang.lower() == "italian" or lang == "4":
        return "IT"
    else:

        return "Invalid language choice."

    
def run():
    
    print(f"SAFE PROGRAMMING JOKE\n=====================")
    lang = display_menu()
    lang_code = choose_language(lang)
    api_joke = get_safe_joke()
    if api_joke:
        data_joke = extract_joke_data(api_joke)
        analyze_data= analyze_joke(data_joke)
        translated_data = translate_joke(data_joke["joke"],lang_code)
        print(f"Original text:\n{data_joke["joke"]}\n")
        print(f"Translation:\n{translated_data}\n")
        print(f"Information:\nCategory: {data_joke["category"]}\nWords: {analyze_data["words"]}\nCharacters: {analyze_data["chars"]}")
        save_joke(data_joke, analyze_data, translated_data,lang_code)
        add_to_history(data_joke,translated_data,lang_code)


