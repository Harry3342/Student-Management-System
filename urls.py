from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Example path, adjust as necessary
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
