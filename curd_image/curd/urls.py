from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('display',views.display,name='display'),
    path('update/<int:edit_id>', views.update,name='update'),
    path('delete/<int:delete_id>', views.delete,name='delete'),
    path('preview/<int:preview_id>',views.preview,name='preview'),
    path('aboutUs',views.aboutUs,name='aboutUs'),
]
