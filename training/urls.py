from django.conf.urls import patterns, include, url

urlpatterns = patterns('training.views',
    # Examples:
    url(r'^home$', 'training_home', name='training_home'),
)
