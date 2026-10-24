import random

def get_random_dhikr():
    """Return a random dhikr phrase with meaning."""
    dhikr_phrases = [
        {"phrase": "Astaghfirullah", "meaning": "I seek forgiveness from Allah"},
        {"phrase": "SubhanAllah", "meaning": "Glory be to Allah"},
        {"phrase": "Alhamdulillah", "meaning": "All praise is due to Allah"},
        {"phrase": "Allahu Akbar", "meaning": "Allah is the Greatest"},
        {"phrase": "La ilaha illallah", "meaning": "There is no god but Allah"},
        {"phrase": "SubhanAllahi wa bihamdihi", "meaning": "Glory be to Allah and praise Him"},
        {"phrase": "SubhanAllahi Al-Azim", "meaning": "Glory be to Allah, the Magnificent"},
        {"phrase": "Hasbunallahu wa ni'mal wakeel", "meaning": "Allah is sufficient for us, and He is the best disposer of affairs"},
        {"phrase": "La hawla wa la quwwata illa billah", "meaning": "There is no power nor strength except with Allah"},
        {"phrase": "Ya Hayyu Ya Qayyum, birahmatika astagheeth", "meaning": "O Ever-Living, O Sustainer, by Your mercy I seek help"},
        {"phrase": "Sallallahu 'alayhi wa sallam", "meaning": "Peace and blessings be upon him"},
        {"phrase": "Rabbi inni lima anzalta ilayya min khayrin faqir", "meaning": "My Lord, indeed I am in need of whatever good You send down to me"},
        {"phrase": "Allahumma inni as'aluka husnal khatimah", "meaning": "O Allah, I ask You for a good ending"},
        {"phrase": "Allahumma inni as'aluka al-jannah", "meaning": "O Allah, I ask You for Paradise"},
        {"phrase": "Allahumma ajirni minan naar", "meaning": "O Allah, protect me from the Fire"}
    ]
    return random.choice(dhikr_phrases)


def save_reflection(phrase, reflection, filename="reflections.txt"):
    """Save a reflection about a dhikr phrase to a file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{phrase}: {reflection}\n")


def view_reflections(filename="reflections.txt"):
    """Read and display all saved reflections."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("No reflections saved yet.")
            else:
                print("\n--- Your Dhikr Reflections ---")
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No reflections file found yet.")
