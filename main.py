from tkinter import *
from tkinter import ttk , colorchooser , messagebox
from PIL import Image, ImageFont , ImageDraw
from tkinter import filedialog
from PIL.Image import Resampling

#--------------- Text on image -------------------------------#
x_position = 350           # text position
y_position = 200
my_color = (0 , 0 , 0)      # text color

font_family = "Fonts/FreeMono.ttf" # text font family

#------------------------------- Select an image from a directory ----------------------------------#
image_file = filedialog.askopenfile(initialdir='/',title="Select image",filetypes=[("Png files","*.png*"),("Png files","*.jpg*")]).name

# Create Window Frame
window = Tk()
window.minsize(900 , 900)
window.resizable(False,False)
window.config(bg='#95d3f5')


# ------------- Update an Image ---------------------------#
def update() :
    #------------ Exception handling for a font size --------------------#
    try :
        usr_fnt_sz = int(ask_font_size.get())
    except ValueError :
        font_size = 20

    else :
        if usr_fnt_sz > 5 :
            font_size = usr_fnt_sz
        else :
            font_size = 20
    # Save Image with changes
    global resized_image
    resized_image = Image.open(image_file).resize((770,600),Resampling.LANCZOS) #resizing the image
    text_font = ImageFont.truetype(size=font_size , font=font_family)
    text_to_insert = text_entry.get()
    edit_image = ImageDraw.Draw(resized_image)
    edit_image.text((x_position , y_position) , text_to_insert , my_color , font=text_font)
    resized_image.save("result.png")
    global image2
    image2 = PhotoImage(file="result.png")
    canvas.itemconfig(image_container , image=image2)


# ---------- Create a canvas ------------------#
canvas = Canvas(window , width=900 , height=900,bg='#95d3f5')
canvas.place(x=0 , y=0)

# Add image to the canvas
image_container = canvas.create_image(70 , 20 , anchor="nw")

# ----------------- Text entry ---------------------#
text_entry = Entry(window , width=20)
text_entry.insert(0 , "Add text")
text_entry.place(x=115 , y=650)


# -------- Color Choser---------------#
def color() :
    global my_color
    my_color = colorchooser.askcolor()[0]
    update()


ask_color = ttk.Button(text="Choose color" , command=color)
ask_color.place(x=285 , y=650)

# ------------------- Font Size Selector -----------------------#

font_size_lbl = ttk.Label(window , text="Font size")
font_size_lbl.place(x=395 , y=650)
ask_font_size = Entry(window , width=8)
ask_font_size.insert(0 , '20')
ask_font_size.place(x=455 , y=650)


# ------------- Font Family OptionMenu -----------------#
def select(family) :
    global font_family
    font_family = f"Fonts/{family}.ttf"
    update()


font_family_lbl = Label(text="Font Family")
font_family_lbl.place(x=545 , y=650)
menu = StringVar()
drop_option = ttk.OptionMenu(window , menu , 'FreeMono' , 'FreeMono' , 'LondrinaOutline-Regular' ,
                             'PassionsConflict-Regular' , 'SansitaSwashed-VariableFont_wght' , command=select)
drop_option.config(width=15)
drop_option.place(x=625 , y=650)


# ------------- Change an Image When Enter Key is pressed ---------------------------------------#


def entered(e) :
    update()  # Call function see


window.bind('<Return>' , entered)  # To bind 'Enter' key
# ------------- Change an ImageText When Key is pressed ---------------------------------------#
def key_pressed(e) :
    entry = str(text_entry.focus_get())
    if entry == ".!entry":
        update()  # Call function see


window.bind('<Key>' , key_pressed)

# --------------------  Inserted text position control --------------------#
position_info = ttk.Label(window,text="Double tap on image for a position or use arrow keys.")
position_info.config(background= '#95d3f5')
position_info.place(x=95,y=625)
def mouse(p) :
    global x_position , y_position
    x_position = p.x-70
    y_position = p.y-20
    update()

def up(e):
    global  y_position
    y_position -= 10
    update()
def down(e):
    global  y_position
    y_position += 10
    update()
def right(e):
    global  x_position
    x_position += 10
    update()
def left(e):
    global  x_position
    x_position -= 10
    update()
window.bind('<Up>' , up)
window.bind('<Down>' , down)
window.bind('<Left>' , left)
window.bind('<Right>' , right)
window.bind('<Double-Button-1>' , mouse)


# --------------------- Save and Exit ------------------------------#
def save() :
    update()
    global resized_image
    files = [("png","*.png*")]
    file = filedialog.asksaveasfile(filetypes=files, defaultextension='.png').name
    resized_image.save(file)
    save_exit = messagebox.askyesno("Save and Exit" , message='Do you want to exit!')
    if save_exit :
        window.quit()

save_exit_btn = ttk.Button(text="Save" , command=save)
save_exit_btn.place(x=400 , y=700)
update()
window.mainloop()
