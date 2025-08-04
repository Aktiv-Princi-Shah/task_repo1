# -*- coding: UTF-8 -*-
main_dict = {}

def insert_country():
    ''' country creation function '''
    countries = input("Enter country name(s) (comma-separated): ").split(',')
    for country in countries:
        country = country.strip()
        # Skips blank user inputs
        if not country:
            continue
        if country not in main_dict:
            main_dict[country] = {}
        else:
            print(f"{country} already exists.")

def insert_state():
    ''' state creation function '''
    country = input("Enter country name: ").strip()
    if not country:
        return
    if country not in main_dict:
        print("Country doesn't exist. Please insert country first.")
        return
    states = input("Enter state name(s) (comma-separated): ").split(',')
    for state in states:
        state = state.strip()
        # Skips blank user inputs
        if not state:
            continue
        if state not in main_dict[country]:
            main_dict[country][state] = []
        else:
            print(f"{state} already exists in {country}.")

def insert_city():
    ''' city creation function '''
    country = input("Enter country name: ").strip()
    if not country or country not in main_dict:
        print("Country doesn't exist. Please insert country first.")
        return
    state = input("Enter state name: ").strip()
    if not state:
        return
    if state not in main_dict[country]:
        print("State doesn't exist. Please insert state first.")
        return
    cities = input("Enter city name(s) (comma-separated): ").split(',')
    for city in cities:
        city = city.strip()
        # Skips blank user inputs
        if not city:
            continue
        if city not in main_dict[country][state]:
            main_dict[country][state].append(city)
        else:
            print(f"{city} already exists in {state}, {country}.")

def update_country():
    ''' country updation function '''
    old_country = input("Enter existing country name: ").strip()
    if old_country not in main_dict:
        print("Country not found.")
        return
    new_country = input("Enter new name for the country: ").strip()
    # Skips blank user inputs
    if not new_country:
        print("New country name cannot be blank.")
        return
    main_dict[new_country] = main_dict.pop(old_country)
    print("Country name updated successfully.")

def update_state():
    ''' state updation function '''
    country = input("Enter country name: ").strip()
    if country not in main_dict:
        print("Country not found.")
        return
    old_state = input("Enter existing state name: ").strip()
    if old_state not in main_dict[country]:
        print("State not found.")
        return
    new_state = input("Enter new name for the state: ").strip()
    # Skips blank user inputs
    if not new_state:
        print("New state name cannot be blank.")
        return
    main_dict[country][new_state] = main_dict[country].pop(old_state)
    print("State name updated successfully.")

def update_city():
    ''' city updation function '''
    country = input("Enter country name: ").strip()
    if country not in main_dict:
        print("Country not found.")
        return
    state = input("Enter state name: ").strip()
    if state not in main_dict[country]:
        print("State not found.")
        return
    old_city = input("Enter existing city name: ").strip()
    if old_city not in main_dict[country][state]:
        print("City not found.")
        return
    new_city = input("Enter new name for the city: ").strip()
    # Skips blank user inputs
    if not new_city:
        print("New city name cannot be blank.")
        return
    idx = main_dict[country][state].index(old_city)
    main_dict[country][state][idx] = new_city
    print("City name updated successfully.")

def delete_country():
    ''' country deletion function '''
    country = input("Enter country name to delete: ").strip()
    if country in main_dict:
        del main_dict[country]
        print(f"{country} deleted successfully.")
    else:
        print("Country not found.")

def delete_state():
    ''' state deletion function '''
    country = input("Enter country name: ").strip()
    if country not in main_dict:
        print("Country not found.")
        return
    state = input("Enter state name to delete: ").strip()
    if state in main_dict[country]:
        del main_dict[country][state]
        print(f"{state} deleted successfully.")
    else:
        print("State not found.")

def delete_city():
    ''' city deletion function '''
    country = input("Enter country name: ").strip()
    if country not in main_dict:
        print("Country not found.")
        return
    state = input("Enter state name: ").strip()
    if state not in main_dict[country]:
        print("State not found.")
        return
    city = input("Enter city name to delete: ").strip()
    if city in main_dict[country][state]:
        main_dict[country][state].remove(city)
        print(f"{city} deleted successfully.")
    else:
        print("City not found.")

def display_data():
    ''' dictionary data display function '''
    if not main_dict:
        print("No data available.")
        return
    for country, states in main_dict.items():
        print(f"\nCountry: {country}")
        for state, cities in states.items():
            city_data = [c for c in cities if c.strip()]
            print(f"  State: {state}  \n   Cities: {', '.join(city_data)}")

def insert_menu():
    ''' data creation menu function '''
    print("\nInsert Menu:")
    print("1. Insert Country\n2. Insert State\n3. Insert City")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        insert_country()
    elif choice == '2':
        insert_state()
    elif choice == '3':
        insert_city()
    else:
        print("Invalid choice.")

def update_menu():
    ''' data updation menu function '''
    print("\nUpdate Menu:")
    print("1. Update Country\n2. Update State\n3. Update City")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        update_country()
    elif choice == '2':
        update_state()
    elif choice == '3':
        update_city()
    else:
        print("Invalid choice.")

def delete_menu():
    ''' data deletion menu function '''
    print("\nDelete Menu:")
    print("1. Delete Country\n2. Delete State\n3. Delete City")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        delete_country()
    elif choice == '2':
        delete_state()
    elif choice == '3':
        delete_city()
    else:
        print("Invalid choice.")

def main_menu():
    ''' data crud main menu function '''
    while True:
        print("\n======= Main Menu =======")
        print("1. Insert\n2. Update\n3. Delete\n4. Display\n5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            insert_menu()
        elif choice == '2':
            update_menu()
        elif choice == '3':
            delete_menu()
        elif choice == '4':
            display_data()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()