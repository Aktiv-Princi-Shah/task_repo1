import xlwt
from xlwt import Workbook

wb = Workbook()
sheet = wb.add_sheet("Countries")

main_data = {}
csv_data = []
def create_data():
    """
    define: create_data
    description: Interactively prompts the user to input hierarchical data for countries, states, and cities.
                 The data is stored in a global dictionary, `main_data`, with the following structure:
                 `{country_name: {state_name: [city1, city2, ...]}}`.
                 The function uses nested loops to allow the user to add multiple countries,
                 each with multiple states, and each state with multiple cities.
    """
    global main_data
    while True:
        country_input = input("Enter if you want to add a country (y/n):")
        if country_input == 'n':
            if main_data:
                print("You created Data: ",main_data)
            return
        elif country_input != 'y':
            print("Unknown Option")
            continue
        else:
            country_name = input("Enter the country name: ")
            if country_name in main_data:
                print("This country already exists. Please enter new country name.")
                continue
            main_data[country_name] = {}
            while True:
                state_input = input("Enter if you want to add a state (y/n):")
                if state_input == 'n':
                    break
                elif state_input != 'y':
                    print("Unknown Option")
                    continue
                else:
                    state_name = input("Enter the state name: ")
                    if state_name in main_data[country_name]:
                        print("This state already exists. Please enter new state name.")
                        continue
                    main_data[country_name][state_name] = []
                    while True:
                        city_input = input("Enter if you want to add a city (y/n):")
                        if city_input == 'n':
                            break
                        elif city_input != 'y':
                            print("Unknown Option")
                            continue
                        else:
                            city_name = input("Enter the city name: ")
                            if city_name in main_data[country_name][state_name]:
                                print("This city already exists. Please enter new city name.")
                                continue
                            main_data[country_name][state_name].append(city_name)

def static_data(dict_data):
    """
    define: static_data
    description: Flattens a nested dictionary of country, state, and city data into a list of lists.
                 This function iterates through the nested dictionary and converts it into a
                 structured list suitable for writing to a spreadsheet, ensuring that parent
                 values (country and state) are only listed on the first row of their respective
                 groupings to avoid redundancy.
    param: dict_data
    """
    if not dict_data:
        print("No data to export.")
        return
    for country in dict_data:
        if not dict_data[country]:
            csv_data.append([country, "", ""])
            continue
        for sidx, state in enumerate(dict_data[country]):
            state_cities = dict_data[country][state]
            if not state_cities:
                csv_data.append([country if sidx == 0 else "", state, ""])
            else:
                for cidx, city in enumerate(state_cities):
                    csv_data.append([
                        country if sidx == 0 and cidx == 0 else "",
                        state if cidx == 0 else "", city])

def data_in_excel(data_list, filename="countries.xls"):
    """
    define: data_in_excel
    description: Writes a list of data to an Excel file with a specific format.
                 The function creates a new sheet, adds a header row for 'Country', 'State', and 'City',
                 and then populates the sheet with the provided data list. It also includes
                 a blank row between each country's data for better readability.
    """

    header_style = xlwt.easyxf("Font: bold 1")
    sheet.write(0, 0, "Country", header_style)
    sheet.write(0, 1, "State", header_style)
    sheet.write(0, 2, "City", header_style)
    row_idx = 2
    prev_country = None

    for country, state, city in data_list:
        if country and country != prev_country and prev_country is not None:
            row_idx += 1

        sheet.write(row_idx, 0, country)
        sheet.write(row_idx, 1, state)
        sheet.write(row_idx, 2, city)
        prev_country = country or prev_country
        row_idx = row_idx + 1
    wb.save(filename)
    print(f"Data saved in the {filename}")

while True:
    choice = input("\n1. Inbuilt data to make Excel\n2. New build data to make Excel\n3. Exit\nWhat do you want: ")
    if choice == "1":
        csv_data = []
        static_data({
            'India': {"Gujarat": ['Ahmedabad', "Gandhinagar"], 'Rajasthan': ["Udaipur", "Jodhpur"]},
            'Pakistan': {"Punjab": ['Lahore', "Faisalabad"], 'Sindh': ["Karachi", "Hyderabad"]}
        })
        data_in_excel(csv_data)
        break
    elif choice == "2":
        csv_data = []
        create_data()
        static_data(main_data)
        data_in_excel(csv_data)
        break
    elif choice == "3":
        print("Thank You, Exiting!")
        exit()
    else:
        print("Invalid input! Please enter from choices mentioned in the above menu.")
