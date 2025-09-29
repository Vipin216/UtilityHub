from django.shortcuts import render
from .models import GPA
from .forms import GPAForm


from django.shortcuts import render

def cgpa_calculator(request):
    cgpa = None  # default (before form submit)

    if request.method == "POST":
        credits_list = request.POST.getlist("credits")
        grades_list = request.POST.getlist("grades")

        total_credits = 0
        weighted_sum = 0

        for c, g in zip(credits_list, grades_list):
            try:
                c = float(c)
                g = float(g)  # assuming grade points like 10, 9, 8
                total_credits += c
                weighted_sum += c * g
            except ValueError:
                pass  # skip if input invalid

        if total_credits > 0:
            cgpa = round(weighted_sum / total_credits, 2)

    return render(request, "page1.html", {"cgpa": cgpa})

# Create your views here.
