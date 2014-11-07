from django.conf.urls import patterns, include, url

urlpatterns = patterns('exam.views',
    # Examples:
    url(r'^home$', 'exam_home', name='exam_home'),
    url(r'^question$', 'get_question', name="question"),
    url(r'^question/answer$', 'answer_question', name="answer_question"),
    url(r'^result$', 'get_result', name="result"),
    url(r'^total$', 'response_total', name="total"),
)
