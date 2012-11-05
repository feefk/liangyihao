from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('home.views',
   (r"^$", "main"),
   (r"(?P<page>.*)/$", "main"),
   #(r"about/$", "about"),
   #(r"contact/$", "contact"),
   #(r"home/$", "home"),
)
