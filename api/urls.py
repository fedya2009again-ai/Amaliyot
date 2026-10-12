from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, CategoryViewSet, JobViewSet, register

router = DefaultRouter()

router.register("category", CategoryViewSet, basename="category")
router.register("job", JobViewSet, basename="job")
router.register("comment", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", register, name="register"),
    path("api-auth/", include("rest_framework.urls")),
    path("category/<int:category_id>/jobs/", JobViewSet.as_view({"get": "list"}), name="jobviewset"),
]