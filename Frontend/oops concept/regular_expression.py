import re
# pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
# # pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# email = "shaklainashraf01@gmail.com"
# if re.match(pattern,email):
#     print("valid email")
# else:
#     print("invalid email")    



pattern = r"^[a-zA-Z0-9_+-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = 'shaklainashraf2001@77gmail.99.com'
if re.match(pattern,email):
    print("valid email pattern")
else:
    print("invalid email pattern")  


    
      