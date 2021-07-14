import streamlit as s
from PIL import Image
import os

@s.cache

def load_image(file):
    image = Image.open(file)
    return image

def main():

    menu = ["Home","Drive", "Login", "SignUp", "About"]

    choice = s.sidebar.selectbox("NavBar",menu)

    if choice == "Home":
        s.title("DaxDrive")
        s.text("Storing Is Important!")
        s.text("-By Priyam Das ")

        image = Image.open("media/img.png")
        s.image(image, width = 700)

    elif choice == "Drive":
        s.title("DaxDrive")
        s.text("Storing Is Important!")
        s.text("")
        s.text("")
        s.warning("Make sure that your file is not more than 200MB.")
        file = s.file_uploader("Upload the file below.", type = ["png", "jpeg", "jpg", "gif"])
        if file is not None:
            s.success("Successfully Uploaded")
            s.image(load_image(file))
            with open(os.path.join("files", file.name), "wb") as f:
                f.write(file.getbuffer())

            s.success("File Saved Successfully")

    elif choice == "Login":
        s.subheader("Work In Progress(Login)")

    elif choice == "SignUp":
        s.subheader("Work In Progress(SignUp)")

    elif choice == "About":
        s.subheader("Work In Progress(About)")    
    
    return main

if __name__ == '__main__':
    main()