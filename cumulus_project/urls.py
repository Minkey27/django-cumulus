from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

from photos.models import Photo

admin.autodiscover()

photo_dict = {
    'queryset': Photo.objects.all()
}

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^photos/$', 'django.views.generic.list_detail.object_list', photo_dict),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )