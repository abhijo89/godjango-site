from django.conf.urls import patterns, url
from django.views.generic import DetailView

from episode.models import Video

urlpatterns = patterns(
    '',
    url(
        r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$',
        DetailView.as_view(
            template_name="episode/video.html", context_object_name="video",
            model=Video), name="episode"),
)
