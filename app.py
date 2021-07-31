from flask import Flask , render_template , request
import wolframalpha
app= Flask(__name__)

app_id='648VR2-QQQ46VWA33'
client = wolframalpha.Client(app_id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def result():
    try:
        if request.form["msg"]=='Hello':
            return 'Hi, how can I help you?'
        if request.form["msg"].upper().rstrip('?')== 'WHO ARE YOU?' or request.form["msg"].upper().rstrip('?')=='INTRODUCE YOURSELF' or request.form["msg"].upper().rstrip('?')=='WHAT IS YOUR NAME' or request.form["msg"].upper().rstrip('?')=='WHO ARE YOU' or request.form["msg"].upper().rstrip('?')=='WHAT IS YOUR NAME?':
            return 'I am Lara'
        if request.form["msg"].upper().rstrip('?')=='WHO MADE YOU' or request.form["msg"].upper().rstrip('?')=='WHO CREATED YOU' or request.form["msg"].upper().rstrip('?')=='WHO IS YOUR DEVELOPER' or request.form["msg"].upper().rstrip('?')=='WHO DEVELOPED YOU' or request.form["msg"].upper().rstrip('?')=='WHO IS YOUR FATHER' or request.form["msg"].upper().rstrip('?')=='WHO IS YOUR MOTHER' or request.form["msg"].upper().rstrip('?')=='WHOSE CREATION YOU ARE':
            return 'Aaditya has developed me.'
        msg = request.form["msg"]
        res=client.query(msg)
        answer = next(res.results).text
        return answer
    except:
        return "Sorry, Can't find that. An internal error."    
