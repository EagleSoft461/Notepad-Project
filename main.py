import tkinter as tk
from tkinter import filedialog, colorchooser, simpledialog, font

# Dil verilerini içeren sözlük
LANG_DATA = {
    "tr": {
        "app_title": "EagNotepad",
        "file_menu_label": "Dosya",
        "file_new": "Yeni",
        "file_open": "Aç",
        "file_save": "Kaydet",
        "file_exit": "Çıkış",
        "edit_menu_label": "Düzenle",
        "edit_cut": "Kes",
        "edit_copy": "Kopyala",
        "edit_paste": "Yapıştır",
        "format_menu_label": "Biçim",
        "format_font": "Yazı Tipi Değiştir",
        "format_color": "Renk Değiştir",
        "lang_menu_label": "Dil",
        "lang_tr": "Türkçe",
        "lang_en": "English",
        "dialog_font_title": "Yazı Tipi",
        "dialog_font_prompt": "Font adı girin (ör. Arial, Courier, Times New Roman):"
    },
    "en": {
        "app_title": "EagNotepad",
        "file_menu_label": "File",
        "file_new": "New",
        "file_open": "Open",
        "file_save": "Save",
        "file_exit": "Exit",
        "edit_menu_label": "Edit",
        "edit_cut": "Cut",
        "edit_copy": "Copy",
        "edit_paste": "Paste",
        "format_menu_label": "Format",
        "format_font": "Change Font",
        "format_color": "Change Color",
        "lang_menu_label": "Language",
        "lang_tr": "Turkish",
        "lang_en": "English",
        "dialog_font_title": "Font",
        "dialog_font_prompt": "Enter font name (e.g., Arial, Courier, Times New Roman):"
    }
}

# Başlangıç dili Türkçe olarak ayarlandı
current_lang = "tr"

# Fonksiyonlar
def yeni_dosya():
    text_area.delete(1.0, tk.END)

def dosya_ac():
   file_path = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

   if file_path:
       with open(file_path, "r", encoding="utf-8") as file:
           text_area.delete(1.0, tk.END)
           text_area.insert(tk.END, file.read())

def dosya_kaydet():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))

# ---------------- Düzenle Menüsü ----------------
def kes():
    text_area.event_generate("<<Cut>>")

def kopyala():
    text_area.event_generate("<<Copy>>")

def yapistir():
    text_area.event_generate("<<Paste>>")

# ---------------- Yazı Tipi ve Renk ----------------
def yazitipi_degistir():
    secilen_font = simpledialog.askstring(LANG_DATA[current_lang]["dialog_font_title"], LANG_DATA[current_lang]["dialog_font_prompt"])
    if secilen_font:
        current_font = font.Font(font=text_area["font"])
        text_area.configure(font=(secilen_font, current_font["size"]))

def renk_degistir():
    renk = colorchooser.askcolor()[1]
    if renk:
        text_area.configure(fg=renk)

# Dil değiştirme fonksiyonu
def set_language(lang):
    global current_lang
    current_lang = lang
    update_ui_language()

# Kullanıcı arayüzü metinlerini güncelleme fonksiyonu
def update_ui_language():
    lang = LANG_DATA[current_lang]
    root.title(lang["app_title"])
    
    # Menüleri güncelleme
    menu_bar.entryconfig(1, label=lang["file_menu_label"])
    dosya_menu.entryconfig(0, label=lang["file_new"])
    dosya_menu.entryconfig(1, label=lang["file_open"])
    dosya_menu.entryconfig(2, label=lang["file_save"])
    dosya_menu.entryconfig(4, label=lang["file_exit"])
    
    menu_bar.entryconfig(2, label=lang["edit_menu_label"])
    duzenle_menu.entryconfig(0, label=lang["edit_cut"])
    duzenle_menu.entryconfig(1, label=lang["edit_copy"])
    duzenle_menu.entryconfig(2, label=lang["edit_paste"])
    
    menu_bar.entryconfig(3, label=lang["format_menu_label"])
    bicim_menu.entryconfig(0, label=lang["format_font"])
    bicim_menu.entryconfig(1, label=lang["format_color"])

    menu_bar.entryconfig(4, label=lang["lang_menu_label"])
    dil_menu.entryconfig(0, label=lang["lang_tr"])
    dil_menu.entryconfig(1, label=lang["lang_en"])

# Ana pencere
root = tk.Tk()
root.geometry("600x400")

# Menü çubuğu
menu_bar = tk.Menu(root)

# Dosya menüsü
dosya_menu = tk.Menu(menu_bar, tearoff=0)
dosya_menu.add_command(label="", command=yeni_dosya)
dosya_menu.add_command(label="", command=dosya_ac)
dosya_menu.add_command(label="", command=dosya_kaydet)
dosya_menu.add_separator()
dosya_menu.add_command(label="", command=root.quit)
menu_bar.add_cascade(label="", menu=dosya_menu)

# Düzenle menüsü
duzenle_menu = tk.Menu(menu_bar, tearoff=0)
duzenle_menu.add_command(label="", command=kes)
duzenle_menu.add_command(label="", command=kopyala)
duzenle_menu.add_command(label="", command=yapistir)
menu_bar.add_cascade(label="", menu=duzenle_menu)

# Biçim menüsü
bicim_menu = tk.Menu(menu_bar, tearoff=0)
bicim_menu.add_command(label="", command=yazitipi_degistir)
bicim_menu.add_command(label="", command=renk_degistir)
menu_bar.add_cascade(label="", menu=bicim_menu)

# Dil menüsü 
dil_menu = tk.Menu(menu_bar, tearoff=0)
dil_menu.add_command(label="", command=lambda: set_language("tr"))
dil_menu.add_command(label="", command=lambda: set_language("en"))
menu_bar.add_cascade(label="", menu=dil_menu)

# Menü pencereye eklenmesi için 
root.config(menu=menu_bar)

# Metin alanı
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

# Uygulama başlatıldığında dili ayarla
update_ui_language()

# Programı çalıştır
root.mainloop()