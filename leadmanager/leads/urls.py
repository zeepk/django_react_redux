from rest_framework import routers
from .api import (LeadViewSet, UserViewSet, EntryViewSet)

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/users', UserViewSet, 'users')
router.register('api/entries', EntryViewSet, 'entries')

urlpatterns = router.urls
