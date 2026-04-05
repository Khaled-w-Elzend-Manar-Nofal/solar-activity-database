import os
import time
import sqlite3
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, StringVar, Label, Entry, LabelFrame, Button
import customtkinter
import customtkinter as ctk
from pathlib import Path

# ─────────────────────────────────────────────
# images and assets helper
# ─────────────────────────────────────────────
def asset(filename):
    return os.path.join(os.path.dirname(__file__), "assets", filename)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, "assets") 
ACCENT_COLOR = "#3B8ED0"
BG_COLOR = "#1a1a1a"

def load_image(filename, subsample=1):
    path = os.path.join(MEDIA_DIR, filename)
    if not os.path.exists(path):
        print(f"Warning: {filename} not found at {path}")
        return None
    img = tk.PhotoImage(file=path)
    if subsample > 1:
        img = img.subsample(subsample, subsample)
    return img

# ─────────────────────────────────────────────
# IMAGE REGISTRY
# Every PhotoImage is stored here for the entire program lifetime.
# Without this, Python's garbage collector destroys images as soon
# as the local variable that created them goes out of scope, making
# them silently disappear from the UI.
# ─────────────────────────────────────────────
_IMAGE_CACHE: dict = {}

def load_image(filename: str, subsample: int = 1):
    """
    Load a .png from the assets folder, cache it, and return it.
    Prints a clear warning and returns None if the file is missing,
    instead of crashing the whole app.
    """
    key = f"{filename}@{subsample}"
    if key in _IMAGE_CACHE:
        return _IMAGE_CACHE[key]

    path = asset(filename)
    if not os.path.isfile(path):
        print(f"[IMAGE NOT FOUND] {path}")
        print(f"  → Make sure '{filename}' is inside the 'assets' folder next to solar_app.py")
        return None
    try:
        img = tk.PhotoImage(file=path)
        if subsample > 1:
            img = img.subsample(subsample, subsample)
        _IMAGE_CACHE[key] = img      # kept alive forever — never GC'd
        return img
    except Exception as e:
        print(f"[IMAGE ERROR] Could not load '{filename}': {e}")
        return None


# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
DB_PATH     = os.path.join(BASE_DIR, "data/solar_cycles.db")
BTN_STYLE   = {"bg_color": "#c3d9ef", "fg_color": "#c3d9ef"}
SIDEBAR_CLR = "#9abfe4"

DATASET_CONFIG = [
    {"key": "start_end", "label": "start date & end date", "columns": ("solar cycle", "start date", "end date"),     "sql": "CS, ST, ED"},
    {"key": "duration",  "label": "duration",               "columns": ("solar cycle", "duration"),                  "sql": "CS, DU"},
    {"key": "maximum",   "label": "date-SSN of max",        "columns": ("solar cycle", "date of max", "SSN of max"), "sql": "CS, DMAX, MAX"},
    {"key": "minimum",   "label": "date-SSN of min",        "columns": ("solar cycle", "date of min", "SSN of min"), "sql": "CS, DMIN, MIN"},
    {"key": "spotless",  "label": "spotless days",           "columns": ("solar cycle", "spotless days"),             "sql": "CS, SP"},
]

CYCLE_FIELDS = [
    ("Start Month",        "SMonth"),
    ("Start Year",         "SYear"),
    ("End Month",          "EMonth"),
    ("End Year",           "EYear"),
    ("Duration",           "D"),
    ("Spotless Days",      "SD"),
    ("Date of Max",        "DOM"),
    ("Monthly SSN of Max", "MSOM"),
    ("Date of Min",        "DOMin"),
    ("Monthly SSN of Min", "MSOMin"),
]

FLARE_SWITCH_CONFIG = [
    {"label": "start time & end time", "columns": ("start time", "end time"), "sql": ("St", "En")},
    {"label": "class",                 "columns": ("class",),                 "sql": ("Cl",)},
    {"label": "Active region",         "columns": ("Active region",),         "sql": ("AC",)},
    {"label": "position",              "columns": ("position",),              "sql": ("Po",)},
]

POWERFUL_FLARE_TABLES = {
    21: "Powerful_flareS21",
    22: "Powerful_flareS22",
    23: "Powerful_flareS23",
    24: "Powerful_flareS24",
}

POWERFUL_FLARE_COLUMNS = (
    "Number of solar flare", "Day", "Month", "Year",
    "Start time", "Peak time", "End time",
    "Class", "Position", "Active region",
)

SSN_PANEL_CONFIG = [
    {"nav_label": "Daily Sun Spot Number",   "table": "Daily_SSN",   "columns": ("Year", "Month", "Day", "SSN"),
     "search_col": "Year", "plot_title": "Daily sunspot number",   "plot_x": (1818, 2022, 6), "smooth": True},
    {"nav_label": "Monthly Sun Spot Number", "table": "Monthly_SSN", "columns": ("Year", "Month", "SSN"),
     "search_col": "Year", "plot_title": "Monthly sunspot number", "plot_x": (1749, 2022, 7), "smooth": True},
    {"nav_label": "Yearly Sun Spot Number",  "table": "Yearly_SSN",  "columns": ("Year", "SSN"),
     "search_col": "Year", "plot_title": "Yearly sunspot number",  "plot_x": (1700, 2021, 8), "smooth": False},
]


# ─────────────────────────────────────────────
# DATABASE
# ─────────────────────────────────────────────
def db_fetch_all(query, params=()):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(query, params)
        return cur.fetchall()


# ─────────────────────────────────────────────
# UI HELPERS
# ─────────────────────────────────────────────
def make_label_frame(parent, text, relx, rely, relwidth, relheight):
    lf = LabelFrame(parent, text=text)
    lf.pack(fill="both", expand=True, padx=50, pady=10)
    lf.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
    return lf


def make_canvas_frame(parent):
    c = tk.Canvas(parent, bg="white", width=1200, height=1000)
    c.place(relx=0, rely=0, relheight=1, relwidth=1)
    f = tk.Frame(c, bg="white")
    f.place(relx=0, rely=0, relheight=1, relwidth=1)
    return f


def make_treeview(parent, columns, relx=0.02, rely=0.18, relwidth=0.9, relheight=0.8):
    tv = ttk.Treeview(parent, columns=columns, show="headings")
    tv.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
    tv.column("#0", width=0, stretch="no")
    for col in columns:
        tv.heading(col, text=col, anchor="center")
        tv.column(col, anchor="center", width=100)
    return tv


def populate_treeview(tv, columns, rows):
    tv.delete(*tv.get_children())
    tv["columns"] = columns
    tv.column("#0", width=0, stretch="no")
    for col in columns:
        tv.heading(col, text=col)
        tv.column(col, anchor="center", width=120)
    for row in rows:
        tv.insert("", tk.END, values=row)


def make_switch_row(parent, config_list, start_relx=0.02, col_gap=0.2):
    switches = {}
    for i, cfg in enumerate(config_list):
        sw = customtkinter.CTkSwitch(parent, text=cfg["label"], onvalue="on", offvalue="off")
        sw.place(relx=start_relx + (i // 2) * col_gap, rely=0.02 + (i % 2) * 0.08)
        switches[cfg["label"]] = sw
    return switches


def make_detail_fields(parent, field_defs):
    vars_ = {name: StringVar() for _, name in field_defs}
    for row_idx, (label_text, var_name) in enumerate(field_defs):
        Label(parent, text=label_text).grid(row=row_idx, column=5, padx=10, pady=5)
        Entry(parent, textvariable=vars_[var_name]).grid(row=row_idx, column=6, padx=10, pady=5)
    return vars_


def make_cycle_combobox(parent, field_vars, row=3):
    options = [str(r[0]) for r in db_fetch_all("SELECT CS FROM solar_cycle1")]
    Label(parent, text="Select Cycle:").grid(row=row, column=1, padx=10, pady=10)
    combo = ttk.Combobox(parent, textvariable=StringVar(), values=options)
    combo.grid(row=row, column=2, padx=10, pady=10)

    def on_select(event):
        rows = db_fetch_all("SELECT * FROM solar_cycle1 WHERE CS=?", (combo.get(),))
        if not rows:
            return
        for i, (_, fname) in enumerate(CYCLE_FIELDS):
            field_vars[fname].set(rows[0][i + 1])

    combo.bind("<<ComboboxSelected>>", on_select)
    return combo


def export_to_csv(data):
    if not data:
        messagebox.showerror("No Data", "No data available to export.")
        return
    path = filedialog.asksaveasfilename(
        initialdir=os.getcwd(), title="Save CSV",
        filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
    )
    if not path:
        return
    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(data)
    messagebox.showinfo("Exported", f"Data saved to {os.path.basename(path)}.")


def plot_ssn(table, title, x_range=None, smooth=False):
    rows = db_fetch_all(f'SELECT Year, SSN FROM "{table}"')
    if not rows:
        messagebox.showwarning("No data", f"No data in {table}.")
        return
    x = np.array([r[0] for r in rows])
    y = np.array([r[1] for r in rows], dtype=float)
    if smooth:
        y = gaussian_filter1d(y, sigma=2)
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel("SSN")
    if x_range:
        ax.set_xticks(np.arange(*x_range))
        plt.xticks(rotation="vertical")
    ax.plot(x, y)
    plt.tight_layout()
    plt.show()


# ─────────────────────────────────────────────
# PANEL: SOLAR CYCLES
# ─────────────────────────────────────────────
def build_solar_cycles_panel(frame1):
    outer   = make_canvas_frame(frame1)
    data_lf = make_label_frame(outer, "Data",      0.03, 0.01, 0.9, 0.50)
    sel_lf  = make_label_frame(outer, "Selection", 0.03, 0.51, 0.9, 0.48)

    switches = {}
    for i, cfg in enumerate(DATASET_CONFIG):
        sw = customtkinter.CTkSwitch(data_lf, text=cfg["label"], onvalue="on", offvalue="off")
        sw.place(relx=0.02 + (i // 2) * 0.2, rely=0.02 + (i % 2) * 0.08)
        switches[cfg["key"]] = sw

    tv = ttk.Treeview(data_lf)
    tv.place(relx=0.02, rely=0.18, relwidth=0.9, relheight=0.8)

    field_vars = make_detail_fields(sel_lf, CYCLE_FIELDS)
    make_cycle_combobox(sel_lf, field_vars)

    mydata = []

    def show_data():
        nonlocal mydata
        sql_cols  = ["CS"]
        disp_cols = ["solar cycle"]
        for cfg in DATASET_CONFIG:
            if switches[cfg["key"]].get() == "on":
                sql_cols  += cfg["sql"].replace(" ", "").split(",")
                disp_cols += list(cfg["columns"][1:])
        if len(sql_cols) == 1:
            messagebox.showwarning("Selection", "Please select at least one option.")
            return
        rows = db_fetch_all(f"SELECT {', '.join(sql_cols)} FROM Solar_cycle")
        mydata = list(rows)
        populate_treeview(tv, disp_cols, rows)

    customtkinter.CTkButton(data_lf, text="Show Data",  command=show_data,                    **BTN_STYLE).place(relx=0.67, rely=0.02)
    customtkinter.CTkButton(data_lf, text="Export CSV", command=lambda: export_to_csv(mydata), **BTN_STYLE).place(relx=0.83, rely=0.02)


# ─────────────────────────────────────────────
# PANEL: SSN (Daily / Monthly / Yearly)
# ─────────────────────────────────────────────
def build_ssn_panel(frame1, cfg: dict):
    outer   = make_canvas_frame(frame1)
    data_lf = make_label_frame(outer, "Data",      0.03, 0.01, 0.9, 0.42)
    sel_lf  = make_label_frame(outer, "Selection", 0.03, 0.44, 0.9, 0.34)

    table   = cfg["table"]
    columns = cfg["columns"]
    s_col   = cfg["search_col"]

    tv = make_treeview(data_lf, columns, rely=0.05, relheight=0.9)

    mydata = []

    def load(rows):
        nonlocal mydata
        mydata = list(rows)
        tv.delete(*tv.get_children())
        for row in rows:
            tv.insert("", tk.END, values=row)

    load(db_fetch_all(f"SELECT * FROM {table}"))

    q_var = StringVar()
    Label(sel_lf, text=f"Filter by {s_col}:").place(relx=0.03, rely=0.25)
    Entry(sel_lf, textvariable=q_var).place(relx=0.15, rely=0.25)

    def search():
        load(db_fetch_all(f'SELECT * FROM {table} WHERE "{s_col}" LIKE ?', (f"%{q_var.get()}%",)))

    Button(sel_lf, text="Show data", command=search).place(relx=0.30, rely=0.25)
    customtkinter.CTkButton(sel_lf, text="Export CSV", command=lambda: export_to_csv(mydata),                                              **BTN_STYLE).place(relx=0.10, rely=0.55)
    customtkinter.CTkButton(sel_lf, text="Plot",       command=lambda: plot_ssn(table, cfg["plot_title"], cfg["plot_x"], cfg["smooth"]),    **BTN_STYLE).place(relx=0.10, rely=0.40)


# ─────────────────────────────────────────────
# PANEL: SOLAR FLARES
# ─────────────────────────────────────────────
def show_powerful_flares(cycle_number: int):
    table = POWERFUL_FLARE_TABLES.get(cycle_number)
    if not table:
        messagebox.showerror("Error", f"No data configured for cycle {cycle_number}.")
        return
    rows = db_fetch_all(f"SELECT * FROM {table}")
    win = tk.Toplevel()
    win.title(f"Most Powerful Flares – Solar Cycle {cycle_number}")
    sb = ttk.Scrollbar(win, orient="vertical")
    sb.pack(side="right", fill="y")
    tv = ttk.Treeview(win, columns=POWERFUL_FLARE_COLUMNS, show="headings", yscrollcommand=sb.set)
    sb.configure(command=tv.yview)
    tv.pack(fill="both", expand=True)
    for col in POWERFUL_FLARE_COLUMNS:
        tv.heading(col, text=col, anchor="center")
        tv.column(col, anchor="center", width=80)
    for row in rows:
        tv.insert("", tk.END, values=row)


def build_flares_panel(frame1):
    outer   = make_canvas_frame(frame1)
    data_lf = make_label_frame(outer, "Data",               0.03, 0.01, 0.9, 0.50)
    pwr_lf  = make_label_frame(outer, "Most Powerful Data", 0.03, 0.52, 0.9, 0.45)

    switches = make_switch_row(data_lf, FLARE_SWITCH_CONFIG)

    tv = ttk.Treeview(data_lf)
    tv.place(relx=0.02, rely=0.18, relwidth=0.9, relheight=0.78)

    mydata = []

    def show_data():
        nonlocal mydata
        sql_cols  = ["Da"]
        disp_cols = ["Date"]
        for cfg in FLARE_SWITCH_CONFIG:
            if switches[cfg["label"]].get() == "on":
                sql_cols  += list(cfg["sql"])
                disp_cols += list(cfg["columns"])
        if len(sql_cols) == 1:
            messagebox.showwarning("Selection", "Please select at least one option.")
            return
        rows = db_fetch_all(f"SELECT {', '.join(sql_cols)} FROM Solar_flare")
        mydata = list(rows)
        populate_treeview(tv, disp_cols, rows)

    customtkinter.CTkButton(data_lf, text="Show Data",  command=show_data,                    **BTN_STYLE).place(relx=0.70, rely=0.09)
    customtkinter.CTkButton(data_lf, text="Export CSV", command=lambda: export_to_csv(mydata), **BTN_STYLE).place(relx=0.85, rely=0.09)

    date_var = StringVar()
    Label(pwr_lf, text="Filter by Date:").place(relx=0.53, rely=0.08)
    Entry(pwr_lf, textvariable=date_var).place(relx=0.63, rely=0.08)

    def search():
        rows = db_fetch_all("SELECT * FROM Solar_flare WHERE Da LIKE ?", (f"%{date_var.get()}%",))
        populate_treeview(tv, ["Date", "start time", "end time", "class", "Active region", "position"], rows)

    Button(pwr_lf, text="Search", command=search).place(relx=0.78, rely=0.08)

    for i, cycle in enumerate(POWERFUL_FLARE_TABLES):
        customtkinter.CTkButton(
            pwr_lf,
            text=f"Most powerful 10 flares – Solar Cycle {cycle}",
            command=lambda c=cycle: show_powerful_flares(c),
            **BTN_STYLE,
        ).place(relx=0.02, rely=0.10 + i * 0.20)


# ─────────────────────────────────────────────
# MAIN DATABASE WINDOW
# ─────────────────────────────────────────────
def build_main_window(top):
    # Main Container
    main_container = customtkinter.CTkFrame(top, fg_color="#121212")
    main_container.pack(fill="both", expand=True)

    # 1. Sidebar 
    sidebar = customtkinter.CTkFrame(main_container, width=200, corner_radius=0, fg_color="#1e1e1e")
    sidebar.place(relx=0, rely=0, relwidth=0.18, relheight=1)

    # 2. Content Area (replaces old frame1)
    content_area = customtkinter.CTkFrame(main_container, fg_color="#1a1a1a", corner_radius=15)
    content_area.place(relx=0.2, rely=0.02, relwidth=0.78, relheight=0.96)

    def clear_content():
        for widget in content_area.winfo_children():
            widget.destroy()

    def navigate(builder_func, cfg=None):
        clear_content()
        if cfg:
            builder_func(content_area, cfg) # Pass content_area to the panel
        else:
            builder_func(content_area)

    nav_items = [
        ("Solar Cycles", build_solar_cycles_panel, None),
        ("Daily SSN",   build_ssn_panel, SSN_PANEL_CONFIG[0]),
        ("Monthly SSN", build_ssn_panel, SSN_PANEL_CONFIG[1]),
        ("Yearly SSN",  build_ssn_panel, SSN_PANEL_CONFIG[2]),
        ("Solar Flares", build_flares_panel, None),
    ]

    for i, (label, func, cfg) in enumerate(nav_items):
        btn = customtkinter.CTkButton(
            master=sidebar, # Fixed name
            text=label,
            height=45,
            fg_color="transparent",
            hover_color="#2b2b2b",
            command=lambda f=func, c=cfg: navigate(f, c)
        )
        btn.place(relx=0.1, rely=0.15 + (i * 0.08), relwidth=0.8)

    # Load initial view
    navigate(build_solar_cycles_panel)


# ─────────────────────────────────────────────
# SPLASH SCREEN (ROOT WINDOW)
# ─────────────────────────────────────────────
root = customtkinter.CTk()
root.title("Solar Activity Database")
root.geometry("1100x700")

# Load app icon
app_icon = load_image("app_icon.png")
if app_icon:
    root.iconphoto(False, app_icon)

# 1. Training Logo (EUT) - Positioned in the top right
training_ph = load_image("EUT.png")
if training_ph:
    logo_lbl = customtkinter.CTkLabel(root, image=training_ph, text="")
    logo_lbl.place(relx=0.8, rely=0.05, relheight=0.22, relwidth=0.15)

# 2. Header Section (Titles)
header_frame = customtkinter.CTkFrame(root, fg_color="transparent")
header_frame.place(relx=0.5, rely=0.25, anchor="center")

customtkinter.CTkLabel(
    header_frame, 
    text="SOLAR ACTIVITY DATABASE", 
    font=customtkinter.CTkFont(family="Inter", size=48, weight="bold"),
    text_color="#000000"
).pack()

customtkinter.CTkLabel(
    header_frame, 
    text="TEAM 48 | Physics| Port Said University ", 
    font=customtkinter.CTkFont(size=18, slant="italic"),
    text_color=ACCENT_COLOR
).pack(pady=5)

# 3. Credits Section (The Cards)
credits_frame = customtkinter.CTkFrame(root, fg_color="#19AEB4", corner_radius=15)
credits_frame.place(relx=0.25, rely=0.6, anchor="center", relwidth=0.35, relheight=0.25)

customtkinter.CTkLabel(credits_frame, text="DEVELOPED BY", font=customtkinter.CTkFont(size=14, weight="bold"), text_color=ACCENT_COLOR).pack(pady=(15, 5))
customtkinter.CTkLabel(credits_frame, text="Khaled W. Elzend\nManar A. Nofal", font=customtkinter.CTkFont(size=18)).pack()

super_frame = customtkinter.CTkFrame(root, fg_color="#19AEB4", corner_radius=15)
super_frame.place(relx=0.75, rely=0.6, anchor="center", relwidth=0.35, relheight=0.25)

customtkinter.CTkLabel(super_frame, text="SUPERVISION", font=customtkinter.CTkFont(size=14, weight="bold"), text_color=ACCENT_COLOR).pack(pady=(15, 5))
customtkinter.CTkLabel(super_frame, text="Dr. Wael Mohamed", font=customtkinter.CTkFont(size=18)).pack()

# 4. Launch Logic
def start_app():
    launch_btn.destroy()
    progress = customtkinter.CTkProgressBar(root, width=400, mode="determinate", progress_color=ACCENT_COLOR)
    progress.place(relx=0.5, rely=0.85, anchor="center")
    progress.set(0)
    
    for i in range(1, 11):
        time.sleep(0.1)
        progress.set(i/10)
        root.update_idletasks()
    
    root.withdraw()
    top = customtkinter.CTkToplevel(root)
    top.title("Dashboard - Solar Activity Database")
    top.state("zoomed") # Open the main window maximized
    if app_icon:
        top.iconphoto(False, app_icon)
    build_main_window(top)

# 5. Launch Button
# If you have 'arrow.png', we can use it as an icon on the modern button
arrow_icon = load_image("arrow.png", subsample=3)

launch_btn = customtkinter.CTkButton(
    root, 
    text="ENTER DATABASE →" if not arrow_icon else " ENTER DATABASE",
    compound="right",
    font=customtkinter.CTkFont(size=16, weight="bold"),
    height=50,
    width=250,
    corner_radius=25,
    command=start_app
)
launch_btn.place(relx=0.5, rely=0.95, anchor="center")

if __name__ == "__main__":
    root.mainloop()