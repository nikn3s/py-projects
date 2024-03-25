import tkinter as tk 
from tkinter import StringVar, ttk
import sv_ttk
import requests as req

class ExpandableFrame(ttk.Frame):
    def __init__(self, master, widgets:list, notHolders:bool, tog_btn, gridx=0, gridy=0):
        super().__init__(master)
        self.widgets = widgets
        self.notHolders = notHolders
        self.gridx = gridx
        self.gridy =gridy
        self.grid(row=gridx+1, column=gridy+1)
        self.expanded = False
        self.toggle_btn = tog_btn.config(command=self.toggleExpand)

        self.labels = self.widgets[:4]
        self.holders = self.widgets[4:]

    def toggleExpand(self):
        if self.expanded:
                for widget in self.labels:
                    widget.grid_remove()
                for widget in self.holders:
                    widget.grid_remove()
                self.expanded = False
        else:
            for i, widget in enumerate(self.labels):
                widget.grid(row=i+7, column=self.gridx, pady=5)
            for i, widget in enumerate(self.holders):
                widget.grid(row=i+7, column=self.gridx+1, pady=5)
        

class errorScreen(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.grab_set()
        self.geometry("200x100")
        self.error_label = ttk.Label(self, text="Input a valid city name")
        self.close_btn = ttk.Button(self, text="Ok", command=self.destroy)

        self.error_label.pack(pady=20)
        self.close_btn.pack()

class mainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        sv_ttk.set_theme("dark")

        self.title("Weatherly")
        self.geometry("400x400")

        self.city_var = StringVar()

        self.city_label = ttk.Label(self, text='Enter city name: ', font=("Helvevatica", 12))
        self.togglebtn = ttk.Button(text="Extra Data")
        self.city_entry = ttk.Entry(self, textvariable=self.city_var)
        self.refresh_btn = ttk.Button(self, text="Refresh", command=self.updateWeather)

        self.location_label = ttk.Label(self, text="Location: ")
        self.location_holder = ttk.Label(self, text="")
        self.temp_label = ttk.Label(self, text="Temperature: ")
        self.temp_holder = ttk.Label(self, text="")
        self.descrip_label = ttk.Label(self, text="Description: ")
        self.descrip_holder = ttk.Label(self, text="")
    
        self.pres_label = ttk.Label(self, text="Pressure: ")
        self.pres_holder = ttk.Label(self, text="")
        self.humid_label = ttk.Label(self, text="Humidity: ")
        self.humid_holder = ttk.Label(self, text="")
        self.wind_label = ttk.Label(self, text="Wind speed:")
        self.wind_holder = ttk.Label(self, text="")

        self.extraWidgetLBL = [self.location_label, self.pres_label, self.humid_label, self.wind_label]
        self.extraWidgetHDR = [self.location_holder, self.pres_holder, self.humid_holder, self.wind_holder]

        self.extraWidgets = self.extraWidgetLBL + self.extraWidgetHDR

        self.onePadX = 20
        self.onePadY = 10

        self.togglebtn.grid(column=1, row=1)
        self.city_label.grid(column=0,row=0, pady=self.onePadY, padx=self.onePadX)
        self.city_entry.grid(column=0,row=1, pady=self.onePadY, padx=self.onePadX)
        self.refresh_btn.grid(column=0,row=2, pady=self.onePadY, padx=self.onePadX)
        self.temp_label.grid(column=0,row=3, pady=5, padx=5)
        self.temp_holder.grid(column=1,row=3,pady=5,padx=5)
        self.descrip_label.grid(column=0,row=4,pady=5)
        self.descrip_holder.grid(column=1,row=4,pady=5)

        self.displayExtraInfo()

    def displayExtraInfo(self)->None:
        ExpandableFrame(self, self.extraWidgets,notHolders=True, gridx=0, gridy=0, tog_btn=self.togglebtn)


    def updateWeather(self)->None:
        try:
            values = self.getWeather(self.city_var.get())
            print(values)
            self.temp_holder.config(text=f"{round(values[0], 2)}°C")
            self.descrip_holder.config(text=values[1])
            self.location_holder.config(text=f"{values[6]}, {values[5]}")
            self.pres_holder.config(text=f'{values[2]}hPa')
            self.humid_holder.config(text=f"{values[3]}%")
            self.wind_holder.config(text=f"{round(values[4]*3.6,0)}km/h")
        except Exception:
            pass

    def getWeather(self, city:str) ->list:
        city = city.strip().lower()
        self.API_KEY = 'your_api_key'
        self.url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.API_KEY}'
        self.get_data = req.get(self.url)
        print(self.url)
        self.details = []
        if self.get_data.status_code == 200:
            self.data = self.get_data.json()
            self.details.append(self.data["main"]["temp"]-273.15)
            self.details.append(self.data['weather'][0]['description'])
            self.details.append(self.data['main']['pressure'])
            self.details.append(self.data['main']['humidity'])
            self.details.append(self.data['wind']['speed'])
            self.details.append(self.data['sys']['country'])
            self.details.append(self.data['name'])
            print(self.details)
            return self.details
        else:
            self.openErrornous()
    
    def openErrornous(self):
        try:
            errorScreen(self)
        except Exception:
            pass

app = mainScreen()
app.mainloop()