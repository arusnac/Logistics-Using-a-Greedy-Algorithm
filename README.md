# Logistics-Using-a-Greedy-Algorithm

This is a simple application that takes a CSV of addresses and the distances between each address.

The algorithm takes a group of packages and sorts them to create the shortest path. This is done using a weighted graph I made from scratch.
I chose a greedy algorithm to accomplish this due to the fact it was simple to implement and was sufficiently efficient. It was able to accomplish
the goals of the project (meeting package delivery times) with plenty of time to spare.

It has a simple interface to show that each route/group of packages is delivered according to its specifications which is located in another CSV file.

**What I would do differently**

In this application I distributed the packages to the 3 delivery trucks manually. Next time I would attempt to find an automated way to do this. As the manual
load is not the most efficient and doesn't allow for a different set of packages with different specifications.
