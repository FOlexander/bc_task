from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  path('', views.download_view, name='dload'),
                  path('info/', TemplateView.as_view(template_name='info.html'), name='info'),
                  path('media/<path:file_path>/', views.download_file, name='download_file'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
