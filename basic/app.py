from flask import Flask, render_template
# local imports
from config import app_config

app = Flask(__name__)
app.config.from_object(app_config['development'])

@app.route("/", methods=['GET', 'POST'])
def main() -> render_template:
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
