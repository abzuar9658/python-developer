import tkinter as tk
from PIL import Image, ImageTk

def center_image_with_text(window, image_path, text_to_display):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Create a canvas to display the image
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.grid(row=0, column=0, padx=5, pady=5)

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Calculate the position for the text to be centered
    x_center = image.width // 2
    y_center = image.height // 2

    # Display the text on the canvas
    canvas.create_text(x_center, y_center, text=text_to_display, font=("Arial", 20), fill="white", anchor=tk.CENTER)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Text on Image Example")
    root.geometry("500x500")

    # Set the path to the image you want to display
    image_path = "tomato.png"

    # Set the text you want to display on top of the image
    text_to_display = "Hello, Tkinter!"

    # Display the image and text on the canvas
    center_image_with_text(root, image_path, text_to_display)

    # Start the tkinter main loop
    root.mainloop()
