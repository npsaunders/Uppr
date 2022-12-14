from django.urls import path, include

from . import views

# *****   VIEW  => urls.py + views.py => in Model/View/Template ******
# The urls.py is the first stop after a user clicks on a button/enters a url.
# Each defined path has an associated view which then handles the actual routing,
# dispatches for querying the database, and finally rendering a html page.
# the format is path('url',views._____, name='')
urlpatterns = [
    path('', views.home, name='home'),
    #-------- Questions -------
    path('questions/', views.questions_index, name='index'),
    path('questions/<int:question_id>/', views.questions_detail, name='detail'),
    path('questions/create/',views.QuestionCreate.as_view(),name = 'questions_create'),
    # <int:pk>  assure that our primary key is an integer
    path('questions/<int:pk>/update/', views.QuestionUpdate.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete/', views.QuestionDelete.as_view(), name='questions_delete'),
    # ------ User Profile --------    
    path('profiles/', views.ProfileList.as_view(), name='profiles_index'),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profiles_detail'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profiles_delete'),
    # ----------
    path('interview_time/',views.interview_time, name="interview_time"),
    # authentication/authorization paths
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]