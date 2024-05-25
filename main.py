#### Write a program which takes usernames until -1 and make list
#### of these usernames, program should add @iba-suk.edu.pk to end of 
#### each username to make it an email. Additionally program should 
#### generate an unique password for every email and display it.

#### password requirement : 
####    9 digits/characters
####    from ASC II code 33 to 122
    
#### Sample Input:
####    jawad
####    Dua
    
#### Sample Output:
    
#### jawad@iba-suk.edu.pk
#### *#%_hRLaN


#### dua@iba-suk.edu.pk
#### z>E\fx7&b



import random

#function for 9 digit long random password
def rand_pass():
    password = ""
    for x in range(9):
        num = random.randint(33,122)        
        char = chr(num)
        password += char
    print(password)

#makes list of user name
username = input("Enter username")
usernames = []
sentinental_value = str(-1)

while username != sentinental_value:
    usernames.append(username)
    username = input("Enter username")
    
    
#displays result
for email in usernames:
    email = email + "@iba-suk.edu.pk" 
    print()  #empty line
    print(email)
    rand_pass()
    print() #empty line
    



