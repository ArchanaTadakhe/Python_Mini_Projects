from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as  tk

root =tk.Tk()
root.title("Images Slideshows Viewer")

#List of Image Path

image_paths = [
               r"C:\Users\E080841\OneDrive - MFP Michelin\Pictures\Saved Pictures\Flower.jpeg",
               r"C:\Users\E080841\OneDrive - MFP Michelin\Pictures\Saved Pictures\House.jpeg",r"C:\Users\E080841\OneDrive - MFP Michelin\Pictures\Saved Pictures\Car.jpeg",
    r"C:\Users\E080841\OneDrive - MFP Michelin\Pictures\Saved Pictures\Rabbit.jpeg"]

#Resize image
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]

#PIL method use

photo_images=[ImageTk.PhotoImage(image) for image in images]
label=tk.Label(root)
label.pack()
def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)
slideshow= cycle(photo_images)

def start_slidshow():
    for _ in range(len(image_paths)):
        update_image()
play_button=tk.Button(root,text="Play Slideshow", command=start_slidshow())
play_button.pack()

root.mainloop()


