from utils import get_random_dhikr, save_reflection, view_reflections

dhikr = get_random_dhikr()
print("Today's Dhikr:", dhikr["phrase"])
print("Meaning:", dhikr["meaning"])

choice = input("Do you want to (1) write a reflection or (2) view past reflections? ")

if choice == "1":
    reflection = input("Write your reflection: ")
    save_reflection(dhikr["phrase"], reflection)
    print("Reflection saved successfully!")
elif choice == "2":
    view_reflections()
else:
    print("Invalid choice.")


