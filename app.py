from flask import Flask, render_template
app=Flask(__name__)

# @app.route('/')
# def index():
#     return "hello"

# @app.route('/total/<n1>/<n2>')
# def total(n1,n2):
#     # total=int(n1)+int(n2)
#     return str(int(n1)+int(n2))

@app.route('/')
def index():
    poem=[{
        'title':'Tinh da tu',
        'body':'Dau giong',
        'author':{'Ly Bach','gender':'female'}
    },
    {
        'title':'Tinh da tu',
        'body':'Dau giong',
        'author':'Ly Bach','gender':'male'}
    }]
    return render_template('index.html',data=poem)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)


