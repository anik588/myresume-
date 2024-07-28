from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
def home(request):
    form = ContactForm()  # Create an instance of ContactForm

    context = {
        'form': form,
        'title': 'Welcome to My Resume',
        'content': 'This is the home page of my resume website.'
        # Add any other context data you want to pass to the template
    }
    return render(request, 'index.html', context)

def portfolio_ecommerce(request):
    return render(request, 'portfolio-ecommerce.html')

def portfolio_blogsite(request):
    return render(request, 'portfolio-blogsite.html')


from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ContactForm  # Assuming ContactForm is defined in your app

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import ContactForm

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import ContactForm
import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
import datetime  # Ensure datetime is imported

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
import datetime  # Ensure datetime is imported

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Render the email template with context
            context = {
                'name': name,
                'email': email,
                'message': message,
                'year': datetime.datetime.now().year
            }
            html_content = render_to_string('email.html', context)

            # Create the email
            subject = 'New Message Request'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.DEFAULT_FROM_EMAIL]  # Replace with actual recipient if needed
            email_message = EmailMultiAlternatives(subject, '', from_email, recipient_list)
            email_message.attach_alternative(html_content, "text/html")

            try:
                email_message.send()
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            except Exception as e:
                print(f"Error sending email: {e}")
                return JsonResponse({'success': False, 'message': 'An error occurred while sending the message.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form submission.'})

    return render(request, 'index.html', {'form': ContactForm()})






