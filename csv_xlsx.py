import csv

def Create():
    """
    Data variable : In this function to only create data and store in Data Variable
    Country_want, State_Want, City_want: This three variable to use of Country, State, City to want you add or not
    Country_Name, State_Name, City_Name: This Three variable use of new add value in dictionary 

    Description : Create Function to use of create new data. if their data already exist to show msg.
    """
    global Data
    while True:
        Country_Want = input("enter you want country or not, write y/n = ")
        if Country_Want == 'n':
            if not Data:pass
            else:
                print("you created Data: ")
            return
        elif Country_Want != 'y':
            print("Unknown Option")
            continue
        else:
             Country_Name = str(input("enter country name: "))
             if Country_Name in Data:
                 print("This name already added please try delete or new country")
                 continue
             Data[Country_Name] = {}
             while True:
                 State_Want = input(f"Enter you want add state in {Country_Name} country or not, write y/n = ")
                 if State_Want == 'n':
                     break
                 elif State_Want != 'y':
                     print("Unknown Option")
                     continue
                 else:
                     State_Name = str(input("Enter State name: "))
                     if State_Name in Data[Country_Name]:
                         print(f"This name already added in {Country_Name} please try delete or update state ")
                         continue
                     Data[Country_Name][State_Name] = []
                     while True:
                         city_want = input(f"enter you want to add city {Country_Name} in {State_Name} city or not, write y/n = ")
                         if city_want == 'n':
                             break
                         elif city_want != 'y':
                             print("Unknown Option")
                             continue
                         else:
                             city_name = str(input("Enter City name: "))
                             if city_name in Data[Country_Name][State_Name]:
                                 print(f"This name already added in {Country_Name} in {State_Name}please try delete or new city")
                                 continue
                             Data[Country_Name][State_Name].append(city_name)
csv_import_data = []
def dict_2_list(Dictionary):
    """
        Data variable : In this function to only create data and store in Data Variable
        state, city: This two variable to use of State and City is first or not
        Country, States, Cities: This Three variable use of dictionary open and get this value and append in list

        Description : Dict_2_list this function work to Dictionary to convert list.
        """
    if not Dictionary:
        print("Not any Data")
        return
    for Country in Dictionary:
        if Dictionary[Country] == {}:
            one_data = [Country,"",""]
            csv_import_data.append(one_data)
            one_data = []
            continue
        else:
            city, state = 1, 1
            for states in Dictionary[Country]:
                if state == 1:
                    one_data = [Country,states]
                    state+=1
                else:
                    one_data = ["",states]
                if not Dictionary[Country][states]:
                    one_data.append("")
                    csv_import_data.append(one_data)
                    one_data = []
                else:
                    for cities in Dictionary[Country][states]:
                        if city ==1:
                            one_data.append(cities)
                            city +=1
                            csv_import_data.append(one_data)
                            one_data = []
                        else:
                            one_data = ["","",cities]
                            csv_import_data.append(one_data)
                            one_data = []
                    city=1

Data = {}
# Ask choise for what you data create or exist data work
while True:
    choice_cre_exi = input("\nInbuild data to make csv = inbuild\nNew build data to make csv = new\nwhat you want:")
    match choice_cre_exi:
        case "inbuild":
            dict_2_list({'india':{"Guj":['Ahmedabad',"Gandhinagar"],'Raj':["Udaipur","Jodhpur"]},'Pak':{"Guj":['Ahmedabad',"Gandhinagar"],'Raj':["Udaipur","Jodhpur"]}})
            break
        case "new":
            Create()
            dict_2_list(Data)
            break
        case _:
            print("please write existing type")
# This portion is open csv write a list data
with open("output.csv",'a', newline='') as file:
    writer = csv.writer(file)
    for data in csv_import_data:
        writer.writerow(data)
print(csv_import_data)
