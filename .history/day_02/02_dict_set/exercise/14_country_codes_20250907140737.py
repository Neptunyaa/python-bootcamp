# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
}

code_number = int(input("How many country code: "))
for _ in range(code_number):
    country_name = input("Enter country name: ")
    country_codes.add(country_name)
print(country_codes)
