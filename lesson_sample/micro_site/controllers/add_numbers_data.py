from urllib.parse import parse_qs
from utils import render_template

def add_numbers_data(environ):
    method = environ["REQUEST_METHOD"]

    if method == "POST":
        try:
            size = int(environ.get("CONTENT_LENGTH", 0) or 0)
        except ValueError:
            size = 0
        body = environ["wsgi.input"].read(size).decode("utf-8")
        params = parse_qs(body)

        num1 = int(params.get("num1", [0])[0])
        num2 = int(params.get("num2", [0])[0])
        result = num1 + num2

        return render_template("boundaries/addition.html", add=result)
    else:
        # GET のときは入力フォームを返す
        return render_template("boundaries/addition_form.html")
