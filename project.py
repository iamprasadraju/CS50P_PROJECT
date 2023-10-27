from tabulate import tabulate
import pyfiglet
import sys
import csv

# ANSI escape codes for colors


class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAZANTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'


font = pyfiglet.figlet_format("Password Manager", font="small")
print(font)
print("                                 Created by " +
      colors.RED + "Prasad Raju ❤️❤️❤️"+colors.END)
print()


def main():
    while True:
        print("list of commands:")
        print(" ")
        print(colors.YELLOW + "         V   -- view all list of passwords" + colors.END)
        print(colors.YELLOW + "         C   -- create a New password" + colors.END)
        print(colors.YELLOW + "         D   -- Delete a password" + colors.END)
        print(colors.YELLOW + "         U   -- Update the password" + colors.END)
        print(colors.YELLOW + "         E   -- Exit the Program" + colors.END)

        print("\n")
        print()
        command = input(colors.BLUE + "Enter Command: " + colors.END).upper()

        if command == "V":
            view()
        elif command == "C":
            create()
        elif command == "D":
            delete()
        elif command == "U":
            update()
        elif command == "E":
            quit_program()
        else:
            print("\n")
            print(colors.RED + "Invalid command, Try again !\n" + colors.END)


def view():
    with open("data.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        table = tabulate(reader, headers="firstrow", tablefmt="rounded_grid")
        print(table)
        print()


def create():
    website_name = input("Enter Website name or Application name: ")
    username = input("Enter Username: ")
    password = input("Enter your Password: ")
    confirm_password = input("Confirm Your Password: ")
    if password == confirm_password:
        add_data("data.csv", website_name, username, password)
        print(colors.GREEN + "Data added successfully." + colors.END)
        print()
    else:
        print(colors.RED + "Password does not match !!!. Try again !" + colors.END)


def delete():
    website_name = input(
        colors.RED + "Enter your Application name that you want to delete: " + colors.END)
    msg = input(colors.CYAN + "Are you Sure? [y/n] " + colors.CYAN).lower()
    if msg == "y" or msg == "yes":
        delete_data("data.csv", website_name)
    else:
        print(colors.GREEN + "Deletion has been Cancelled" + colors.END)


def quit_program():
    msg = input(colors.GREEN + "are you sure? [y/n] " + colors.END).lower()
    if msg == "y" or msg == "yes":
        sys.exit()
    else:
        main()


def update():
    website_name = input(
        colors.MAZANTA + "Enter the application name that you want to update: " + colors.MAZANTA)
    msg = input(colors.CYAN + "Are you Sure? [y/n] " + colors.CYAN).lower()
    if msg == "y" or msg == "yes":
        update_data("data.csv", website_name)
    else:
        print(colors.MAZANTA + "Update canceled." + colors.END)


def add_data(filename, website_name, username, password):
    with open(filename, 'a', newline='') as f:
        fieldnames = ['Website Name', 'Username', 'Password']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        f.seek(0, 2)
        if f.tell() == 0:
            writer.writeheader()

        writer.writerow({'Website Name': website_name,
                        'Username': username, 'Password': password})


def delete_data(filename, website_name):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    new_rows = []

    for row in rows:
        if row[0] != website_name:
            new_rows.append(row)

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)

        if len(new_rows) != len(rows):
            print(
                colors.GREEN + f"The data of {website_name} has been deleted Successfully." + colors.END)
            print()
        else:
            print("No data found with " + colors.MAZANTA +
                  f" {website_name}." + colors.END)
            print()


def update_data(filename, website_name):
    new_list = []
    match_found = False

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    for row in data:
        if row[0] == website_name:
            new_value = input(
                colors.BLUE + "Enter Updated Password: " + colors.BLUE)
            row[2] = new_value
            match_found = True
        new_list.append(row)

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_list)

    if match_found:
        print(colors.GREEN +
              f"The data of {website_name} has been updated Successfully." + colors.END)
        print()
    else:
        print("No data found with " + colors.MAZANTA +
              f"{website_name}." + colors.END)


if __name__ == "__main__":
    main()
