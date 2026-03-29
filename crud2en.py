import csv  # Used to handle CSV files (similar to Excel tables)
import json  # Used to handle JSON files (structured text data)
import os  # Used to manage directories and file paths

# Define where data files will be stored
DATA_FOLDER = "data"
CSV_FILE = os.path.join(DATA_FOLDER, "data.csv")
JSON_FILE = os.path.join(DATA_FOLDER, "data.json")


def create_folder_if_not_exists():
    """
    Ensures that the data folder exists.
    If it does not exist, it will be created.
    """
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


# ========== JSON SECTION ==========


def read_json_records():
    """
    Reads all records from the JSON file.
    Returns an empty list if the file does not exist.
    """
    if not os.path.exists(JSON_FILE):
        return []

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json_records(records):
    """
    Saves all records into the JSON file.
    """
    create_folder_if_not_exists()

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=4)


def create_json_record(record):
    """
    Adds a new record to the JSON file.
    """
    records = read_json_records()
    records.append(record)
    save_json_records(records)


def update_json_record(id_value, id_field, new_data):
    """
    Updates a record in the JSON file based on an ID.
    """
    records = read_json_records()

    for record in records:
        if record.get(id_field) == id_value:
            record.update(new_data)
            save_json_records(records)
            return True

    return False


def delete_json_record(id_value, id_field):
    """
    Deletes a record from the JSON file based on an ID.
    """
    records = read_json_records()
    new_records = []
    deleted = False

    for record in records:
        if record.get(id_field) == id_value:
            deleted = True
        else:
            new_records.append(record)

    if deleted:
        save_json_records(new_records)

    return deleted


# ========== CSV SECTION ==========


def read_csv_records():
    """
    Reads all records from the CSV file.
    Returns an empty list if the file does not exist.
    """
    if not os.path.exists(CSV_FILE):
        return []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def create_csv_record(record):
    """
    Adds a new record (row) to the CSV file.
    """
    create_folder_if_not_exists()
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=record.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(record)


def update_csv_record(id_value, id_field, new_data):
    """
    Updates a record in the CSV file based on an ID.
    """
    records = read_csv_records()

    if len(records) == 0:
        return False

    updated = False

    for record in records:
        if record.get(id_field) == id_value:
            record.update(new_data)
            updated = True
            break

    if updated:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)

    return updated


def delete_csv_record(id_value, id_field):
    """
    Deletes a record from the CSV file based on an ID.
    """
    records = read_csv_records()

    if len(records) == 0:
        return False

    new_records = []
    deleted = False

    for record in records:
        if record.get(id_field) == id_value:
            deleted = True
        else:
            new_records.append(record)

    if deleted:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(new_records)

    return deleted
