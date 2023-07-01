
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'home'),
    path('<int:pk>/<int:page>',views.index_filter,name = "filter"),
    # path('pagination', views.pagination_ajax,name='pagination_ajax'),
]
