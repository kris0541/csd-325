# Name: Kris Kleiner
# Date: May 3 2026
# Assignment: Module 7 - Test Cases
# Purpose: Create and test a function that formats city, country, population, and language information.


def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language.title()}"

    return result


if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", 13960000))
    print(city_country("madrid", "spain", 3223000, "spanish"))