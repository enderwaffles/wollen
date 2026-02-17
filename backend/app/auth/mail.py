

import smtplib
import random

def sendcode(email):
    email = email

    code = random.randint(1000, 9999)
    code = str(code)
    print(f"\n\n\n\n{code}\n\n\n")
    password = "naar cszd midi iogy"
    login = "enderworldlife2019@gmail.com"
    obj_msg = smtplib.SMTP(host="smtp.gmail.com", port=587)
    obj_msg.starttls()
    try:
        obj_msg.login(user=login, password=password)
        obj_msg.sendmail(login, email, f"Your code {code}")
    except Exception as e:
        print(f"error {e}")

    return code