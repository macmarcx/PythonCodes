import tkinter as tk
from tkinter import messagebox

def search_email():
    # Get the value from the email entry field
    email = entry_email.get()

    # Here you can call the function to search the email on the other website
    # Replace the code below with the actual call to your search function
    # Fictional example:
    search_result = search_on_other_site(email)

    # Display the result in a message box
    messagebox.showinfo("Search Result", search_result)

def search_on_other_site(email):
    # Replace this fictional code with the actual logic to search on your site
    # You can use libraries like requests to interact with the web
    # Fictional example:
    result = f"Performing search for email: {email}"
    return result

# Create the main window
window = tk.Tk()
window.title("Email Search")

# Create and position the widgets
label_email = tk.Label(window, text="Enter the email:")
label_email.pack(pady=10)

entry_email = tk.Entry(window)
entry_email.pack(pady=10)

search_button = tk.Button(window, text="Search", command=search_email)
search_button.pack(pady=10)

# Start the main loop of the graphical interface
window.mainloop()
