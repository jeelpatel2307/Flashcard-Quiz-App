# Flashcard Quiz App

The Flashcard Quiz App is a simple web application built using Python with Flask for the server-side and HTML for the client-side. The app allows users to create flashcards, quiz themselves, and view their quiz history.

## Features

- **View Flashcards:**
    - Users can view a list of flashcards on the home page.
- **Take Quiz:**
    - Users can take a quiz using the flashcards.
    - The quiz result is displayed after submission, showing the user's score.
- **Add Flashcards:**
    - Users can add new flashcards with questions and answers.

## Server-side (Python with Flask)

The server-side code (`app.py`) is responsible for handling HTTP requests, managing flashcards, and storing quiz history. Flask is used as the web framework.

- **Flashcards File (`flashcards.json`):**
    - Stores flashcards as a JSON file.
    - The `get_flashcards` and `save_flashcards` functions handle flashcard data.
- **Quiz History File (`quiz_history.json`):**
    - Stores quiz history as a JSON file.
    - The `get_quiz_history` and `save_quiz_history` functions handle quiz history data.
- **Routes:**
    - `/`: Displays the list of flashcards and provides links to take a quiz or add a new flashcard.
    - `/quiz`: Presents the flashcards for a quiz and allows users to submit their answers.
    - `/quiz/result/<int:score>`: Shows the result of the quiz, indicating the user's score.
    - `/add_flashcard`: Provides a form to add a new flashcard.

## Client-side (HTML)

The client-side code includes HTML templates (`templates` folder) for different pages of the app.

- **`index.html`:**
    - Displays the list of flashcards.
    - Provides links to take a quiz or add a new flashcard.
- **`quiz.html`:**
    - Presents the flashcards for a quiz.
    - Allows users to submit their answers.
- **`quiz_result.html`:**
    - Shows the result of the quiz, indicating the user's score.
- **`add_flashcard.html`:**
    - Provides a form to add a new flashcard.

## How to Run

1. Save the server-side code in a file (e.g., `app.py`).
2. Save the client-side code in a folder named `templates` with the specified HTML files.
3. Install Flask:
    
    ```bash
    pip install Flask
    
    ```
    
4. Run the server:
    
    ```bash
    python app.py
    
    ```
    
5. Open a web browser and go to `http://localhost:5000` to use the Flashcard Quiz App.

## Customization

- Customize the flashcards in the `flashcards.json` file or add more functionality to support different quiz formats.
- Improve the UI and styling for a better user experience.

---

## Author

Jeel patel
