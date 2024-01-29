# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# File to store flashcards and quiz history
flashcards_file = 'flashcards.json'
history_file = 'quiz_history.json'

# Check if flashcards file exists, if not, create an empty one
if not os.path.isfile(flashcards_file):
    with open(flashcards_file, 'w') as f:
        json.dump({}, f)

# Check if quiz history file exists, if not, create an empty one
if not os.path.isfile(history_file):
    with open(history_file, 'w') as f:
        json.dump([], f)

def get_flashcards():
    """
    Get the flashcards from the flashcards file.

    Returns:
    - dict: Dictionary of flashcards.
    """
    with open(flashcards_file, 'r') as f:
        flashcards = json.load(f)
    return flashcards

def save_flashcards(flashcards):
    """
    Save the flashcards to the flashcards file.

    Args:
    - flashcards (dict): Dictionary of flashcards.
    """
    with open(flashcards_file, 'w') as f:
        json.dump(flashcards, f)

def get_quiz_history():
    """
    Get the quiz history from the quiz history file.

    Returns:
    - list: List of quiz history entries.
    """
    with open(history_file, 'r') as f:
        history = json.load(f)
    return history

def save_quiz_history(history):
    """
    Save the quiz history to the quiz history file.

    Args:
    - history (list): List of quiz history entries.
    """
    with open(history_file, 'w') as f:
        json.dump(history, f)

@app.route('/')
def index():
    flashcards = get_flashcards()
    return render_template('index.html', flashcards=flashcards)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        flashcards = get_flashcards()
        return render_template('quiz.html', flashcards=flashcards)
    elif request.method == 'POST':
        flashcards = get_flashcards()
        user_responses = {key: request.form[key] for key in request.form.keys()}
        correct_count = sum([1 for key, value in user_responses.items() if flashcards[key]['answer'] == value])
        history = get_quiz_history()
        history.append({'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'score': correct_count})
        save_quiz_history(history)
        flash('Quiz submitted successfully!', 'success')
        return redirect(url_for('quiz_result', score=correct_count))

@app.route('/quiz/result/<int:score>')
def quiz_result(score):
    return render_template('quiz_result.html', score=score)

@app.route('/add_flashcard', methods=['GET', 'POST'])
def add_flashcard():
    if request.method == 'GET':
        return render_template('add_flashcard.html')
    elif request.method == 'POST':
        flashcards = get_flashcards()
        question = request.form['question']
        answer = request.form['answer']
        flashcards[question] = {'question': question, 'answer': answer}
        save_flashcards(flashcards)
        flash('Flashcard added successfully!', 'success')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)






<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcard Quiz App</title>
</head>
<body>

    <h1>Flashcard Quiz App</h1>

    <ul>
        {% for flashcard in flashcards.values() %}
            <li>
                <strong>{{ flashcard.question }}</strong>: {{ flashcard.answer }}
            </li>
        {% endfor %}
    </ul>

    <a href="/quiz">Take Quiz</a>
    <a href="/add_flashcard">Add Flashcard</a>

</body>
</html>






<!-- templates/quiz.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcard Quiz</title>
</head>
<body>

    <h1>Flashcard Quiz</h1>

    <form action="/quiz" method="post">
        {% for flashcard in flashcards.values() %}
            <p>
                <strong>{{ flashcard.question }}</strong>: 
                <input type="text" name="{{ flashcard.question }}" required>
            </p>
        {% endfor %}
        <button type="submit">Submit Quiz</button>
    </form>

</body>
</html>





<!-- templates/quiz_result.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Result</title>
</head>
<body>

    <h1>Quiz Result</h1>

    <p>Your score: {{ score }}/5</p>

    <a href="/">Back to Home</a>

</body>
</html>






<!-- templates/add_flashcard.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Flashcard</title>
</head>
<body>

    <h1>Add Flashcard</h1>

    <form action="/add_flashcard" method="post">
        <label for="question">Question:</label>
        <input type="text" id="question" name="question" required>
        <br>
        <label for="answer">Answer:</label>
        <input type="text" id="answer" name="answer" required>
        <br>
        <button type="submit">Add Flashcard</button>
    </form>

    <a href="/">Back to Home</a>

</body>
</html> 
