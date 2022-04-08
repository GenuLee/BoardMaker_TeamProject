from django.urls import URLPattern, path
from blog.views import index

app_name = "blog"
urlpatterns = [
  # index
  path('', index, name = 'index'),
  # about me
  #path('aboutme/', aboutMe, name = 'aboutMe')
]