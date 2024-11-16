from tkinter import*
import joblib
import numpy as np

model=joblib.load(r"multi classification\multiclass model.joblib")

def check():
    data=input_entry.get()
    data=list(map(float,data.split(",")))

    data=np.array(data).reshape(1,-1)
    prediction=model.predict(data)
    
    if prediction==0:
        output_label.config(text=f"You are addicted with drug A ")
    
    elif prediction==1:
        output_label.config(text=f"You are  addicted with drug B ")

    
  
    elif prediction==2:
        output_label.config(text=f"You are  addicted with drug C ")

    
    elif prediction==3:
        output_label.config(text=f"You are addicted with drug Y")

    
    elif prediction==4:
        output_label.config(text=f"You are addicted with drug X")

    else:
        output_label.config(text="pls enter ur symptoms")


app=Tk()
app.geometry("900x500")
app.title("Multi Class Model")
app.config(bg="Blue")

heading=Label(app,text="Multi Class Model",font="robot 35 bold", fg="white",bg="pink" )
heading.pack(fill='x',ipady=30)

input_label=Label(app,text="enter here wagyara wagyara:",font="robot 20 bold", fg="white",bg="grey")
input_label.pack(pady=20)

input_entry=Entry(app,font="arial 20 italic")
input_entry.pack(pady=20)

btn=Button(app,text="Check",font="halvetica 25 bold", bg="red" ,fg="white",command=check)
btn.pack(pady=20)


output_label=Label(app,font="arial 20 italic",bg="blue",fg="white")
output_label.pack(pady=30)
app.mainloop()