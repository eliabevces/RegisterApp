from django.urls import path
from RegisterApp import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.list_users, name='list_user'),
    path('new', views.add_user, name='add_user'),
    path('update/<int:id>', views.update_user, name='update_user'),
    path('delete/<int:id>', views.delete_user, name='delete_user'),
    # path('upload_file', views.upload_file, name='upload_file')
]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
