import tkinter as tk
import threading
import time

# Autoclicker upgrades are purposely low for your grading purposes.
# The total cookies amount
increase = 0

# The starting cost for each of the upgrades.
upgradecost = 10
upgradecost2 = 1000
upgradecost3 = 10000
upgradecost4 = 10
upgradecost5 = 50
upgradecost6 = 100

# Cookies per click
cpc = 1

# Autoclicker tracker
autoclicker = 0

# Functions
# Cookie Clicking
def picture():
    global increase
    increase += cpc
    label["text"] = increase
# Upgrade functions (Cookies per click upgrades)
def upgrade():
    global increase
    global upgradecost
    global cpc
    if increase >= upgradecost:
        increase -= upgradecost
        upgradecost += 100
        cpc += 2
        label["text"] = increase
        upgradebutton["text"] = f"{upgradecost} Cookies to Upgrade (+2)"
        CPCCount["text"] = f"Cookies Per Click: {cpc}"
    return upgradecost

def upgrade2():
    global increase 
    global upgradecost2
    global cpc
    if increase >= upgradecost2:
        increase -= upgradecost2
        upgradecost2 += 1000
        cpc += 25
        label["text"] = increase
        upgradebutton2["text"] = f"{upgradecost2} Cookies to Upgrade (+25)"
        CPCCount["text"] = f"Cookies Per Click: {cpc}"
    return upgradecost2

def upgrade3():
    global increase
    global upgradecost3
    global cpc
    if increase >= upgradecost3:
        increase -= upgradecost3
        upgradecost3 += 10000
        cpc += 100
        label["text"] = increase
        upgradebutton3["text"] = f"{upgradecost3} Cookies to Upgrade (+100)"
        CPCCount["text"] = f"Cookies Per Click: {cpc}"
    return upgradecost3

# Autoclicker upgrade functions.

def upgrade4():
    global increase
    global upgradecost4
    global cpc
    global autoclicker
    if increase >= upgradecost4:
        increase -= upgradecost4
        upgradecost4 += 10000
        autoclicker = autoclicker + 5
        label["text"] = increase
        upgradebutton4["text"] = f"{upgradecost4} Cookies to Upgrade (Autoclicker +5)"
        return upgradecost4

def upgrade5():
    global increase
    global upgradecost5
    global cpc
    global autoclicker
    if increase >= upgradecost5:
        increase -= upgradecost5
        upgradecost5 += 20000
        autoclicker = autoclicker + 10
        label["text"] = increase
        upgradebutton5["text"] = f"{upgradecost5} Cookies to Upgrade (Autoclicker +10)"
        return upgradecost5

def upgrade6():
    global increase
    global upgradecost6
    global cpc
    global autoclicker
    if increase >= upgradecost6:
        increase -= upgradecost6
        upgradecost6 += 30000
        autoclicker = autoclicker + 25
        label["text"] = increase
        upgradebutton6["text"] = f"{upgradecost6} Cookies to Upgrade (Autoclicker +25)"
        return upgradecost6

# Autoclicker Function
def Autoclicker():
    global autoclicker
    global increase
    while True:
        time.sleep(.5)
        increase = label["text"] + autoclicker
        label["text"] = increase

# Autoclicker Threads
autoclick = threading.Thread(target=Autoclicker)
autoclick.start()

# Title
root = tk.Tk()
root.title("Cookie Clicker")

# Images to use for the upgrades
img = tk.PhotoImage(file="./assets/cookie.png").subsample(3)
img2 = tk.PhotoImage(file="./assets/upgrade1.png").subsample(7)
img3 = tk.PhotoImage(file="./assets/upgrade2.png").subsample(9)
img4 = tk.PhotoImage(file="./assets/upgrade3.png").subsample(7)
img5 = tk.PhotoImage(file="./assets/upgrade4.png").subsample(7)
img6 = tk.PhotoImage(file="./assets/upgrade5.png").subsample(7)
img7 = tk.PhotoImage(file="./assets/upgrade6.png").subsample(7)

# Texts and Buttons
label = tk.Label(root,text=0,font= 500)
label.grid(row=0, column=0)

# This tracks cookie per click whenever the player upgrades.
CPCCount = tk.Label(root,text=f"Cookies Per Click: {cpc}")
CPCCount.grid(row=1,column=0)
ent = tk.Entry()

# Upgrade buttons for better cookies per click, and the autoclicker upgrade.
upgradebutton = tk.Button(root,text=f"{upgradecost} Cookies to Upgrade (+2)",image=img2, compound="left",command=upgrade, font=500)
upgradebutton.grid(row=3, column=0)

upgradebutton2 = tk.Button(root,text=f"{upgradecost2} Cookies to Upgrade (+25)", image=img5, compound = "left", command=upgrade2, font=500)
upgradebutton2.grid(row=4, column=0)

upgradebutton3 = tk.Button(root,text=f"{upgradecost3} Cookies to Upgrade (+100)", image=img3, compound="left", command=upgrade3)
upgradebutton3.grid(row=5, column=0)

upgradebutton4 = tk.Button(root,text=f"{upgradecost4} Cookies to Upgrade (Autoclicker +5)", image=img4, compound="left", command=upgrade4)
upgradebutton4.grid(row=6, column=0)

upgradebutton5 = tk.Button(root, text=f"{upgradecost5} Cookies to Upgrade (Autoclicker +10)", image=img6, compound="left", command=upgrade5)
upgradebutton5.grid(row=7,column=0)

upgradebutton6 = tk.Button(root, text=f"{upgradecost6} Cookies to Upgrade (Autoclicker +20)", image=img7, compound="left", command=upgrade6)
upgradebutton6.grid(row=8,column=0)

# The cookie button to increase the amount of cookies
button = tk.Button(root,image=img, command=picture)
button.grid(row=2, column = 0)

root.mainloop()