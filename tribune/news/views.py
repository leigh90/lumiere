from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from django import forms
from django.http import HttpResponse


from cloudinary.forms import cl_init_js_callbacks  
from .models import Image
from .forms import ImageForm


def upload(request):
    context = dict(backend_form=ImageForm())
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'add_image.html', context)

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def news_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def archives(request, past_date):
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    day = convert_dates(date)
    html = f'''
    <html>
        <body>
            <h1> News for {day} {date.day}-{date.month}-{date.year} </h1>
        </body>
    </html>
    '''
    print(date)
    print(day)
    return HttpResponse(html)


