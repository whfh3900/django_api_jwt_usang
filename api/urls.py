from django.urls import path
from .views import *

urlpatterns = [
    path('token/', TokenObtainView.as_view(), name='token_obtain'),
    path('search/', SearchView.as_view(), name='search'),
    path('count/', RequestCountView.as_view(), name='count'),
    path('download/', DownloadView.as_view(), name='download'),

]
