# myfile= open('shaklain.txt','w')
# myfile.write("hello i am shaklain ashraf!")
# myfile.close()
# print("file creation succesfully")

# myfile=open('ashraf.txt','w')
# myfile.write("hello python")
# myfile.close()
# print("done")

# file_path= "C:/Users/HP/Videos/OneDrive/Desktop/Python full stack/Frontend/gym"
# myfile=open ('ashrafi'.txt','w')
# myfile.write(file_path)
# myfile.close()
# print("your file creation succesfully")


# file_path= "C:/Users/HP/Videos/OneDrive/Desktop/Python full stack/Frontend/gym"
# myfile=open('shaklain.txt','w')
# myfile.write(file_path)
# myfile.close()
# print("yes hello!")

# msg=input("write your text message:")
# with open('pra.txt', 'w')as myfile:
#     myfile.write(msg)

# import os
# file_path="C:/Users/HP/Videos/OneDrive/Desktop/Python full stack/Frontend/filepython/shaklain2.txt"
# if os.path.isfile(file_path):
#   print(" file is already exist")
# else:  
#   myfile=open('file_path','w')
#   myfile.write("hello amma ")
#   myfile.close()
#   print("file created with path succesfully")


# data=['my name is shaklain','\n we are learning python','\n in file handling']
# myfile=open('zaid.txt','w')
# myfile.writelines(data)
# myfile.close()
# print("file created succesfully")


# myfile= open('zaid.txt','a')
# myfile.write("\n hiii dear sir")
# myfile.close()
# print("file updated")


# myfile=open('zaid.txt','r')
# content=myfile.readlines()
# print(content)

# myfile=open('zaid.txt','a')
# myfile.write("\n shaklain ashraf is a very good boy")
# myfile.close()
# print("text added succesfully")

# with open ('kaan.txt','r')
# content= myfile.read()

# import os
# # os.remove("pra.txt")
# os.rename("shaklain.txt ,ashrafi.txt")


# with open('sindhu.txt','w') as myfile:
#     myfile.write("hello dear how are you")
# print("file created with open fuction")    
    


# data=['hello everyone','\n my name is shaklain','\n now i am learning','\n file handling']
# myfile= open('mujahid.txt','w')
# myfile.writelines(data)
# myfile.close()
import os
# old_path = "C:/Users/HP/Videos/OneDrive/Desktop/Python full stack/Frontend/filepython/sind.txt"
# new_path = "C:/Users/HP/Videos/OneDrive/Desktop/Python full stack/Frontend/filepython/rehan.txt"
# os.rename(old_path,new_path)
# print("file rename succesfully!")

# src_path = "C:/Users/HP/Videos/OneDrive/Desktop/Python full stack/Frontend/filepython"
# for file in os.listdir(src_path):
#     print(file)

# os.remove('ashraf.txt')
# print("file removed succesfully")

directory = "C:/Users/HP/Videos/OneDrive/Desktop/Python full stack/Frontend/filepython/ashrafi"
os.makedirs(directory)
print("directory is created")