from devAppWeb import app

@app.route('/')
def index():
    return 'Hello, Michael!'