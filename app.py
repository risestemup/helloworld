from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    # Nicholas' update: added functionality to print names (just fill in your names in the array list, it should avoid any merge conflict):
    # !dont forget the comma 
    names = [
        "Nicholas is here!"
    ]

    items = "".join(f"<li>{name}</li>" for name in names);
    return f"""
        <h1>Hello World!</h1>
        <ol>{items}</ol>
    """

    # commented original: cant have 2 returns
    # return "Hello World!"

if __name__ == "__main__":
    app.run()
