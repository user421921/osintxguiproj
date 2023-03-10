import tkinter as tk
import os
from os import system as c

def save_variables():
    global fname, lname, state, city
    fname = fname_entry.get()
    lname = lname_entry.get()
    state = state_entry.get()
    city = city_entry.get()
    #
    c("firefox")
    
    c("start www.fastpeoplesearch.com/name/"+fname+"-"+lname+"_"+city+"-"+state)
    c("start www.searchpeoplefree.com/find/"+fname+"-"+lname+"/"+state+"/"+city)
    c("start www.peoplesearchnow.com/person/"+fname+"-"+lname+"_"+city+"_"+state)
    c("start www.truepeoplesearch.com/results?name="+fname+"-"+lname+"&citystatezip="+city+"-"+state)
    c("start www.spokeo.com/"+fname+"-"+lname+"?loaded=1")
    
    #
    root.destroy()

root = tk.Tk()
root.title("User Information")
root.geometry("300x200")

fname_label = tk.Label(root, text="First Name")
fname_label.pack()
fname_entry = tk.Entry(root)
fname_entry.pack()

lname_label = tk.Label(root, text="Last Name")
lname_label.pack()
lname_entry = tk.Entry(root)
lname_entry.pack()

state_label = tk.Label(root, text="State")
state_label.pack()
state_entry = tk.Entry(root)
state_entry.pack()

city_label = tk.Label(root, text="City")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

save_button = tk.Button(root, text="Save Variables", command=save_variables)
save_button.pack()

root.mainloop()
