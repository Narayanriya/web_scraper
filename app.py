from flask import Flask, render_template
from modules.webscrap import timesofindia,indianexpress,indiatoday,firstpost,toe_res,ie_res,it_res,fp_res

app = Flask(__name__)

timesofindia()
indianexpress()
indiatoday()
firstpost()


@app.route('/')
def table():
    return render_template("home.html", toe_data= toe_res,ie_data= ie_res,it_data= it_res,fp_data= fp_res)

if __name__ == '__main__':
	#print jdata   FLASK_DEBUG=1 flask run
  app.run(debug=True)