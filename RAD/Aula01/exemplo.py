from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola():
    return 'Olá, Mamãe e papai!'

if __name__ == "__main__":
    app.run()
