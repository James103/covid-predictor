from django.contrib import admin
from django.urls import path, include
from core.views import CountryViewSet, EntryViewSet, FormulaViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
# router.register(r'entries', EntryViewSet)
# router.register(r'formulas', FormulaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]