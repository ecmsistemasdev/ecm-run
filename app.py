import os
from flask import Flask

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def index():
    return f'<h1>Hello World! </h1>'



#app.run(host="0.0.0.0", port=port)
if __name__ == "__main__":
    app.run(debug=True, port=port)

#    app.run(debug=True)
    
