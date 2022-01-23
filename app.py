from flask import Flask, render_template, url_for,request

app = Flask(__name__)

@app.route('/',methods =["GET", "POST"])
def calc():
    #Verify submit and # was entered
    if request.method == "POST" and request.form.get("money") != '':
        #int(request.form.get("money")) > 1:
        amount = request.form.get("money")
        
        #Integrate API for pulling live conversion 
        if amount < 0:
            err = "Enter number greater than 1"
            return render_template("home.html",err =err)
        dict1 = {}
        cad = round(float(amount) * 1.26, 2)
        peso = round(float(amount) * 20.47 ,2)
        euro = round(float(amount) * 0.88 , 2)
        
        
        dict1["USD"] = amount
        dict1["CAN"] = cad
        dict1["Peso"] = peso
        dict1["Euro"] = euro

        

        
        return render_template("home.html",dict1=dict1)
    else:
        enter = "Please enter a number > 1"
    return render_template("home.html",enter=enter)

#def index():
#    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)