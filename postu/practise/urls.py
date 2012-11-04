from django.conf.urls import patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('practise.views',
   (r'^upload_img/$', 'upload_img'),
   (r'^upload/$', 'upload'),
   (r'^bootstrap/$', 'bootStrap'),
)
