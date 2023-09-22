from django.urls import path
from .views import TokenObtainView, SearchView, RequestCountView

urlpatterns = [
    path('token/', TokenObtainView.as_view(), name='token_obtain'),
    path('search/', SearchView.as_view(), name='search'),
    path('count/', RequestCountView.as_view(), name='count'),

]
