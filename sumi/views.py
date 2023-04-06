from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import BookForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect

# Create your views here.
def home(request):
        template = loader.get_template('sumi.html')
        return HttpResponse(template.render())
def book(request):
        name= request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        number = request.POST.get('number')
        start = request.POST.get('start')
        destination = request.POST.get('destination')
        customerrequest = request.POST.get('request')
        submitbutton= request.POST.get('Submit')
        if(request.method == 'POST'):
                form = BookForm()
                
                context= {'name': name,'submitbutton': submitbutton, 'email': email, 'country':country, 'phone': phone,
                                'startdate': startdate, 'enddate': enddate, 'number': number, 'customerrequest':customerrequest
                                }
               
                email = EmailMultiAlternatives(
                'Request for Travel Agency Services',
                "",
                settings.EMAIL_HOST_USER,
                ['joshuashalla1@gmail.com'],
                reply_to=[f'{email}, '],
                headers={'Message-ID': 'foo'},
                )
                html_content = f'<p>I am writing theis email to request for your travel agency services. </p><p>The following are my details:</p><p>Start Location: {start}</p> <p>Destination:  {destination}</p> <p>Start Date: {startdate}</p> <p>End Date:  {enddate}</p> <p> Phone:  {phone}</p><p> Number of Peopple:  {number}</p><p>Customer Request:     {customerrequest}</p><p><b>Regards</b></p><p><b>{name}<b></p>'
                email.attach_alternative(html_content, 'text/html')
                email.send(fail_silently=False)
                # subject = 'Request for Travel Agency Services'
                # message = f'Hi {name}, '
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = ['joshuashalla1@gmail.com', ]
                # html_template =  render_to_string()
                # plain_message = strip_tags(html_template)
                # send_mail( subject, plain_message, email_from, recipient_list, html_message=html_template )
       
        return render(request, 'book.html')
def about(request):
        template = loader.get_template('about.html')
        return HttpResponse(template.render())
def contact(request):
        name= request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        submitbutton= request.POST.get('Submit')
        if(request.method == 'POST'):
                email = EmailMultiAlternatives(
                f'{subject}',
                f"Hi {name} ",
                settings.EMAIL_HOST_USER,
                ['joshuashalla1@gmail.com'],
                reply_to=[f'{email}, '],
                headers={'Message-ID': 'foo'},
                )
                html_content = f'<p>{message}</p><p>Regards</p><p>{name}</p>'
                email.attach_alternative(html_content, 'text/html')
                email.send(fail_silently=False)
        return render(request, 'contact.html')
        # template = loader.get_template('contact.html')
        # return HttpResponse(template.render())
def gallery(request):
        template = loader.get_template('gallery.html')
        return HttpResponse(template.render())
def error_404_view(request, exception):
   
         return render(request, '404.html')