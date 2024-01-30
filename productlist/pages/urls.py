
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django_distill import distill_path

app_name = 'pages'

urlpatterns = [
	# main view
	distill_path('', views.index, name='home'),
	distill_path('delete_product/<int:id>', views.delete_product, name='delete_product'),
	distill_path('mark_product/<int:id>', views.mark_product, name='mark_product'),
	distill_path('add_product', views.add_product, name='add_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)