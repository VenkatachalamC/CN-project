

import smtplib
from email.message import EmailMessage


def send_mail():
    #Setting mail contents
    msg=EmailMessage()
    msg['subject']='Crawled details'
    msg['From']='Crawler'
    msg['To']=['','']
    msg.set_content('The book details crawled from website are sent in this attachment')
    #Add attachments to the mail
    try:
        with open('WebCrawler/details.db','rb') as f:
            file_data=f.read()
            file_name='details'
            msg.add_attachment(file_data,maintype="application",subtype="db",filename=file_name)

        #logging to the SMTP server
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.starttls()
            server.login('MailId' , 'Password')
            #sending the mail
            server.send_message(msg)
            print("mail sent")
            server.quit()
    except:
        print('File not Found...')

