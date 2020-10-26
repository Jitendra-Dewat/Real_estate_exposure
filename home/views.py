from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import Contact,Profiledetail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from home.forms import ProfiledetailForm
from properties.models import Postforselling, Imgesofproperties,Postforrent, Roommateprofile, Employees
from math import ceil
import json
import re
from datetime import date

# Create your views here.
def checkname(name):
    if name.replace(" ", "").isalpha():
        return True
    else:
        return False

def chekemail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if(re.search(regex,email)):
        return True
    else:
        return False

def checkpwd(passwd):
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 8:  
        val = False
          
    if len(passwd) > 20: 
        val = False
          
    if not any(char.isdigit() for char in passwd):      
        val = False
          
    if not any(char.isupper() for char in passwd): 
        val = False
          
    if not any(char.islower() for char in passwd): 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        val = False
    if val: 
        return val 

def checkphone(phone):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    if(Pattern.match(phone)):
        return True
    else:
        return False


def calculateAge(birthDate): 
    print(birthDate)
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age



def trimstr(strl):
    newstr = ""
    for character in strl:
        if character is ' ':
            newstr += character
            continue
        if character.isalnum():
            newstr += character
    return newstr




def home(request):
    allhomes = Postforselling.objects.all()
    allsellinghomes = []
    x=0
    for home in allhomes:
        if(home.ownerid == request.user):
            pass
        else:
            if(x==8):
                break
            allsellinghomes.append(home)
            x=x+1
    sellen = len(allsellinghomes)

    allhomes = Postforrent.objects.all()
    allrentinghomes = []
    x=0
    for home in allhomes:
        if(home.ownerid == request.user):
            pass
        else:
            if(x==8):
                break
            allrentinghomes.append(home)
            x=x+1
    renlen = len(allrentinghomes)

    flatmates = Roommateprofile.objects.all()
    allflatmates = []
    x=0
    for mate in flatmates:
        if(mate.email == request.user):
            pass
        else:
            if(x==8):
                break
            allflatmates.append(mate)
            x=x+1
    flatlen = len(allflatmates)

    employees = Employees.objects.all()
    allemployees = []
    x=0
    for employee in employees:
        if(x==8):
            break
        allemployees.append(employee)
        x=x+1
    emplen = len(allemployees)

    params = {'allsellinghomes':allsellinghomes, 'allrentinghomes':allrentinghomes, 'allflatmates':allflatmates, 'allemployees':allemployees, 'sellen':sellen, 'renlen':renlen, 'flatlen':flatlen, 'emplen':emplen}
    return render(request, 'home/home.html',params )
    

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please Fill The Form Correctly')
            
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your Message hase been successfully sent')
        
        
    return render(request, 'home/contact.html')

# Authentication  APIs
def handleSignup(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['email']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if(checkpwd(pass1)):
            pass
        else:
            messages.error(request, "Password length should > 8 or < 20 character and should contain at least a number, a small and a capital alphabate and a special symbol $ @ # %")
            return redirect('home')

        if(chekemail(email)):
            pass
        else:
            messages.error(request, "email Format is not Valid")
            return redirect('home')

        isexist = User.objects.filter(email=email)
        if(len(isexist)>0):
            messages.error(request, 'Email Already Exist')
            return redirect('home')
    
        

        #print(username, profile, fname, mname, lname, dob, gender, phone, address, address2, country, statename, city, zipf, email, pass1, pass2)
        #checks for erroreneous inputs
        #first_3_char = username[:3]
        #if not first_3_char.isalpha():
           # messages.error(request, 'User name first three character should be letters')
           # return redirect('home')

       # if len(username) > 15:
         #   messages.error(request, 'User name must be less than 15 character')
          #  return redirect('home')
       # if not username.isalnum():
           # messages.error(request, 'User should only contain letters and numeric values')
           # return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, 'Password did not match')
            return redirect('home')

        # Create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, 'Your  account has been successfully created')
        return redirect('home')

    else:
        return HttpResponse('404 Not Found')

def getprofile(request):
    if request.user.is_authenticated:
        data = Profiledetail.objects.filter(email=request.user)
        
        if request.method == 'POST' and User.is_authenticated and len(data) < 1:
            email = request.user
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            dob = request.POST['dob']
            gender = request.POST['gender']
            phone = request.POST['phone']
            address = request.POST['address']
            address2 = request.POST['address2']
            country = request.POST['country']
            statename = request.POST['statename']
            city = request.POST['city']
            zipf = request.POST['zipf']
            prfilepic = request.FILES['prfilepicfile']
            uniprofile = email


            address = trimstr(address)
            address2 = trimstr(address2)

            #fs=FileSystemStorage()
            #fs.save(prfilepic.name, prfilepic)

            if(checkname(fname) and checkname(lname) and checkname(mname)):
                pass
            else:
                messages.error(request, 'name Should be a valid string')
                return redirect('home')
            
            if(checkphone(phone)):
                pass
            else:
                messages.error(request, "Phone No's first digit should contain number between 7 to 9 and can have 11 digits also by including 0 at the starting and 12 digits also by including 91 at the starting ")
                return redirect('home')



            if(checkname(country)):
                pass
            else:
                messages.error(request, 'Country name Should be a valid string')
                return redirect('home')
            
            if(checkname(statename)):
                pass
            else:
                messages.error(request, 'State name Should be a valid string')
                return redirect('home')
            
            if(checkname(city)):
                pass
            else:
                messages.error(request, 'City name Should be a valid string')
                return redirect('home')

            if(zipf.isnumeric() and len(zipf) > 5 and len(zipf) < 7):
                pass
            else: 
                messages.error(request, 'Pincode Should be a number and should be 6 digit')
                return redirect('home')




            profiledetail = Profiledetail(email=uniprofile, firstname=fname, middlename=mname, lastname=lname, dob=dob, gender=gender, phone=phone, address=address, address2=address2, country=country, statename=statename, city=city, zipf=zipf, image=prfilepic)
            profiledetail.save()
            messages.success(request, 'Your Profile hase been successfully uploded')
            return redirect('home')
            #form = ProfiledetailForm(request.POST, request.FILES)
            #if form.is_valid():
                #form.save()
            #messages.success(request, 'Your Profile hase been successfully uploded')
            #return redirect('home')
        else:
            messages.error(request,"You can't setup your profile 2 times Because you have done that already")
            return redirect('home')
    else:
        messages.error(request,'Please Login First')
        return redirect('home')
            
        

def handleLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully Logged In')
            return redirect('home')

        else:
            messages.error(request, 'Invalid Credentials please try again')
            return redirect('home')
    return HttpResponse('404 Not Found')   


    

def handleLogout(request):
    #if request.method == 'POST':
    logout(request)
    messages.success(request, 'successfully Logged Out')
    return redirect('home')


