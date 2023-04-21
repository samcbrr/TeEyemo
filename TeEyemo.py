import tkinter as tk
import webbrowser as wb
from tkinter import messagebox
from tkinter import scrolledtext as st
from tkinter.simpledialog import askstring
import datetime
import pyttsx3

root = tk.Tk()
root.geometry('700x780')
root.title("Te Eyemo")
root.configure(bg='#fff875')
root.iconphoto(True, tk.PhotoImage(file='icon.png'))

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.say('')
engine.runAndWait()
engine.setProperty('rate', 165)

my_voice = messagebox.askquestion("Setting up (1/2)", "Hi! Do you prefer a male voiceover?")
if my_voice == 'yes':
    my_voice = engine.setProperty('voice', voices[0].id)
else:
    my_voice = engine.setProperty('voice', voices[1].id)

name = tk.simpledialog.askstring('Setting up (2/2)', 'Kindly input your nickname:')
messagebox.showinfo("", "Are you ready? Let's go!")

engine.say(name + ',' + 'Welcome to T Eyemo!')
engine.runAndWait()

upper_frame = tk.Frame(root, bg='black', bd=10)
upper_frame.place(relx=0.5, relwidth=1, relheight=0.175, anchor='n')

mid_frame = tk.Frame(root, bg='black')
mid_frame.place(relx=0.5, rely=0.212, relwidth=0.9, relheight=0.555, anchor='n')

lower_frame = tk.Frame(root, bg='black', bd=10)
lower_frame.place(relx=0.5, rely=0.785, relwidth=0.9, relheight=0.175, anchor='n')

label_1A = tk.Label(upper_frame, text="Welcome to Te Eyemo: Love your Eyes Project!",
                    bg='black', fg='white', font=("Rockwell", 15))
label_1A.place(rely=0.05, relwidth=1, relheight=0.275)
label_1B = tk.Label(upper_frame, text="(We encourage you to answer our survey above, to help us improve this program.)",
                    bg='black', fg='white', font=("Rockwell", 10))
label_1B.place(rely=0.3, relwidth=1, relheight=0.2)

label_3 = tk.Label(lower_frame, text="Try Te Eyemo's other features to avoid digital eyestrain and its symptoms!",
                   bg='black', fg='white', font=("Rockwell", 12))
label_3.place(relwidth=1, relheight=0.2)


def finding1():
    text_area = st.ScrolledText(mid_frame, width=30, height=8, font=("Arial", 12))
    text_area.place(rely=0.27, relwidth=1, relheight=0.74)
    text_area.insert(tk.INSERT,
                     """
                                                                       OH NO! 
                                DON'T WORRY THOUGH, BECAUSE WE GOT YOU!

WHAT IS EYESTRAIN? 
    The term eyestrain describes a group of symptoms which occur in some people after extended use of the eyes. Although eyestrain can be uncomfortable, it does   not lead to any eye damage.

WHY AM I EXPERIENCING EYESTRAIN?
    One of the biggest causes of eyestrain is the daily use of digital screens for several     hours at a time. The following scenarios could cause a digital eyestrain:

-Maintaining poor posture when viewing a digital device
-Failing to blink as often as normal 
-Holding a digital device too far or too close to your eyes 
-Being exposed to extended amounts of blue light, which is the light commonly emitted     from digital devices 
-Viewing a screen that does not have properly adjusted lighting 

WHAT CAN I DO ABOUT IT?
    Practice the following routines to avoid the symptoms of digital eyestrain:

-Reduce the blue light of your device and adjust the brightness of it
-Use a doctor prescribed computer glasses
-Keep the right distance to your device
-Use Te Eyemo's features below to avoid eyestrain and its symptoms

WHEN SHOULD I CONSULT AN EYE DOCTOR?
    Eyestrain cases can mostly recover with proper device use and proper eye care rou-    tines, but if you experience an eyestrain that is severe and prolonged, better consult it with your eye doctor.
                    """)
    text_area.configure(state='disabled')


def finding2():
    text_area = st.ScrolledText(mid_frame, width=30, height=8, font=("Arial", 12))
    text_area.place(rely=0.27, relwidth=1, relheight=0.74)
    text_area.insert(tk.INSERT,
                     """
                                                              GOOD FOR YOU!
                              BUT HERE ARE SOME THINGS YOU SHOULD KNOW

WHAT IS BLUE LIGHT?
    -Blue light is emitted by digital electronic devices, but it only produce a fraction of what is emitted by the sun.
    -Visible blue light passes the cornea and lens, and reaches the retina.
    -Prolonged use of digital electronic devices causes eyestrain and other related symp- toms.
    -Overexposure to blue light can damage the retina and may lead to macular degenera-  tion and vision loss.
    -Blue light is essential in regulating circadian rhythm, however, exposure to it at late      night can disrupt the cycle, causing sleepless nights and daytime fatigue.

EYESTRAIN SYMPTOMS:
    - Sore, tired, burning or itching eyes 
    - Watery or dry eyes 
    - Difficulty concentrating 
    - Blurred or double vision 
    - Headache 
    - Feeling that you cannot keep your eyes open 
    - Increased sensitivity to light 
    - Pain or strain in the neck, shoulders or back 

TIPS TO AVOID EYESTRAIN:
    - Reduce blue light: Adjust the color temperature of your screen to “warmer” colors such  as red and orange to reduce blue light emission, which can also cause eye strain. 
    - Reduce glare: Purchase an anti-glare screen that can be installed on your computer. Additionally, if you already wear corrective eyeglasses, make sure that your lenses are   made with anti-reflective (AR) coatings. 
    - Computer glasses: Computer glasses may be a good option if you spend many hours on a computer, even if you don’t usually wear glasses for distance or reading. 
    - Brightness: Adjust the brightness of your screen so it’s similar to the brightness of      your room. 
    - Keep blinking: To avoid dry eyes, try to remember to blink 10 times (with full eyelid    closure), every 20 minutes. 
    - Employ the 20-20-20 rule: o reduce the risk of tired eyes by constantly focusing on     your screen, look away from your computer at least every 20 minutes and gaze at an object at least 20 feet away for a minimum of 20 seconds. 
    - Use Eye Drops: When you blink less, your eyes can get dry and irritated. You can re-   solve this with the use of eye drops like artificial tears.

WHEN TO CONSULT AN EYE DOCTOR?
    Eyestrain cases can mostly recover with proper device use and proper eye care rou-    tines, but if you experience an eyestrain that is severe and prolonged, better   consult it with your eye doctor.
                    """)
    text_area.configure(state='disabled')


def start():
    cb1a = tk.Label(mid_frame, bg='black', fg='white', text='Are you experiencing digital eyestrain symptoms like: ',
                   font=('Rockwell', 12))
    cb1a.place(relwidth=1, relheight=0.1)
    cb1b = tk.Label(mid_frame, bg='black', fg='white', text="Headaches, Irritated eyes, Blurred/double vision, and Back/neck pain?",
                   font=('Rockwell', 11))
    cb1b.place(rely=0.075, relwidth=1, relheight=0.1)
    button_4 = tk.Button(mid_frame, text="Yes", command=finding1)  # for Yes
    button_4.place(relx=0.275, rely=0.17, relwidth=0.2, relheight=0.06)
    button_5 = tk.Button(mid_frame, text="No", command=finding2)  # for No
    button_5.place(relx=0.55, rely=0.17, relwidth=0.22, relheight=0.06)

button_1 = tk.Button(upper_frame, text="Get Started!", bg='white', fg='black', command=start)
button_1.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.3)


def timer(a=1200):
    if a > 0:
        root.after(1000, timer, a-1)
        a = (datetime.timedelta(seconds=a))
    else:
        engine.say(
            'Eye Break, ' + name + ', Have you looked at something 20 feet away for 20 seconds? If not, let me countdown for you.')
        engine.runAndWait()
        result = messagebox.askquestion("Eye Break!",
                                        "Done?")
        if result == 'no':
            try:
                d = 20
                if d > 0:
                    root.after(1000, timer, d - 1)
                    d = (datetime.timedelta(seconds=d))
            except:
                return
            timer_label['text'] = d
        else:
            engine.say('''That's good to know!''')
            engine.runAndWait()
    timer_label['text'] = a

timer_label = tk.Label(lower_frame)
timer_label.place(relx=0.10, rely=0.65, relwidth=0.25, relheight=0.2)


def reminder1(b=3000):
    if b > 0:
        root.after(1000, reminder1, b-1)
        b = (datetime.timedelta(seconds=b))
    else:
        engine.say(name + ''', It's Work break!, Stretch those arms, and take a deep breath!''')
        engine.runAndWait()
        messagebox.showinfo("Work break!",
                            "Done?'")
    label_r1['text'] = b

label_r1 = tk.Label(lower_frame)
label_r1.place(relx=0.375, rely=0.65, relwidth=0.25, relheight=0.2)


def reminder2(c=5400):
    if c > 0:
        root.after(1000, reminder2, c-1)
        c = (datetime.timedelta(seconds=c))
    else:
        engine.say('Water break!, Drink your water bitch!')
        engine.runAndWait()
        messagebox.showinfo("Water break!",
                            "Water keeps our body hydrated and our brain energized, now drink up!")
    label_r2['text'] = c

label_r2 = tk.Label(lower_frame)
label_r2.place(relx=0.65, rely=0.65, relwidth=0.25, relheight=0.2)

instruction = tk.Label(lower_frame, text='(To restart a certain feature after it is done, just press its button again.)',
                       bg='black', fg='white', font=("Rockwell", 10))
instruction.place(rely=0.88, relwidth=1, relheight=0.175)
feature_1 = tk.Button(lower_frame, text="20-20-20 Rule", command=timer)
feature_1.place(relx=0.10, rely=0.325, relwidth=0.25, relheight=0.3)
feature_2 = tk.Button(lower_frame, text="Desk Exercise Reminder", command=reminder1)
feature_2.place(relx=0.375, rely=0.325, relwidth=0.25, relheight=0.3)
feature_3 = tk.Button(lower_frame, text="Water Break Reminder", command=reminder2)
feature_3.place(relx=0.65, rely=0.325, relwidth=0.25, relheight=0.3)


def signup():
    wb.open('https://forms.gle/ipsNGJrmuTNwrDkK7')

menubar = tk.Menu(root, activeforeground='black', bg='#DEB887')
menubar.add_command(label="Hello " + name + ", can you spare us some time to answer a survey?", command=signup)
root.config(menu=menubar)

root.mainloop()
