from flask import Flask
import os
app = Flask(__name__)

@app.route("/")

def hello():
    baseDir = os.path.dirname(__file__)
    path = os.path.join(baseDir, "names")

    # Define array to store filenames
    names = []
    for fileName in sorted(os.listdir(path)):
        # def all intern name must be txt format
        if not fileName.endswith(".txt"):
            continue # skip if format not exact

        # after read, construct path and append
        fullDir = os.path.join(path, fileName)

        '''reads the content of a .txt file, 
        removes extra spaces or newlines, 
        and adds it to the names list.
        '''
        with open(fullDir, "r", encoding="utf-8") as f:
            names.append(f.read().strip())
        
    # Build the HTML for display
    items = "".join(f"<li>{n}</li>" for n in names)
    return f"""
        <h1>Hello World!</h1>
        <ol>
            {items}
        </ol>
    """ 

if __name__ == "__main__":
    app.run()
