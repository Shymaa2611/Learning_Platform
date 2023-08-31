
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from pages import views
urlpatterns = [
    path('google_bard_response/', views.google_bard_response),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('pages.urls')) ,
    path('accounts/',include('accounts.urls')) 
]
# Media setting #
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header='HELp'

