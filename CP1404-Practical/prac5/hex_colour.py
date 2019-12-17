def main():
    colour_hex = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                  "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0",
                  "antiquewhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                  "aquamarine4": "#458b74", "azure1": "#f0ffff"}

    name_color = input("Enter a colour name: ").upper()
    while name_color != "":
        print("The code for {} is {}".format(name_color, colour_hex.get(name_color)))
        name_color = input("Enter a colour name: ").upper()
main()