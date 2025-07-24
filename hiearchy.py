main_dict = {}

def insert_data():
    while True:
        country = input("Enter Country Name (or 'Q' to exit/ 'S' to stop): ")
        if country == 'Q':
            return
        if country == 'S':
            break
        if country not in main_dict:
            main_dict[country] = {}

        while True:
            state = input("Enter State for " + country + " (or 'Q' to exit/ 'S' to stop): ")
            if state == 'Q':
                return
            if state == 'S':
                break
            if state not in main_dict[country]:
                main_dict[country][state] = []

            while True:
                city = input("Enter City for " + state + " (or 'Q' to exit/ 'S' to stop): ")
                if city == 'Q':
                    return
                if city == 'S':
                    break
                if city not in main_dict[country][state]:
                    main_dict[country][state].append(city)
                else:
                    print("City already exists in the state.")

def update_data():
    print("\nUpdate Menu:")
    print("1. Update Country Name\n2. Update State Name\n3. Update City Name\n4. Append City\n5. Add New State")
    update_choice = input("Enter your choice: ")

    if update_choice == '1':
        old_country = input("Enter existing Country name: ")
        if old_country not in main_dict:
            print("Country not found.")
            return
        new_country = input("Enter new name for the country: ")
        main_dict[new_country] = main_dict.pop(old_country)
        print("Country name updated successfully.")

    elif update_choice == '2':
        country = input("Enter Country name: ")
        if country not in main_dict:
            print("Country not found.")
            return
        old_state = input("Enter existing State name: ")
        if old_state not in main_dict[country]:
            print("State not found.")
            return
        new_state = input("Enter new name for the state: ")
        main_dict[country][new_state] = main_dict[country].pop(old_state)
        print("State name updated successfully.")

    elif update_choice == '3':
        country = input("Enter Country name: ")
        if country not in main_dict:
            print("Country not found.")
            return
        state = input("Enter State name: ")
        if state not in main_dict[country]:
            print("State not found.")
            return
        old_city = input("Enter existing City name: ")
        if old_city not in main_dict[country][state]:
            print("City not found.")
            return
        new_city = input("Enter new name for the city: ")
        idx = main_dict[country][state].index(old_city)
        main_dict[country][state][idx] = new_city
        print("City name updated successfully.")

    elif update_choice == '4':
        country = input("Enter Country name: ")
        if country not in main_dict:
            print("Country not found.")
            return
        state = input("Enter State name: ")
        if state not in main_dict[country]:
            print("State not found.")
            return
        city = input("Enter City to add: ")
        if city not in main_dict[country][state]:
            main_dict[country][state].append(city)
            print("City added successfully.")
        else:
            print("City already exists in the state.")

    elif update_choice == '5':
        country = input("Enter Country name to add new state: ")
        if country not in main_dict:
            print("Country not found.")
            return
        new_state = input("Enter new state name: ")
        if new_state not in main_dict[country]:
            main_dict[country][new_state] = []
            print("State added successfully.")
        else:
            print("State already exists in the country.")

    else:
        print("Invalid choice.")

def delete_data():
    print("Delete Menu:")
    print("1. Delete Country\n2. Delete State \n3. Delete City \n4. Exit")
    del_choice = input("Enter your choice: ")

    if del_choice == '1':
        country = input("Enter Country to delete: ")
        if country in main_dict:
            del main_dict[country]
            print("Country delted!!")
        else:
            print("Country not found.")
    elif del_choice == '2':
        country = input("Enter Country: ")
        if country in main_dict:
            state = input("Enter State to Delete: ")
            if state in main_dict[country]:
                del main_dict[country][state]
                print("State deleted!!")
            else:
                print("State not found in the country.")
    elif del_choice == '3':
        country = input("Enter Country: ")
        if country in main_dict:
            state = input("Enter State: ")
            if state in main_dict[country]:
                city = input("Enter City to Delete: ")
                if city in main_dict[country][state]:
                    main_dict[country][state].remove(city)
                    print("City deleted!! :(")
                else:
                    print("City not found in the state.")
            else:
                print("State not found in the country.")
        else:
            print("Country not found.")

    elif del_choice == '4':
        print("Exiting...")
        return
    else:
        print("Invalid choice.")

def display_data():
    print("--- Your Data ---")
    if not main_dict:
        print("No data available.")
    else:
        for country, states in main_dict.items():
            print("Country: ", country)
            for state, cities in states.items():
                print(" State: ", state)
                if cities:
                    print(" cities: ", cities)
                else:
                    print(" No cities added. ")

while True:
    print(" Menu ")
    print("1. Insert\n2. Update\n3. Delete\n4. Display\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        insert_data()
    elif choice == '2':
        update_data()
    elif choice == '3':
        delete_data()
    elif choice == '4':
        display_data()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid Choice Insertion. Please enter between 1-5.")

def insert_data():
    while True:
        country = input("Enter Country Name (or 'Q' to exit/ 'S' to stop): ")
        if country == 'Q':
            return
        if country == 'S':
            break
        if country not in main_dict:
            main_dict[country] = {}

        while True:
            state = input("Enter State for " + country + " (or 'Q' to exit/ 'S' to stop): ")
            if state == 'Q':
                return
            if state == 'S':
                break
            if state not in main_dict[country]:
                main_dict[country][state] = []

            while True:
                city = input("Enter City for " + state + " (or 'Q' to exit/ 'S' to stop): ")
                if city == 'Q':
                    return
                if city == 'S':
                    break
                if city not in main_dict[country][state]:
                    main_dict[country][state].append(city)
                else:
                    print("City already exists in the state.")

def update_data():
    print("\nUpdate Menu:")
    print("1. Update Country Name\n2. Update State Name\n3. Update City Name\n4. Append City\n5. Add New State")
    update_choice = input("Enter your choice: ")

    if update_choice == '1':
        old_country = input("Enter existing Country name: ")
        if old_country not in main_dict:
            print("Country not found.")
            return
        new_country = input("Enter new name for the country: ")
        main_dict[new_country] = main_dict.pop(old_country)
        print("Country name updated successfully.")

    elif update_choice == '2':
        country = input("Enter Country name: ")
        if country not in main_dict:
            print("Country not found.")
            return
        old_state = input("Enter existing State name: ")
        if old_state not in main_dict[country]:
            print("State not found.")
            return
        new_state = input("Enter new name for the state: ")
        main_dict[country][new_state] = main_dict[country].pop(old_state)
        print("State name updated successfully.")

    elif update_choice == '3':
        country = input("Enter Country name: ")
        if country not in main_dict:
            print("Country not found.")
            return
        state = input("Enter State name: ")
        if state not in main_dict[country]:
            print("State not found.")
            return
        old_city = input("Enter existing City name: ")
        if old_city not in main_dict[country][state]:
            print("City not found.")
            return
        new_city = input("Enter new name for the city: ")
        idx = main_dict[country][state].index(old_city)
        main_dict[country][state][idx] = new_city
        print("City name updated successfully.")

    elif update_choice == '4':
        country = input("Enter Country name: ")
        if country not in main_dict:
            print("Country not found.")
            return
        state = input("Enter State name: ")
        if state not in main_dict[country]:
            print("State not found.")
            return
        city = input("Enter City to add: ")
        if city not in main_dict[country][state]:
            main_dict[country][state].append(city)
            print("City added successfully.")
        else:
            print("City already exists in the state.")

    elif update_choice == '5':
        country = input("Enter Country name to add new state: ")
        if country not in main_dict:
            print("Country not found.")
            return
        new_state = input("Enter new state name: ")
        if new_state not in main_dict[country]:
            main_dict[country][new_state] = []
            print("State added successfully.")
        else:
            print("State already exists in the country.")

    else:
        print("Invalid choice.")

def delete_data():
    print("Delete Menu:")
    print("1. Delete Country\n2. Delete State \n3. Delete City \n4. Exit")
    del_choice = input("Enter your choice: ")

    if del_choice == '1':
        country = input("Enter Country to delete: ")
        if country in main_dict:
            del main_dict[country]
            print("Country delted!!")
        else:
            print("Country not found.")
    elif del_choice == '2':
        country = input("Enter Country: ")
        if country in main_dict:
            state = input("Enter State to Delete: ")
            if state in main_dict[country]:
                del main_dict[country][state]
                print("State deleted!!")
            else:
                print("State not found in the country.")
    elif del_choice == '3':
        country = input("Enter Country: ")
        if country in main_dict:
            state = input("Enter State: ")
            if state in main_dict[country]:
                city = input("Enter City to Delete: ")
                if city in main_dict[country][state]:
                    main_dict[country][state].remove(city)
                    print("City deleted!! :(")
                else:
                    print("City not found in the state.")
            else:
                print("State not found in the country.")
        else:
            print("Country not found.")

    elif del_choice == '4':
        print("Exiting...")
        return
    else:
        print("Invalid choice.")

def display_data():
    print("--- Your Data ---")
    if not main_dict:
        print("No data available.")
    else:
        for country, states in main_dict.items():
            print("Country: ", country)
            for state, cities in states.items():
                print(" State: ", state)
                if cities:
                    print(" cities: ", cities)
                else:
                    print(" No cities added. ")

while True:
    print(" Menu ")
    print("1. Insert\n2. Update\n3. Delete\n4. Display\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        insert_data()
    elif choice == '2':
        update_data()
    elif choice == '3':
        delete_data()
    elif choice == '4':
        display_data()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid Choice Insertion. Please enter between 1-5.")