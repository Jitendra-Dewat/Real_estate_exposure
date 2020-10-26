from django.contrib import admin
from properties.models import Postforselling, Imgesofproperties, Soldproperties, Postforrent, Imgesofrentalproperties, Serviceproviderprofile, Employees, Roommateprofile, Roommateprofilepropimages


# Register your models here.
admin.site.register(Postforselling)
admin.site.register(Imgesofproperties)
admin.site.register(Soldproperties)
admin.site.register(Postforrent)
admin.site.register(Imgesofrentalproperties)
admin.site.register(Roommateprofile)
admin.site.register(Roommateprofilepropimages)
admin.site.register(Serviceproviderprofile)
admin.site.register(Employees)




