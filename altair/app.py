import pandas as pd
import altair as alt
from flask import Flask, render_template
# local imports
from config import app_config

app = Flask(__name__)
app.config.from_object(app_config['development'])

@app.route("/", methods=['GET', 'POST'])
def main() -> render_template:
  # code for creating altair chart
  df = pd.DataFrame({'x': [1, 2, 4, 8, 16], 'y': [1, 2, 4, 8, 16]})
  chart = (alt
            .Chart(df)
            .mark_line(clip=True)
            .encode(
                alt.X('x'),
                alt.Y('y'))
                #tooltip=['X', 'Y'])
            .interactive()
            .to_json())

  return render_template('index.html', chart=chart)

if __name__ == '__main__':
    app.run()
