from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('weather/', include('weather.urls')),
    path('list/', include('to_do_list.urls')),
]
