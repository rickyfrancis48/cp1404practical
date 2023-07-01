COLOURS = {"Absolute Zero": "#0048ba",
           "Acid Green": "#b0bf1a",
           "AliceBlue": "#f0f8ff",
           "Alizarin crimson": "#e32636",
           "Amaranth": "#e52b50",
           "Amber": "#ffbf00",
           "Amethyst": "#9966cc",
           "AntiqueWhite": "#faebd7",
           "AntiqueWhite1": "#ffefdb",
           "AntiqueWhite2": "#eedfcc"}

colour_name = input("What colour? ")
while colour_name != "":
    try:
        print(COLOURS[colour_name])
    except KeyError:
        print("Invalid input")
    colour_name = input("What colour? ")
