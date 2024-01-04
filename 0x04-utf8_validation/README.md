# 0x04 utf8_validation

# Requirements
## General
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
4. All your files should end with a new line
5. The first line of all your files should be exactly #!/usr/bin/python3
6. A README.md file, at the root of the folder of the project, is mandatory
7. Your code should use the PEP 8 style (version 1.7.x)
8. All your files must be executable




## TASK 
Write a method that determines if a given data set represents a valid UTF-8 encoding.

1. Prototype: def validUTF8(data)
2. Return: True if data is a valid UTF-8 encoding, else return False
3. A character in UTF-8 can be 1 to 4 bytes long
4. The data set can contain multiple characters
5. The data will be represented by a list of integers
6. Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer


```
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$

```


```
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```
