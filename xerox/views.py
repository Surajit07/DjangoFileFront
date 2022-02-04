from django.http import HttpResponse
from django.shortcuts import render,redirect
def home(request):
    return render(request,"index.html")
def result(request):
    name=request.GET['name']
    address=request.GET['P']
    number=request.GET['G']
    document=request.GET['category']
    print(document)
    from twilio.rest import Client
    
    sid='ACf558482fe175137e372639a0cd29b1cc'
    authToken='86ec24f461704a665d8d3137b226576c'

    client=Client(sid,authToken)

    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+19034742974'
    
    message=client.messages.create(body=name,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    message=client.messages.create(body=address,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)

    message=client.messages.create(body=number,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    message=client.messages.create(body=document,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    return redirect("https://xeroxfin.herokuapp.com/")
