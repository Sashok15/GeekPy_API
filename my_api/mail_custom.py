import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from my_api.local_settings import *


def send_email(amount, time, category_name):
    # me == my email address
    # you == recipient's email address
    me = "lordyhard@gmail.com"
    you = "onlyimholol@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Parsing"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Statistic"
    html = """\
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
                <h1>statistic</h1>
                <table border=1>
                    <tr>
                        <th>name_category</th>
                        <th>amaunt</th>
                        <th>time</th>
                    </tr>
                    <tr>
                        <td>{2}</td>
                        <td>{0}</td>
                        <td>{1}</td>
                    </tr>    
                </table>
            </head>
            <body>
            
            </body>
            </html>
        """.format(amount, time, category_name)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach paxrts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587) #465 587
    s.ehlo()
    s.starttls()
    # re-identify ourselves as an encrypted connection
    # s.ehlo()
    s.login(LOGIN, PASSWORD)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()
