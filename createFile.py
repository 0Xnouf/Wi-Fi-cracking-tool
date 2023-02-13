import datetime  # to print the current date and time in the file


def create_file(name, pswd):  # create the text file to be sent through email
    result = open("result.txt", "w")
    result.write("***********************************************************************\n"
                 "**           WE CRACKED A NEW Wi-Fi PASSWORD SUCCESSFULLY !!         \n"
                 "**  Details:-                                                        \n"
                 "**                                                                   \n"
                 "** - Wi-Fi name : {}                                                   \n"
                 "** - Password : {}                                                     \n"
                 "** - Time of the attack : {}                                         \n"
                 "***********************************************************************"
                 .format(name, pswd, datetime.datetime.now()))
