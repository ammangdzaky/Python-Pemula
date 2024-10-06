# IMPORT
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

### PENGATURAN AWAL
window = tk.Tk()
window.config(bg="black")
window.geometry("400x300")
window.resizable(False,False)
window.title("BODY MASS INDEX CALCULATOR")


### FRAME
frame = ttk.Frame(window)
# ada 3 penempatan: grid, pack, place
frame.pack(padx=20, pady=20, fill="x", expand=True )

### ISI
# VARIABLE
BERAT = tk.IntVar()
TINGGI = tk.IntVar()

# FUNGSI
def fungsi():
    berat = BERAT.get()
    tinggi = TINGGI.get()
    if tinggi <= 0 or berat <= 0:
        pesan = 'MASUKKAN TINGGI DAN BERAT YANG BENAR'
    else:
        imt = (berat / ((tinggi/100)**2))
        if imt < 18.5:
            hasil = "BERAT BADAN ANDA KURANG"
        elif 18.5<=imt<=22.9:
            hasil = "BERAT BADAN ANDA KURANG"
        elif 23<=imt<=29.9:
            hasil = "BERAT BADAN ANDA BERLEBIH DAN CENDERUNG OBESITAS"
        else:
            hasil= "ANDA OBESITAS"
    pesan = f"""IMT ANDA = {imt:.1f}
    {hasil}""" 
    showinfo(title="HASIL", message=pesan)


### ELEMENT


# BERAT
label_berat = ttk.Label(frame, text='MASUKKAN BERAT (KG)') # label
label_berat.pack(padx=10, expand=True, fill="x")      # label
entry_berat = ttk.Entry(frame, textvariable=BERAT)    # entry
entry_berat.pack(padx=10, expand=True, fill="x")      # entry

# TINGGI
label_tinggi = ttk.Label(frame, text="MASUKKAN TINGGI (CM)")
label_tinggi.pack(padx=10, expand=True, fill="x")
entry_tinggi = ttk.Entry(frame, textvariable=TINGGI)
entry_tinggi.pack(padx=10, expand=True, fill="x")

# TOMBOL    
tombol = ttk.Button(frame, text="ENTER", command=fungsi)
tombol.pack(pady=10, padx=10, expand=True, fill="x")














window.mainloop()

