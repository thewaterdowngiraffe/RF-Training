# Setup
1. install python. (3.13.12 was the supported version for qweb).
2. create a virtual python env (best practice)
3. install the requirements `pip install -r requirements.txt`
4. if you want the [rpaframework](https://github.com/robocorp/rpaframework?tab=readme-ov-file) library you will need to install sepratly `pip install rpaframework`. This library has install issues on python versions above 3.10.x when included in the requirements.txt file.
## VS code
Extensions:
- Auto Docstring
    > njpwerner.autodocstring
- autopep8
    > ms-python.autopep8
- prettier
    > esbenp.prettier-vscode
- pylance
    > ms-python.vscode-pylance
- pylint
    > ms-python.pylint
- rainbow csv
    > mechatroner.rainbow-csv
- robo code
    > d-biehl.robotcode


# Robot Framework
This is an open source framework developed by Nokia ([History - Copado](https://www.copado.com/resources/blog/what-is-robot-framework-the-story-behind-a-robotic-testing-ecosystem-crt)). the language syntax is developed to optionally leverage [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) ([BDD other notes](https://cucumber.io/docs/bdd/))

## Features and Limitations
Robot Framework aims to act as a one stop shop for all automation needs. It does this by providing high quality documentation, and mapping industry standard libraries like selenium, playwright, autoit, Appium, FlaUI and others to the language along side with dedicated documentation.

With robot framework being built on python you can expand the feature set to anything python supports such as load testing APIs, supporting complex data logic/objects, compiling builds using system commands or even binding other testing frameworks or libraries into one unified language. with python support there is no limit. It is possible to even have python call C/C++ code since python is built on C.
> I don't recommend calling c functions as there are better methods to validate c code with robot framework: build unit tests in Cunit (or others) and have python run the system command to trigger the unit test then parse the results and report back.

^ with the way robot framework is built, there are no limits to what you can do as long as you know what you want to do.


They also support [remote servers](https://github.com/robotframework/RemoteInterface?tab=readme-ov-file) with other languages (says it supports python, PHP, .net and others)
you can even expand it with other languages. the example they provide is for [rust](https://docs.robotframework.org/docs/extending_robot_framework/custom-libraries/non-python_library).
## Usage and Relevance
With the onboarding of [Copado](https://www.copado.com/) platform we can directly utilize [Copado Robotic Testing](https://www.copado.com/product-overview/copado-robotic-testing) (CRT). A hyper simplified summary of the product is Robot framework bundled with two proprietary libraries **[QMobile](https://docs.copado.com/resources/Storage/copado-robotic-testing-publication/CRT%20Site/qwords-reference/current/qwords/_attachments/QMobile.html)** and **[QVision](https://docs.copado.com/resources/Storage/copado-robotic-testing-publication/CRT%20Site/qwords-reference/current/qwords/_attachments/QVision.html)** ([Qweb](https://github.com/qentinelqi/qweb) is also bundled, but it is not proprietary).

> Qweb was created by Qentinel as an open sourced library with the Apache 2.0 license prior to  Copado [acquiring](https://www.copado.com/resources/blog/copado-agreement-to-acquire-leading-ai-testing-company) Qentinel hence why it is non proprietary.

Robot framework has been leveraged to provide the testing team with a testing automation solution that is cost friendly, non proprietary, and easy to learn without superficial limitations superimposed by a vendor.

With CRT leveraging robot framework it makes support easy and expandability endless.


## Docs
- [Framework Website](https://robotframework.org/)
- [Open Source Code](https://github.com/robotframework/robotframework)

- [Robot framework Docs](https://docs.robotframework.org/)

# Intro
if you want to skip everything just do these [public lessons](https://github.com/qentinelqi/qweb_workshop?tab=readme-ov-file) provided by the owners of the Qweb library.

for a more detailed doc on how the language works and the ins and outs please read or skim over the official [docs](https://docs.robotframework.org/docs)

## file types
there are two types of files `.robot` and `.resource`
`.robot` files are your test cases and your `.resource` files are where you would place reusable code or code that the `.robot` files depend on.

you cant/shouldn't import a `.robot` file

files are based on sections declared by the name.
*** name ***


### Available in all files
- Settings
	- Imports (library, resources and variables). Enables calling functions, variables or other data from other files or libraries.
	- Documentation. Documents what the files does
- Variables. declare local variables to a file. they overwrite based on import order.
- Keywords. Functions that are used by other keywords or testcases. (no overwriting)
- Comments. gives you a dedicated space to comment within a file for bulk comments. fully ignored by the code.
### `.resource` exclusive
- settings
	- keyword tags. Allows for function based tags to be applied to keywords such as error handling.
### `.robot` exclusive
- settings.
	- testcase teardown. function or keyword that will run when the test case is finished.
	- testcase setup. function or keyword that will run before running the testcase.
	- suite setup same functionality as testcase setup but runs before any testcase in the file runs
	- suite teardown. same functionality as testcase teardown but runs after the final test case finishes in the file.
	- test case tags. allows for test cases to be tagged. can be viewed and filtered in the logs after a run.
	- metadata. allows for tagging test cases without the tags being visible in the report logs. useful if tying test cases to JIRAs.
- test case / tasks
	- this is what will be executed.



# [Data types](https://docs.robotframework.org/docs/variables)
Dictionary
list (array)
variable (anything else)

python doesn't take data types seriously since its either a variable or not. The data types that robot framework assign are simply the structure of the declaration simply dictating how they get interpreted into said variable.

The bellow are the same things in python and robot framework

I have added type hinting even though it does not have any impact to the code
```python
list_example:list = [1,2,3,4,5]
dict_example:dict = {"name":"john smith","age":50}
none_val = None
bool_val:bool = True
```

```RobotFramework
@{list_example}=    1    2    3    4    5
&{dict_example}=    name=john smith    age=50
${none_val}=    ${None}
${bool_val}=    ${True}
```

you can expand the data types though the use of python
Example
```python
# person.py
class Person:
	def __init__(self,
				 name=None,
				 age=None,
				 phone_number=None,
				 email_address=None):
		self.name_first, self.name_last = self.__parse_name(name)
		self.phone_number = phone_number
		self.email_address = email_address
	def __parse_name(self,name)->tuple[str,str]:
		if " " in name:
			return tuple(name.split(" ",maxsplit=1))
		return (name, None)

def createPerson(name,
			     age,
			     *,
			     phone_number=None,
			     email_address=None)->Person:
    return Person(name,age,phone_number,email_address)
def getPhoneNumber(person:Person):
	return person.phone_number
def getFisrtName(person:Person):
	return person.name_first
def getLastName(person:Person):
	return person.name_last
def getEmailAddress(person:Person):
	return person.email_address
```

Small example
```RobotFramework
*** Settings ***
Library    person.py

*** Variables ***
${Fisrt Name}       John
${Last Name}        Smith
${Age}              50
${Phone Number}     8558558555
${Email Address}    testUser@test.com

*** Test Cases ***
Validate Phone Number Is Correct
	${person}    createPerson    ${Fisrt Name} ${Fisrt Name}
	...    ${Age}
	...    phone_number=${Phone Number}
	...    email_address=${Email Address}
	Evaluate    getPhoneNumber
	${pn}    Get Phone Number    ${person}
	should be equal    ${pn}    ${Phone Number}
```


# Training
- Python excellent resources these will explain everything.
	- [W3 school](https://www.w3schools.com/python/default.asp)
	- [geeks for geeks](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)

- Qweb | web - copado
	- [training lessons with solutions](https://github.com/qentinelqi/qweb_workshop?tab=readme-ov-file)


manual lessons:
- [Lesson 1](./Lesson%201/readme.md)
- [Lesson 2](./Lesson%202/readme.md)
- [Lesson 3](./Lesson%203/readme.md)
- [Lesson 4](./Lesson%204/readme.md)
- [Lesson 5](./Lesson%205/readme.md)
- [Lesson 6](./Lesson%206/readme.md)
- [Lesson 7](./Lesson%207/readme.md)
- [Lesson 8](./Lesson%208/readme.md)
