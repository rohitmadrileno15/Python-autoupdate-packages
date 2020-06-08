from subprocess import call
import time
call("pip freeze > requirements.txt"  ,shell=True)
time.sleep(4)
print("Creating Environment for the update")
read = open("requirements.txt", 'r')
array_of_packages=[]

for line in read:
    array_of_packages.append(line)

for _, name_of_package in enumerate(array_of_packages):
    name_of_package = name_of_package.split("=",1)[0]
    call("pip install --upgrade " + name_of_package, shell=True)
    time.sleep(5)
    print('*****')
    print("upgraded",name_of_package)
