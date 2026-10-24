import random
from datetime import datetime

def get_random_dhikr():
    """Return a random dhikr phrase with meaning."""
    dhikr_phrases = [
        {"phrase": "Astaghfirullah", "meaning": "I seek forgiveness from Allah"},
        {"phrase": "SubhanAllah", "meaning": "Glory be to Allah"},
        {"phrase": "Alhamdulillah", "meaning": "All praise is due to Allah"},
        {"phrase": "Allahu Akbar", "meaning": "Allah is the Greatest"},
        {"phrase": "La ilaha illallah", "meaning": "There is no god but Allah"},
        {"phrase": "Hasbunallahu wa ni'mal wakeel", "meaning": "Allah is sufficient for us, and He is the best disposer of affairs"},
        {"phrase": "La hawla wa la quwwata illa billah", "meaning": "There is no power nor strength except with Allah"},
        {"phrase": "Allahumma inni as'aluka al-jannah", "meaning": "O Allah, I ask You for Paradise"},
        {"phrase": "Allahumma ajirni minan naar", "meaning": "O Allah, protect me from the Fire"},
        {"phrase": "Ya Hayyu Ya Qayyum", "meaning": "O Ever-Living, O Sustainer"}
    ]
    return random.choice(dhikr_phrases)

def save_reflection(phrase, reflection, filename="reflections.txt"):
    """Save a reflection with date and time."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{now} | {phrase}: {reflection}\n")

def view_reflections(filename="reflections.txt"):
    """Read and return all reflections."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
        
def reset_reflections(filename="reflections.txt"):
    """Clear all reflections."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("")
