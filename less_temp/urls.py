"""less_temp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include

from main.views import UserLogin, profile, AdvLogoutView, ChangeAdvUserView

from main.views import register_user, new_form
from django.views.generic import TemplateView

urlpatterns = [
    # 13.04
    path('dinamo/', include('dinamo.urls')),
    path('show_dict/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('',include('movies.urls')),

    path('accounts/login/', UserLogin.as_view(), name='login'),
    path('accounts/logout/', AdvLogoutView, name='logout'),
    path('accounts/profile/', profile, name='profile'),
# регистрация
    path('accounts/register/',register_user, name='register'),
    path('accounts/register/done/',TemplateView.as_view(template_name='auth/register_done.html'), name='register_done'),

    path('accounts/profile/update/', ChangeAdvUserView.as_view(), name='user_update'),
# изменить пароль
    path('accounts/profile/change_pass', PasswordChangeView.as_view(template_name='auth/change_pass.html'), name='password_change'),
# уведомление о смене пароля
    path('accounts/profile/change_pass/change_done', PasswordChangeView.as_view(template_name='auth/change_done.html'), name='password_change_done'),
    path('prod/', include('main.urls')),
    # path('', include('movies.urls')),
    path('new_form/', new_form, name='new_form'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
