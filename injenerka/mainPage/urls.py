from rest_framework import routers
from .api import CustomerViewSet, CartViewSet, CartProductViewSet, ProductViewSet, OrderViewSet, ProductOrderViewSet , ImgProductViewSet, LoginViewSet, TableOrdersViewSet, RatingViewSet


router = routers.DefaultRouter() # роутер по умолчанию


router.register('api/customer', CustomerViewSet, 'customer') # регаем api.url с QuerySet

router.register('api/cartproduct', CartProductViewSet, 'cartproduct') # регаем api.url с QuerySet

router.register('api/cart', CartViewSet, 'cart') # регаем api.url с QuerySet

router.register('api/product', ProductViewSet, 'product') # регаем api.url с QuerySet

router.register('api/order', OrderViewSet, 'order') # регаем api.url с QuerySet

router.register('api/productorder', ProductOrderViewSet, 'productorder') # регаем api.url с QuerySet

router.register('api/imgproduct', ImgProductViewSet, 'imgproduct') # регаем api.url с QuerySet

router.register('api/login', LoginViewSet, 'login') # регаем api.url с QuerySet

router.register('api/tableorders', TableOrdersViewSet, 'tableorders') # регаем api.url с QuerySet

router.register('api/rating', RatingViewSet, 'rating') # регаем api.url с QuerySet


urlpatterns = router.urls