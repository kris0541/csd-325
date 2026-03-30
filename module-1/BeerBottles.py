
# Name: Kris Kleiner
# Date: 03/29/2026
# Assignment: Module 1-3 - On the Wall
# Purpose: This program asks the user how many bottles of beer
# are on the wall and counts down to 1 using a function.


def countdown_bottles(bottles):
    """This function counts down the number of bottles."""

    for count in range(bottles, 0, -1):
        if count > 1:
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")

            if count - 1 == 1:
                print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down and pass it around, {count - 1} bottles of beer on the wall.\n")

        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, 0 bottles of beer on the wall.\n")


def main():
    """Main function of the program."""

    bottles = int(input("Enter number of bottles: "))
    countdown_bottles(bottles)
    print("Time to buy more bottles of beer.")


main()