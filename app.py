from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route("/")
def main(): 
    return 'test'
if __name__ =='__main__':  
    app.run(debug = True)  

@app.route("/showSignUp")
def showSignUp():
    return 'test'
if __name__ =='__main__':  
    app.run(debug = True)  
    



  

   