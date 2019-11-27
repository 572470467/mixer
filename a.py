File Edit Options Buffers Tools Python Help                                                                                                                                                                 
import time
import B
from flask import Flask, jsonify
import random
app = Flask(__name__)
list=[{'pos':0,'sensors':[0,1,1,1,1]},{'pos':1,'sensors':[1,0,1,1,1]},{'pos':2,'sensors':[1,1,0,1,1]},{'pos':3,'sensors':[1,1,1,0,1]},{'pos':4,'sensors':[1,1,1,1,0]}]
text=['正在接粉体...','正在混合粉体...','正在倒粉体到下锅...','正在制作润湿剂...','正在混合磨料...','正在将润湿剂泵进磨料...','正在将磨料倒下锅混合，完成后倒进小车...']
list0=[[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]

def random_A():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(7))
    return list0[int(dic[str(i)])]

def random_status():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(5))
    return dic[str(i)]

@app.route('/carrier/status')
def status():
    d=list[int(random_status())]
    return jsonify(d)

@app.route('/carrier/moveto/<groupid>')
def moveto(groupid):
    d=groupid
    return jsonify(d)

@app.route('/mixer/<groupid>')
def button(groupid):
    if groupid=='000':
        return str(B.A())
    elif groupid=='100':
        return str(B.B())
    elif groupid=='200':
        return str(B.C())
    elif groupid=='300':
        return str(B.D())
    elif groupid=='400':
        return str(B.E())
    elif groupid=='500':
        return str(B.F())
    elif groupid=='600':
        return str(B.G())
#@app.route('/mixer/<groupid>')                                                                                                                                                                            
#def button(groupid):                                                                                                                                                                                      
#    #d=list[int(groupid[0])]                                                                                                                                                                              
#    num=int(groupid[0])                                                                                                                                                                                   
#    d=text[num]                                                                                                                                                                                           
#    return jsonify(d)                                                                                                                                                                                      

@app.route('/mixerstatus/')
def status_A():
    d={'status':random_A()}
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)


