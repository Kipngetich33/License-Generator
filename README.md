# License-Generator
Clone the repository from github
```bash
$ git clone <repository link>
```
Change directory to the just cloned repository
```bash
$ cd License-Generator
```
Open a python shell (python 2.7)
```bash
$ python2.7
```
Import Class Key from key_generator.py
```bash
$ from key_generator import Key
```
Create an instance of the Key
```bash
$ key_instance = Key()
```
Call the main function from the key instance
```bash
$ key_instance.main()
```
Follow the steps that will be provided by the program until a message similar the following:
```bash
“Successfully generated and saved a monthly licence.Please commit the changes and push the changes online”
Below the message you will get the license key details that you will need to send to the user similar to the following:
Send below License Details to Client
{'period_name': 'monthly', 'unique_license_key': '440Q-C4XK-RMB1-UAO8-3JLQ', 'time': 2592000}
```
