from django.urls import include, path
from rest_framework.decorators import action
from django.contrib import admin
from rest_framework import routers
from backend import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Incluye las URLs de autenticación de DRF
    path('api/cards/<str:type>/', views.DataCardApiView.as_view(), name='cards'),
    path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
    path('send_email/', views.send_emails.as_view(), name='email'),
    path('interfaz/', include(router.urls)),  # Incluye las URLs generadas por el router (si tienes otros ViewSets)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)