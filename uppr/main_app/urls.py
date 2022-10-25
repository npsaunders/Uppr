from django.urls import path, include

from . import views

# *****   VIEW  => urls.py + views.py => in Model/View/Template ******
# The urls.py is the first stop after a user clicks on a button/enters a url.
# Each defined path has an associated view which then handles the actual routing,
# dispatches for querying the database, and finally rendering a html page.
# the format is path('url',views._____, name='')
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #-------- Questions -------
    path('questions/', views.questions_index, name='index'),
    path('questions/<int:question_id>/', views.questions_detail, name='detail'),
    path('questions/create/',views.QuestionCreate.as_view(),name = 'questions_create'),
    # <int:pk>  assure that our primary key is an integer
    path('questions/<int:pk>/update/', views.QuestionUpdate.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete/', views.QuestionDelete.as_view(), name='questions_delete'),
    # ------ Categories --------    
    path('categories/', views.CategoryList.as_view(), name='categories_index'),
    #path('categories/', views.categories_index, name='categories_index'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='categories_detail'),
    path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='categories_delete'),
    # path('questions/<int:question_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
    # ----------
    path('interview_time/',views.interview_time, name="interview_time"),
    # authentication/authorization paths
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]