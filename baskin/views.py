from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def home(requests):
    return render(requests, 'baskin/index.html')

# def form(requests):
#     if requests.method == 'POST':
#         name = requests.POST['name']
#         roof_age= int(requests.POST.get('roof_age'))
#         email = requests.POST['email']
#         phone = requests.POST['phone']
#         address = requests.POST['address']
#         monthly_bill = requests.POST['monthly_bill'] 
#         # HOA = requests.POST['HOA']
#         HOA  = requests.POST.get('HOA','off')
#         print(type(HOA))
#         if HOA == 'on':
#             HOA = True
#         else:
#             HOA = False

#         battery = requests.POST['battery']
#         # print(battery)
#         if battery == 'on':
#             battery = True
#         else:
#             battery = False
        
#         foundation = requests.POST['foundation'] 
#         # print(foundation)
#         if foundation == 'on':
#             foundation = True
#         else:
#             foundation = False
#         roof_type = requests.POST['roof_type']
#         availability= requests.POST['availability']
#         bill = requests.POST['bill']

#         details = Details(
#             name = name, 
#             roof_age = roof_age, 
#             email = email,
#             phone = phone, 
#             address = address,
#             monthly_bill = monthly_bill, 
#             HOA = HOA, 
#             battery = battery, 
#             foundation = foundation, 
#             roof_type = roof_type,
#             availability= availability,
#             bill = bill
#         )
#         print(HOA)
        # print(name, roof_age, email, phone, address, monthly_bill, HOA,battery, foundation, roof_type, availability, bill)
        # details.save()
        # print('Saved to db')
    # return render(requests, 'baskin/form.html')

# def register(requests):
#     context ={}
#     context['form']= DetailsForm()
#     return render(requests, "baskin/register.html", context)

def faq(requests):
    return render(requests, "baskin/faq.html")

def contact(requests):
    return render(requests, "baskin/contact.html")

def services(requests):
    return render(requests, "baskin/service.html")

def commercial(requests):
    return render(requests, "baskin/commercial.html")

def residential(requests):
    return render(requests, "baskin/residential.html")

def whysolar(requests):
    return render(requests, "baskin/whysolar.html")

def gogreen(requests):
    return render(requests, "baskin/gogreen.html")

# def register(requests):
#     if requests.method == 'POST':
#         form = RegisterForm(requests.POST, requests.FILES)
#         name = requests.POST['name']
#         roof_age= int(requests.POST.get('roof_age'))
#         email = requests.POST['email']
#         phone = requests.POST['phone']
#         address = requests.POST['address']
#         monthly_bill = requests.POST['monthly_bill'] 
#         HOA  = requests.POST.get('HOA')
#         battery = requests.POST['battery']
#         foundation = requests.POST['foundation'] 
#         roof_type = requests.POST['roof_type']
#         availability= requests.POST['availability']
#         bill = requests.POST.get('bill', False)
#         questions = requests.POST['questions']
#         details = Details(
#             name = name, 
#             roof_age = roof_age, 
#             email = email,
#             phone = phone, 
#             address = address,
#             monthly_bill = monthly_bill, 
#             HOA = HOA, 
#             battery = battery, 
#             foundation = foundation, 
#             roof_type = roof_type,
#             availability= availability,
#             bill = bill,
#             # questions = questions,
#         )
#         print(name, roof_age, email, phone, address, HOA,battery, foundation, roof_type, availability, bill,questions)
#         details.save()
#         print('Saved to db')
#     else:
#         print('db is not working')
#         form = RegisterForm()
#     context = {'form':form}
#     return render(requests, 'baskin/register.html', context)

def register(requests):
    if requests.method == 'POST':
        form = RegisterForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
            print('Saved to db')
            messages.success(requests, 'Thank you for submitting your form')
            return render(requests, 'baskin/index.html')
            
    else:
        form = RegisterForm()

        context = {'form':form}
        return render(requests, 'baskin/register.html', context)



