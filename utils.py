import random
from datetime import datetime

# ✅ Expanded Dhikr Phrases (100 entries)
dhikr_phrases = [
    ("SubhanAllah", "Glory be to Allah"),
    ("Alhamdulillah", "All praise is due to Allah"),
    ("Allahu Akbar", "Allah is the Greatest"),
    ("La ilaha illallah", "There is no god but Allah"),
    ("Astaghfirullah", "I seek forgiveness from Allah"),
    ("Hasbunallahu wa ni'mal wakeel", "Allah is sufficient for us, and He is the best disposer of affairs"),
    ("La hawla wa la quwwata illa billah", "There is no power nor strength except with Allah"),
    ("Sallallahu 'alayhi wa sallam", "Peace and blessings be upon him"),
    ("Rabbi zidni ilma", "My Lord, increase me in knowledge"),
    ("Allahumma inni as'aluka al-jannah", "O Allah, I ask You for Paradise"),
    ("Allahumma ajirni minan naar", "O Allah, protect me from the Fire"),
    ("Allahumma inni as'aluka husnal khatimah", "O Allah, I ask You for a good ending"),
    ("Allahumma inni as'aluka sihhatan fi iman", "O Allah, grant me health with faith"),
    ("Allahumma inni as'aluka rizqan tayyiban", "O Allah, grant me pure sustenance"),
    ("Allahumma inni as'aluka tawfiqan fi deen", "O Allah, grant me success in religion"),
    ("Allahumma inni as'aluka sabran jameelan", "O Allah, grant me beautiful patience"),
    ("Allahumma inni as'aluka qalban saleeman", "O Allah, grant me a sound heart"),
    ("Allahumma inni as'aluka maghfiratan wa rahmah", "O Allah, grant me forgiveness and mercy"),
    ("Allahumma inni as'aluka barakatan fi rizq", "O Allah, bless my sustenance"),
    ("Allahumma inni as'aluka 'afiyatan fi dunya wal akhirah", "O Allah, grant me well-being in this world and the Hereafter"),
    ("Allahumma inni as'aluka hubbaka", "O Allah, grant me Your love"),
    ("Allahumma inni as'aluka husnal akhlaq", "O Allah, grant me good character"),
    ("Allahumma inni as'aluka 'ilman nafi'an", "O Allah, grant me beneficial knowledge"),
    ("Allahumma inni as'aluka shifaa'an min kulli daa'", "O Allah, grant me healing from every illness"),
    ("Allahumma inni as'aluka barakatan fi waqt", "O Allah, bless my time"),
    ("Allahumma inni as'aluka barakatan fi 'amal", "O Allah, bless my deeds"),
    ("Allahumma inni as'aluka barakatan fi 'ilm", "O Allah, bless my knowledge"),
    ("Allahumma inni as'aluka barakatan fi 'umr", "O Allah, bless my lifespan"),
    ("Allahumma inni as'aluka barakatan fi ahl", "O Allah, bless my family"),
    ("Allahumma inni as'aluka barakatan fi maal", "O Allah, bless my wealth"),
    ("Allahumma inni as'aluka barakatan fi walad", "O Allah, bless my children"),
    ("Allahumma inni as'aluka barakatan fi deen", "O Allah, bless my religion"),
    ("Allahumma inni as'aluka barakatan fi dunya", "O Allah, bless my worldly life"),
    ("Allahumma inni as'aluka barakatan fi akhirah", "O Allah, bless my Hereafter"),
    ("Allahumma inni as'aluka barakatan fi qalb", "O Allah, bless my heart"),
    ("Allahumma inni as'aluka barakatan fi niyyah", "O Allah, bless my intention"),
    ("Allahumma inni as'aluka barakatan fi sabr", "O Allah, bless my patience"),
    ("Allahumma inni as'aluka barakatan fi shukr", "O Allah, bless my gratitude"),
    ("Allahumma inni as'aluka barakatan fi tawbah", "O Allah, bless my repentance"),
    ("Allahumma inni as'aluka barakatan fi dhikr", "O Allah, bless my remembrance"),
    ("Allahumma inni as'aluka barakatan fi salah", "O Allah, bless my prayer"),
    ("Allahumma inni as'aluka barakatan fi sawm", "O Allah, bless my fasting"),
    ("Allahumma inni as'aluka barakatan fi hajj", "O Allah, bless my pilgrimage"),
    ("Allahumma inni as'aluka barakatan fi sadaqah", "O Allah, bless my charity"),
    ("Allahumma inni as'aluka barakatan fi jihad", "O Allah, bless my striving"),
    ("Allahumma inni as'aluka barakatan fi quran", "O Allah, bless my recitation of the Qur'an"),
    ("Allahumma inni as'aluka barakatan fi tasbih", "O Allah, bless my glorification of You"),
    ("Allahumma inni as'aluka barakatan fi tahmid", "O Allah, bless my praise of You"),
    ("Allahumma inni as'aluka barakatan fi takbir", "O Allah, bless my declaration of Your greatness"),
    ("Allahumma inni as'aluka barakatan fi tahlil", "O Allah, bless my declaration of Your oneness"),
    ("Allahumma inni as'aluka barakatan fi istighfar", "O Allah, bless my seeking forgiveness"),
    ("Allahumma inni as'aluka barakatan fi tawakkul", "O Allah, bless my reliance on You"),
    ("Allahumma inni as'aluka barakatan fi ikhlas", "O Allah, bless my sincerity"),
    ("Allahumma inni as'aluka barakatan fi taqwa", "O Allah, bless my God-consciousness"),
    ("Allahumma inni as'aluka barakatan fi husnul khuluq", "O Allah, bless my good manners"),
    ("Allahumma inni as'aluka barakatan fi husnul khatimah", "O Allah, bless my good ending"),
    ("Allahumma inni as'aluka barakatan fi rahmah", "O Allah, bless me with mercy"),
    ("Allahumma inni as'aluka barakatan fi maghfirah", "O Allah, bless me with forgiveness"),
    ("Allahumma inni as'aluka barakatan fi hidayah", "O Allah, bless me with guidance"),
    ("Allahumma inni as'aluka barakatan fi nur", "O Allah, bless me with light"),
    ("Allahumma inni as'aluka barakatan fi sakinah", "O Allah, bless me with tranquility"),
    ("Allahumma inni as'aluka barakatan fi aman", "O Allah, bless me with safety"),
    ("Allahumma inni as'aluka barakatan fi barakah", "O Allah, bless me with abundance"),
    ("Allahumma inni as'aluka barakatan fi 'afiyah", "O Allah, bless me with well-being"),
    ("Allahumma inni as'aluka barakatan fi sabr wa shukr", "O Allah, bless me with patience and gratitude"),
    ("Allahumma inni as'aluka barakatan fi tawfiq", "O Allah, bless me with success"),
    ("Allahumma inni as'aluka barakatan fi barakah fi kulli shay", "O Allah, bless me with blessings in everything"),
    ("Allahumma inni as'aluka barakatan fi barakah fi waqt", "O Allah, bless me with blessings in time"),
    ("Allahumma inni as'aluka barakatan fi barakah fi rizq", "O Allah, bless me with blessings in sustenance"),
    ("Allahumma inni as'aluka barakatan fi barakah fi 'amal", "O Allah, bless me with blessings in deeds"),
    ("Allahumma inni as'aluka barakatan fi barakah fi 'ilm", "O Allah, bless me with blessings in knowledge"),
    ("Allahumma inni as'aluka barakatan fi barakah fi qalb", "O Allah, bless me with blessings in heart"),
    ("Allahumma inni as'aluka barakatan fi barakah fi niyyah", "O Allah, bless me with blessings in intention"),
    ("Allahumma inni as'aluka barakatan fi barakah fi sabr", "O Allah, bless me with blessings in patience"),
    ("Allahumma inni as'aluka barakatan fi barakah fi shukr", "O Allah, bless me with blessings in gratitude"),
    ("Allahumma inni as'aluka barakatan fi barakah fi tawbah", "O Allah, bless me with blessings in repentance"),
    ("Allahumma inni as'aluka barakatan fi barakah fi dhikr", "O Allah, bless me with blessings in remembrance"),
    ("Allahumma inni as'aluka barakatan fi barakah fi salah", "O Allah, bless me with blessings in prayer"),
    ("Allahumma inni as'aluka barakatan fi barakah fi sawm", "O Allah, bless me with blessings in fasting"),
    ("Allahumma inni as'aluka barakatan fi barakah fi hajj", "O Allah, bless me with blessings in pilgrimage"),
    ("Allahumma inni as'aluka barakatan fi barakah fi sadaqa", "O Allah, bless me with blessings in patience"),
    ("Allahumma inni as'aluka barakatan fi barakah fi qiyamah", "O Allah, bless me with blessings in the Hereafter"),
    ("Allahumma inni as'aluka barakatan fi barakah fi jannah", "O Allah, bless me with blessings in Paradise"),
]

def get_random_dhikr():
    """Return a random dhikr phrase and its meaning."""
    return random.choice(dhikr_phrases)

def save_reflection(phrase, reflection, filename="reflections.txt"):
    """Save reflection with timestamp, only if reflection is not empty."""
    reflection = reflection.strip()
    if not reflection:  # ✅ validation: skip empty reflections
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{phrase} ({timestamp}): {reflection}\n")

def reset_reflections(filename="reflections.txt"):
    """Clear all reflections safely without deleting the file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("")  # ✅ overwrite with empty content

