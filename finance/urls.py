from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'categorias', 'CategoryViewSet', basename= 'transaction')

urlpatterns = router.urls