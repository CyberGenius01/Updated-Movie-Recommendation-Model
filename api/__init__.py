from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd38f517fdac19aa6ba4052ef6173d8c2bd1fda52ed94ffea6a585516ff40dd7a';

from api import routes