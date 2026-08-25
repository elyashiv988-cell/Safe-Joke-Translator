
def save_joke(joke_data, analysis, translated_joke, language):

    with open("/Users/elyashiv/kodcode/projects/Safe-Joke-Translator/output/joke.txt", "w", encoding="utf-8") as file:
        file.write("SAJE JOKE\n")
        file.write("=========\n")
        file.write(f"Category: {joke_data["category"]}\nJoke ID: {joke_data["joke_id"]}\nOriginal text: {joke_data["joke"]}\nTranslation language: {language}\nTranslation: {translated_joke[::-1]}\nWords: {analysis["words"]}\nCharacters: {analysis["chars"]}")

def add_to_history(joke_data, translated_joke, language):
    with open("/Users/elyashiv/kodcode/projects/Safe-Joke-Translator/output/history.txt", "a", encoding="utf-8") as file:
            file.write(f"\nJoke ID: {joke_data["joke_id"]}\nCategory: {joke_data["category"]}\nOriginal text: {joke_data["joke"]}\nTranslation language: {language}\nTranslation: {translated_joke[::-1]}\n=======================")


