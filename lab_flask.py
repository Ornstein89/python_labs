import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<title>Page Title</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>Simple Flask webpage</h1>
<p>Простейшая веб-страница на Flask</p>

</body>
</html>
'''