from flask import Flask, request, Markup, abort

app = Flask(__name__)
#flask GET,POST

@app.route('/')
def index():
    html = '''
    <form action="/test">
        <p><label>test: </label>
        <input type="text" name="query" value="default">
        <button type="submit" formmethod="get">GET</button>
        <button type="submit" formmethod="post">POST</button></p>
    </form>
    '''
    
    return Markup(html)


@app.route('/test', methods=['GET', 'POST'])
def test():
        if request.method == 'GET':
            return request.args.get('query', '')
        elif request.method == 'POST':
            return request.form['query']
        else:
            return abort(400)


if __name__ == '__main__':
    app.run()