from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    #path('signup/', views.signup,name='signup'),
    #path('signin/', views.signin,name='signin'),
    path('choiceform/',views.choice_form,name='choice_view'),
    path('questionform/<int:id>',views.edit_question_form,name='question_view'),
    path('newquestion/',views.create_new_question,name='new_question_view'),
    path('',views.home, name = 'home'),
    path('<slug>/result/',views.results, name = 'result'),
    path('<slug>/',views.detail, name = 'detail'),
    path('<slug>/vote/', views.vote, name='pollvote'),   
    
    
]