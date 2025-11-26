import tkinter as tk
import threading

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x380")
root.resizable(False, False)

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=8)

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (meters):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=6)

suggestion_label = tk.Label(root, text="", font=("Arial", 11), wraplength=380, fg="gray20")
suggestion_label.pack(pady=4)

description_label = tk.Label(root, text="", font=("Arial", 10), wraplength=380, fg="gray35")
description_label.pack(pady=4)

bar_frame = tk.Frame(root)
bar_frame.pack(pady=12)
canvas = tk.Canvas(bar_frame, width=360, height=40, highlightthickness=0)
canvas.pack()

scale_label_frame = tk.Frame(root)
scale_label_frame.pack(fill="x", padx=20)
tk.Label(scale_label_frame, text="<18.5", font=("Arial", 9)).pack(side="left")
tk.Label(scale_label_frame, text="18.5–24.9", font=("Arial", 9)).pack(side="left", expand=True)
tk.Label(scale_label_frame, text="25–29.9", font=("Arial", 9)).pack(side="left", expand=True)
tk.Label(scale_label_frame, text="≥30", font=("Arial", 9)).pack(side="right")

indicator = None

def draw_bar():
    canvas.delete("all")
    w = 360
    segments = [
        (0.0, 18.5, "#a7d8ff"),
        (18.5, 25.0, "#b6f2c2"),
        (25.0, 30.0, "#ffe7a3"),
        (30.0, 40.0, "#ffb3b3"),
    ]
    min_bmi = 10.0
    max_bmi = 40.0
    for a, b, color in segments:
        x1 = ((max(a, min_bmi) - min_bmi) / (max_bmi - min_bmi)) * w
        x2 = ((min(b, max_bmi) - min_bmi) / (max_bmi - min_bmi)) * w
        canvas.create_rectangle(x1, 0, x2, 40, fill=color, outline="")

    canvas.create_rectangle(0, 0, w, 40, outline="#ccc")

def update_indicator(bmi):
    global indicator
    min_bmi = 10.0
    max_bmi = 40.0
    w = 360
    pos = (max(min_bmi, min(max_bmi, bmi)) - min_bmi) / (max_bmi - min_bmi) * w
    canvas.delete("indicator")
    canvas.create_line(pos, 0, pos, 40, width=3, fill="#333", tags="indicator")
    canvas.create_polygon(pos-6, 40, pos+6, 40, pos, 48, fill="#333", tags="indicator")

draw_bar()

def show_bmi(w, h):
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.insert(0, w)
    height_entry.insert(0, h)
    bmi = round(w / (h ** 2), 2)
    if bmi < 18.5:
        category = "Underweight"
        suggestion = "Try adding more nutritious meals and healthy snacks."
        description = "BMI below the healthy range. Your body may need more energy and nutrients."
    elif bmi < 25:
        category = "Normal weight"
        suggestion = "Great! Keep maintaining a balanced diet and regular activity."
        description = "BMI is in the healthy range. Continue current healthy habits."
    elif bmi < 30:
        category = "Overweight"
        suggestion = "Consider light exercise and mindful eating to improve health."
        description = "BMI slightly above ideal range. Small lifestyle changes can help."
    else:
        category = "Obese"
        suggestion = "Start with small lifestyle changes like daily walks and balanced meals."
        description = "BMI above recommended range. Gradual healthy habits can support improvement."
    result_label.config(text=f"Your BMI is {bmi} — {category}")
    suggestion_label.config(text=suggestion)
    description_label.config(text=description)
    update_indicator(bmi)

def calculate_from_console():
    try:
        w = float(input("Enter your weight in kilograms: "))
        h = float(input("Enter your height in meters: "))
    except Exception:
        root.after(0, lambda: result_label.config(text="Console input invalid."))
        return
    bmi = round(w / (h ** 2), 2)
    print(bmi)
    if bmi < 18.5:
        print("You are underweight")
        print("Suggestion: Add nutritious meals and healthy snacks.")
        print("Description: BMI below healthy range; body may need more nutrients.")
    elif bmi < 25:
        print("You have normal weight")
        print("Suggestion: Maintain your healthy habits.")
        print("Description: BMI in healthy range.")
    elif bmi < 30:
        print("You are overweight")
        print("Suggestion: Try light exercise and mindful eating.")
        print("Description: BMI slightly higher; small lifestyle changes help.")
    else:
        print("You are obese")
        print("Suggestion: Start with small daily improvements.")
        print("Description: BMI above recommended range; gradual habits support change.")
    root.after(0, lambda: show_bmi(w, h))

tk.Button(root, text="Calculate BMI (UI)", command=lambda: root.after(0, lambda: show_bmi(float(weight_entry.get() or 0), float(height_entry.get() or 0)))).pack(pady=6)

threading.Thread(target=calculate_from_console, daemon=True).start()

root.mainloop()
