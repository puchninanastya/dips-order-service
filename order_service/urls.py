from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'orders/(?P<order_id>\d+)/courses', views.OrderCourseViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^orders/?P<order_id>.+)/courses$', views.OrderCourseList.as_view(), name='order-course-list'),
]
