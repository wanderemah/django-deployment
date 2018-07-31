from django.conf.urls import url
from . import views


app_name = 'isaac'

urlpatterns = [
    url(r'^register',views.register, name='register'),
]