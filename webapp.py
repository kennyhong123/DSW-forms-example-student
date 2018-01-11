from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response" methods=["POST"])
def render_response():
    color=request.forms['color']
    if color == 'pink':
        reply = "Disguisting"
    else:
        reply = "I hate color because I'm colorblind"
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
