from flask import Flask, request
import random

app = Flask(__name__)

truths = [
    "What is your most embarrassing moment?",
    "Who do you secretly admire?",
    "What is one habit you want to change?",
    "Have you ever cheated in an exam?",
    "What is your biggest fear?"
]

dares = [
    "Dance for 1 minute",
    "Do 15 squats",
    "Sing a song loudly",
    "Act like your favorite teacher",
    "Talk non-stop for 30 seconds"
]

current_player = "Player 1"
current_task = ""

@app.route("/", methods=["GET", "POST"])
def home():
    global current_player, current_task

    if request.method == "POST":
        choice = request.form["choice"]

        if choice == "truth":
            current_task = random.choice(truths)
        elif choice == "dare":
            current_task = random.choice(dares)

        # switch player
        if current_player == "Player 1":
            current_player = "Player 2"
        else:
            current_player = "Player 1"

    return f"""
    <h1>Truth or Dare 🌍</h1>
    <h2>Current Turn: {current_player}</h2>

    <form method="post">
        <button name="choice" value="truth">Truth</button>
        <button name="choice" value="dare">Dare</button>
    </form>

    <h3>{current_task}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
