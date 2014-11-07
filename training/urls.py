from django.conf.urls import patterns, include, url

urlpatterns = patterns('training.views',
    # Examples:
    url(r'^home$', 'home_page', name='home'),
    url(r'^question$', 'get_question', name="question"),
    url(r'^question/answer$', 'answer_question', name="answer_question"),
    url(r'^result$', 'get_result', name="result"),
    url(r'^total$', 'response_total', name="total"),
)