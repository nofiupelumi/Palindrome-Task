first_name= "John"
last_name ='Doe'
full_name = first_name + ' ' +last_name
#print(full_name)

# print(full_name[5])
# practice=(full_name[2:5])
# print( practice, len(practice))

# practice2=(full_name[-1:-4]) # This is semantically wrong
# print( practice2, len(practice2))

# practice3=(full_name[-4:-1])
# print( practice3, len(practice3))

# practice4=(full_name[4:1]) #This is semantically wrong
# print( practice4, len(practice4))

# practice5=(full_name[1:4])
# print( practice5, len(practice5))

# practice6=(full_name[:5])
# print( practice6, len(practice6))

# practice7=(full_name[2:])
# print( practice7, len(practice7))

# practice9=(full_name[-1:0:])
# print( practice9, len(practice9))

# practice10=(full_name[:6:2])
# print( practice10, len(practice10))

# practice11=(full_name[:6:-4])
# print( practice11, len(practice11))

# practice12=(full_name[:-2])
# print( practice12, len(practice12))

# practice3=(full_name[-8:-2:-2])
# print( practice3, len(practice3))

# practice3=(full_name[-8:-2:2])
# print( practice3, len(practice3))

#Palindrome
#eg:mama,noon.

# Algorithm
# 1.Accept word from user
# convert it to lower case
# Reverse the word 
# Remove spaces 
# compare the word and the reversed world
# if they are the same then its a palindrome
# print result

#coding
# word= input('Enter a word: ')
# Word= word.lower()
# reversed_word= word[::-1]
# word = word.replace(' ','')
# if word==reversed_word:
#     print('The word is a paindrome')
# else:
#     print('The word is not a palindrome') 

# _='he'
# print(_)

# i=0
# while i<3:
#    print(i)
#    i+=1
#    print(i+1)


# cl=[2,3,1]
# print(cl.remove(2),cl)

#  x=2
#  y=10
# x*=y*x+1

# li= 'python'.split()
# print(li, len(li))

# print(1 or 3)
# print(1 and 3)
# print(0 and 2 and 3)
#print(0 and 2 or 1 or 4)
#print(0 or False and 1)

# x=1
# if x==1:
#     print("wow!")
# elif x<2:
#     print('wow again')
# else:
#     print("No wow!")
#print(bool(' ') + 4)
# s='beginning'
# print(s.replace('n','N',-1))
# li=['A',2, 'rat']
# li.extend('BCD')
# print(li)
# li= [1,2,3,4,5]
# print(5.0 in li, end='')
# print('5' in li)

# s='amazing'
# print(s.index('a', 2 , 2))

# s=['123']
# print('-'.join(s))
# a=[5,4,5.6,3,'pythongeeks']
# print(bool(a[-2:-4]))
# s='python possibilities'
# print(len(s.partition('p')[0]))
#print(1,2,3,4,5, sep=',' ,end='.')
# a= {'name':'abc'}
# b=a
# c=a.copy()
# a['name']='xyz'
# print(b['name'],c['name'])

# s1={2,3,1,6,9}
# s2={1,3,5,7}
# len(s1^s2)

# for i,v in enumerate(['s','h','i','n','e']):
#     print(i,v, sep='-', end=':')