from tkinter import*
import joblib
model=joblib.load(r"C:\Users\sharm\OneDrive\Desktop\ml\af_multiple_reg\classification\insurence predictor.joblib")

def predict():
    input_=int(input_entry.get())
    predicted_value=model.predict([[input_]])
    print(predicted_value)
    if predicted_value==1:
        output_label.config(text=f"u r eligiable")
    else:
        output_label.config(text=f"u r not eligible")

app=Tk()
app.geometry("700x500")
app.title("ip")
app.config(bg="green")
heading = Label(app, text = "INSURENCE   PREDICTOR", font = "robot 35 bold", bg = "green", fg = "white")
heading.pack(fill = "x", ipady = 30)

input_label = Label(app, text = "Enter Age...", font = "robot 20 bold", bg = "green", fg = "blue")
input_label.place(x = 60, y = 130)

input_entry = Entry(app, font = "robot 20 bold", bg = "white", fg = "black")
input_entry.place(x = 230, y = 160)

btn = Button(app, text = "PREDICT", font = "robot 25 bold", bg = "blue", fg = "red", command = predict)
btn.place(x = 270, y = 250)

output_label = Label(app,font = "robot 20 bold", bg = "green", fg = "white")
output_label.place(x = 180, y = 350)

app.mainloop()