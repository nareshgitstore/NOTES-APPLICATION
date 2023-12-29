import customtkinter as ctk
import tkinter.messagebox as tkMessageBox

# Create the main application window
app = ctk.CTk()
app.geometry("400x500")
app.title("MAIN")

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create a frame for the page content
page_frame = ctk.CTkFrame(app)
page_frame.pack(fill='both', expand=True)

def sign_up():
    app.destroy()
    import register_page  # Import the register_page code

    # Create an instance of the register page app
    register_app = register_page.app
    register_app.geometry("400x500")  # Set the desired geometry for the registration page
    register_app.title("Registration")

    # Run the registration page app
    register_app.mainloop()

def sign_in():
    app.destroy()
    import login_page  # Import the login_page code

    # Create an instance of the login page app
    login_app = login_page.app
    login_app.geometry("400x500")  # Set the desired geometry for the login page
    login_app.title("Login")

    # Run the login page app
    login_app.mainloop()

# Function to quit the application
def quit_app():
    result = tkMessageBox.askquestion("Quit", "Are you sure you want to close the application?")
    if result == "yes":
        app.destroy()

# Create a masterframe to contain the widgets
masterframe = ctk.CTkFrame(page_frame)
masterframe.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Create the title label inside the masterframe
title_label = ctk.CTkLabel(masterframe, text="COMPLAINT APP", font=("Helvetica", 20))
title_label.pack(pady=20)

# Create Login button inside the masterframe
login_button = ctk.CTkButton(masterframe, text="Login",  font=("Helvetica", 12), command=sign_in)
login_button.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.1)

# Create Signup button inside the masterframe
signup_button = ctk.CTkButton(masterframe, text="Signup",  font=("Helvetica", 12), command=sign_up)
signup_button.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.1)

# Create a Quit button inside the masterframe
quit_button = ctk.CTkButton(page_frame, text="Quit",  font=("Helvetica", 12), command=quit_app)
quit_button.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.1)

# Run the application
app.mainloop()
