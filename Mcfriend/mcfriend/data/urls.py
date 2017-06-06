from django.conf.urls import url,include
from . import views
app_name = 'data'
urlpatterns = [
	url(r'^$',views.profile,name='profile'),
	url(r'^list/$',views.userlist,name='userlist'),
	url(r'^(?P<user_username>[a-z]*[0-9]*)/$',views.user,name='user'),
]