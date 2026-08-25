# Safe Joke Translator

A simple Python CLI application that fetches safe programming jokes, translates them using DeepL, analyzes text length, and saves the results locally.

## Features

- Fetches safe programming jokes from JokeAPI.
- Filters out NSFW and flagged content.
- Translates jokes to Hebrew, Spanish, French, or Italian via DeepL API.
- Handles Hebrew text formatting.
- Analyzes joke word count and character count.
- Saves the current joke to output/joke.txt and appends to output/history.txt.

## Prerequisites and Installation

1. Install required dependencies:
   pip install -r requirements.txt

2. Create the output folder:
   mkdir -p output

3. Setup DeepL API Key:
   Create a .env file in the root directory and add:
   KEY=your_deepl_api_key_here

## How to Run

1. Run the script:
   python main.py

2. Follow the prompt to select a language (1-4).
3. The original joke, translation, and statistics will be displayed and saved.

## License

MIT License