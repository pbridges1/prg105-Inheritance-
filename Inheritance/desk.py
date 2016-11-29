import inheritance


def main():
    desk = inheritance.Desk('desk', 'wood', 60, 36, 30, 377.57, 'center', 6)
    print("Item: " + desk.get_category())
    print("Material: " + desk.get_material())
    print("Length: " + str(desk.get_length()))
    print("Width: " + str(desk.get_width()))
    print("Height: " + str(desk.get_height()))
    print("Price: " + "${:0,.2f}".format(desk.get_price()))
    print("Location of drawers: " + desk.get_location())
    print("Number of drawers: " + str(desk.get_number_of_drawers()))
    print("\n")
    print desk
main()
