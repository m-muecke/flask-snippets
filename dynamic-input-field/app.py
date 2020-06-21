from flask import Flask, render_template, jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField
# local imports
from config import app_config

app = Flask(__name__)
app.config.from_object(app_config['development'])

class Form(FlaskForm):
    country = SelectField('country', choices=[('GER', 'Germany'),
                                              ('FRA', 'France'),
                                              ('SWE', 'Sweden'),
                                              ('ENG', 'England')])
    city = SelectField('city', choices=[])

@app.route("/", methods=['GET', 'POST'])
def main() -> render_template:
    form = Form()
    form.city.choices = [('HH', 'Hamburg'), ('MUC', 'Munich')]
    return render_template('index.html', form=form)

@app.route('/city/<string:country>')
def classification(country) -> jsonify:

    city_list = {
        'GER': [{'id': 'HH', 'name': 'Hamburg'},
                {'id': 'MUC', 'name': 'Munich'}],
        'FRA': [{'id': 'PAR', 'name': 'Paris'},
                {'id': 'L', 'name': 'Lyon'}],
        'SWE': [{'id': 'STK', 'name': 'Stockholm'},
                {'id': 'GTH', 'name': 'Gothenburg'}],
        'ENG': [{'id': 'LON', 'name': 'London'},
                {'id': 'LIV', 'name': 'Liverpool'}],
    }.get(country)

    return jsonify({'cities': city_list})

if __name__ == '__main__':
    app.run()
