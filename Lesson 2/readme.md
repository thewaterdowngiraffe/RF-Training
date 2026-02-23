# Goals
Before starting read the [OOP section](#oop)

Python is important to Robot framework since that is what its built on.
to start we will do a few things.

To start simple you will make 3 custom objects: car, motorcycle and plane.

Each vehicle object must have the following functions:
- top_speed
- passengers
- vehicle_type
- brand


task:
1. Create a file called `vehicles.py`
2. Create 3 classes `car`, `motorcycle` and `plane`
3. run the following command `pytest .\test_import.py`
4. using the class mapping bellow hard code the values bellow to the corresponding object.
	- i will be testing that i can get the values out of the object.
	- run `pytest test_objects.py` to confirm it worked
5. lets make it dynamic, update the variables from hard coded to be a default that can be passed into the `__init__` function. [How to set default values](https://www.geeksforgeeks.org/python/default-arguments-in-python/)
	- run `pytest test_objects.py` to confirm that you didn't break it.
	- run `pytest test_objects_final.py` to test that your new changes worked
		- test that you didn't break it and test that the default value works
6. next you will be racing your vehicles
	1. locate the `Task 2.py` file.
	2. read and action the instructions
	3. run it
	4. notice the issue where the speed keeps increasing after it is done. within the vehicle class implement a way so that when self.done is true the speed stops going up.

class mapping:

|              | car   | motorcycle   | plane   |
| ------------ | ----- | ------------ | ------- |
| top_speed    | 140   | 200          | 700     |
| passengers   | 3     | 1            | 50      |
| vehicle_type | "car" | "motorcycle" | "plane" |




> [!NOTE]
> You do not need to use OOP for this, but it is recommended to try.
> If you get stuck with OOP, create them normally then after passing, try to updated it to use OOP

# Python
How python works can be learned from either of these resources: [geeks for geeks](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)  [w3school](https://www.w3schools.com/python/default.asp)
They will give you more than i can.

## Variables
Variables hold data, they can be written to, read from and overwritten.
There are lots of data types here are the ones you will come across the most

| name  | full name  | summary                                                                  |
| ----- | ---------- | ------------------------------------------------------------------------ |
| list  | array      | an array of data, can be any data type. starts at index of 0             |
| int   | integer    | any whole number                                                         |
| float | float      | any number with a decimal point                                          |
| bool  | boolean    | true of false \| 1/0                                                     |
| set   | set        | its like a list, but there can only be one instance of each unique value |
| dict  | dictionary | think of it like a json, you pull data out using its `key`               |
| str   | string     | list of letters &/or numbers.                                            |

Python doesn't care much about how you store variables and you can 'cast' a variable to a type as needed given it meets the requirements.
Example:
- int(True) == 1
- bool(0) == False
- int("10") == 10
- float(10) == 10.0
- int(9.5) == 9
- list(set(\[1,1,3,4,2\])) == \[1,3,4,2\]

## Functions

Functions can take in variables and return values.
They do something.
lets say i want to pass 11/10 or 7 numbers and place it into the correct phone number formula.

```python
def format_phone_number(number):
	number = str(number)
	match len(number):
		case 7:
			return f"{number[-7:-4]}-{number[-4:]}"
		case 10:
			return f"({number[0:-7]}) {number[-7:-4]}-{number[-4:]}"
		case 11:
			return f"{number[0]} ({number[1:-7]}) {number[-7:-4]}-{number[-4:]}"
		case _:
			return "invalid phone number try again"
```

> the trick used above is how python can manipulate lists. For details read [this](https://www.w3schools.com/python/python_lists_access.asp).




## Classes/Objects
classes and objects are just a way to bundle functions and/or data within one single consistent variable.
details can be found [here](https://www.geeksforgeeks.org/python/python-classes-and-objects/) or [here](https://www.w3schools.com/python/python_classes.asp)

all classes have a `__init__` this allows them to be initialized.
Data stored within a class is located under `self`.
all functions within a class need to have `self` if they are defined within a function.

there are things like
`__repr__`, `__str__`, `__int__` ,`__iter__`,`__len__` and many others
each has a purpose:
- `__int__` this allows for you to cast your object as a integer.
- `__iter__` this allows you to iterate of the object or cast it to a list
- `__len__` allows you to call `len()` on your object and get a value
- `__repr__` if this is not found, `__str__` will be used, but it allows you to create a more advanced/detailed `__str__`. use `__str__` for when the user will see it and `__repr__` for when you need all the details.


# Code Concepts
## OOP
OOP is the practice of inheritance.
It allows you to create custom objects that inherited parts from the parent class.

(This is missing a lot of concepts, but this is the super high level.)
The best way to think of OOP is think of similarities between things and how the relation works is a "is" or "has".

Example:
Humans and monkeys are both primates.
Hawk and a crow are both birds.
Cod is not a primate nor a bird so we cant group it in there so a cod is a fish.

Primates, birds and fish are all animals.
Given that a human is a primate and a primate is an animal, we now have our groupings as listed here:

- animal
	- primates
        - human
        - monkey
    - bird
        - hawk
        - crow
    - fish
        - cod

So lets define some of these classes regarding data points or functions we want.

Example class structure:
animal:
- name
- age
- height
- weight

primates(animal):
- running speed
- jump height

bird(animal):
- wing span
- flying speed

fish(animal):
- fin count
- swimming speed


Looking top down
A human would have the following properties if it inherits the primates class:
- name
- age
- height
- weight
- running speed
- jump height

So lets apply this in code (i've made some changes to show how you can modify things)

```python
class animal:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class primates(animal):
    def __init__(self, age, height, running_speed, jump_height, name="primates"):
        weight = (20/703)*height ^ 2
        super().__init__(name, age, height, weight)
        self.running_speed = running_speed
        self.jump_height = jump_height


class bird(animal):
    def __init__(self, age, height, weight, wing_span, name="bird"):
        super().__init__(name, age, height, weight)
        self.wing_span = wing_span
        self.flying_speed = (wing_span**2)/weight


class fish(animal):
    def __init__(self, age, height, weight, fin_count, name="fish"):
        super().__init__(name, age, height, weight)
        self.fin_count = fin_count
        self.swimming_speed = height * fin_count/weight
```

Then the main classess that we would then use:
```python

class human(primates):
    def __init__(self, age, height, running_speed, jump_height, name="human"):
        super().__init__(age, height, running_speed, jump_height, name)


class monkey(primates):
    def __init__(self, age, height, running_speed, jump_height, name="monkey"):
        super().__init__(age, height, running_speed, jump_height, name)


class hawk(bird):
    def __init__(self, age, height, weight, wing_span, name="hawk"):
        super().__init__(age, height, weight, wing_span, name)


class crow(bird):
    def __init__(self, age, height, weight, wing_span, name="crow"):
        super().__init__(age, height, weight, wing_span, name)


class cod(fish):
    def __init__(self, age, height, weight, fin_count, name="cod"):
        super().__init__(age, height, weight, fin_count, name)
```

OOP allows for reusable code to be created easily and be modified with ease. The general consensus is that OOP makes reading the code more difficult in most scenarios.

The other concept of OOP is "has"
Example:
Person has a bank account.
A bank account is not part of a person and therefore can not be added under the person object.

A person does not allways have a bank account.

I would model this as follows:

```python

class person:
    def __init__(self,name):
        self.name = name
        self.bank_account = None

    def set_bank_account(self,account:bank_account):
        self.bank_account = account

class bank_account:
    def __init__(self,bank_name):
        self.bank_name = bank_name


Keegan = Person("Keegan")
keegan_bank_account = bank_account("savings")
Keegan.set_bank_account(keegan_bank_account)
```
In this example i created a person object.
Then i created the persons bank account then i set that persons bank account to the bank account object.

> OOP is not a requirement but it does reduce the amount of code and therefore opportunities for errors in some scenarios.
