import csv
import hashtable
import nodes
from datetime import datetime, timedelta, time


class Truck:
    def __init__(self):
        self.miles = None
        self.packages = []
        self.route = []
        self.start_time = None
        self.end_time = None
        self.current_time = None
        self.id = 0
        self.flag = None

    def set_route(self, route):
        self.route = route;

    def get_route(self):
        return self.route

    def remove(self, package):
        self.route.remove(package)

    def get_total_mileage(self):
        return self.total

    def set_start(self, time):
        self.start_time = time

    def get_start(self):
        return self.start_time

    def set_current(self, time):
        self.current_time = time

    def get_current(self):
        return self.current_time

    def set_end(self, time):
        self.end_time = time

    def get_end(self):
        return self.end_time

    def add_pkg(self, pkg):
        self.packages.append(pkg)

    def set_packages(self, packages):
        self.packages = packages

    def get_packages(self):
        return self.packages

    def remove_package(self, pkg):
        self.packages.remove(pkg)
        self.route.append(pkg[1])

    def set_miles(self, miles):
        self.miles = miles

    def get_miles(self):
        return self.miles

    # Flag for when packed #9 needs to be updated
    def set_flag(self, flag):
        self.flag = flag


truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()
package_table = hashtable.HashTable()


def prep_trucks(sh, sm, ss, eh, em, es):
    truck2pkg = []
    truck1pkg = []
    truck3pkg = []

    restrict_start = timedelta(hours=sh, minutes=sm, seconds=ss)
    restrict_end = timedelta(hours=eh, minutes=em, seconds=es)

    # Open and read the package data
    file = open('packages.csv')
    csvreader = csv.reader(file)

    next(csvreader, None)

    update_packages = []
    for row in csvreader:
        update_packages.append(row)

    # Add additional space for a status for packages
    for i in update_packages:
        i.append('')

    all_packages = []

    # Insert packages into the hashtable
    for i in update_packages:
        package_table.insert(i[0], i)

    # Get a list of all packages so they can be sorted onto the trucks
    i = 1
    while i < 41:
        index = str(i)
        package = package_table.get_by_key(index)
        all_packages.append(package)
        i += 1

    if truck_3.flag:
        fix_address('9')

    ref_packages = []
    i = 1
    # Use for reference for keys in package_table
    while i < 41:
        index = str(i)
        package = package_table.get_by_key(index)
        ref_packages.append(package)
        i += 1

    # Sort all packages into specified trucks
    for pkg in all_packages:
        if pkg[7] == "Can only be on truck 2":
            truck2pkg.append(pkg)
            all_packages.remove(pkg)

    for pkg in all_packages:
        if pkg[7] == "Delayed on flight---will not arrive to depot until 9:05 am":
            truck2pkg.append(pkg)
            all_packages.remove(pkg)

    for pkg in all_packages:
        if pkg[0] == "13" or pkg[0] == "14" or pkg[0] == "15" or pkg[0] == "16" or pkg[0] == "19" or pkg[0] == "20":
            truck1pkg.append(pkg)

    for pkg in all_packages:
        if pkg[5] == "10:30 AM" and pkg[0] != "13" and pkg[0] != "14" and pkg[0] != "15" and pkg[0] != "16" and pkg[
            0] != "19" and pkg[0] != "20":
            truck1pkg.append(pkg)

    for pkg in truck1pkg:
        all_packages.remove(pkg)

    for pkg in all_packages:
        if pkg[7] == "Wrong address listed":
            truck3pkg.append(pkg)
            all_packages.remove(pkg)

    i = 0
    # Allocate according to space left on each truck
    while i < 8:
        truck2pkg.append(all_packages[i])
        all_packages.remove(all_packages[i])
        i += 1

    n = 0
    while n < 3:
        truck1pkg.append(all_packages[n])
        all_packages.remove(all_packages[n])
        n += 1

    for p in all_packages:
        truck3pkg.append(p)

    # Set packages to instance of each truck, run through greedy algorithm to get the route
    # Run through the function to calculate time. Set mileage, start time, end time, current time to all instances
    # of truck
    truck_1.set_packages(truck1pkg)
    truck_2.set_packages(truck2pkg)
    truck_3.set_packages(truck3pkg)

    truck_2.set_start(timedelta(hours=9, minutes=5))
    truck_1.set_start(timedelta(hours=8, minutes=0))

    # Restrict updates to packages to fall in with the time passed in
    if restrict_end < truck_1.get_start():
        for p in ref_packages:
            if p[7] != "Delayed on flight---will not arrive to depot until 9:05 am":
                package_table.update_status(p[0], 'At Hub', str(restrict_end))
    if truck_1.get_start() < restrict_end < truck_2.get_start():
        for p in truck_2.get_packages():
            if p[7] != "Delayed on flight---will not arrive to depot until 9:05 am" and p[7] != 'Wrong address listed':
                package_table.update_status(p[0], 'At Hub', str(restrict_end))
        for p in truck_3.get_packages():
            if p[7] != "Delayed on flight---will not arrive to depot until 9:05 am" and p[7] != 'Wrong address listed':
                package_table.update_status(p[0], 'At Hub', str(restrict_end))
    if truck_3.get_start() != None:
        if truck_2.get_start() < restrict_end < truck_3.get_start():
            for p in truck_3.get_packages():
                if p[7] != 'Wrong address listed':
                    package_table.update_status(p[0], 'At Hub', str(restrict_end))
    if restrict_end > timedelta(hours=10, minutes=20):
        for p in truck_3.get_packages():
            if p[7] == 'Wrong address listed':
                package_table.update_status(p[0], 'At Hub', str(restrict_end))

    format_truck_1 = format(truck_1.get_packages())
    dist, returned_route = nodes.load_graph(to_sort=format_truck_1)

    if restrict_end > truck_1.get_start():
        mileage, end_time = calculate_time(returned_route, dist, truck_1.get_start(), 1, restrict_start, restrict_end)
        truck_1.set_end(end_time)
        truck_1.set_miles(mileage)

    format_truck_2 = format(truck_2.get_packages())
    dist, returned_route = nodes.load_graph(to_sort=format_truck_2)

    if restrict_end > truck_2.get_start():
        mileage, end_time = calculate_time(returned_route, dist, truck_2.get_start(), 2, restrict_start, restrict_end)
        truck_2.set_end(end_time)
        truck_2.set_miles(mileage)

    if truck_2.get_end() is not None:
        format_truck_3 = format(truck_3.get_packages())

    truck_3.set_route(format_truck_3)
    dist, returned_route = nodes.load_graph(to_sort=format_truck_3)
    truck_3.set_miles(dist)
    truck_1.set_start(timedelta(hours=8, minutes=0))
    truck_3.set_start(truck_2.get_end())

    if truck_3.get_start() is not None:
        if restrict_end > truck_3.get_start():
            mileage, end_time = calculate_time(returned_route, dist, truck_3.get_start(), 3, restrict_start,
                                               restrict_end)
            truck_3.set_end(end_time)
            truck_3.set_miles(mileage)


def fix_address(address):
    package_table.update_address(address, '410 S State St', '84111')


# returns total mileage
def get_total_mileage(m1, m2, m3):
    return m1 + m2 + m3


# Takes in the route, start time, distances and truck id. Calculates mileage and time
def calculate_time(returned_route, distances, start_time, truck_id, restricted_start, restricted_end):
    current_time = start_time
    total_mileage = 0
    delivered = []
    time = []
    i = 0
    set_out_for_delivery(truck_id, 'Out for delivery', current_time)
    while i < len(distances):
        minutes_to_add = ((distances[i]) / 18) * 60
        time_add = timedelta(minutes=minutes_to_add)
        current_time += time_add
        if current_time < restricted_end:
            total_mileage += distances[i]
            delivered.append(returned_route[i + 1])
            time.append(str(current_time))
            update_package(returned_route[i + 1], truck_id, str(current_time))
        i += 1

    end_time = current_time

    return total_mileage, end_time


# Update status to be out for delivery
def set_out_for_delivery(truck_id, status, current_time):
    if truck_id == 1:
        for p in truck_1.get_packages():
            package_table.update_status(p[0], 'Out For Delivery', str(current_time))

    if truck_id == 2:
        for p in truck_2.get_packages():
            package_table.update_status(p[0], 'Out For Delivery', str(current_time))

    if truck_id == 3:
        for p in truck_3.get_packages():
            package_table.update_status(p[0], 'Out For Delivery', str(current_time))


# Update status to be delivered
def update_package(package, truck_id, current_time):
    if truck_id == 1:
        for p in truck_1.get_packages():
            if p[1] in package:
                package_table.update_status(p[0], 'Delivered', current_time)

    if truck_id == 2:
        for p in truck_2.get_packages():
            if p[1] in package:
                package_table.update_status(p[0], 'Delivered', current_time)

    if truck_id == 3:
        for p in truck_3.get_packages():
            if p[1] in package:
                package_table.update_status(p[0], 'Delivered', current_time)


# Format the route so that it can be associated with distances from the distance file
def format(packages):
    format_for_graph = []
    i = 0
    while i < len(packages):
        address = packages[i][1] + " (" + packages[i][4] + ")"
        format_for_graph.append(address)
        i += 1

    return format_for_graph
