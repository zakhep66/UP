from rest_framework import routers

from .api import CustomerViewSet, CartViewSet, CartProductViewSet, ProductViewSet, OrderViewSet, ProductOrderViewSet, \
    ImgProductViewSet, LoginViewSet, TableOrdersViewSet, RatingViewSet

router = routers.DefaultRouter()  # роутер по умолчанию

router.register('api/customer', CustomerViewSet, 'customer')
router.register('api/cartproduct', CartProductViewSet, 'cartproduct')
router.register('api/cart', CartViewSet, 'cart')
router.register('api/product', ProductViewSet, 'product')
router.register('api/order', OrderViewSet, 'order')
router.register('api/productorder', ProductOrderViewSet, 'productorder')
router.register('api/imgproduct', ImgProductViewSet, 'imgproduct')
router.register('api/login', LoginViewSet, 'login')
router.register('api/tableorders', TableOrdersViewSet, 'tableorders')
router.register('api/rating', RatingViewSet, 'rating')




urlpatterns = router.urls
