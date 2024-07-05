import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    password = generate_password()
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack(pady=10)

# Create a button to generate a new password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=5)

# Start the main loop
root.mainloop()
