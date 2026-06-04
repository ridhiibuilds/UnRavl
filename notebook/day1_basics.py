#variables pracitce



def garment_condition():
    
    garment_type = input("What type of garment is it? ").strip().lower()
    garment_color = input("Color of garment? ").strip().lower()
    times_worn = int(input("How many times have you worn it? "))    
    
    is_bored = input("Are you bored of it? (yes/no) ").strip().lower() == "yes"  #(this is very imp cause we used manual yes and no instead of true false so to let comp know yes is ture we gotta write this otherwise even if user says no the comp think its a yes stored as string)
    is_damaged = input("Is it damaged? (yes/no) ").strip().lower() == "yes"
    doesnt_fit = input("Does it not fit anymore? (yes/no) ").strip().lower() == "yes"
    
    print(f"\n=== UnRavl Analysis ===")
    print(f"Garment: {garment_type}")
    print(f"Color: {garment_color}")
    print(f"Times worn: {times_worn}")
    
    if is_bored:
        print("→ You're bored of it. Let's transform it.")
    if is_damaged:
        print("→ It's damaged. Let's repair or upcycle it.")
    if doesnt_fit:
        print("→ It doesn't fit. Let's resize or reconstruct it.")
    if not is_bored and not is_damaged and not doesnt_fit:
        print("→ Seems fine! Are you sure you want to transform it?")

garment_condition()

