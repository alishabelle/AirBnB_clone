# 0x00. AirBnB clone - The console

## Description

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

## Usage
### To start console
```
./console
```
### How to create a BaseModel Object
```
(hbnb) create BaseModel
```
### How to display a list of string representation of all objects
```
(hbnb) all
or
(hbnb) all BaseModel
```
### How to display str representation of a specific BaseModel object
```
(hbnb) show BaseModel [object id]
```
### How to delete an object
```
(hbnb) destroy BaseModel [object id]
```

### [1. Be PEP8 compliant!](./tests/)
* Write beautiful code that passes the PEP8 checks.


### [2. Unittests](./models/base_model.py)
* All your files, classes, functions must be tested with unit tests


### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes:


### [4. Create BaseModel from dictionary](./models/engine/file_storage.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()).


### [5. Store first object](./console.py)
* Now we can recreate a BaseModel from another one by using a dictionary representation:


### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter:


### [7. Console 0.1](./models/user.py)
* Update your command interpreter (console.py) to have these commands:


### [8. First User](./models/state.py)
* Write a class User that inherits from BaseModel:


### [9. More classes!](./console.py)
* Write all those classes that inherit from BaseModel:


---

## Author
* **HausCloud** - [HausCloud](https://github.com/HausCloud)
* **alishabelle** - [alishabelle](https://github.com/alishabelle)
