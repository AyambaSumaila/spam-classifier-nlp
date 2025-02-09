from flask import Flask, render_template, request 


import pickle 

app=Flask(__name__)

pipe=pickle.load(open("my_model_naive.pk", "rb"))


@app.route('/', methods=['GET', 'POST'])

def main():
    if request.method=="POST":
        text=request.form 
        emails=text['email']
        print(emails)
        list_email=[emails]
        
        output=pipe.predict(list_email)[0]
        print(output)

        return render_template("show.html", prediction=output)
    
    else:
        return render_template("index.html")
    


if __name__=="__main__":
    app.run(debug=True)
