import time
from tkinter import *
from tkinter import ttk , colorchooser , messagebox
from PIL import Image , ImageTk , ImageFont , ImageDraw

x_position = 350
y_position = 200
my_color = (0 , 0 , 0)
font_family = "Fonts/FreeMono.ttf"
image_file = "Images/img.png"
# Create Window Frame
window = Tk()
window.minsize(900 , 900)
window.config(bg='#95d3f5')


# ------------- Update an Image ---------------------------#
def see() :
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
    global real_image
    real_image = Image.open(image_file)
    text_font = ImageFont.truetype(size=font_size , font=font_family)
    text_to_insert = text_entry.get()
    edit_image = ImageDraw.Draw(real_image)
    edit_image.text((x_position , y_position) , text_to_insert , my_color , font=text_font)
    real_image.save('result.png')
    global image2
    image2 = PhotoImage(file='result.png')
    canvas.itemconfig(image_container , image=image2)


# ---------- Create a canvas ------------------#
canvas = Canvas(window , width=900 , height=900,bg='#95d3f5')
canvas.place(x=0 , y=0)

# -------------------- Open an Image ------------------------#
image1 = ImageTk.PhotoImage(file=image_file)

image2 = PhotoImage(file='result.png')

# Add image to the canvas
image_container = canvas.create_image(70 , 20 , anchor="nw" , image=image1)

# ----------------- Text entry ---------------------#
text_entry = Entry(window , width=20)
text_entry.insert(0 , "Add text")
text_entry.place(x=70 , y=650)


# -------- Color Choser---------------#
def color() :
    global my_color
    my_color = colorchooser.askcolor()[0]
    see()


ask_color = ttk.Button(text="Choose color" , command=color)
ask_color.place(x=240 , y=650)
# ------------------- Font Size Selector -----------------------#

font_size_lbl = ttk.Label(window , text="Font size")
font_size_lbl.place(x=350 , y=650)
ask_font_size = Entry(window , width=8)
ask_font_size.insert(0 , '20')
ask_font_size.place(x=410 , y=650)


# ------------- Font Family OptionMenu -----------------#
def select(family) :
    global font_family
    font_family = f"Fonts/{family}.ttf"
    see()


font_family_lbl = Label(text="Font Family")
font_family_lbl.place(x=500 , y=650)
menu = StringVar()
drop_option = ttk.OptionMenu(window , menu , 'FreeMono' , 'FreeMono' , 'LondrinaOutline-Regular' ,
                             'PassionsConflict-Regular' , 'SansitaSwashed-VariableFont_wght' , command=select)
drop_option.config(width=15)
drop_option.place(x=580 , y=650)


# ------------- Change Image When Enter Key is pressed ---------------------------------------#


def entered(e) :
    see()  # Call function see


window.bind('<Return>' , entered)  # To bind 'Enter' key


# -------------------- Double click on mouse to select position --------------------#
position_info = ttk.Label(window,text="Double tap on image for a position.")
position_info.config(background= '#95d3f5')
position_info.place(x=70,y=600)
def mouse(p) :
    global x_position , y_position
    x_position = p.x-70
    y_position = p.y-20
    see()


window.bind('<Double-Button-1>' , mouse)


# ------------- Update an Image -----------------------#
def updated() :
    see()


update = ttk.Button(text="Update" , command=updated)
update.place(x=740 , y=650)


# --------------------- Save and Exit ------------------------------#


def save() :
    see()
    save_exit = messagebox.askyesno("Save and Exit" , message='Do you want to exit!')
    if save_exit :
        window.quit()


save_exit_btn = ttk.Button(text="Save and Exit" , command=save)
save_exit_btn.place(x=400 , y=700)

window.mainloop()
