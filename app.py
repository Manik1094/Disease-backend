from flask import Flask

#Init app
app = Flask(__name__)


#Run server
if __name__ == '__main__':
    app.run(debug=True)