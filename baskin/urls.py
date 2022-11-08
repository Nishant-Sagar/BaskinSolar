from django.urls import URLPattern, path
from . import views
# from 'baskin' import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('form', views.form, name = 'form'),
    path('faq', views.faq, name = 'faq'),
    path('contact', views.contact, name = 'contact'),
    path('services', views.services, name = 'services'),
    path('commercial', views.commercial, name = 'commercial'),
    path('residential', views.residential, name = 'residential'),
    path('whysolar', views.whysolar, name = 'whysolar'),
    path('register', views.register, name = 'register'),
    path('gogreen', views.gogreen, name = 'gogreen'),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()