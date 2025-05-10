def next_day():
    txt=input("What a day of the week is it today?")
    txt=txt.lower().strip()
    if txt=="monday":
        new_txt="tuesday"
    elif txt=="tuesday":
        new_txt="wednesday"
    elif txt=="wednesday":
        new_txt="thursday"
    elif txt=="thursday":
        new_txt="friday"
    elif txt=="friday":
        new_txt="saturday"
    elif txt=="saturday":
        new_txt="sunday"
    elif txt=="sunday":
        new_txt="monday"
    else:
        print("There is no day of the week")
        return
    print(f"Tomorrow - {new_txt}")
    def get_name():
        name=input("Good afternoon! What is your name?")
        if name.strip()==" .,:;!?_"=="":
            name="Mr X"
        return name
    def hello():
        name=get_name()
        print(f"Nice to meet you, {name}!")
        next_day()
    hello()