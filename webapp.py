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
      replylist1 = ['fluffy1$2@', 'p@w$#*', 't0pD0gCru!$!ng','f!r3d0gr3ady^*', 'art!cfur#2#4#6@!', 'd0gw!+hW!ngs!@#', 'b3@$td0gg0@', 'm@y$3@$0n@ld0gs', 'c0pd0gg0@@!']
      reply2 = (random.choice(replylist1))
    else:
      replylist2 = ['c@+v!d30$#', 'c@+n!pcr@zy*', 'w!ldc@+p@r+y@','@ttitud3catw^8', 'c@t+theLa$+@irbend3r', 'cr@zy+w!ldc@t', 'h@ppyc@+unk0wn#&', 'my$+ic@lcA+!', 'hungry@rmyC@+$^#']
      reply2 = (random.choice(replylist2))
   
    n = int(request.args['num'])
    reply3 = str((n/3))
    return render_template('response.html', response2 = reply2, response3 = reply3) 
    
    
if __name__=="__main__":
    app.run(debug=True)
#https://www.w3schools.com/python/ref_random_seed.as  *used for random*

   