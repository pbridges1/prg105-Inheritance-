import inheritance


def main():
    chair = inheritance.OfficeFurniture('chair', 'wood', 14, 12, 24, 125.57)
    print("Item: " + chair.get_category())
    print("Material: " + chair.get_material())
    print("Length: " + str(chair.get_length()))
    print("Width: " + str(chair.get_width()))
    print("Height: " + str(chair.get_height()))
    print("Price: " + "${:0,.2f}".format(chair.get_price()))

    print chair
main()
