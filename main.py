#making a tuple
SECURE = (('a','@'), ('and','&'), ('i','!'), ('s','$'), ('d','#'),('p','%'),('o','*'), (' ','^'))


#function
def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)

    return password


if __name__ == "__main__":
        password = input("enter your thinked password:  ")
        password = securePassword(password)
        print(f"your secured password is {password}")





