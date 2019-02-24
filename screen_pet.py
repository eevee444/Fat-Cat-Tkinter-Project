#Fat Cat
#Author: eevee444
#Last modified date: 2/23/19

from Tkinter import HIDDEN, NORMAL, Tk, Canvas

#Defining blinking
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)
def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

#Defining eye-crossing
def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left,-10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False

#Defining sticking out tongue
def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False
        
#Defining petting
def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <=350):
        c.itemconfigure(blush_left, state=NORMAL)
        c.itemconfigure(blush_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
    return

#Ending petting
def hide_happy(event):
    c.itemconfigure(blush_left, state=HIDDEN)
    c.itemconfigure(blush_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return

#Defining tickling
def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(3000, toggle_tongue)
    root.after(3000, toggle_pupils)
    return

#Canvas
root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg='slateblue', highlightthickness=0)

#Body
c.body_color = 'mediumpurple1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
#Ears
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)

#Feet
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

#Eyes and pupils                     
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_left = c.create_oval(140,145,150, 155, outline='black', fill='black')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black',fill='black')

#Normal mouth
mouth_normal = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=NORMAL)

#Petting face
mouth_happy = c.create_line(170, 250, 200, 292, 230, 250, smooth=1, width=2, state=HIDDEN)
blush_left = c.create_oval(70, 180, 120, 230, outline='hotpink', fill='hotpink', state=HIDDEN)
blush_right = c.create_oval(280, 180, 330, 230, outline='hotpink', fill='hotpink', state=HIDDEN)

#Sad face
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2,state=HIDDEN)
#Tongue
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='deeppink', fill='deeppink', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='deeppink', fill='deeppink', state=HIDDEN)

c.pack()

#Animations
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)

c.eyes_crossed = False
c.tongue_out = False
root.after(1000, blink)
root.mainloop()
