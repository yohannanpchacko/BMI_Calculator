# BMI Calculator

from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome"
# BMI calculation page

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        hight=float(request.form['hight'])/100
        weight=float(request.form['weight'])
        BMI=weight/(hight*hight)
        
        if BMI >=35:
            return f"your BMI is {BMI} it is critical and consult a doctor"
        elif BMI >=30 and BMI<35:
            return f"your BMI is {BMI} you need to excercise 1hour 6 days/week"
        elif BMI  >=25 and BMI<30:
            return f"your BMI is {BMI} you need to excercise 1 hour 4 days/week"
        else:
            return f"your BMI is {BMI} your helth is ok do regular excercise"

        
        # return render_template('result.html',results=BMI)


if __name__=='__main__':
    app.run(debug=True)
