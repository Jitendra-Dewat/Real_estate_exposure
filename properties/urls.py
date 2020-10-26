from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postforsale',views.postforsale, name='postforsale' ),
    path('hadlepostforsale',views.hadlepostforsale, name="hadlepostforsale"),
    path('properties/saledetail/<int:propertyid>', views.saledetail, name="saledetail"),
    path('properties/payment/<int:propertyid>', views.payment, name="payment"),
    path('properties/saledetail/payment/<int:propertyid>', views.payment, name="payment"),
    path('postforrent',views.postforrent, name='postforrent'),
    path('hadlepostforrent',views.hadlepostforrent, name="hadlepostforrent"),
    path('roommateprofile', views.roommateprofile, name="roommateprofile"),
    path('roommateprofilehandle', views.roommateprofilehandle, name="roommateprofilehandle"),
    path('serviceproviderprofile', views.serviceproviderprofile, name="serviceproviderprofile"),
    path('serviceproviderprofilehandle', views.serviceproviderprofilehandle, name="serviceproviderprofilehandle"),
    path('addemployee', views.addemployee, name="addemployee"),
    path('addemployeehandle', views.addemployeehandle, name="addemployeehandle"),
    path('allsellingprop', views.allsellingprop, name="allsellingprop"),
    path('properties/rentdetail/<int:propertyid>', views.rentdetail, name="rentdetail"),
    path('allrentingprop', views.allrentingprop, name="allrentingprop"),
    path('allemployee', views.allemployee, name="allemployee"),
    path('properties/employeedetail/<int:employeeid>', views.employeedetail, name="employeedetail"),
    path('roommates', views.roommates, name="roommates"),
    path('properties/roommatedetail/<int:roommateprofileid>', views.roommatedetail, name="roommatedetail"),
    path('aboutyou', views.aboutyou, name="aboutyou"),
    path('properties/saledelete/<int:propertyid>', views.saledelete, name="saledelete"),
    path('properties/rentdelete/<int:propertyid>', views.rentdelete, name="rentdelete")
    

    

    
]