# ☀️ Solar Activity Database & Analyzer

 Python-based graphical user interface (GUI) and SQLite database system designed for the storage, retrieval, and analysis of historical solar activity. This tool allows people to quickly explore sunspot numbers and solar flare data through a dashboard.

---

## 🚀 Features

* **Modern Interactive UI**: Built with `CustomTkinter` for a sleek, high-performance dark-themed experience.
* **Comprehensive Data Access**: 
    * **Sunspot Numbers (SSN)**: Access Daily, Monthly, and Yearly records dating back to 1700.
    * **Solar Cycles**: Detailed statistics for individual cycles, including start/end dates and durations.
    * **Solar Flares**: Analysis of powerful flares across Cycles 21–24.
* **Scientific Visualization**: Integrated `Matplotlib` plotting with optional **Gaussian smoothing** ($1\sigma$) for noise reduction in daily datasets.
* **Data Export**: Filtered search results and processed data can be exported directly to `.csv` for external analysis.
* **SQL Backend**: Efficient data management using a localized SQLite database.

## 🛠️ Technical Stack

* **Language**: Python 3.11+
* **GUI Framework**: `CustomTkinter` (Modernized Tkinter wrapper)
* **Data Science Libraries**: `NumPy`, `SciPy` (for Gaussian filtering), `Matplotlib`
* **Database**: `SQLite3`
* **Styling**: High-DPI support with a custom "Glassmorphism" aesthetic.

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/solar-activity-database.git](https://github.com/your-username/solar-activity-database.git)
    cd solar-activity-database
    ```

2.  **Install dependencies**:
    ```bash
    pip install customtkinter numpy scipy matplotlib
    ```

3.  **Run the application**:
    ```bash
    python main.py
    ```

## 📂 Project Structure

```text
├── assets/             # Icons and UI images (EUT logo, app icon, arrow)
├── data/               # SQLite database (solar_cycles.db)
├── main.py             # Main application entry point & Splash screen
└── requirements.txt    # List of Python dependencies
## 🤝 Credits

**Developed By:**  
Khaled Elzend  
Manar A. Nofal  

**Supervision:**  
Dr. Wael Mohamed