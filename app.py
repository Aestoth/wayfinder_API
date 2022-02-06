from flask import Flask
from flask_cors import CORS
from routes import api



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(api.blueprint)





if __name__ == '__main__':
    app.run(debug=True)















