# AirBnB_clone

This project is aimed towards creating a exact clone of the
AirBnB website, with some of its features. The project is set to
evolve in stages with the first step being: `Write a command 
interpreter to manage your AirBnB objects`.

## Step 1: Write a command interpreter to manage your AirBnB objects
Using ```cmd.Cmd``` This first step covers the following features 
for the command interpreter features:

+ Create a new object (ex: a new User or a new Place)
+ Retrieve an object from a file, a database etc…
+ Do operations on objects (count, compute stats, etc…)
+ Update attributes of an object
+ Destroy an object


## Clone this repository
Clone the repository to your machine with the following:
```$ git clone https://github.com/Uthmanduro/AirBnB_clone.git```


## How to start the AirBnB Command Interpreter
After cloning the repository, the interpreter can be started using:

```
$ ./console.py
```


For a start, the console had no intro screen, so the only visible
changes you will noticed is the change of prompt:

```
(hbnb)
```


## How to use the AirBnB Command Interpreter
Get yourself farmilar with all the basic commands using `help`,
with no additional arguements: the prompt will show a list of
possible commands, each of which is properly documented.

## Examples

### Using `help` command

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all

        all [class]: Prints a list containing string representation
        of all instances in the storage path, optional `[class]` name
        can be passed to print only a list of  matching object with
        the class.

        valid <classes>: ['BaseModel', 'User', 'State', 'City',
                          'Amenity', 'Place', 'Review']
        
(hbnb)  
```


### Using `create` command

```
(hbnb) help create

        create <class>: creates a new instance of <class>, and saves the
        new <class> instance into a JSON file, then prints/return the
        instace id of new <class> instance.

        valid <classes>: ['BaseModel', 'User', 'State', 'City',
                          'Amenity', 'Place', 'Review']
        
(hbnb) create BaseModel
5df9ed71-6987-4677-afab-69aecae4e0ed
(hbnb) 
```


### Using `show` command

```
(hbnb) help show

        show <class> <instance id>: Prints the string representation
        of the instance with matching `instance id`.

        valid <classes>: ['BaseModel', 'User', 'State', 'City',
                          'Amenity', 'Place', 'Review']
        
(hbnb) show BaseModel 8f8a68a6-eee8-42e4-a488-28200576ad32
[BaseModel] (8f8a68a6-eee8-42e4-a488-28200576ad32) {'id': '8f8a68a6-eee8-42e4-a488-28200576ad32', 'created_at': datetime.datetime(2023, 2, 11, 13, 42, 25, 362754), 'updated_at': datetime.datetime(2023, 2, 11, 13, 42, 25, 362939)}
(hbnb) 
```
