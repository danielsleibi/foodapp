from django.urls import path
from .views import index, details, create_item, update_item, delete_item
app_name = 'food'
urlpatterns = [
    path('', index, name='food'),
    path('<int:item_id>/', details, name='details'),
    path('add/', create_item, name='create-item'),
    path('edit/<int:item_id>/', update_item, name='edit-item'),
    path('remove/<int:item_id>/', delete_item, name='remove-item'),
]
