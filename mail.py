import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


def mail(location, delivery_number, img_link):
    mail_content = '''
    <head>
        <p> Location: {} </p>
        <p> Delivery number: {} </p>
    </head>
    <img src={} width="200"  height="200" > </img>
    '''.format(location, delivery_number, img_link)

    # Infos
    sender_address = 'your_sender_email@gmail.com'
    sender_pass = 'password'
    receiver_address = 'receiver_email@gmail.com'

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "Delivery Number: {}".format(delivery_number)
    message.attach(MIMEText(mail_content, 'html'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP_SSL('smtp.gmail.com', 465) #use gmail with port
    # session.starttls() #enable security
    session.ehlo()
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')