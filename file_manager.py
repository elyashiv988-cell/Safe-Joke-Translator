

def display_menu():
    lang = input(f"Choose a translation language:\n\n1. Hebrew\n2. Spanish\n3. French\n4. Italian")
    return lang

def choose_language(lang):

    if lang.lower() == "hebrew" or lang == "1":
        return "he"
    elif lang.lower() == "spanish" or lang == "2":
        return "es"
    elif lang.lower() == "french" or lang == "3":
        return "fr"
    elif lang.lower() == "italian" or lang == "4":
        return "it"
    else:
        return "Invalid language choice."


