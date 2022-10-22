from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Question

# *****   VIEW  => urls.py + views.py => in Model/View/Template ******
# The views.py is the second stop after a user clicks on a button/enters a url.
# The urls.py paths send the request along to here. 
# 
# *** Home page ( render home.html )
def home(request):
    return render(request, "home.html")

# *** About page ( render about.html )
def about(request):
    return render(request, "about.html")

# *** INTERVIEW_TIME html page; pass in all questions; render the interview_time page ***
def interview_time(request):
    questions = Question.objects.all()
    return render(request,"interview_time.html", {"questions": questions})

# ----------------- QUESTION FUNCTIONS -------------------

# *** QUESTION_INDEX  html page; pass in all questions; Render all questions ***
def questions_index(request):
    questions = Question.objects.all()
    return render(request, "questions/index.html", {"questions": questions})

# *** QUESTION -> DETAIL  {pass a specific question to the detail.html page
# based on the question_id} render detail.html page ***
def questions_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request,"questions/detail.html",{"question": question,})

# --------------------- SIGN UP NEW USER  ---------------------------

# Function for creating a new user
def signup(request):
    # Initialize the error_message as an empty string
    error_message = ""
    # do the following if submitting a registration form
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            # goto index page so the rest of the code is skipped
            return redirect("index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)

#----------------- CLASS BASED VIEWS   'C'reate, 'U'pdate, & 'D'elete  ---------

class QuestionCreate(CreateView):
    model = Question
    fields = ['user_question','answer1', 'answer2','answer3','answer4','time_allowed']
    success_url = "/questions/"

    # This inherited method is called when a
    # valid question form is being submitted
    # def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        # form.instance.user = self.request.user  # form.instance is the question
        # Let the CreateView do its job as usual
        # return super().form_valid(form)
        
class QuestionUpdate(UpdateView):
    model = Question
    fields = ['user_question']


class QuestionDelete(DeleteView):
    model = Question
    success_url = "/questions/"
