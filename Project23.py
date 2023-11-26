#Examples  on Decorators
# create an authorization decorator that checks if a user is authorized a  function
# write a program about a retry decorator that retries a function for  a given duration, 
#if  it raises a specific exception

import random
import time
def retry_decorator(max_duration , trigger_exception):
    def decorator(f):
        def wrapper(*arg,**kwargs):
            num_retry = 0
            while num_retry < max_duration:
                try:
                    response= f(*arg,**kwargs)
                    return response
                except trigger_exception as e:
                    print(f'retrying{f.__name__} as a result of {e}')
                    num_retry += 1
                    #introduce a random delay before retrying
                    delay= random.uniform(0.1,1.0)
                    time.sleep(delay)
            raise Exception(f'maximum attempt{max_duration}reached for{f.__name__}') 
        return wrapper
    return decorator
   
@retry_decorator(3,ConnectionError)
def atm_connection():
    x=random.random () 
    print(x)
    if x< 0.8: 
        raise ConnectionError("ATM connection fail")
    print("fail to connect to ATM server")
b=atm_connection()   
b



# Write a program on an authorization decorator that checks if a user is auhorized to execute a function

def auth_decorator(f):
    def wrapper_func(teacher, *args, **kwargs):
        if teacher == 'mathematics_teacher':
            return f(*args, **kwargs)
        else:
            raise PermissionError("Sorry! You ain't a maths teacher. You can't perform this function.")
    return wrapper_func


#@auth_decorator
def maths_func_only():
    print("Mathematical functions are executed here!")

# instantiate the func
teacher = maths_func_only
    
# create non-maths teachers
teacher_abubakar = 'biology_teacher'
    
# create maths teacher
teacher_ire = 'mathematics_teacher'

# call func
teacher(teacher_abubakar)


try:
    teacher(teacher_abubakar)
except PermissionError as e:
    print(e)