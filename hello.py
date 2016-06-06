from flask import Flask, Response, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/redir')
def redir():
    return redirect('/')

# I want Flask to return local redirect, without specifying host.
# (for Javascript reasons)
# http://stackoverflow.com/questions/30006740/how-can-i-tell-flask-not-to-add-host-scheme-info-to-my-redirect
class FixedLocationResponse(Response):
    autocorrect_location_header = False

@app.route('/redir_local')
def redir_local():
    return redirect("/", Response=FixedLocationResponse)

if __name__ == "__main__":
    app.run()
