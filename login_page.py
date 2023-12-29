import tkinter.messagebox as tkmb
import mysql.connector
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
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
# Selecting GUI theme - dark, light, system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("400x500")
app.title("Login")
show_password_var = tk.BooleanVar()
show_password_var.set(False)
def sign_up():
    app.destroy()
    import register_page  # Import the register_page code

    # Create an instance of the register page app
    register_app = register_page.app
    register_app.geometry("400x550")  # Set the desired geometry for the registration page
    register_app.title("Registration")

    # Run the registration page app
    register_app.mainloop()
def toggle_password_visibility():
    global show_password_var
    show_password = show_password_var.get()
    if show_password:
        user_pass.configure(show="")
    else:
        user_pass.configure(show="*")

def login():
    global current_user, current_psw
    username = user_entry.get()
    password = user_pass.get()

    # Retrieve user data from the database
    cursor.execute("SELECT note FROM notesapp WHERE username = %s AND password = %s", (username, password))
    user_data = cursor.fetchall()

    if user_data:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully")

        # Update the global variables with the new username and password
        current_user = username
        current_psw = password
        user_entry.delete(0, 'end')
        user_pass.delete(0, 'end')
        # Schedule the function to open the notes page after 2000 milliseconds (2 seconds)
        app.after(1000, open_notes_page, app, current_user, current_psw)  # Pass the arguments here

    else:
        tkmb.showwarning(title='Wrong credentials', message='Please check your username and password')

def open_notes_page(app, current_user, current_psw):
    # Create the main application window using customtkinter
    app = ctk.CTk()
    app.title("Notes Application")
    app.geometry("400x550")


    # Define a variable to store the current user's username
    current_user = ""
    current_psw = ""

    def store_data():
        global current_user, current_psw
        data = app.text_input.get("1.0", "end-1c")
        if data:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="naresh",
                    password="1234567890",
                    database="complaint"
                )
                cursor = connection.cursor()

                # Use the current username to insert data for the current user
                cursor.execute("UPDATE notesapp SET note = %s WHERE username = %s AND password = %s",
                               (data, current_user, current_psw))

                connection.commit()
                connection.close()

                messagebox.showinfo("Success", "Data stored successfully!")

                # Clear the input text field after storing data
                app.text_input.delete("1.0", "end")
            except Exception as e:
                messagebox.showerror("Error", f"Error storing data: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter some information.")

    # Function to view data from the database
    def view_data():
        global current_user, current_psw
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="naresh",
                password="1234567890",
                database="complaint"
            )
            cursor = connection.cursor()

            # Use the current_user variable to retrieve data for the current user
            cursor.execute("SELECT note FROM notesapp WHERE username=%s AND password=%s", (current_user, current_psw))

            result = cursor.fetchall()
            connection.close()

            if result:
                # Convert the list to a string and insert it into the text widget
                note_text = str(result[0][0])
                app.text_input.delete("1.0", "end")
                app.text_input.insert("1.0", note_text)
            else:
                app.text_input.delete("1.0", "end")
                messagebox.showinfo("Information", "No data found for the specified user.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error connecting to MySQL: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"Error retrieving data: {e}")

    # Function to clear the input text field
    def clear_text():
        app.text_input.delete("1.0", "end")

    # Create the main application window using customtkinter
    app = ctk.CTk()
    app.title("Notes Application")
    app.geometry("400x550")

    # Create the title label
    title_label = ctk.CTkLabel(app, text="NOTES", font=("Helvetica", 20))
    title_label.pack(pady=20)

    # Create the input text area
    app.text_input = ctk.CTkTextbox(app, height=250, width=250)
    app.text_input.pack()

    # Create the Store button
    store_button = ctk.CTkButton(app, text="Store", command=store_data)
    store_button.pack(pady=10)

    # Create the View button
    view_button = ctk.CTkButton(app, text="View", command=view_data)
    view_button.pack(pady=10)

    # Create the Clear button
    clear_button = ctk.CTkButton(app, text="Clear", command=clear_text)
    clear_button.pack(pady=10)

    # Run the application
    app.mainloop()



def forgot_password():
    def reset_password():
        username = reset_user_entry.get()
        email = reset_email_entry.get()

        # Check if the username and email exist in the database
        cursor.execute("SELECT * FROM notesapp WHERE username = %s AND email = %s", (username, email))
        user_data = cursor.fetchone()

        if user_data:
            new_password = reset_pass_entry.get()
            # Update the password in the database
            update_query = "UPDATE notesapp SET password = %s WHERE username = %s"
            data = (new_password, username)
            cursor.execute(update_query, data)
            db.commit()
            tkmb.showinfo(title="Password Reset", message="Password has been reset successfully.")
            reset_window.destroy()
            app.deiconify()  # Reopen the login page
        else:
            tkmb.showerror(title="Invalid Username or Email", message="Username or email not found in the database.")

    def back_to_login():
        reset_window.destroy()
        app.deiconify()  # Reopen the login page

    app.withdraw()  # Hide the login page
    reset_window = ctk.CTkToplevel(app)
    reset_window.title("Forgot Password")
    reset_window.geometry("400x500")

    ctk.CTkLabel(reset_window, text="Enter your username:").pack(pady=5)
    reset_user_entry = ctk.CTkEntry(reset_window, placeholder_text="Username")
    reset_user_entry.pack(pady=5)

    ctk.CTkLabel(reset_window, text="Enter your email:").pack(pady=5)
    reset_email_entry = ctk.CTkEntry(reset_window, placeholder_text="Email")
    reset_email_entry.pack(pady=5)

    ctk.CTkLabel(reset_window, text="Enter your new password:").pack(pady=5)
    reset_pass_entry = ctk.CTkEntry(reset_window, placeholder_text="New Password", show="*")
    reset_pass_entry.pack(pady=5)

    reset_button = ctk.CTkButton(reset_window, text='Reset Password', command=reset_password)
    reset_button.pack(pady=10)

    back_to_login_button = ctk.CTkButton(reset_window, text='Back to Login', command=back_to_login)
    back_to_login_button.pack(pady=10)



def open_registration_page(event):
    def register_user():
        new_username = new_user_entry.get()
        new_password = new_pass_entry.get()

        if new_username and new_password:
            # Insert user data into the database
            insert_query = "INSERT INTO notesapp(username, password) VALUES (%s, %s)"
            data = (new_username, new_password)
            cursor.execute(insert_query, data)
            db.commit()

            tkmb.showinfo(title="Registration Successful", message="You have successfully registered.")
            register_window.destroy()
        else:
            tkmb.showerror(title="Registration Error", message="Username and password cannot be empty.")

    register_window = ctk.CTkToplevel(app)
    register_window.title("Sign Up")
    register_window.geometry("400x500")

    ctk.CTkLabel(register_window, text="Enter your username:").pack(pady=5)
    new_user_entry = ctk.CTkEntry(register_window, placeholder_text="Username")
    new_user_entry.pack(pady=5)

    ctk.CTkLabel(register_window, text="Enter your password:").pack(pady=5)
    new_pass_entry = ctk.CTkEntry(register_window, placeholder_text="Password", show="*")
    new_pass_entry.pack(pady=5)

    register_button = ctk.CTkButton(register_window, text='Register', command=register_user)
    register_button.pack(pady=10)

label = ctk.CTkLabel(app, text="WELCOME BACK")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='LOGIN')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

show_password_checkbox = ctk.CTkCheckBox(master=frame, text='Show Password', variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.pack(pady=5, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

forgot_pass_label = ctk.CTkLabel(master=frame, text='Forgot Password?')
forgot_pass_label.pack(pady=5, padx=10)
forgot_pass_label.configure(cursor="hand2")
forgot_pass_label.bind("<Button-1>", lambda event: forgot_password())

register_button = ctk.CTkButton(master=frame, text='Sign up', command=sign_up)
register_button.pack(pady=12, padx=10)

app.mainloop()
