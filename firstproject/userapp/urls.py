from unicodedata import name
from django.urls import path
from .views import forms,modelform,form3, userreg,home,userreg2,viewdata,deletstud,updatestud,setcookie,getcookie
urlpatterns = [
     path('form/',forms,name='form1'),
    path('modelform/',modelform,name='form2'),
    path('form3/',form3,name='form3'),
    path('viewdata/',viewdata,name='view'),
    path('deletestud/<uid>',deletstud,name='delet'),
    path('updatestud/<uid>',updatestud,name='updat'),
    path('userreg/',userreg,name='userreg'),
    path('userreg2/',userreg2,name='userreg2'),
    path('home/', home,name='h'),
    path('setcookie/',setcookie,name='set'),
    path('getcookie/',getcookie,name='get'),
]