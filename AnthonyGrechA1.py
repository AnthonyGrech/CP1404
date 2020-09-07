"""
Name: Anthony Grech
Date started: 01/08/2020
GitHub URL: https://github.com/AnthonyGrech/CP1404.git
"""

import csv

f = open("places.csv", "r")
travel_passport = csv.reader(f)
cities = []
counties = []
priority = []
plan_too = []
have_been = []
n_or_v = []

for row in travel_passport:
    cities.append(row[0])
    counties.append(row[1])
    priority.append(row[2])
    n_or_v.append(row[3])
    if row[3] == "n":
        plan_too.append(row[0])
    if row[3] == "v":
        have_been.append(row[0])


print(cities)
print(counties)
print(priority)
print(plan_too)
print(have_been)
print("Travel Tracker 1.0 - by Anthony Grech")
print(len(cities), "places loaded from places.csv")


def main_menu():
    """main menu controlling decision making"""
    choice = input("""
                          L - List Places
                          A - Add new place
                          M - Mark place as visited
                          Q - Quit

                          choice: """)
    print()
    if choice == "L" or choice == "l":
        list_places()

    elif choice == "A" or choice == "a":
        add_new_place()
    elif choice == "M" or choice == "m":
        mark_as_visited()
    elif choice == "Q" or choice == "q":
        f.close()
        q = open("places.csv", "w")
        q.truncate()
        writer = csv.writer(q)
        writer.writerows(cities)
        writer.writerows(counties)
        writer.writerows(priority)
        print(len(cities), "places saved to csv")
        print("Have a nice day")
        f.close()
    else:
        print("Invalid menu choice")
    main_menu()


def list_places(rows_counter=1):
    """Function for listing cities and countries with coresponding priorities"""
    for rows in travel_passport:
        if rows[3] == "n":
            visited_key = "*"
            rows_counter += 1
            print(visited_key, rows_counter, ".", rows[0], "in", rows[1], "priority", rows[2])
        if rows[3] == "v":
            print(rows_counter, ".", rows[0], "in", rows[1], "priority", rows[2])
    print(len(cities), "places.", "you still want to visit", len(plan_too), "places")
    main_menu()


def add_new_place():
    """Function for adding a new city"""
    new_city = input("Name:")
    if new_city == "":
        print("Input cannot be blank")
        add_new_place()
    cities.append(new_city)
    plan_too.append(new_city)
    new_country = input("Country:")
    if new_country == "":
        print("Input cannot be blank")
        add_new_place()
    counties.append(new_country)
    new_priority = input("Priority:")
    if new_priority < "0":
        print("Invalid input; please enter a valid number")
        new_priority = input("Priority:")
    priority.append(new_priority)
    print(cities[-1], "in", counties[-1], "added to Travel Tracker")
    main_menu()


def mark_as_visited():
    """Function for marking city as visited"""
    for rows2 in travel_passport:
        if rows2[3] == "n":
            print(rows2[0], "in", rows2[1], "priority", rows2[2])
        if rows2[3] == "v":
            print(rows2[0], "in", rows2[1], "priority", rows2[2])
    print(len(cities), "places.", "you still want to visit", len(plan_too), "places")
    visited = input(float("Enter the number of a place you would like to mark visited"))
    if visited < "0":
        print("Invalid input; please enter a valid number")
        visited = input(float("Enter the number of a place you would like to mark visited"))
        n_or_v[visited].append("v")
    print(cities[visited], "in", counties[visited], "marked as visited")
    main_menu()


main_menu()

# How long did the entire assignment 1 project take you?
# 5 Days

# What do you plan to do differently in your development process for assignment 2?
# Work longer on task to complete csv aspect