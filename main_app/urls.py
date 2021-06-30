from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/', views.games_index, name='index'),
    path('systems/', views.systems_index, name='index'),
    path('stores/', views.stores_index, name='index'),
    
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('systems/create/', views.SystemCreate.as_view(), name='systems_create'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),

    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='games_detail'),

    path('systems/<int:pk>/update/', views.SystemUpdate.as_view(), name='systems_update'),
    path('systems/<int:pk>/delete/', views.SystemDelete.as_view(), name='systems_delete'),
    path('systems/<int:pk>/', views.SystemDetail.as_view(), name='systems_detail'),

    path('stores/<int:store_id>/', views.stores_detail, name='stores_detail'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
]
