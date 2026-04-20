# Kris Kleiner
# Date: April 19, 2026
# Module 4 Assignment

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'

def get_weather_data():
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                continue
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows


def plot_highs(dates, highs):
    plt.figure()
    plt.plot(dates, highs, color='red')
    plt.title("Daily High Temperatures - Sitka, 2018")
    plt.xlabel('Date')
    plt.ylabel('Temperature (F)')
    plt.show()


def plot_lows(dates, lows):
    plt.figure()
    plt.plot(dates, lows, color='blue')
    plt.title("Daily Low Temperatures - Sitka, 2018")
    plt.xlabel('Date')
    plt.ylabel('Temperature (F)')
    plt.show()


def main():
    dates, highs, lows = get_weather_data()

    while True:
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            plot_highs(dates, highs)

        elif choice == '2':
            plot_lows(dates, lows)

        elif choice == '3':
            print("Exiting program. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

