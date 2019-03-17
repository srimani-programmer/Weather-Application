# A GUI weather Application in Python3
# done by @Sri_Programmer
# python v3.7.2

# imports

import tkinter as tk
import requests
from PIL import ImageTk, Image


# Width and Size value for the screen
HEIGHT = 600
WIDTH = 880

def format_output(weather):
    try:
        name = str(weather['name'])
        descrption = str(weather['weather'][0]['description'])
        temp = str(weather['main']['temp'])

        final_result = 'Name: {} \nCondition: {} \nTemperature (°C): {}'.format(name, descrption, temp)
    except Exception:
        final_result = 'Something went wrong while fetching details'

    return final_result

    

def get_weather(city):
    weather_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID' : weather_key, 'q' : city, 'units' : 'metric'}
    response = requests.get(url, params=parameters)
    weather_report = response.json()

    output_label['text'] = format_output(weather_report)
    

# Creating a main window
window = tk.Tk()
window.title('Weather Application')

# Creating the canvas for the window to increase the size
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
background_image = tk.PhotoImage('/Users/srimanikanta/Desktop/Weather Application/bg1.png')
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.pack()
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()

# Background image
'''
background_image = tk.PhotoImage(Image.open('./bg1.png'))
logo = tk.Label(window, image=background_image)
logo.pack()
'''

# Creating the frame
frame = tk.Frame(window, bg='#25CCF7',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


# Creating entry feild
entry = tk.Entry(frame, font=('Monaco' , 20))
entry.place(relwidth=0.65, relheight=1)

# creating button.
button = tk.Button(frame, font=('Monaco',18), text="Get Weather", command= lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# creating the output frame

output_frame = tk.Frame(window, bd=10, bg='#25CCF7')
output_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# creating the output label

output_label = tk.Label(output_frame, font=('Monaco', 18), justify='left',anchor='nw',bd=4)
output_label.place(relwidth=1, relheight=1)

window.mainloop()

