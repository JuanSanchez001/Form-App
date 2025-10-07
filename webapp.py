from flask import Flask, url_for, render_template, request


app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    return render_template('response.html')
    #optradio = request.args['optradio']
   # if optradio == 'Short':
    #    reply1 = "Amazing Choice!"
    #else: 
    #    reply1 = "test"
      
    preferences = request.args['preferences']
    if preferences == 'Dog':
        reply2 = "test1"
    else:
        reply2 = "test2"
    n = int(request.args['multNum'])
    reply3 = "3 / " + str(n) + " = " + str((3/n))
    return render_template('response.html',  response2 = reply2, response3 = reply3)
if __name__=="__main__":
    app.run(debug=False)
#https://www.w3schools.com/python/ref_random_seed.asp##response1 = reply1,z