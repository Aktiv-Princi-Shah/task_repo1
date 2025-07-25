import csv

locations = {}
def build_location_data():
    global locations
    while True:
        country_choice = input("Add a country? (y/n): ")
        if country_choice == 'n':
            if not locations:
                print("No data created.")
            else:
                print("Created data:")
            return
        elif country_choice != 'y':
            print("Invalid option. \nPlease type 'y' or 'n'.")
            continue

        country = input("Enter country name: ")
        if country in locations:
            print("Country already exists. Try deleting it or add a new one.")
            continue
        locations[country] = {}

        while True:
            state_choice = input(f"Add a state in {country}? (y/n): ")
            if state_choice == 'n':
                break
            elif state_choice != 'y':
                print("Invalid option.")
                continue

            state = input("Enter state name: ")
            if state in locations[country]:
                print("State already exists. Try a different one.")
                continue
            locations[country][state] = []

            while True:
                city_choice = input(f"Add a city in state '{state}' of '{country}'? (y/n): ")
                if city_choice == 'n':
                    break
                elif city_choice != 'y':
                    print("Invalid input.")
                    continue

                city = input("Enter city name: ")
                if city in locations[country][state]:
                    print("City already added.")
                    continue

                locations[country][state].append(city)

csv_data = []

def convert_dict_to_list(loc_dict):
    if not loc_dict:
        print("No data to convert.")
        return

    for country in loc_dict:
        if not loc_dict[country]:
            csv_data.append([country, "", ""])
            continue

        for state in loc_dict[country]:
            cities = loc_dict[country][state]
            if not cities:
                csv_data.append([country, state, ""])
            else:
                first_row = True
                for city in cities:
                    if first_row:
                        csv_data.append([country, state, city])
                        first_row = False
                    else:
                        csv_data.append(["", "", city])

while True:
    choice = input(
        "\nTo use built-in data type 'default'\nTo enter your own data type 'manual'\nYour choice: ").strip().lower()

    if choice == "default":
        sample_data = {
            "India": {
                "Gujarat": ["Ahmedabad", "Surat"],
                "Rajasthan": ["Jaipur", "Udaipur"]
            },
            "Nepal": {
                "Bagmati": ["Kathmandu", "Lalitpur"],
                "Gandaki": ["Pokhara"]
            }
        }
        convert_dict_to_list(sample_data)
        break
    elif choice == "manual":
        build_location_data()
        convert_dict_to_list(locations)
        break
    else:
        print("Invalid choice. Please type 'default' or 'manual'.")

with open("output.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Country", "State", "City"])
    for row in csv_data:
        writer.writerow(row)

print("\nCSV data saved successfully.")
print("Final data:\n", csv_data)