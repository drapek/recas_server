from django.conf.urls import url, include

from users import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='panel_index'),
    url(r'login/$', views.LoginView.as_view(), name='panel_login'),
    url(r'logout/$', views.LogoutView.as_view(), name='panel_logout'),
]
