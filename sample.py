def hide_char():
    name="Rama"
    char='a'
    count=0
    hidden_string=""
    for c in name:
        if c==char:
            hidden_string +=""
            
        else:
            hidden_string += c
    print(hidden_string)

hide_char()
