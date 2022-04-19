from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/as123123d', admin.site.urls),
    path('', include('mari.urls'))
]
