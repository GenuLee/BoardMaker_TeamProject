from django.urls import URLPattern, path
from blog.views import index, portfolio

app_name = "blog"
urlpatterns = [
  # index
  path('', index, name = 'index'),
  path('portfolio/', portfolio, name = 'portfolio'),
  # about me
  #path('aboutme/', aboutMe, name = 'aboutMe')
]