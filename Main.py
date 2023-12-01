import tkinter as tk

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Project Name")

# Set window size and position
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

# Background Image

bg_image = tk.PhotoImage(file="s.jpg")
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Project Name in the middle at the top
project_name = tk.Label(root, text="LP Exercices", font=("Arial", 30))
project_name.pack(pady=20)

# Frame to contain exercise buttons
exercise_frame = tk.Frame(root)
exercise_frame.pack(pady=20)

# Function to handle exercise selection
def select_exercise():
    # Implement the logic to handle exercise selection here
    pass

# Example buttons for exercises in three rows
for i in range(1, 10):
    exercise_button = tk.Button(exercise_frame, text=f"Exercise {i}", command=select_exercise, width=10, height=1, font=("Arial", 15), bg="white", fg="black", activebackground="black", activeforeground="white")
    exercise_button.grid(row=(i-1)//3, column=(i-1)%3, padx=10, pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=exit_program, width=10, height=1, font=("Arial", 20), bg="white", fg="black", activebackground="black", activeforeground="white")
exit_button.pack(pady=20)

# Status Bar
status_bar = tk.Label(root, text="Status: Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Collaborators at the bottom corner
collaborators = tk.Label(root, text="Collaborators:  A, B, C, D, E" , bd=1, relief=tk.SUNKEN, anchor=tk.W)
collaborators.pack(side=tk.BOTTOM, anchor=tk.SE, pady=10)

# Packing elements to display
root.mainloop()
