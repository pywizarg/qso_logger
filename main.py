import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from supabase_client import save_qso, get_bands, get_modes, get_countries

class QSOLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QSO Logger")
        self.root.geometry("500x1200")
        self.root.resizable(False, False)

        self.frame = tb.Frame(root, padding=20)
        self.frame.pack(fill=BOTH, expand=True)

        self.bands_dict = {band["name"]: band["id"] for band in get_bands().data}
        self.modes_dict = {mode["name"]: mode["id"] for mode in get_modes().data}
        self.countries_dict = {country["name"]: country["id"] for country in get_countries().data}

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

        tb.Label(self.frame, text="Frequency (MHz)").pack(anchor=W)
        self.frequency = tb.Entry(self.frame)
        self.frequency.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Band").pack(anchor=W)
        self.band = tb.Combobox(self.frame, values=list(self.bands_dict.keys()), state="readonly")
        self.band.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Mode").pack(anchor=W)
        self.mode = tb.Combobox(self.frame, values=list(self.modes_dict.keys()), state="readonly")
        self.mode.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Country").pack(anchor=W)
        self.country = tb.Combobox(self.frame, values=list(self.countries_dict.keys()), state="readonly")
        self.country.pack(fill=X, pady=5)

        tb.Label(self.frame, text="RST Sent").pack(anchor=W)
        self.rst_sent = tb.Entry(self.frame)
        self.rst_sent.pack(fill=X, pady=5)

        tb.Label(self.frame, text="RST Received").pack(anchor=W)
        self.rst_rcvd = tb.Entry(self.frame)
        self.rst_rcvd.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Grid Square").pack(anchor=W)
        self.grid_square = tb.Entry(self.frame)
        self.grid_square.pack(fill=X, pady=5)

        tb.Label(self.frame, text="Operator").pack(anchor=W)
        self.operator = tb.Entry(self.frame)
        self.operator.pack(fill=X, pady=5)

        #tb.Label(self.frame, text="Comments").pack(anchor=W)
        #self.comments = tb.Entry(self.frame)
        #self.comments.pack(fill=X, pady=5)

        tb.Button(self.frame, text="Guardar QSO", bootstyle=SUCCESS, command=self.save).pack(pady=20)

    def save(self):
        required_fields = [
            self.callsign.get(),
            self.date.get(),
            self.time.get(),
            self.frequency.get(),
            self.band.get(),
            self.mode.get(),
            self.country.get(),
            self.rst_sent.get(),
            self.rst_rcvd.get()
        ]

        if any(field.strip() == '' for field in required_fields):
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        try:
            band_id = self.bands_dict[self.band.get()]
            mode_id = self.modes_dict[self.mode.get()]
            country_id = self.countries_dict[self.country.get()]
        except KeyError:
            messagebox.showerror("Error", "Band, Mode o Country seleccionados no son válidos.")
            return

        qso_data = {
            "callsign": self.callsign.get(),
            "qso_date": self.date.get(),
            "qso_time": self.time.get(),
            "frequency": self.frequency.get(),
            "band_id": band_id,
            "mode_id": mode_id,
            "country_id": country_id,
            "rst_sent": self.rst_sent.get(),
            "rst_received": self.rst_rcvd.get(),
            "grid_square": self.grid_square.get(),
            "operator": self.operator.get(),
            #"comments": self.comments.get()
        }

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
        self.frequency.delete(0, tk.END)
        self.band.set('')
        self.mode.set('')
        self.country.set('')
        self.rst_sent.delete(0, tk.END)
        self.rst_rcvd.delete(0, tk.END)
        self.grid_square.delete(0, tk.END)
        self.operator.delete(0, tk.END)
        #self.comments.delete(0, tk.END)

if __name__ == "__main__":
    app = tb.Window(themename="minty")
    QSOLoggerApp(app)
    app.mainloop()
