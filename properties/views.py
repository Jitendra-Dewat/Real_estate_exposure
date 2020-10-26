from django.shortcuts import render, HttpResponse, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
from properties.models import Postforselling, Imgesofproperties, Soldproperties, Postforrent, Imgesofrentalproperties, Roommateprofile, Roommateprofilepropimages, Serviceproviderprofile, Employees
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from home.models import Profiledetail
from home.views import trimstr, calculateAge, checkphone,checkpwd,chekemail,checkname

# Create your views here.

def postforsale(request):
    return render(request, 'properties/postforsale.html')

def hadlepostforsale(request):
    if request.user.is_authenticated:
        data = Profiledetail.objects.filter(email=request.user)
        if(len(data) < 1):
            messages.error(request, 'First Setup your Profile')
            return redirect('home')
        if request.method == 'POST' and User.is_authenticated:
            ownerid = request.user
            address = request.POST['address']
            address2 = request.POST['address2']
            country = request.POST['country']
            statename = request.POST['statename']
            city = request.POST['city']
            zipf = request.POST['zipf']
            parking= request.POST['parking']
            furnshid = request.POST['furnshid']
            airconditioner = request.POST['airconditioner']
            swimmingpool= request.POST['swimmingpool']
            cunstructionyear = request.POST['cunstructionyear']
            price = request.POST['price']
            area = request.POST['area']
            propertytype = request.POST['propertytype']
            description = request.POST['description']
            dateposted = datetime.datetime.now()
            mainimage = request.FILES['mainimage']
            image = request.FILES.getlist('images')

            address = trimstr(address)
            address2 = trimstr(address2)
            description = trimstr(description)

            if(checkname(country)):
                pass
            else:
                messages.error(request, 'Country name Should be a valid string')
                return redirect('postforsale')
            
            if(checkname(statename)):
                pass
            else:
                messages.error(request, 'State name Should be a valid string')
                return redirect('postforsale')
            
            if(checkname(city)):
                pass
            else:
                messages.error(request, 'City name Should be a valid string')
                return redirect('postforsale')

            if(zipf.isnumeric() and len(zipf) > 5 and len(zipf) < 7):
                pass
            else: 
                messages.error(request, 'Pincode Should be a number and should be 6 digit')
                return redirect('postforsale')

            if(price.isnumeric()):
                pass
            else: 
                messages.error(request, 'Price Should be a number')
                return redirect('postforsale')

            if(area.isnumeric()):
                pass
            else: 
                messages.error(request, 'area Should be a number')
                return redirect('postforsale')

            if(checkname(propertytype)):
                pass
            else:
                messages.error(request, 'Property type name Should be a valid string')
                return redirect('postforsale')
            


            postforsale = Postforselling(ownerid=ownerid, address=address, address2=address2, country=country, statename=statename, city=city, zipf=zipf, parking=parking, furnshid=furnshid, ac=airconditioner, swimmingpool=swimmingpool, cunstructionyear=cunstructionyear, price=price, area=area, dateposted=dateposted, propertytype=propertytype, description=description, mainimage=mainimage)
            postforsale.save()
            propertydata =  Postforselling.objects.filter(ownerid=request.user)
            #print(propertydata)
            propertydata = propertydata[len(propertydata)-1]
            propertytype2 = propertydata.propertytype
            #Postforselling(propertyid2 =  propertydata.propertyid)
            propertyid2 = propertydata.propertyid
            
            
            
            pid = Postforselling.objects.filter(propertyid = propertyid2)

            for file in image:
                imgesofproperties = Imgesofproperties(propertyid=pid[0], propertytype=propertytype2, image=file)
                imgesofproperties.save()
            
            messages.success(request, 'Your Post Has been posted successfully')
            return redirect('home')

    else:
         messages.error(request,'Please Login First')
         return redirect('home')
            
        

def saledetail(request, propertyid):
    propertydetails = Postforselling.objects.filter(propertyid = propertyid)
    propertydetails = propertydetails[0]
    email = propertydetails.ownerid
    personaldetails = Profiledetail.objects.filter(email=email)
    personaldetails = personaldetails[0]
    images = Imgesofproperties.objects.filter(propertyid = propertyid)
    allimg = []
    for i in images:
        img = i.image
        allimg.append(img)

    params = {'detail':propertydetails, 'images':allimg, 'personaldetails':personaldetails}
    return render(request, 'properties/saleviewdetail.html', params)

def rentdetail(request, propertyid):
    propertydetails = Postforrent.objects.filter(propertyid = propertyid)
    propertydetails = propertydetails[0]
    email = propertydetails.ownerid
    personaldetails = Profiledetail.objects.filter(email=email)
    personaldetails = personaldetails[0]
    images = Imgesofrentalproperties.objects.filter(propertyid = propertyid)
    allimg = []
    for i in images:
        img = i.image
        allimg.append(img)

    params = {'detail':propertydetails, 'images':allimg, 'personaldetails':personaldetails}
    return render(request, 'properties/rentviewdetail.html', params)

def employeedetail(request, employeeid):
    employee = Employees.objects.filter(employeeid = employeeid)
    employee = employee[0]
    params = {'employee':employee}
    return render(request, 'properties/employeedetail.html', params)


def roommatedetail(request, roommateprofileid):
    flatmate = Roommateprofile.objects.filter(roommateprofileid=roommateprofileid)
    flatmate = flatmate[0]

    roommateprofilepropimages = Roommateprofilepropimages.objects.filter(roommateprofileid=roommateprofileid)
    params = {'flatmate':flatmate, 'roommateprofilepropimages':roommateprofilepropimages}
    return render(request, 'properties/roommatedetail.html', params)

def payment(request, propertyid):
    
    if request.user.is_authenticated:
        pay=1

        if(pay):
            propertydetails = Postforselling.objects.filter(propertyid = propertyid)
            propertydetails = propertydetails[0]
            oldownerid = propertydetails.ownerid
            propertyid = propertydetails.propertyid
            address  = propertydetails.address
            address2 = propertydetails.address2
            country = propertydetails.country
            statename = propertydetails.statename
            city = propertydetails.city
            zipf = propertydetails.zipf
            cunstructionyear = propertydetails.cunstructionyear
            parking = propertydetails.parking
            furnshid  = propertydetails.furnshid
            ac = propertydetails.ac
            swimmingpool = propertydetails.swimmingpool
            description = propertydetails.description
            price = propertydetails.price
            area = propertydetails.area
            dateposted = propertydetails.dateposted
            propertytype = propertydetails.propertytype
            mainimage = propertydetails.mainimage
            solddate  = datetime.datetime.now()
            newownerid = request.user

            soldproperties = Soldproperties(oldownerid=str(oldownerid), propertyid=propertyid, address=address, address2=address2, country=country, statename=statename, city=city, zipf=zipf, cunstructionyear=cunstructionyear, parking=parking, furnshid=furnshid, ac=ac, swimmingpool=swimmingpool, description=description, price=price, area=area, dateposted=dateposted,propertytype=propertytype, mainimage=mainimage, solddate=solddate, newownerid=str(newownerid))
            soldproperties.save()
            propertydetails.delete()
            messages.success(request,'successfully Bought')
            return redirect('home')
    else:
        messages.error(request,'Please Login First')
        return redirect('home')

def postforrent(request):
    return render(request, 'properties/postforrent.html')
    

def hadlepostforrent(request):
    if request.user.is_authenticated:
        data = Profiledetail.objects.filter(email=request.user)
        if(len(data) < 1):
            messages.error(request, 'First Setup your Profile')
            return redirect('home')
    
        if request.method == 'POST' and User.is_authenticated:
            ownerid = request.user
            address = request.POST['address']
            address2 = request.POST['address2']
            country = request.POST['country']
            statename = request.POST['statename']
            city = request.POST['city']
            zipf = request.POST['zipf']
            parking= request.POST['parking']
            furnshid = request.POST['furnshid']
            airconditioner = request.POST['airconditioner']
            swimmingpool= request.POST['swimmingpool']
            cunstructionyear = request.POST['cunstructionyear']
            rentpermonth = request.POST['rent']
            area = request.POST['area']
            propertytype = request.POST['propertytype']
            description = request.POST['description']
            dateposted = datetime.datetime.now()
            mainimage = request.FILES['mainimage']
            image = request.FILES.getlist('images')
            maxallowedtanent = request.POST['maxtanent']
            livingtanent = request.POST['livingtanent']


            address = trimstr(address)
            address2 = trimstr(address2)
            description = trimstr(description)

            if(checkname(country)):
                pass
            else:
                messages.error(request, 'Country name Should be a valid string')
                return redirect('postforrent')
            
            if(checkname(statename)):
                pass
            else:
                messages.error(request, 'State name Should be a valid string')
                return redirect('postforrent')
            
            if(checkname(city)):
                pass
            else:
                messages.error(request, 'City name Should be a valid string')
                return redirect('postforrent')

            if(zipf.isnumeric() and len(zipf) > 5 and len(zipf) < 7):
                pass
            else: 
                messages.error(request, 'Pincode Should be a number and should be 6 digit')
                return redirect('postforrent')

            if(rentpermonth.isnumeric()):
                pass
            else: 
                messages.error(request, 'Price Should be a number')
                return redirect('postforrent')

            if(area.isnumeric()):
                pass
            else: 
                messages.error(request, 'area Should be a number')
                return redirect('postforrent')

            if(checkname(propertytype)):
                pass
            else:
                messages.error(request, 'Property type name Should be a valid string')
                return redirect('postforrent')
            
            if(maxallowedtanent.isnumeric()):
                pass
            else: 
                messages.error(request, 'maxallowedtanent Should be a number')
                return redirect('postforrent')
            
            if(livingtanent.isnumeric()):
                pass
            else: 
                messages.error(request, 'livingtanent Should be a number')
                return redirect('postforrent')
            

            postforrent = Postforrent(ownerid=ownerid, address=address, address2=address2, country=country, statename=statename, city=city, zipf=zipf, parking=parking, furnshid=furnshid, ac=airconditioner, swimmingpool=swimmingpool, cunstructionyear=cunstructionyear, rentpermonth=rentpermonth, area=area, dateposted=dateposted, propertytype=propertytype, description=description, mainimage=mainimage, maxallowedtanent=maxallowedtanent, livingtanent=livingtanent)
            postforrent.save()
            propertydata =  Postforrent.objects.filter(ownerid=request.user)
            #print(propertydata)
            propertydata = propertydata[len(propertydata)-1]
            propertytype2 = propertydata.propertytype
            #Postforselling(propertyid2 =  propertydata.propertyid)
            propertyid2 = propertydata.propertyid
            
           
            pid = Postforrent.objects.filter(propertyid = propertyid2)
           


            
            for file in image:
                imgesofrentalproperties = Imgesofrentalproperties(propertyid=pid[0], propertytype=propertytype2, image=file)
                imgesofrentalproperties.save()
            
            messages.success(request, 'Your Post Has been posted successfully')
            return redirect('home')

    else:
         messages.error(request,'Please Login First')
         return redirect('home')


def roommateprofile(request):
    return render(request, 'properties/roommateprofile.html')

def roommateprofilehandle(request):
    if request.user.is_authenticated:
        data = Roommateprofile.objects.filter(email=request.user)
        if request.method == 'POST' and User.is_authenticated and len(data) < 1:
            email = request.user
            prfilepicfile = request.FILES['prfilepicfile']
            firstname = request.POST['fname']
            middlename = request.POST['mname']
            lastname = request.POST['lname']
            dob  = request.POST['dob']
            gender = request.POST['gender']
            phone = request.POST['phone']
            address = request.POST['address']
            address2 = request.POST['address2']
            country = request.POST['country']
            statename = request.POST['statename']
            city = request.POST['city']
            zipf = request.POST['zipf']
            smoking = request.POST['smoking']
            alchohal = request.POST['alchohal']
            nonvegitarian = request.POST['nonvegitarian']
            earlybird  = request.POST['earlybird']
            bio = request.POST['bio']
            rent = request.POST['rent']
            area = request.POST['area']
            propertytype = request.POST['propertytype']
            mainimage = request.FILES['mainimage']
            maxtanent = request.POST['maxtanent']
            livingtanent = request.POST['livingtanent']
            expecteddescriptionofguy = request.POST['expecteddescriptionofguy']
            image = request.FILES.getlist('images')

            address = trimstr(address)
            address2 = trimstr(address2)
            bio = trimstr(bio)
            expecteddescriptionofguy = trimstr(expecteddescriptionofguy)

            if(checkname(firstname) and checkname(lastname) and checkname(middlename)):
                pass
            else:
                messages.error(request, 'name Should be a valid string')
                return redirect('roommateprofile')
            
            if(checkphone(phone)):
                pass
            else:
                messages.error(request, "Phone No's first digit should contain number between 7 to 9 and can have 11 digits also by including 0 at the starting and 12 digits also by including 91 at the starting ")
                return redirect('roommateprofile')

            if(checkname(country)):
                pass
            else:
                messages.error(request, 'Country name Should be a valid string')
                return redirect('roommateprofile')
            
            if(checkname(statename)):
                pass
            else:
                messages.error(request, 'State name Should be a valid string')
                return redirect('roommateprofile')
            
            if(checkname(city)):
                pass
            else:
                messages.error(request, 'City name Should be a valid string')
                return redirect('roommateprofile')

            if(zipf.isnumeric() and len(zipf) > 5 and len(zipf) < 7):
                pass
            else: 
                messages.error(request, 'Pincode Should be a number and should be 6 digit')
                return redirect('roommateprofile')

            if(rent.isnumeric()):
                pass
            else: 
                messages.error(request, 'Rent Should be a number')
                return redirect('roommateprofile')

            if(area.isnumeric()):
                pass
            else: 
                messages.error(request, 'area Should be a number')
                return redirect('roommateprofile')

            if(checkname(propertytype)):
                pass
            else:
                messages.error(request, 'Property type name Should be a valid string')
                return redirect('roommateprofile')
            
            if(maxtanent.isnumeric()):
                pass
            else: 
                messages.error(request, 'maxallowedtanent Should be a number')
                return redirect('roommateprofile')
            
            if(livingtanent.isnumeric()):
                pass
            else: 
                messages.error(request, 'livingtanent Should be a number')
                return redirect('roommateprofile')
            


            roommateprofile = Roommateprofile(email=email, prfilepicfile=prfilepicfile, firstname=firstname, middlename=middlename, lastname=lastname, dob=dob, gender=gender, phone=phone, address=address, address2=address2, country=country, statename=statename, city=city, zipf=zipf, smoking=smoking, alchohal=alchohal, nonvegitarian=nonvegitarian, earlybird=earlybird, bio=bio, rent=rent, area=area, propertytype=propertytype, mainimage=mainimage, maxtanent=maxtanent, livingtanent=livingtanent, expecteddescriptionofguy=expecteddescriptionofguy,)
            roommateprofile.save()

            roommateprofiledata = Roommateprofile.objects.filter(email=request.user)
            roommateprofiledata  = roommateprofiledata[len(roommateprofiledata)-1]
            propertytype2 = roommateprofiledata.propertytype

            roommateprofileid2 = roommateprofiledata.roommateprofileid

            roommatepid = Roommateprofile.objects.filter(roommateprofileid = roommateprofileid2)


            for file in image:
                roommateprofilepropimages = Roommateprofilepropimages(roommateprofileid=roommatepid[0], propertytype=propertytype2, image=file)
                roommateprofilepropimages.save()


            messages.success(request, 'Your Roommate Profile Has been created successfully')
            return redirect('home')
        else:
            messages.error(request,"You can't create multiple profile with single email")
            return redirect('home')



    else:
         messages.error(request,'Please Login First')
         return redirect('home')
    

def serviceproviderprofile(request):
    return render(request, 'properties/serviceproviderprofile.html')

def serviceproviderprofilehandle(request):
    if request.user.is_authenticated:
        data = Serviceproviderprofile.objects.filter(email=request.user)

        if request.method == 'POST' and User.is_authenticated and len(data) < 1:
            email  = request.user
            regno = request.POST['regno']
            name = request.POST['name']
            phone = request.POST['phone']
            estyear = request.POST['estyear']
            address = request.POST['address']
            address2 = request.POST['address2']
            country = request.POST['country']
            statename = request.POST['statename']
            city = request.POST['city']
            zipf = request.POST['zipf']
            bio = request.POST['bio']

            address = trimstr(address)
            address2 = trimstr(address2)
            bio = trimstr(bio)

            if(regno.isnumeric() and  len(regno) == 6 ):
                pass
            else: 
                messages.error(request, 'Registration No Should be a number and should be 6 digit')
                return redirect('serviceproviderprofile')

            if(checkname(name)):
                pass
            else:
                messages.error(request, 'Name Should be a valid string')
                return redirect('serviceproviderprofile')

            if(checkphone(phone)):
                pass
            else:
                messages.error(request, "Phone No's first digit should contain number between 7 to 9 and can have 11 digits also by including 0 at the starting and 12 digits also by including 91 at the starting ")
                return redirect('serviceproviderprofile')

            if(checkname(country)):
                pass
            else:
                messages.error(request, 'Country name Should be a valid string')
                return redirect('serviceproviderprofile')
            
            if(checkname(statename)):
                pass
            else:
                messages.error(request, 'State name Should be a valid string')
                return redirect('serviceproviderprofile')
            
            if(checkname(city)):
                pass
            else:
                messages.error(request, 'City name Should be a valid string')
                return redirect('serviceproviderprofile')

            if(zipf.isnumeric() and len(zipf) > 5 and len(zipf) < 7):
                pass
            else: 
                messages.error(request, 'Pincode Should be a number and should be 6 digit')
                return redirect('serviceproviderprofile')

            serviceproviderprofile = Serviceproviderprofile(email=email, regno=regno, name=name, phone=phone, estyear=estyear, address=address, address2=address2, country=country, statename=statename, city=city, zipf=zipf, bio=bio)
            serviceproviderprofile.save()
            messages.success(request, 'Your Service Provider Profile Has been created successfully Now You can Add Employees')
            return redirect('addemployee')
        else:
            messages.error(request,"You can't create multiple Service provider profile with single email")
            return redirect('home')
    else:
         messages.error(request,'Please Login First')
         return redirect('home')
    

    

def addemployee(request):
    return render(request, 'properties/addemployee.html')

def addemployeehandle(request):
    if request.user.is_authenticated:
        data = Serviceproviderprofile.objects.filter(email=request.user)
        if request.method == 'POST' and User.is_authenticated and len(data) > 0:
            serviceproviderprofileid = data[0]
            prfilepic = request.FILES['prfilepicfile']
            firstname = request.POST['fname']
            middlename = request.POST['mname']
            lastname = request.POST['lname']
            dob  = request.POST['dob']
            gender = request.POST['gender']
            phone = request.POST['phone']
            address = request.POST['address']
            address2 = request.POST['address2']
            country = request.POST['country']
            statename = request.POST['statename']
            city = request.POST['city']
            zipf = request.POST['zipf']
            bio = request.POST['bio']
            charges = request.POST['charges']
            worktype = request.POST['worktype']
            vacantstatus = request.POST['vacantstatus']

            address = trimstr(address)
            address2 = trimstr(address2)
            bio = trimstr(bio)

            if(checkname(firstname) and checkname(lastname) and checkname(middlename)):
                pass
            else:
                messages.error(request, 'name Should be a valid string')
                return redirect('addemployee')
            
            if(checkphone(phone)):
                pass
            else:
                messages.error(request, "Phone No's first digit should contain number between 7 to 9 and can have 11 digits also by including 0 at the starting and 12 digits also by including 91 at the starting ")
                return redirect('addemployee')

            if(checkname(country)):
                pass
            else:
                messages.error(request, 'Country name Should be a valid string')
                return redirect('addemployee')
            
            if(checkname(statename)):
                pass
            else:
                messages.error(request, 'State name Should be a valid string')
                return redirect('addemployee')
            
            if(checkname(city)):
                pass
            else:
                messages.error(request, 'City name Should be a valid string')
                return redirect('addemployee')

            if(zipf.isnumeric() and len(zipf) > 5 and len(zipf) < 7):
                pass
            else: 
                messages.error(request, 'Pincode Should be a number and should be 6 digit')
                return redirect('addemployee')
            
            if(checkname(worktype)):
                pass
            else:
                messages.error(request, 'worktype  Should be a valid string')
                return redirect('addemployee')
            
            if(charges.isnumeric()):
                pass
            else: 
                messages.error(request, 'charge Should be a number')
                return redirect('addemployee')
            

            employees = Employees(serviceproviderprofileid=serviceproviderprofileid, prfilepic=prfilepic, firstname=firstname, middlename=middlename, lastname=lastname, dob=dob, gender=gender, phone=phone, address=address, address2=address2, country=country, statename=statename, city=city, zipf=zipf, bio=bio, charges=charges, worktype=worktype, vacantstatus=vacantstatus)
            employees.save()
            messages.success(request, 'Your Have added an employee profile linked to your profile')
            return redirect('home')
        else:
            messages.error(request,'Please First create a service provider profile to register your service provider Company than you can add employees ')
            return redirect('serviceproviderprofile')

    else:
        messages.error(request,'Please Login First')
        return redirect('home')


def allsellingprop(request):
    allhomes = Postforselling.objects.all()
    allsellinghomes = []
    for home in allhomes:
        if(home.ownerid == request.user):
            pass
        else:
            allsellinghomes.append(home)
    params = {'allsellinghomes':allsellinghomes}
    return render(request, 'properties/allsellinghomes.html',params )

def allrentingprop(request):
    allhomes = Postforrent.objects.all()
    allrentinghomes = []
    for home in allhomes:
        if(home.ownerid == request.user):
            pass
        else:
            allrentinghomes.append(home)
    params = {'allrentinghomes':allrentinghomes}
    return render(request, 'properties/allrentinghomes.html',params )


def allemployee(request):
    allemployees = Employees.objects.all()
    params = {'allemployees':allemployees}
    return render(request, 'properties/allemployees.html',params )
    
def roommates(request):
    roommates = Roommateprofile.objects.all()
    allroommates = []
    for home in roommates:
        if(home.email == request.user):
            pass
        else:
            allroommates.append(home)
    params = {'allroommates':allroommates}
    return render(request, 'properties/allroommates.html',params )


def aboutyou(request):
    profiledetail = Profiledetail.objects.filter(email=request.user)
    
    prolen = len(profiledetail)
    if(len(profiledetail) > 0):
        profiledetail = profiledetail[0]

    sellingpsot = Postforselling.objects.filter(ownerid = request.user)
    sellen = len(sellingpsot)
    
    rentpost = Postforrent.objects.filter(ownerid = request.user)
    renlen = len(rentpost)

    flatemateprofile = Roommateprofile.objects.filter(email=request.user)
    flatelen = len(flatemateprofile)
    if(len(flatemateprofile) > 0):
        flatemateprofile = flatemateprofile[0]

    serviceproviderprofile = Serviceproviderprofile.objects.filter(email=request.user)
    serlen = len(serviceproviderprofile)
    if(len(serviceproviderprofile)):
        serviceproviderprofile = serviceproviderprofile[0]
        serviceproviderprofileid = serviceproviderprofile.serviceproviderprofileid
        employees = Employees.objects.filter(serviceproviderprofileid=serviceproviderprofileid)
        params ={'employees':employees}

    params = {'profiledetail':profiledetail, 'sellingpsot':sellingpsot, 'rentpost':rentpost, 'flatemateprofile':flatemateprofile, 'serviceproviderprofile':serviceproviderprofile, 'renlen':renlen, 'sellen':sellen, 'prolen':prolen, 'flatelen':flatelen, 'serlen':serlen }
    

    return render(request, 'properties/aboutyou.html', params)

def saledelete(request, propertyid):
    propertydetails = Postforselling.objects.filter(propertyid = propertyid)
    propertydetails.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('aboutyou')

def rentdelete(request, propertyid):
    propertydetails = Postforrent.objects.filter(propertyid = propertyid)
    propertydetails.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('aboutyou')