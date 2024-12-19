def hide_char():
    name="Rama"
    for i in name:
        if i=="a":
            continue
        print(i,end="")
hide_char()