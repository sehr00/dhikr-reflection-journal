# 🕌 Dhikr Reflection Journal

A simple Python program that helps you reflect on daily dhikr (remembrance of Allah).  
Each time you run the program, it shows a random dhikr phrase with its meaning, and you can either write a reflection or view your past reflections.

---



---
## Project Structure

Dhikr Reflection Journal/
├── main.py          # Program entry point
├── utils.py         # Helper functions
├── reflections.txt  # Saved reflections
└── README.md        # Documentation



---

## ▶️ How to Run
1. Clone or download the project.
2. Run the program:
   ```bash
   python main.py




---
## Features
- Display a random dhikr phrase with meaning
- Write and save personal reflections to `reflections.txt`
- View all past reflections in a clean format
- Expandable list of dhikr phrases (includes SubhanAllah, Alhamdulillah, Allahu Akbar, La ilaha illallah, and many more)



## Example Output
Today's Dhikr: La hawla wa la quwwata illa billah
Meaning: There is no power nor strength except with Allah
Do you want to (1) write a reflection or (2) view past reflections? 1
Write your reflection: This reminds me to rely only on Allah.
Reflection saved successfully!



## 📌 Project Roadmap: Dhikr Reflection Journal

This project is under active development. Here are the planned milestones:

### ✅ Completed
- Basic program structure (`main.py` + `utils.py`)
- Random Dhikr phrase generator
- Save reflections to `reflections.txt`
- View past reflections

### 🚀 Next Steps
- Add reset function to clear reflections
- Save date/time with each reflection
- Search reflections by keyword
- Export reflections to CSV/JSON
- Improve error handling (default option if no input given)

### 🌟 Future Enhancements
- GUI version (Tkinter or PyQt)
- Web app version (Flask/Django)
- Mobile app integration
- Cloud sync with GitHub or Google Drive




























# 🕌 Dhikr Reflection Journal

A simple Python + Flask project that helps you reflect on daily dhikr (remembrance of Allah).  
Each time you run the program, it shows a random dhikr phrase with its meaning, and you can either write a reflection or view your past reflections.  
Now available in both **terminal** and **web app** versions.

---

## 📂 Project Structure
Dhikr Reflection Journal/
├── main.py          # Terminal version entry point
├── app.py           # Flask web app entry point
├── utils.py         # Helper functions (dhikr, save, reset, etc.)
├── reflections.txt  # Saved reflections
├── templates/       # HTML templates (index.html, reflections.html)
├── static/          # CSS styling (style.css)
├── README.md        # Documentation
└── LICENSE          # License file

---

## ▶️ How to Run (Terminal Version)
1. Clone or download the project.
2. Run the program:
   ```bash
   python main.py


---

## ▶️ How to Run (Web Version)
1.Clone the repo:
git clone https://github.com/yourusername/Dhikr-Reflection-Journal.git
cd Dhikr-Reflection-Journal
2.Install dependencies:
pip install flask
3.Run the app:
python app.py
4.Open your web browser and go to:
 http://127.0.0.1:5000/ to access the app.


 ---

✨ Features
Display a random dhikr phrase with meaning

Write and save personal reflections to reflections.txt

View all past reflections in a clean format

Reset button to clear all reflections

Date/time stamps for each reflection

Expandable list of dhikr phrases

Styled web interface with CSS


---

## 📖 Example Output (Terminal)
Today's Dhikr: La hawla wa la quwwata illa billah
Meaning: There is no power nor strength except with Allah
Do you want to (1) write a reflection or (2) view past reflections? 1
Write your reflection: This reminds me to rely only on Allah.
Reflection saved successfully!


---

## 📖 Web Version Usage Example
🏠 Home Page
Shows a random Dhikr phrase with its meaning.

Provides a text box to write your reflection.

Click Save Reflection to store it.

📜 Reflections Page
Displays all saved reflections with date/time stamps.

Example entries:
2026-10-24 12:25:10 | Alhamdulillah: I felt grateful today.
2026-10-24 12:26:45 | Astaghfirullah: I asked forgiveness sincerely.
Includes a Reset All Reflections button to clear the journal.
🎨 Styling
Pages are styled with static/style.css for a clean, journal-like look.

Buttons, text areas, and reflection entries are neatly formatted.


---

📌 Project Roadmap
✅ Completed
Basic program structure (main.py + utils.py)

Random Dhikr phrase generator

Save reflections to reflections.txt

View past reflections

Reset function to clear reflections

Save date/time with each reflection

Flask web version with templates + CSS


🚀 Next Steps
Search reflections by keyword

Export reflections to CSV/JSON

Improve error handling (default option if no input given)

🌟 Future Enhancements
GUI version (Tkinter or PyQt)

Mobile app integration

Cloud sync with GitHub or Google Drive

Deployment to Heroku or PythonAnywhere

---

🌟 Example Screenshots