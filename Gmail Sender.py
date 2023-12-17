import os


sender = 'kazikiwi55@gmail.com'
reciver = 'kazi@siyam.nyc'

subject = "noobra"

contents = """
siyam is noob 
"""

while True:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=reciver, subject=subject, contents=contents)

    print("Email Sent!")

