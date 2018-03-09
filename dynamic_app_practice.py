import flask

app = flask.Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template('dynamic_app_template.html')

@app.route('/suggestions')
def suggestions():
    text = flask.request.args.get('jsdata')
    return "<ul>{}</ul>".format('\n'.join('<li>{}</li>'.format(i) for i in [text]*__import__('random').randint(1, 10)))


if __name__ == '__main__':
    app.debug = True


app.run()
