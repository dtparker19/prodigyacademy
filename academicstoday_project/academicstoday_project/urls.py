from django.urls import include, re_path, path
from django.contrib import admin
from django.conf.urls.static import static, settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'academicstoday_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path(r'^admin/', admin.site.urls),
               
    # This regex makes the default URL for the website to launch this view.
    re_path(r'', include('landpage.urls')),
    re_path(r'^registration/', include('registration.urls')),
    re_path(r'^login/', include('login.urls')),
    re_path(r'^account/', include('account.urls')),
    re_path(r'^registrar/', include('registrar.urls')),
    re_path(r'^student/', include('student.urls')),
    re_path(r'^teacher/', include('teacher.urls')),
    re_path(r'^publisher/', include('publisher.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
