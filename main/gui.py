from main import get_weather
import PySimpleGUI as sg

temp, status = get_weather()

print(f"Temperature is: {temp}\nStatus is: {status}")

def main(temp, status):


	sg.theme('DarkBlue')   
	
	layout = [  [sg.Text(f"Temperature is: {temp}")],
	            [sg.Text(f"Status is: {status}")],
	            ]

	
	window = sg.Window('Window Title', layout)
	
	while True:
	    event, values = window.read()
	    if event == sg.WIN_CLOSED:
	        break

	window.close()
main(temp, status)