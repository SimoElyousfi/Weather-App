import tkinter as tk
from tkinter import messagebox
import requests
import json

api_key = "36a7f07130362f73bdce84ed965e9c36"


# Call current weather data
def fetch_data(city):
    global api_key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        json_data = json.loads(response.content)
        return json_data


def get():
    global switch
    try:
        temp = fetch_data(switch.get())["main"]["temp"]
        description = fetch_data(switch.get())["weather"][0]["description"]
        messagebox.showinfo(f"Weather in {switch.get()}", f"{temp} {description}")
    except TypeError as e:
        messagebox.showerror("Error", "Error fetching weather data, maybe city name incorrect")


win = tk.Tk()
win.title("Weather App")

switch = tk.StringVar()
switch.set("")
# Input
entry = tk.Entry(win, width=20, textvariable=switch)
entry.pack()

# Button
button = tk.Button(win, text="Get Weather", command=get)
button.pack()

tk.mainloop()
