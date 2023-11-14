from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DummyGameView, GameViewSet, MinimumRequirementsViewSet, RecommendedRequirementsViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'minimum-requirements', MinimumRequirementsViewSet)
router.register(r'recommended-requirements', RecommendedRequirementsViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    # path('dummygame', DummyGameView.as_view()),
    path('', include(router.urls)),
]
