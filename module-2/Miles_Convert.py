# Name: Kris Kleiner
# Date: January 31, 2026
# Assignment: Module 4.2 Assignment

# This program converts miles to kilometers
# and displays the total of both

def main():
    # Display welcome screen.
    welcome()
    # Get the number of miles
    # Keep prompting until the user enters a valid, non-negative number.
    while True:
        try:
            miles_driven = float(input('Please enter your miles driven: '))
            if miles_driven < 0:
                print('Please enter a positive number')
            else:
                break
        except ValueError:
            print('Please enter a numeric value')
    # Convert Miles to Kilometers
    miles_to_km(miles_driven)

# The welcome function displays an introductory message
def welcome():
    print('This program converts miles to kilometers')
    print('1 mile = 1.60934 kilometers')
    print()

# The miles_to_km function accepts a number of miles
# and converts it to kilometers
# and displays the total miles and total kilometers
def miles_to_km(miles):
    kilometers = (miles * 1.60934)
    print(f'{miles} miles = {kilometers:.2f} kilometers')

#call the main function
main()