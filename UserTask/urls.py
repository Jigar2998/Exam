from django.urls import path
from UserTask import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.login, name='login'),
    path('index',views.index, name='index'),
    path('register',views.register, name='register')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)