from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def firstPage():
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html", row=8, col=8, color1="white", color2="black")


@app.route('/4')
def Page4():
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html", row=8, col=4, color1="white", color2="black")


@app.route('/<x>/<y>')
def Pagexy(x, y):
    x = int(x)
    y = int(y)
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html", row=x, col=y, color1="white", color2="black")


@app.route('/<x>/<y>/<col1>/<col2>')
def Pagexycol(x, y, col1, col2):
    x = int(x)
    y = int(y)
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html", row=x, col=y, color1=col1, color2=col2)


if __name__ == "__main__":
    app.run(debug=True)
