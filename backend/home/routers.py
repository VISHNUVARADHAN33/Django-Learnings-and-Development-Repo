from rest_framework.routers import DefaultRouter
from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename='products')
#print(router.urls)                                                         Reson for the useage is you can see what are the urls is generated on the urls
urlpatterns = router.urls