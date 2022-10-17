
# AirBnB clone - The console





## Description
The AirBnB clone - The console project is a team project realised during the first year at Holberton School. It's the first projectof the serie of project whose purpose is to create our own version of the AirBnB website on both front and back end.


## Learning Objectives
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Console commands
| Commands | Usage | Description |
| --- | --- | --- |
| `create` | `create <class_name>` | Create a new instance of a specified class and show its ID|
| `all` | `all <class_name>` | Display the info of all instance (or all of the same class) |
| `show` | `show <class_name> <id>` | Display the info of an instance with its ID|
| `count` | `<class_name>.count()` | Count the number of instance of a class |
| `update` | ` update <class_name> <id> <attribute_name> <attribute_value>` | Update (or create) one attribute of an instance with its ID|
| `update` | ` <class_name>.update("<id>", {"<attribute_name>": <attribute_value>})` | Update (or create) multiple attributes (with a dict) of an instance with its ID|
| `destroy` | `destroy <class_name> <id>` | Destroy an instance with its ID |
| `help` | `help <function_name>` | Display info of one or all functions |

## Usage
```
$ ./console.py
(hbnb) help show
Show string representation of an instance
(hbnb) show BaseModel a5106cf2-5da2-4542-9938-2e5ad23747de
[BaseModel] (a5106cf2-5da2-4542-9938-2e5ad23747de) {'id': 'a5106cf2-5da2-4542-9938-2e5ad23747de', 'created_at': datetime.datetime(2022, 7, 1, 13, 14, 2, 760448), 'updated_at': datetime.datetime(2022, 7, 1, 13, 14, 2, 760454)}
(hbnb) BaseModel.destroy("338edc32-ce7a-4631-a76d-f6a837a5c713")
(hbnb) BaseModel.count()
0
(hbnb) quit
$
```
## Different classes
* BaseModel
* User
* State
* City
* Place
* Amenity
* Review
## Authors


- Santiago Alves - https://github.com/santialvesz
