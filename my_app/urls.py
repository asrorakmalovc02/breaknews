from django.urls import path
from .views import HomePageView,category,post_detail
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	path('',HomePageView.as_view(),name='index'),
	path('category/<int:category_id>/',views.category,name="category"),
	path('post_detail/<int:news_id>/',views.post_detail,name="post_detail")



]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)

