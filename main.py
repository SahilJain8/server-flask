from flask import Flask,jsonify,request
from summary import do_it
from api import get_data
import warnings

warnings.filterwarnings('ignore')

app=Flask(__name__)


app.secret_key = "secret key"





@app.route("/")
def index():
    return jsonify("Hello wordl")


@app.route("/predection",methods=['GET',"POST"])
def pred():
    if request.method=="POST":
        text_data=request.form["text"]
        if len(text_data)>500:
            text_data=do_it(text_data)
            

        check=get_data(text_data)
        if check:
            return jsonify("It is correct ")
        else:
            return jsonify("there is an incorrect information regrading policy")
    else:
        return jsonify("error")







    
if __name__=="__main__":
    app.run()
