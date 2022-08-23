from app import app

@app.route('/')
@app.route('/index')
def index():
    return '<h1 align="center">This is microblog</h1>'
