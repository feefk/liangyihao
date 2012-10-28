from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('home.urls')),
    (r'^home/$', include('home.urls')),
    (r'^blog/$', include('blog.urls')),
    (r'^practise/', include('practise.urls')),

    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATICFILES_ROOT}),
  
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATICFILES_ROOT}),
    # Examples:
    # url(r'^$', 'postu.views.home', name='home'),
    # url(r'^postu/', include('postu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
