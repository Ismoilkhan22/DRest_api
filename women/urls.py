from django.urls import path

from women.views import WomenAPIView

urlpatterns = [
    path('api/v1/', WomenAPIView.as_view())

]
