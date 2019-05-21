__author__ = 'Kushan'




from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^get',views.get,name='get'),
    url(r'^loginindex',views.loginindex,name='loginindex'),
    url(r'^regindex',views.regindex,name='regindex'),
    url(r'^regdata',views.regdata,name='regdata'),
    url(r'^feedback',views.feedback,name='feedback'),
    #url(r'^logindata',views.logindata,name='logindata'),
    url(r'^contentpage',views.contentpage,name='contentpage'),
    url(r'^showpage',views.showpage,name='showpage'),
    url(r'^resume',views.resume,name='resume')
]