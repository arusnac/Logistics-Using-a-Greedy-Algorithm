import csv

import algorithm
import hashtable
import nodes

from datetime import datetime, timedelta, time

import testalgo


class Truck:
    def __init__(self):
        self.miles = None
        self.packages = []
        self.route = []
        start_time = None
        end_time = None
        current_time = None

    def add_pkg(self, pkg):
        self.packages.append(pkg)

    def set_packages(self, packages):
        self.packages = packages

    def get_packages(self):
        return self.packages

    def remove(self, pkg):
        self.packages.remove(pkg)
        self.route.append(pkg[1])

    def set_miles(self, miles):
        self.miles = miles

    def get_miles(self):
        return self.miles


truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()


def prep_trucks():
    truck2pkg = []
    truck1pkg = []
    truck3pkg = []

    hashtable.HashTable
    hash = hashtable.HashTable()

    file = open('packages.csv')
    csvreader = csv.reader(file)

    next(csvreader, None)
    rows = []

    for row in csvreader:
        hash.insert(row[0], row)
    all_packages = []

    i = 1
    while i < 41:
        index = str(i)
        package = hash.get_by_key(index)
        all_packages.append(package)
        i += 1

    for pkg in all_packages:
        if pkg[7] == "Can only be on truck 2":
            truck2pkg.append(pkg)
            all_packages.remove(pkg)

    for pkg in all_packages:
        if pkg[7] == "Delayed on flight---will not arrive to depot until 9:05 am":
            truck2pkg.append(pkg)
            all_packages.remove(pkg)
    # print(all_packages)
    for pkg in all_packages:
        if pkg[0] == "13" or pkg[0] == "14" or pkg[0] == "15" or pkg[0] == "16" or pkg[0] == "19" or pkg[0] == "20":
            truck1pkg.append(pkg)
            # all_packages.remove(pkg)

    for pkg in all_packages:
        if pkg[5] == "10:30 AM" and pkg[0] != "13" and pkg[0] != "14" and pkg[0] != "15" and pkg[0] != "16" and pkg[
            0] != "19" and pkg[0] != "20":
            truck1pkg.append(pkg)

    for pkg in truck1pkg:
        all_packages.remove(pkg)

    for pkg in all_packages:
        if pkg[7] == "Wrong address listed":
            truck2pkg.append(pkg)
            all_packages.remove(pkg)

    i = 0
    while i < 7:
        truck2pkg.append(all_packages[i])
        all_packages.remove(all_packages[i])
        i += 1

    n = 0
    while n < 3:
        truck1pkg.append(all_packages[n])
        all_packages.remove(all_packages[n])
        n += 1

    truck3pkg = all_packages

    truck_1.set_packages(truck1pkg)
    truck_2.set_packages(truck2pkg)
    truck_3.set_packages(truck3pkg)

    #formatted = format(truck_2.get_packages())
    #dist, returned_route = nodes.load_graph(to_sort=formatted)
    #truck_2.set_miles(dist)

    #calculate_time(returned_route)

    formatted = format(truck_1.get_packages())
    dist, returned_route = nodes.load_graph(to_sort=formatted)
    truck_1.set_miles(dist)
    #print(formatted)
    calculate_time(returned_route, dist)
    #testalgo.greedy()
    #formatted = format(truck_3.get_packages())
    #dist = nodes.load_graph(to_sort=formatted)
    #truck_3.set_miles(dist)

    total_miles = 0
    #total_miles = truck_1.get_miles() + truck_2.get_miles() + truck_3.get_miles()
    #print(total_miles)
    """
    print(format_for_graph)
    #all_packages.remove('13')
    print(all_packages)
    print(len(all_packages))
    print(len(truck1pkg))
    print(len(truck2pkg))
    print(len(truck3pkg))
    print(truck1pkg)
    print(truck2pkg)
    print(truck3pkg)
    #hash.print_items()
    formatted_add = []
    """
    """
    i = 0
    for i in hash:
        index = str(i)
        address = hash.get(index)
        address = address[1] + " (" + address[4] + ")"
        formatted_add.append(address)
        i += 1
    """

def calculate_time(returned_route, distances):
    truck2_start = timedelta(hours = 8, minutes=0)

    print(truck2_start)


    current_time = truck2_start

    delivered = []
    i=0
    while i < len(distances):
        minutes_to_add = ((distances[i])/18)*60
        time_add = timedelta(minutes=minutes_to_add)
        current_time += time_add
        print(current_time)
        i+=1


def format(packages):
    format_for_graph = []
    i = 0
    while i <len(packages):
        index = str(i)
        address = packages[i][1] + " (" + packages[i][4] + ")"
        format_for_graph.append(address)
        i += 1

    return format_for_graph
