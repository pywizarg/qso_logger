import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from supabase_client import save_qso  # Usa la función que ya tienes para guardar QSOs

# Datos de ejemplo, puedes reemplazar por los obtenidos desde la base de datos Supabase
bands = ["160m", "80m", "40m", "30m", "20m", "17m", "15m", "12m", "10m", "6m", "2m"]
modes = ["SSB", "CW", "FM", "AM", "RTTY", "FT8", "FT4", "PSK31", "JT65"]
countries = ["Argentina", "Brazil", "Chile", "Germany", "Japan", "USA", "Spain", "Italy", "Canada"]

class QSOLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QSO Logger")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.frame = tb.Frame(root, padding=20)
        self.frame.pack(fill=BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        tb.Label(self.frame, text="Callsign").pack(anchor=W)
        self.callsign = tb.Entry(self.frame)
        self.callsign.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Date (YYYY-MM-DD)").pack(anchor=W)
        self.date = tb.Entry(self.frame)
        self.date.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Time (HH:MM)").pack(anchor=W)
        self.time = tb.Entry(self.frame)
        self.time.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Band").pack(anchor=W)
        self.band = tb.Combobox(self.frame, values=bands, state="readonly")
        self.band.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Mode").pack(anchor=W)
        self.mode = tb.Combobox(self.frame, values=modes, state="readonly")
        self.mode.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Country").pack(anchor=W)
        self.country = tb.Combobox(self.frame, values=countries, state="readonly")
        self.country.pack(fill=X, pady=5)

        tb.Label(self.frame, text="RST Sent").pack(anchor=W)
        self.rst_sent = tb.Entry(self.frame)
        self.rst_sent.pack(fill=X, pady=5)

        tb.Label(self.frame, text="RST Received").pack(anchor=W)
        self.rst_rcvd = tb.Entry(self.frame)
        self.rst_rcvd.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Comments").pack(anchor=W)
        self.comments = tb.Entry(self.frame)
        self.comments.pack(fill=X, pady=5)

        tb.Button(self.frame, text="Guardar QSO", bootstyle=SUCCESS, command=self.save).pack(pady=15)

    def save(self):
        qso_data = {
            "callsign": self.callsign.get(),
            "date": self.date.get(),
            "time": self.time.get(),
            "band": self.band.get(),
            "mode": self.mode.get(),
            "country": self.country.get(),
            "rst_sent": self.rst_sent.get(),
            "rst_received": self.rst_rcvd.get(),
            "comments": self.comments.get()
        }

        if not all(qso_data.values()):
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        try:
            save_qso(qso_data)
            messagebox.showinfo("Éxito", "QSO guardado correctamente.")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el QSO.\n{str(e)}")

    def clear_fields(self):
        self.callsign.delete(0, tk.END)
        self.date.delete(0, tk.END)
        self.time.delete(0, tk.END)
        self.band.set('')
        self.mode.set('')
        self.country.set('')
        self.rst_sent.delete(0, tk.END)
        self.rst_rcvd.delete(0, tk.END)
        self.comments.delete(0, tk.END)


if __name__ == "__main__":
    app = tb.Window(themename="minty")  # Puedes probar con: "superhero", "flatly", "solar", etc.
    QSOLoggerApp(app)
    app.mainloop()
