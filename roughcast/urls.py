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
from rest_framework.routers import DefaultRouter

from . import views

# @@@ WEBSOCKETS
# from .routing import websockets

router = DefaultRouter()
router.register("accounts", views.AccountsView, basename="accounts")
router.register("users", views.UserViewSet)
router.register(
    "notifications", views.InAppNotificationViewSet, basename="notifications"
)
router.register("subscriptions", views.SubscriptionViewSet, basename="subscriptions")
router.register("teams", views.TeamViewSet)
router.register("teammemberships", views.TeamMembershipViewSet)
router.register("invites", views.TeamInviteViewSet, basename="invites")
router.register("games", views.GameViewSet)
router.register("versions", views.VersionViewSet, basename="versions")
router.register("attached_files", views.AttachedFileViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        "^(?!api|static|media)",
        TemplateView.as_view(template_name="base.html"),
        name="root",
    ),
    # After the root template, so that 404s don't generate client
    # template pages:
    path("api/", include(router.urls)),
    # Just so the email can generate a reverse URL:
    path(
        "change/<uidb64>/<token>",
        TemplateView.as_view(template_name="base.html"),
        name="password_reset_confirm",
    ),
]
# @@@ WEBSOCKETS
# ] + websockets.routes

if settings.DEBUG:  # pragma: nocover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
