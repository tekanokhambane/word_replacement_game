# Word Replacement Game

Welcome to the Word Replacement Game! This is a fun and easy-to-play web app where you can create funny sentences by replacing words with random ones.

## Installation

1. **Download the Game:**
   - Click on the green "Code" button on this page.
   - Select "Download ZIP" and save it on your computer.
   - Extract the ZIP file to a folder.

2. **Install Python:**
   - If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
   - During installation, make sure to check the box that says "Add Python to PATH" (on Windows).

3. **Open Terminal (Command Prompt on Windows):**
   - Search for "Terminal" on macOS/Linux or "Command Prompt" on Windows.

4. **Navigate to the Game Folder:**
   - Use the `cd` command to move to the folder where you extracted the game files.

5. **Set Up the Game:**
   - Run these commands in the terminal:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # macOS/Linux
     venv\Scripts\activate  # Windows
     pip install -r requirements.txt
     ```

## Playing the Game

1. **Start the Game:**
   - In the terminal, run:
     ```bash
     sh start.sh
     ```
     or
     ```bash
     python3 main.py
     ```

2. **Open the Game in Your Browser:**
   - Open your web browser (like Chrome, Firefox, or Safari).
   - Go to this address: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. **Enter a Sentence:**
   - Type a sentence in the box that says "Enter a sentence" on the web page.
   - For example: "The quick brown fox jumps over the lazy dog."

4. **Create Funny Sentences:**
   - Click the "Submit" button.
   - The game will replace some words in your sentence with funny random words.
   - See the new sentence displayed below!

5. **Play Again:**
   - Feel free to enter new sentences and click "Submit" again to create more funny sentences.

## Troubleshooting

- If the game doesn't start or you see an error, make sure you followed all the installation steps correctly.
- You can ask for help in the [issues](https://github.com/tekanokhambane/word-replacement-game/issues) section of the game's GitHub page.

Enjoy playing the Word Replacement Game!
