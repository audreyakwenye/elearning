from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^liste/$', views.liste_events, name='liste_events'),
    url(r'^listes/$', views.ListEvents.as_view(paginate_by=5), name='listes_events'),
    url(r'^(?P<pk>\d+)/detail/$', views.DetailEvents.as_view(), name='detail_event'),
    url(r'^listes/(?P<champ>[\w-]+)/(?P<terme>[\w-]+)/$', views.ListEvents.as_view(paginate_by=5), name='listes_events_filter'),
    url(r'^create/$', views.create_event, name='create_event'),
    url(r'^contact/(?P<pk>\d+)/$', views.ContactDetailView.as_view(), name='contact_detail'),
    url(r'^(\d+)/guest/(\d+)/delete/$', views.delete_guest, name='delete_guest'),
    url(r'^(\d+)/delete/$', views.delete_event, name='delete_event'),
    url(r'^(\d+)/update/$', views.update_event, name='update_event'),
    url(r'^invitation/liste/$', views.InvitationListView.as_view(), name='invitation_list'),
    url(r'^invitation/$', views.InvitationCreateView.as_view(), name='create_invitation'),
]
