# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "EU": "European Union",
    "JP": "Japan",
    "IN": "India",
    "CN": "China",
    "SEA": "Southeast Asia",
}

# TODO: Print the country for the given country code
# TODO: # If the key is not found, print Unknown
country_code = input("Enter country code: ")
print(country_codes.get(country_code, "Unknown country code"))
