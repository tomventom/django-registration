from django.conf.urls import url
from django.contrib.auth.views import login, logout

from accounts.views import HomeView, AboutView, BlogView, RegisterView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = "home"),
    url(r'^about/$', AboutView.as_view(), name = "about"),
    url(r'^blog/$', BlogView.as_view(), name = "blog"),
    url(r'^register/$', RegisterView.as_view(), name = "register"),
    url(r'^login/$', login, { "template_name": "accounts/login.html" }, name = "login"),
    url(r'^logout/$', logout, { "next_page": "/account/"}),
]
