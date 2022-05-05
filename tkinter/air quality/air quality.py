import tkinter
import requests
import json




root = tkinter.Tk()
root.title('zaglavie')
root.iconbitmap('alabala.ico')
root.geometry('400x50')

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=6A18D11C-6B41-4EEA-B27F-00F1679963C3

zipcode='59101'

try:
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode + '&distance=5&API_KEY=6A18D11C-6B41-4EEA-B27F-00F1679963C3')
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == 'Good':
        cvqt = 'Green'
    elif category == 'Moderate':
        cvqt = 'yellow'
    else:
        cvqt = 'red'

    root.configure(bg=cvqt)
    mylabel = tkinter.Label(root, text=f'{city} {quality} {category}', font=('Helvetica', 20), bg=cvqt)
    mylabel.pack()
except Exception as e:
    api = 'error...'


zip = tkinter.Entry(root)
zip.pack()

def check():
    global zipcode
    global mylabel
    zipcode = zip.get()
    mylabel.pack_forget()


    try:
        api_request = requests.get(
            'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode + '&distance=5&API_KEY=6A18D11C-6B41-4EEA-B27F-00F1679963C3')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            cvqt = 'Green'
        elif category == 'Moderate':
            cvqt = 'yellow'
        else:
            cvqt = 'red'

        root.configure(bg=cvqt)
        mylabel = tkinter.Label(root, text=f'{city} {quality} {category}', font=('Helvetica', 20), bg=cvqt)
        mylabel.pack()
    except Exception as e:
        api = 'error...'

but = tkinter.Button(root, text='podai info tapak', command=check)
but.pack()




root.mainloop()