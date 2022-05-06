
from .views import Views
from rest_framework.routers import SimpleRouter



router = SimpleRouter(trailing_slash=False)
router.register("bases", Views)

urlpatterns = router.urls
