# CRUD with CSV and JSON Files

This project allows you to perform CRUD operations (Create, Read, Update, Delete) on records stored in CSV and JSON files using Python dictionaries.

## Structure
- main.py: Main file to run the CRUD application.
- crud.py: Contains the CRUD logic.
- data/: Folder used to store data files (data.csv, data.json).

## Requirements
- Python 3.x

## Usage
Run the following command to start the program:

```bash
python main.py

Follow the on-screen instructions to manage the records.

---

## Explanation of Important Concepts

### os.path.join(folder, file)
This is used to combine a folder name and a file name so the computer knows exactly where the file is located. It’s like saying: “Find the notebook inside the box.”

### os.path.exists(path)
This asks: “Does this folder or file already exist?”  
If it exists → returns True  
If it does not exist → returns False  

### os.makedirs(path)
This tells the computer: “Create a folder with this name.”  
If it already exists, nothing happens. If it does not exist, it creates it so you can store files.

### with open(JSON_FILE, "r", encoding="utf-8") as file:
This is like opening a notebook to read it.  
- `"r"` means read mode  
- `"utf-8"` is used to properly read special characters  
When finished, the file is automatically closed.

### json.dump(records, file, ensure_ascii=False, indent=4)
This writes multiple records into a JSON file.  
- `ensure_ascii=False` allows special characters  
- `indent=4` makes the file organized and easy to read  

### writer = csv.DictWriter(file, fieldnames=record.keys())
This creates a special writer for CSV files. Imagine writing rows into a spreadsheet:
- `file` is the file you are writing into  
- `fieldnames=record.keys()` defines the columns (e.g., name, age, id)  

Each dictionary becomes a row.

### Difference between csv.DictWriter and json.dump
- **csv.DictWriter** writes data as rows and columns in a table. Each record is a row, and each field (name, age, etc.) is a column. It is ideal for simple data.
- **json.dump** writes data as a list of dictionaries. Each record can contain nested structures (lists or other dictionaries). It is more flexible and suitable for complex data.

### Visual Example:
- **CSV:**
  | id  | name | age |
  |-----|------|-----|
  | juan| Juan | 10  |
  | ana | Ana  | 12  |

- **JSON:**
  [
    {"id": "juan", "name": "Juan", "age": "10"},
    {"id": "ana", "name": "Ana", "age": "12"}
  ]

In summary: use CSV for table-like data (like Excel), and use JSON for more flexible and complex data structures.

---

This way, anyone who reads your code will understand what each important part does!