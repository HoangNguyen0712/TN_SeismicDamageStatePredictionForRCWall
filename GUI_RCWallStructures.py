# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:21 2020

@author: USER
"""

import PySimpleGUI as sg
import numpy as np
from pickle import load

# ADD TITLE COLOUR ,title_color='white'
sg.theme('Dark Blue 3')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Developed by Hoang Dac Nguyen')],
            [sg.Text('UNIST, South Korea')],
            [sg.Text('Email: nguyenhoangkt712@unist.ac.kr')],
            [sg.Text('Seismic damage-state prediction of R/C structures using machine learning')],
            [sg.Text('Hoang D. Nguyen, Nhan D. Dao, and Myoungsu Shin')],
              
            [sg.Frame(layout=[
            [sg.Text('PGA (g)',size=(15, 1)),sg.InputText(key='-f1-',size=(30, 1))],
            [sg.Text('PSA-1s (g)',size=(15, 1)), sg.InputText(key='-f2-',size=(30, 1))],
            [sg.Text('PSA-2s (g)',size=(15, 1)), sg.InputText(key='-f3-',size=(30, 1))],
            [sg.Text('PSA-3s (g)',size=(15, 1)), sg.InputText(key='-f4-',size=(30, 1))],
            [sg.Text('PSA-4s (g)',size=(15, 1)), sg.InputText(key='-f5-',size=(30, 1))],
            [sg.Text('PSA-5s (g)',size=(15, 1)), sg.InputText(key='-f6-',size=(30, 1))],
            [sg.Text('PSA-5s (g)',size=(15, 1)), sg.InputText(key='-f7-',size=(30, 1))],
            [sg.Text('T1 (s)',size=(15, 1)), sg.InputText(key='-f8-',size=(30, 1))],
            [sg.Text('T2 (s)',size=(15, 1)), sg.InputText(key='-f9-',size=(30, 1))],
            [sg.Text('T3 (s)',size=(15, 1)),sg.InputText(key='-f10-',size=(30, 1))]],title='Input variables')],
            [sg.Frame(layout=[   
            [sg.Text('Damage state (Green, Yellow, or Red)',size=(28, 1))], 
            [sg.Text('XGBoost',size=(15, 1)), sg.InputText(key='-OP1-',size=(30, 1))],
            [sg.Text('CatBoost',size=(15, 1)),sg.InputText(key='-OP2-',size=(30, 1))]],title='Output')],
            [sg.Button('Predict'),sg.Button('Cancel')] 
            

            
            ]

# Create the Window
window = sg.Window('SEISMIC DAMAGE-STATE PREDICTION OF R/C WALL', layout)

filename = 'BestModel_XGB.sav'
loaded_model = load(open(filename, 'rb'))

filename = 'BestModel_CGB.sav'
loaded_model_CGB = load(open(filename, 'rb'))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    #window['-OP-'].update('Please fill all the input parameters')
    if event == 'Predict':
        #window['-OP-'].update(values[0])
        #break
        if values['-f1-'] == '' or values['-f2-'] == '' or values['-f3-'] == '' or values['-f4-'] == '' or values['-f5-'] == '' or values['-f6-'] == '' or values['-f7-'] == '' or values['-f8-'] == '' or values['-f9-'] == '' or values['-f10-'] == '': 

            window['-OP1-'].update('Please fill all the input parameters')

        else:

            x_test=np.array([[float(values['-f1-']),float(values['-f2-']), float(values['-f3-']),float(values['-f4-']),float(values['-f5-']),float(values['-f6-']),float(values['-f7-']),float(values['-f8-']),float(values['-f9-']),float(values['-f10-'])]])
            y_pred_disp = loaded_model.predict(x_test)
            y_pred_disp_CGB = loaded_model_CGB.predict(x_test)
            if y_pred_disp == 1:
                window['-OP1-'].update(("GREEN"))
            elif y_pred_disp == 2:
                window['-OP1-'].update(("YELLOW"))
            else:
                window['-OP1-'].update(("RED"))   
                    
            if y_pred_disp_CGB == 1:
                window['-OP2-'].update(("GREEN"))
            elif y_pred_disp_CGB == 2:
                window['-OP2-'].update(("YELLOW"))
            else:
                window['-OP2-'].update(("RED"))   

window.close()
