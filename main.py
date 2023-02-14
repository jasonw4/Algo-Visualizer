import tkinter as tk
from tkinter import *
from tkinter import ttk

import time


import random

vis = Tk()
vis.wm_title("Algorithm Visualizer")
vis.geometry("1280x800")

#sorting algorithms

def selectionSort(rand_vals, draw, timed):
    for i in range(len(rand_vals)):
        min_idx = i
        for j in range(i+1, len(rand_vals)):
            if rand_vals[min_idx] > rand_vals[j]:
                min_idx = j
        rand_vals[i], rand_vals[min_idx] = rand_vals[min_idx], rand_vals[i]
        draw(rand_vals, ["#FF0000" if x == i or x == i+1 else "#ADD8E6" for x in range(len(rand_vals))])
        time.sleep(timed)
    draw(rand_vals, ["#ADD8E6" for x in range(len(rand_vals))])

def insertionSort(rand_vals, draw, timed):
    for i in range(1, len(rand_vals)):
 
        key = rand_vals[i]
        j = i-1
        while j >= 0 and key < rand_vals[j] :
                rand_vals[j + 1] = rand_vals[j]
                j -= 1
                draw(rand_vals, ["#FF0000" if x == j else "#ADD8E6" for x in range(len(rand_vals))])
        rand_vals[j + 1] = key
    draw(rand_vals, ["#ADD8E6" for x in range(len(rand_vals))])

def quickSort(rand_vals, draw, timed):
    pass

def bubbleSort(rand_vals, draw, timed):
    for i in range(len(rand_vals)):
        for j in range(len(rand_vals)-i - 1):
            if rand_vals[j] > rand_vals[j + 1]:
                rand_vals[j], rand_vals[j + 1] = rand_vals[j + 1], rand_vals[j]
                draw(rand_vals, ["#FF0000" if x == j or x == j+1 else "#ADD8E6" for x in range(len(rand_vals))])
                time.sleep(timed)
    draw(rand_vals, ["#ADD8E6" for x in range(len(rand_vals))])

def mergeSort(maxlist, rand_vals, draw, timed):
    if len(rand_vals) > 1:
        mid = len(rand_vals)//2
        left = rand_vals[:mid]
        right = rand_vals[mid:]
        mergeSort(maxlist, left, draw, timed)
        mergeSort(maxlist, right, draw, timed)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                rand_vals[k] = left[i]
                i += 1
            else:
                rand_vals[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            rand_vals[k] = left[i]
            i += 1
            k += 1
            draw(rand_vals, ["#FF0000" if x == k or x == i else "#ADD8E6" for x in range(len(maxlist))])
 
        while j < len(right):
            rand_vals[k] = right[j]
            j += 1
            k += 1
            draw(rand_vals, ["#FF0000" if x == k or x == j else "#ADD8E6" for x in range(len(maxlist))])
    draw(rand_vals, ["#ADD8E6" for x in range(len(maxlist))])

#simulation
algo_dropdown = StringVar()
algoList = ["Selection Sort", "Insertion Sort", "Quicksort", "Bubble Sort", "Merge Sort"]

rand_vals = []

def draw(rand_vals, color):
    canvas.delete("all")
    canvas_width = 900
    canvas_height = 900
    x_width = canvas_width / len(rand_vals) + 1

    normalized = [i/max(rand_vals) for i in rand_vals]

    for i, height in enumerate(normalized):
        x0 = i*x_width + 6
        y0 = canvas_height - height*750
        x1 = (i+1) * x_width + 4
        y1 = canvas_height
        canvas.create_rectangle(x0, y0-160, x1, y1, fill = color[i])
    
    vis.update_idletasks()

def generate():
    global rand_vals

    rand_vals = []
    for i in range(0, 100):
        rand_vals.append(random.randint(1, 150))
    draw(rand_vals, ["#ADD8E6" for x in range(len(rand_vals))])
    

def sort():
    global rand_vals

    if dropdown.get() == "Bubble Sort":
        bubbleSort(rand_vals, draw, 0.01)
    elif dropdown.get() == "Selection Sort":
        selectionSort(rand_vals, draw, .1)
    elif dropdown.get() == "Insertion Sort":
        insertionSort(rand_vals, draw, .1)
    elif dropdown.get() == "Merge Sort":
        mergeSort(rand_vals, rand_vals, draw, 100)
    elif dropdown.get() == "Quicksort":
        quickSort(rand_vals, draw, 0.1)

#ui
sel_frame = Frame(vis, width = 1000, height = 200, bg = "#FFFFFF")
sel_frame.grid(row = 0, column = 0)

label = Label(sel_frame, text = "Algorithm: ", bg = "#FFFFFF")
label.grid(row = 0, column = 0)

dropdown = ttk.Combobox(sel_frame, textvariable=algo_dropdown, values = algoList)
dropdown.grid(row = 0, column = 1)


gen_array = Button(sel_frame, text = "Generate Array", command = generate, bg = "#FFFFFF")
gen_array.grid(row = 2, column = 0)

sort_button = Button(sel_frame, text = "Sort", command = sort, bg = "#FFFFFF")
sort_button.grid(row = 2, column = 1)


canvas = Canvas(vis, width=1050, height=900, bg="#FFFFFF")
canvas.grid(row=1, column=0, padx=50, pady=10)

#run app
vis.mainloop()

