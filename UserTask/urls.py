from django.urls import path
from UserTask import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('index',views.index, name='index'),
    path('register',views.register, name='register'),
    path('profile',views.profile,name='profile'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    path('change_password/<int:id>',views.change_password, name='change_password'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)