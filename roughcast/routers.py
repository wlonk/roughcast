from collections import OrderedDict

from django.urls import path
from rest_framework import routers


class ExtensibleDefaultRouter(routers.DefaultRouter):
    non_resource_registry = []

    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, _, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        for name, _ in self.non_resource_registry:
            api_root_dict[name] = name

        return self.APIRootView.as_view(api_root_dict=api_root_dict)

    def non_resource_register(self, name, view):
        self.non_resource_registry.append((name, view))
        # invalidate the urls cache
        if hasattr(self, "_urls"):  # pragma: nocover
            del self._urls

    def get_urls(self):
        ret = super().get_urls()
        for name, view in self.non_resource_registry:
            regex = f"{name}/"
            ret.append(path(regex, view, name=name))

        return ret
