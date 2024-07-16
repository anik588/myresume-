from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm

def home(request):
    form = ContactForm()  # Create an instance of ContactForm

    context = {
        'form': form,
        'title': 'Welcome to My Resume',
        'content': 'This is the home page of my resume website.'
        # Add any other context data you want to pass to the template
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=email,
                recipient_list=['your-receiving-email@example.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'index.html', {'form': ContactForm()})
