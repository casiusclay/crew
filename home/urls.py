from django.conf.urls import url
from home.views import HomeView, ApplyCreateView, PostApplyListView, UserProfileView
import home.views as views

app_name='home'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', HomeView.as_view(), name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'apply/(?P<pk>\d+)/$', ApplyCreateView.as_view(), name='apply'),
    url(r'postapplys/(?P<pk>\d+)/$', PostApplyListView.as_view(), name='postapplys'),
    url(r'user/(?P<pk>\d+)/$', UserProfileView.as_view(), name='applicant-profile'),
]