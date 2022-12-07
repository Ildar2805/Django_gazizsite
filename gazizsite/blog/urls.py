from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import *

urlpatterns = [
    path('', cache_page(30)(Posts.as_view()), name='posts'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>', cache_page(60)(ShowPost.as_view()), name='post'),
    path('category/<slug:cat_slug>', cache_page(30)(PostCategory.as_view()), name='category'),
]