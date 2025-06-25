from flask import render_template
from app_init import app

from controllers.loginout_controller import *
from models.loginout_model import *
from controllers.match_controller import *
from models.match_model import *
from controllers.profile_controller import *
from models.profile_model import *
from controllers.saisie_controller import *
from models.saisie_model import *


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)