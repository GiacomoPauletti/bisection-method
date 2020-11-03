import tkinter as tk
from tkinter import ttk
import math
from math import ceil, floor, e, log
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import *
from re import findall
from bisection_method import bisection


#creating the main window
root = tk.Tk()
root.title("bisection method")
 
#USER INPUTS
func_choosen=tk.StringVar()

a_value=tk.StringVar()
b_value=tk.StringVar()
c_value=tk.StringVar()
q_value=tk.StringVar()

left_point_value=tk.StringVar()
left_point_value.set('-69')
right_point_value=tk.StringVar()
right_point_value.set('69')
precision_value=tk.StringVar()

#DEFAULT VALUES FOR USER INPUTS
a_value.set('a')
b_value.set('b')
c_value.set('c')
q_value.set('q')



funcs = {
	'' : ('', ''),
	'constant': (x3 , f'y = {q_value.get()}'),
	'identity': (x3, f'y = {c_value.get()}*x + {q_value.get()}'),
	'parable': (x3, f'y = {b_value.get()}*x^2 + {c_value.get()}*x + {q_value.get()}'),
	'x cubed': (x3, f'y = {a_value.get()}*x^3 + {b_value.get()}*x^2 + {c_value.get()}*x + {q_value.get()}'),
	'exponential': (exponential, f'y = {c_value.get()}*{a_value.get()}^{b_value.get()}x + {q_value.get()}'),
	'logarithm': (logarithm, f'y = {c_value.get()}*log(x + {b_value.get()}, {a_value.get()}) + {q_value.get()}'),
	'sin': (sin, f'y = {a_value.get()}*sin(x + {b_value.get()}) + {q_value.get()}'),
	'cosin': (cosin, f'y = {a_value.get()}*sin(x + {b_value.get()}) + {q_value.get()}')
}

def reload_funcs():
	global funcs

	funcs = {
		'' : ('', ''),
		'constant': (x3 , f'y = {q_value.get()}'),
		'identity': (x3, f'y = {c_value.get()}*x + {q_value.get()}'),
		'parable': (x3, f'y = {b_value.get()}*x^2 + {c_value.get()}*x + {q_value.get()}'),
		'x cubed': (x3, f'y = {a_value.get()}*x^3 + {b_value.get()}*x^2 + {c_value.get()}*x + {q_value.get()}'),
		'exponential': (exponential, f'y = {c_value.get()}*{a_value.get()}^{b_value.get()}x + {q_value.get()}'),
		'logarithm': (logarithm, f'y = {c_value.get()}*log(x + {b_value.get()}, {a_value.get()}) + {q_value.get()}'),
		'sin': (sin, f'y = {a_value.get()}*sin(x + {b_value.get()}) + {q_value.get()}'),
		'cosin': (cosin, f'y = {a_value.get()}*sin(x + {b_value.get()}) + {q_value.get()}')
	}


def show_func(*args):
	reload_funcs()
	global funcs

	current_function.set(funcs[func_choosen.get()][1])


def draw_g():
	reload_funcs()
	global funcs

	av=a_value.get(); bv=b_value.get(); cv=c_value.get(); qv=q_value.get()
	for index, v in enumerate([av, bv, cv, qv]):
		if findall('[a-z-A-Z]', v):
			[av, bv, cv, qv][index] = 0

	
	draw_graph(funcs[func_choosen.get()][0], a=float(a_value.get()), b=float(b_value.get()), c=float(c_value.get()), q=float(q_value.get()))


#function which draws the graph in the graph frame
def draw_graph(funzione, **kwargs):
	#clearing the previous graph
	if len(graph_frm.slaves()) != 0:
		for slave in graph_frm.slaves():
			slave.destroy()

	#settign the graph and implementing it in tkinter
	fig = plt.Figure(figsize=(4,3), dpi=100)
	a = fig.add_subplot(111)
	canvas = FigureCanvasTkAgg(fig, master=graph_frm)
	canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

	#gainign x and y values (and so we have points (x0, y0))
	x = np.arange(-10,10,0.1) if func_choosen.get() != 'logarithm' else np.arange(-1*float(b_value.get()) + 0.1, -1*float(b_value.get()) + 20, 0.1)
	y = funzione(x, **kwargs)
	result = zip(x,y)

	#drawing the function
	for item in tuple(result):
	    a.plot(x, y)

	a.axhline(0, color='black')
	a.axvline(0, color='black')
	canvas.draw()


def bisect():
	reload_funcs()
	global funcs

	funcz=funcs[func_choosen.get()][0]
	intersection_value.set(str(bisezione(f=funcz, 
										intervallo=[float(left_point_value.get()), float(right_point_value.get())], 
										precisione=float(precision_value.get()), 
										a=float(a_value.get()), 
										b=float(b_value.get()), 
										c=float(c_value.get()), 
										q=float(q_value.get()))))


#SETTING A TRACER/OBSERVER FOR USER INPUTS
func_choosen_obs=func_choosen.trace('w', show_func)
a_value_obs=a_value.trace('w', show_func)
b_value_obs=b_value.trace('w', show_func)
c_value_obs=c_value.trace('w', show_func)
q_value_obs=q_value.trace('w', show_func)



#3 MAIN FRAMES
#--------------------------------------------------------------------
#setting frame: the frame where all the settings of the function will be placed
setting_frm = tk.Frame(master=root, width=450, height=501, borderwidth=3, relief=tk.SUNKEN)
setting_frm.columnconfigure(0, weight=1, minsize=math.ceil(int(setting_frm["width"])))
setting_frm.rowconfigure([i for i in range(10)] , weight=1, minsize=math.ceil(int(setting_frm["height"])/15))
#graphic frame: the frame where the equation will be drawn
graph_frm = tk.Frame(master=root, width=450, height=334, borderwidth=3, relief=tk.SUNKEN)

#function frame: the frame where the mathematical function will be displayed
result_frm = tk.Frame(master=root, width=450, height=167, borderwidth=3, relief=tk.SUNKEN)

setting_frm.grid(column=0, row=0, rowspan=3)
graph_frm.grid(column=1, row=0, rowspan=2)
result_frm.grid(column=1, row=2)




#THE SETTING FRAME
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#creating 10 frames (rows) to visually organize the space
frames=[]
for col in range(1):
	frames.append([])
	for row in range(15):
		frame=tk.Frame(master=setting_frm, width=int(setting_frm["width"]), height=int(setting_frm["height"])/15, borderwidth=1)#, relief=tk.SUNKEN)
		frame.grid(column=col, row=row, sticky="nsew")

		#appending the frames into a list. This list will containt the frames subdivided by their column (so there will be 4 subarray)
		frames[col].append(frame)
#--------------------------------------------------------------------

title_lbl=tk.Label(master=frames[0][0], text="SETTINGS SECTION", font=("MS Comic Sans", 15))
title_lbl.pack(fill=tk.BOTH, expand=True)

#FUNCTION SELECTION
#label which describes the use of the combobox
info_lbl=tk.Label(master=frames[0][1], width=30, text="Select the function", font=("Verdana", 10), borderwidth=1, relief=tk.SUNKEN)
info_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#creating the combobox to choose the function that will be analized
#func_choosen=tk.StringVar()
func_cmbox=ttk.Combobox(master=frames[0][1], width=30, textvariable=func_choosen)
func_cmbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#all the possible functions
func_cmbox['values'] = ('',
						'constant',
						'identity',
						'parable',
						'x cubed',
						'exponential',
						'logarithm',
						'sin',
						'cosin')

#setting the default value to None
func_cmbox.current()
#--------------------------------------------------------------------


#FUNCTION COEFFICIENTS

coeff_info_lbl=tk.Label(master=frames[0][3], text="Coefficients of the function (shown in the bottom-right section)", font=("MS Comic Sans", 12), anchor="w")
coeff_info_lbl.pack(fill=tk.BOTH, expand=True)

#entries to input a, b, c and q
a_lbl=tk.Label(master=frames[0][4], width=7, text="a", font=("Verdana", 10), borderwidth=1, relief=tk.SUNKEN)
a_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#a_value=tk.StringVar()
a_ent=tk.Entry(master=frames[0][4], width=22, textvariable=a_value)
a_ent.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


b_lbl=tk.Label(master=frames[0][4], width=7, text="b", font=("Verdana", 10), borderwidth=1, relief=tk.SUNKEN)
b_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#b_value=tk.StringVar()
b_ent=tk.Entry(master=frames[0][4], width=22, textvariable=b_value)
b_ent.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


c_lbl=tk.Label(master=frames[0][5], width=7, text="c", font=("Verdana", 10), borderwidth=1, relief=tk.SUNKEN)
c_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#c_value=tk.StringVar()
c_ent=tk.Entry(master=frames[0][5], width=22, textvariable=c_value)
c_ent.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


q_lbl=tk.Label(master=frames[0][5], width=7, text="q", font=("Verdana", 10), borderwidth=1, relief=tk.SUNKEN)
q_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#q_value=tk.StringVar()
q_ent=tk.Entry(master=frames[0][5], width=22, textvariable=q_value)
q_ent.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#--------------------------------------------------------------------


#SET BOUNDS

set_lbl=tk.Label(master=frames[0][7], text="Insert the bound points of the set", font=("MS Comic Sans", 12), anchor="w")
set_lbl.pack(fill=tk.BOTH, expand=True)


left_point_lbl=tk.Label(master=frames[0][8], width=30, text="Insert the left point", font=("Verdana", 10), borderwidth=1, relief=tk.SUNKEN)
left_point_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#left_point_value=tk.StringVar()
left_point_ent=tk.Entry(master=frames[0][8], width=30, textvariable=left_point_value)
left_point_ent.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


right_point_lbl=tk.Label(master=frames[0][9], width=30, text="Insert the right point",font=("Verdana", 10),  borderwidth=1, relief=tk.SUNKEN)
right_point_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#right_point_value=tk.StringVar()
right_point_ent=tk.Entry(master=frames[0][9], width=30, textvariable=right_point_value)
right_point_ent.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#--------------------------------------------------------------------

#BISECTION PRECISION
prec_lbl=tk.Label(master=frames[0][11], width=30, height=2, text="Insert the precision", font=("Verdana", 10), borderwidth=1, relief=tk.SUNKEN)
prec_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#precision_value=tk.StringVar()
prec_ent=tk.Entry(master=frames[0][11], width=30, textvariable=precision_value)
prec_ent.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#--------------------------------------------------------------------

#BUTTONS TO FIND THE INTERSECTION OR TO DRAW THE FUNCTION
#button that execute the bisection method 
intersec_btn = tk.Button(master=frames[0][14], width=30, text="Find intersection", command=bisect)
intersec_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=3, pady=3)

#!!!must be modified!!
#button that draw the graph
draw_btn = tk.Button(master=frames[0][14], width=30, text="Draw", command=draw_g)
draw_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=3, pady=3)



#THE FUNCTION AND BISEC RESULT FRAMES
#-----------------------------------------------------------
#-----------------------------------------------------------

#frame which contains the function with the coefficients
func_frm=tk.Frame(master=result_frm, width=450, height=math.ceil(int(result_frm["height"])/2))
func_frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=7)

func_info_lbl=tk.Label(master=func_frm, width=30, text="That's the function -->", font=("Verdana", 10))
func_info_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

current_function=tk.StringVar()
func_lbl=tk.Label(master=func_frm, width=30, textvariable=current_function)
func_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


#result of the bisection method shown here
intersec_frm=tk.Frame(master=result_frm, width=450, height=math.ceil(int(result_frm["height"])/2))
intersec_frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=7)

intersec_info_lbl=tk.Label(master=intersec_frm, width=30, text="That's the result -->", font=("Verdana", 10))
intersec_info_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

intersection_value=tk.StringVar()
intersec_lbl=tk.Label(master=intersec_frm, width=30, textvariable=intersection_value)
intersec_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


#listening for events
root.mainloop()


