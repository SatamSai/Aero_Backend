from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path as url


urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('event/',views.EventList.as_view()),
    path('eveimg/<id>',views.EventImgList.as_view()),
    path('competition/',views.CompetitionList.as_view()),
    path('compimg/<id>',views.CompetitionImgList.as_view()),
    path('team/',views.TeamMemberList.as_view()),
    path('post/',views.PostList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)