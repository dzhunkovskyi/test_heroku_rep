from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^(?P<page_number>\d+)/$', views.main, name='main'),
    url(r'^login/', views.login_func, name='login_func'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^$', views.main, name='main'),
]
