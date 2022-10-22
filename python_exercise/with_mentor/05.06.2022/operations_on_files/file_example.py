# f = open("myLetter.txt", "w")
# # write to the file... if fail i make sure to close the file
# try:
#     f.write("I am missing you dear!")
# finally:
#     f.close()


with open("myLetter.txt", "w") as f:
    f.write("I am happy with the weather today. \n")