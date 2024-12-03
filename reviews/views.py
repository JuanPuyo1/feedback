from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
# Create your views here.


# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()

#         return render(request, "reviews/review.html",{
#              "form":form
#         })

#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank_you")

#         return render(request, "reviews/review.html",{
#          "form":form
#         })

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    #post
    success_url = "/thank_you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

def review(request):
    if request.method == 'POST':
        #existing_data = Review.objects.get(pk=1)
        #extract data
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(user_name=form.cleaned_data["user_name"],
            #                 review_text=form.cleaned_data["review_text"],
            #                 rating=form.cleaned_data["rating"])
            #review.save()

            #now can i use the model form method
            form.save()
            return HttpResponseRedirect("/thank_you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html",{
         "form":form
    })
    

def thank_you(request):
    return render(request,"reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["message"] = "This works"
        return context
    

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model= Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

# class DetailReview(TemplateView):
#     template_name = "reviews/detail_review.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs) 
#         review_id = kwargs["id"]  
#         select_review = Review.objects.get(pk=review_id)
#         context["review"] = select_review
#         return context

class DetailReview(DetailView):
    template_name = "reviews/detail_review.html"
    model = Review