from flask import Flask, request, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template("index.html", title="Index")
 
    @app.route('/send')
    def send():
        name = request.args.get("name", "")
        age = request.args.get("age", 0, type=int)
        return "Name is {}, age is {}".format(name, age)

    return app

