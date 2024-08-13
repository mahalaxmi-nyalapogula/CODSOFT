import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My Portfolio")
root.geometry("800x600")

# Create a frame for navigation buttons
nav_frame = tk.Frame(root, bg="lightgrey")
nav_frame.pack(side="top", fill="x")

# Add navigation buttons
def show_home():
    pass  # Hi, I'm Mahalaxmi Nyalapogula

def show_projects():
    pass  # A Python-based on to-do list application with GUI 

def show_skills():
    pass  # Python, Tkinter

def show_contact():
    pass  # mahalaxminyalapogula@gmail.com

btn_home = tk.Button(nav_frame, text="Home", command=show_home)
btn_home.pack(side="left", padx=10, pady=5)

btn_projects = tk.Button(nav_frame, text="Projects", command=show_projects)
btn_projects.pack(side="left", padx=10, pady=5)

btn_skills = tk.Button(nav_frame, text="Skills", command=show_skills)
btn_skills.pack(side="left", padx=10, pady=5)

btn_contact = tk.Button(nav_frame, text="Contact", command=show_contact)
btn_contact.pack(side="left", padx=10, pady=5)

# Home Section
def show_home():
    clear_content()
    label = tk.Label(root, text="Welcome to My Portfolio", font=("Arial", 24))
    label.pack(pady=20)

# Projects Section
def show_projects():
    clear_content()
    label = tk.Label(root, text="My Projects", font=("Arial", 24))
    label.pack(pady=20)
    # Add more widgets to display project details

# Skills Section
def show_skills():
    clear_content()
    label = tk.Label(root, text="My Skills", font=("Arial", 24))
    label.pack(pady=20)
    # Add more widgets to list skills

# Contact Section
def show_contact():
    clear_content()
    label = tk.Label(root, text="Contact Me", font=("Arial", 24))
    label.pack(pady=20)
    # Add widgets for contact form or information

def clear_content():
    for widget in root.winfo_children():
        if widget not in nav_frame.winfo_children():
            widget.destroy()

