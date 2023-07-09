#!/usr/bin/env python
# coding: utf-8

# In[23]:


#anhelina liashynska
def menu():
    print()
    print('Menu')
    print('-------------')
    print('1.Encode')
    print('2.Decode')
    print('3.Quit')
    
    
def encode(user_password):
    password_list = []
    for i in iter(str(user_password)):
        s = int(i)+3
        password_list.append(s)
        
    return password_list
  
    
while True:
    menu()
    option = int(input('Please enter an option: '))
    if option ==1:
        user_password = int(input('Please enter your password to encode:'))
        password = encode(user_password)        
        print('Your password has been encoded and stored!')
    elif option==2:
        decoded_password = decode(password)
        string_password = ''.join([str(i) for i in password])
        print(f'The encoded password is {string_password} and the original password is {decoded_password}.')
    elif option==3:
        break
        


# In[ ]:





# In[ ]:




