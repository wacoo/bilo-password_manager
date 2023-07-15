from flask import Flask, render_template
from api.v1.view import view
from api.v1.auth_view import auth_view

app = Flask(__name__)

app.config["SECRET_KEY"] = '12345'
#app.config.from_object('config.Config')

app.register_blueprint(view, url_prefix='/view')
app.register_blueprint(auth_view, url_prefix='/auth')

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    with app.app_context():
        app.run()

'''from path import Path
import sys
from flask import Flask
from view import view

#dir = Path(__file__).abspath()
#sys.path.insert(0, dir.parent.parent.parent)

app = Flask(__name__)
app.register_blueprint(view)

if __name__ == '__main__':
    app.run(debug=True) '''