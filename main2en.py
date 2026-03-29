from crud2en import *


def show_menu():
    """
    Displays the main menu.
    """
    print("\n--- File CRUD (CSV / JSON) ---")
    print("1. Create record")
    print("2. Read records")
    print("3. Update record")
    print("4. Delete record")
    print("5. Exit")


def get_user_data():
    """
    Collects user input and returns it as a dictionary.
    """
    name = input("Enter name: ")
    age = input("Enter age: ")
    role = input("Enter role: ")

    return {
        "id": name.lower(),
        "name": name,
        "age": age,
        "role": {"id": 1, "name": role},
    }


def get_file_type(message):
    """
    Asks the user to choose between CSV or JSON.
    """
    print(message)
    print("1. CSV")
    print("2. JSON")
    return input("Select an option: ")


if __name__ == "__main__":
    option = ""

    while option != "5":
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            data = get_user_data()
            file_type = get_file_type("Where do you want to save the record?")

            if file_type == "1":
                create_csv_record(data)
                print("Record saved in CSV.")
            elif file_type == "2":
                create_json_record(data)
                print("Record saved in JSON.")
            else:
                print("Invalid file type.")

        elif option == "2":
            file_type = get_file_type("Where do you want to read records from?")

            if file_type == "1":
                records = read_csv_records()
            elif file_type == "2":
                records = read_json_records()
            else:
                print("Invalid file type.")
                records = []

            print("\n--- Records found ---")
            if len(records) == 0:
                print("No records found.")
            else:
                for record in records:
                    print(record)

        elif option == "3":
            id_value = input("Enter the ID of the record to update: ")
            new_data = get_user_data()
            file_type = get_file_type("Which file do you want to update?")

            if file_type == "1":
                updated = update_csv_record(id_value, "id", new_data)
            elif file_type == "2":
                updated = update_json_record(id_value, "id", new_data)
            else:
                updated = False
                print("Invalid file type.")

            if updated:
                print("Record updated successfully.")
            else:
                print("Record not found.")

        elif option == "4":
            id_value = input("Enter the ID of the record to delete: ")
            file_type = get_file_type("Which file do you want to delete from?")

            if file_type == "1":
                deleted = delete_csv_record(id_value, "id")
            elif file_type == "2":
                deleted = delete_json_record(id_value, "id")
            else:
                deleted = False
                print("Invalid file type.")

            if deleted:
                print("Record deleted successfully.")
            else:
                print("Record not found.")

        elif option == "5":
            print("Goodbye!")

        else:
            print("Invalid option. Try again.")
