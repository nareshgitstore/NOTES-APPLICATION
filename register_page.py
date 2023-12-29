
import customtkinter as ctk
import tkinter.messagebox as tkmb
import mysql.connector

# Create a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="naresh",
    password="1234567890",
    database="complaint"
)

# Create a cursor to interact with the database
cursor = db.cursor()

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("400x500")
app.title("Registration")

# Dummy user credentials for demonstration purposes
user_credentials = {}

def register_user():
    new_username = new_user_entry.get()
    new_password = new_pass_entry.get()
    retype_password = retype_pass_entry.get()
    email = email_entry.get()
    contact= contact_entry.get()

    if new_username and new_password and retype_password and email and contact:
        if new_password == retype_password:
            user_credentials[new_username] = new_password

            # Insert user data into the database
            insert_query = "INSERT INTO notesapp(username, password, email, contact) VALUES (%s, %s, %s, %s)"
            data = (new_username, new_password, email, contact)
            cursor.execute(insert_query, data)
            db.commit()

            tkmb.showinfo(title="Registration Successful", message="You have successfully registered.")

            app.after(2000, sign_in)

        else:
            tkmb.showerror(title="Registration Error", message="Passwords do not match.")
    else:
        tkmb.showerror(title="Registration Error", message="All fields are required.")
def sign_in():
    app.destroy()
    import login_page  # Import the login_page code

    # Create an instance of the login page app
    login_app = login_page.app
    login_app.geometry("400x500")  # Set the desired geometry for the login page
    login_app.title("Login")

    # Run the login page app
    login_app.mainloop()

def sign_in():
    app.destroy()
    import login_page  # Import the login_page code

    # Create an instance of the login page app
    login_app = login_page.app
    login_app.geometry("400x500")  # Set the desired geometry for the login page
    login_app.title("Login")

    # Run the login page app
    login_app.mainloop()

# Rest of your code for the registration page remains the same



frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='SIGN UP' ,font=("bold", 20))
label.pack(pady=12, padx=10)

new_user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
new_user_entry.pack(pady=12, padx=10)

new_pass_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
new_pass_entry.pack(pady=12, padx=10)

retype_pass_entry = ctk.CTkEntry(master=frame, placeholder_text="Retype Password", show="*")
retype_pass_entry.pack(pady=12, padx=10)

email_entry = ctk.CTkEntry(master=frame, placeholder_text="Email")
email_entry.pack(pady=12, padx=10)

contact_entry = ctk.CTkEntry(master=frame, placeholder_text="Contact Number")
contact_entry.pack(pady=12, padx=10)

register_button = ctk.CTkButton(master=frame, text='Register', command=register_user)
register_button.pack(pady=12, padx=10)

sign_in_label = ctk.CTkLabel(master=frame, text="Already have an account? ")
sign_in_label.pack(pady=12, padx=10)
register_button = ctk.CTkButton(master=frame, text='login', command=sign_in)
register_button.pack(pady=12, padx=10)
app.mainloop()

