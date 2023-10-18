from django.contrib import admin
from django.urls import path

def redirect_view(request):
  return HttpResponseRedirect('/admin/')

urlpatterns = [
    # path('', redirect_view ),
    # path('admin/', admin.site.urls),
    path('', admin.site.urls),
]
