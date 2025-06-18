from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")

def hello():
    # Nicholas' update: added functionality to print names (just fill in your names in the array list, it should avoid any merge conflict):
    # !dont forget the comma 
    names = [
        "Nicholas is here!",
        "Kyle is here!",
        "Lavin is here :)",
    ]

    items = "".join(f"<li>{name}</li>" for name in names);
    return f"""
        <h1>Hello World!</h1>
        <ol>{items}</ol>
    """

    # commented original: cant have 2 returns
    # return "Hello World!"

# Lavin: debug mode is optional, run with "-d" to enable
if __name__ == "__main__":
    debug_mode = "-d" in sys.argv
    app.run(debug=debug_mode)



