from flask import Flask, url_for, render_template, request
import random


app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    preferences = request.args['preferences']
    if preferences == 'Dog':
      replylist1 = ['OPT', 'POT', 'TOP']
      reply2 = (random.choice(replylist1))
    else:
      replylist2 = ['abc', 'Abc', 'ABC']
      reply2 = (random.choice(replylist2))
    n = int(request.args['num'])
    reply3 = str((3*n))
    return render_template('response.html', response2 = reply2, response3 = reply3) #r=reply2 + reply3#)
    
if __name__=="__main__":
    app.run(debug=True)
#https://www.w3schools.com/python/ref_random_seed.asp##response1 = reply1 response2 = reply2, ,z #optradio = request.args['optradio']
   # if optradio == 'Short':
    #    reply1 = "Amazing Choice!"
    #else: 
    #    reply1 = "test"
   # https://www.w3schools.com/python/ref_func_len.asp
      
   