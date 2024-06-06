import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
from weather import fetch_weather_data  # Ensure this import is correct

def change_background(canvas, new_image_path):
    try:
        image_path = f"Weather_Images/{new_image_path}"
        new_image = Image.open(image_path)
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        resized_image = new_image.resize((canvas_width, canvas_height), Image.LANCZOS)
        new_photo = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, image=new_photo, anchor="nw")
        canvas.image = new_photo  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error loading image '{new_image_path}': {e}")
 # Keep a reference to avoid garbage collection

def fetch_weather(temp_label, desc_label, hum_label, wind_label, entry, canvas, status_label):
    city_name = entry.get()
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    
    status_label.set("Stay tuned with us, We're getting the latest weather updates for you...")
    weather_data = fetch_weather_data(city_name)
    
    if weather_data:
        temp_k = weather_data['main']['temp']
        temp_c = temp_k - 273.15
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        temp_label.config(text=f"{temp_c:.2f}°C")
        desc_label.config(text=f"{description}")
        hum_label.config(text=f"{humidity}%")
        wind_label.config(text=f"{wind_speed} m/s")
        
        # Change background image based on description
        if 'clear' in description:
            if weather_data['main']['feels_like'] < 30:
                change_background(canvas, 'sunny.png')
            else:
                change_background(canvas, 'clearSky.png')
        elif 'broken' in description:
            change_background(canvas, 'broken_Clouds.png')
        elif 'cloud' in description:
            change_background(canvas, 'cloudy.png')
        elif 'rain' in description:
            change_background(canvas, 'rainy.png')
        elif 'snow' in description or 'winter' in description:
            if temp_c < 0:
                change_background(canvas, 'snowy.png')
            else:
                change_background(canvas, 'winter.png')
        elif 'haze' in description:
            change_background(canvas,'haze.png')
    else:
        temp_label.config(text="Error fetching weather data")
        desc_label.config(text="")
        hum_label.config(text="")
        wind_label.config(text="")
        change_background(canvas, 'default.png')
    
    status_label.set("")

def on_button_click(temp_label, desc_label, hum_label, wind_label, entry, canvas, status_label):
    threading.Thread(target=fetch_weather, args=(temp_label, desc_label, hum_label, wind_label, entry, canvas, status_label)).start()

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Load the default background image
background_image_path = "Weather_Images/default.png"
background_image = Image.open(background_image_path)
background_image = background_image.resize((1850, 1050), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)


# Create a canvas to place the background image
canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")
canvas.image = background_photo

# Create a frame for weather information
frame = tk.Frame(root, bg="white", bd=10, relief="groove")
frame_window = canvas.create_window(400, 300, window=frame)

# Customize label style
label_style = {"bg": "white", "font": ("Helvetica", 14, "bold")}
display_style = {"bg": "white", "font": ("Helvetica", 14)}

# Example widgets within the frame
location_label = tk.Label(frame, text="Location:", **label_style)
location_label.grid(row=0, column=0, padx=10, pady=5)

location_entry = tk.Entry(frame, font=("Helvetica", 14))
location_entry.grid(row=0, column=1, padx=10, pady=5)

temp_label = tk.Label(frame, text="Temperature:", **label_style)
temp_label.grid(row=1, column=0, padx=10, pady=5)

temp_display = tk.Label(frame, text="--", **display_style)
temp_display.grid(row=1, column=1, padx=10, pady=5)

desc_label = tk.Label(frame, text="Description:", **label_style)
desc_label.grid(row=2, column=0, padx=10, pady=5)

desc_display = tk.Label(frame, text="--", **display_style)
desc_display.grid(row=2, column=1, padx=10, pady=5)

hum_label = tk.Label(frame, text="Humidity:", **label_style)
hum_label.grid(row=3, column=0, padx=10, pady=5)

hum_display = tk.Label(frame, text="--", **display_style)
hum_display.grid(row=3, column=1, padx=10, pady=5)

wind_label = tk.Label(frame, text="Wind Speed:", **label_style)
wind_label.grid(row=4, column=0, padx=10, pady=5)

wind_display = tk.Label(frame, text="--", **display_style)
wind_display.grid(row=4, column=1, padx=10, pady=5)

# Status label for loading message
status_label = tk.StringVar()
status_display = tk.Label(frame, textvariable=status_label, bg="white", font=("Helvetica", 12, "italic"))
status_display.grid(row=5, column=0, columnspan=2, pady=10)

# Update the button callback to pass the labels and entry
button = tk.Button(frame, text="Get Weather Report", font=("Helvetica", 14, "bold"), bg="lightblue",
                   command=lambda: on_button_click(temp_display, desc_display, hum_display, wind_display, location_entry, canvas, status_label))
button.grid(row=6, column=0, columnspan=2, pady=10)

# Center the frame after the main loop starts
def resize(event):
    canvas.coords(frame_window, canvas.winfo_width() // 2, canvas.winfo_height() // 2)

canvas.bind("<Configure>", resize)

# Run the main loop
root.mainloop()


