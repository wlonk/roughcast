"""roughcast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from django_registration.backends.activation.views import RegistrationView

from . import views
from .forms import CustomAuthenticationForm, CustomRegistrationForm
from .routers import ExtensibleDefaultRouter

router = ExtensibleDefaultRouter()
router.non_resource_register("login", views.LoginView.as_view())
router.non_resource_register("logout", views.LogoutView.as_view())
router.register("user", views.UserViewSet)
router.register("team", views.TeamViewSet)
router.register("teammembership", views.TeamMembershipViewSet)
router.register("game", views.GameViewSet)
router.register("version", views.VersionViewSet)
router.register("attached_file", views.AttachedFileViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/login/",
        LoginView.as_view(authentication_form=CustomAuthenticationForm),
        name="login",
    ),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=CustomRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include(router.urls)),
    re_path(
        "^(?!accounts|api|static|media|fonts)",
        TemplateView.as_view(template_name="base.html"),
        name="root",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.FONT_URL, document_root=settings.FONT_ROOT)
