import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

# Define a variable to store the current user's username
current_user = ""
current_psw = ""

# Function to store data in the database
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
            cursor.execute("UPDATE notesapp SET note = %s WHERE username = %s AND password = %s", (data,current_user, current_psw))

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
