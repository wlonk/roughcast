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
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView

from . import views
from .routers import ExtensibleDefaultRouter

router = ExtensibleDefaultRouter()
router.non_resource_register("register", views.RegisterView.as_view())
router.non_resource_register("login", views.LoginView.as_view())
router.non_resource_register("logout", views.LogoutView.as_view())
router.register("user", views.UserViewSet)
router.register(
    "notifications", views.InAppNotificationViewSet, basename="notifications"
)
router.register("team", views.TeamViewSet)
router.register("teammembership", views.TeamMembershipViewSet)
router.register("game", views.GameViewSet)
router.register("version", views.VersionViewSet)
router.register("attached_file", views.AttachedFileViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    re_path(
        "^(?!api|static|media|fonts)",
        TemplateView.as_view(template_name="base.html"),
        name="root",
    ),
    path(
        "/change/<uidb64>/<token>",
        TemplateView.as_view(template_name="base.html"),
        name="password_reset_confirm",
    ),
]

if settings.DEBUG:  # pragma: nocover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.FONT_URL, document_root=settings.FONT_ROOT)
