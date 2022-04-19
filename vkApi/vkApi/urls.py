from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/asd', admin.site.urls),
    path('', include('mari.urls'))
]
