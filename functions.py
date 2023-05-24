def divide(a,b):
    if type(a) is int and type(b) is int:
        return a/b
    return 'a and b must be integers'


# must have exactly the correct amount of arguments passed in or will throw an error
def three_things(a,b,c):
    print("Hi")


#named arguments
def send_email(to_email, from_email, subject, body):
    email = f"""
    to:{to_email}
    from:{from_email}
    subject:{subject}
    ----------------------
    body:{body}
    """
    print(email)
    
    
send_email(subject="MEOW", to_email="blue@gmail.com", from_email="colt@humans.com", body="HI blue,you are a cat!")


# can add defaults for parameters, to avoid the issue thrown when the correct number of arguments are not passed in.
#cannot default the first parameter and have a required parameter afterwords like: def power(num=3,power)

def power(num, power=2):
    return num** power

power(4) # 16
