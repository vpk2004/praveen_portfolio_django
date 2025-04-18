from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost", 
    user = "root" , 
    password = "ayyappan2004", 
    database = "portfolio_database"
    )
pf = conn.cursor()


# Create your views here.

def home(request):
    return render(request, 'main.html')

def submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile_no = request.POST.get("mobile_no")
        email_address = request.POST.get("email_address")
        e_mail_subject = request.POST.get("e_mail_subject")
        sms = request.POST.get("message")

        qry = "INSERT INTO pf_details(full_name, ph_no, e_mail, e_mail_subject, visiter_msg) VALUES (%s, %s, %s, %s, %s)"
        value = (name, mobile_no, email_address, e_mail_subject, sms)
        pf.execute(qry, value)
        conn.commit()

        return render(request,"submit.html")