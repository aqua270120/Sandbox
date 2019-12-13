def main():
    colour_hex = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                  "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0",
                  "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                  "aquamarine4": "#458b74", "azure1": "#f0ffff"}

    name_color = input("Enter a colour name: ")
    while name_color != "":
        print("The code for {} is {}".format(name_color, colour_hex.get(name_color)))
        name_color = input("Enter a colour name: ")
main()