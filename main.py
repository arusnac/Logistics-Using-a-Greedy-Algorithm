import datetime
import truck

truck.prep_trucks(7, 0, 0, 18, 50, 0)

user_input = 0
lookup = 0
i = 1

user_input = input(
    "(1) Look up package by id (2) Look up package by time (3) Look at packages by interval (4) Get total mileage (0) to exit ")

"""Search by package ID"""
if user_input == '1':

    while lookup != '0':
        lookup = input("Enter package ID: (0 to exit)")
        print(truck.package_table.get_by_key(lookup))

"""Check all packages by time"""
if user_input == '2':
    input_time_hours = int(input('\nEnter any time after 8:00 am in military time Hours = : \n'))
    input_time_minutes = int(input('\nMinutes: \n'))

    compare_time = datetime.timedelta(hours=10, minutes=20)
    compare_time_input = datetime.timedelta(hours=input_time_hours, minutes=input_time_minutes)

    if compare_time_input > compare_time:
        update_input = input("\nAddress must be updated for package ID: 9. Update now? (1)\n")
        if update_input == '1':
            truck.truck_3.route.remove('300 State St (84103)')
            truck.truck_3.route.append('410 S State St (84111)')
            truck.fix_address('9')
            truck.truck_3.set_flag(True)

    packages4 = []
    truck.prep_trucks(8, 0, 0, input_time_hours, input_time_minutes, 0)
    print(truck.truck_3.route)
    i = 1
    while i < 41:
        index = str(i)
        packages4.append(truck.package_table.get_by_key(index))
        i += 1
    print(truck.truck_3.route)
    print(*packages4, sep='\n')


"""Check packages in intervals of time"""
if user_input == '3':
    print("\n*********Interval 8:35 am - 9:25 am********* \n")
    packages = []
    truck.prep_trucks(8, 35, 0, 9, 25, 0)
    while i < 41:
        index = str(i)
        packages.append(truck.package_table.get_by_key(index))
        i += 1
    print(*packages, sep='\n')

    update_input = input("\nAddress must be updated for package ID: 9. Update now? (1)\n")
    if update_input == '1':
        truck.truck_3.remove('300 State St (84103)')
        truck.truck_3.route.append('410 S State St (84111)')
        truck.fix_address('9')
        truck.truck_3.set_flag(True)

    next_input = input("\nProceed to next interval? (1)\n")

    if next_input == '1':

        print("\n*********Interval 9:35 am - 10:25 am********* \n")
        packages2 = []
        truck.prep_trucks(9, 35, 0, 10, 25, 0)
        i = 1
        while i < 41:
            index = str(i)
            packages2.append(truck.package_table.get_by_key(index))
            i += 1
        print(*packages2, sep='\n')

        print("\n*********Interval 12:03 pm - 13:12 pm********* \n")
        packages3 = []
        truck.prep_trucks(12, 3, 0, 13, 12, 0)
        i = 1
        while i < 41:
            index = str(i)
            packages3.append(truck.package_table.get_by_key(index))
            i += 1
        print(*packages3, sep='\n')

if user_input == '4':
    print(truck.get_total_mileage(truck.truck_1.get_miles(), truck.truck_2.get_miles(), truck.truck_3.get_miles()))

