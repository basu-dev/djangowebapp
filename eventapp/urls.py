from django.urls import path
from eventapp import views

app_name = "gallery"

urlpatterns = [
    path("", views.index, name="upcoming"),
    path("post/", views.post, name="eventpost"),
    path("event_detail/<int:id>/", views.event_detail, name="eventdetail"),
    path("upcomingevents/", views.upcoming_events, name="upcoming"),
    path("completedevents/", views.completed_events, name="completed"),
    path("delete/<int:id>/", views.deletepost, name="delete"),
    path("eventapp/add_members/<int:id>", views.add_members, name="addmember"),
    path("eventapp/add_member/<int:pid>/<int:mid>", views.add_member, name="addmember"),
]

