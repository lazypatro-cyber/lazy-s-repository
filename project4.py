# image slideshow app
# using PIL0
import tkinter as tick
import time
from PIL import Image, ImageTk

#main window 
root= tick.Tk()
root.title("Image Slideshow")
root.geometry("900x900")

#IMAGE PATH
image_paths= [
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img1.png",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img2.png",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img3.png",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img4.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img5.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img6.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img7.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img8.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img9.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img10.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img11.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img12.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img13.jpg",
    r"C:\Users\win11\OneDrive\Pictures\anime wallpaper\img14.jpg",
]

image_size=(700,700)
image=[]
for img in image_paths:
    path= Image.open(img, 'r')
    path= path.resize(image_size)
    image.append(path)

#convert pil into tinkter 
final_image=[]
for imag in image:
    photo = ImageTk.PhotoImage(imag)
    final_image.append(photo)


#label widget 
image_label= tick.Label(root)
image_label.pack(pady=30)

#slideshow function 
def start_slideshow():
    for photo in final_image:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)

#button 
play_button= tick.Button(
    root,
    text= 'slideshow',
    font=('Arial',17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()