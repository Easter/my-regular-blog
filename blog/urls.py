from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.IndexView.as_view(),name="index"),
    path('blog/<int:pk>/',views.detail,name="detail"),
    path('archives/<int:year>/<int:month>/',views.ArchivesView.as_view(),name="archives"),
    # path('archives/<int:year>/<int:month>/',views.archives,name="archives"),
    path('category/<int:pk>/',views.CategoryView.as_view(),name="category"),
    # path('category/<int:pk>/',views.category,name="category")
    path('tag/<int:pk>/',views.TagView.as_view(),name="tag")
]