from django.shortcuts import render
from .forms import BasicForm
from .models import Customer
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
def home(request):
	form = BasicForm()
	if request.method == 'POST':
		forms = BasicForm(request.POST)

		if forms.is_valid():
			forms.save()
			name = request.POST['name']
			email = request.POST['email']
			choices = request.POST['choices']
			phone = request.POST['phone']
			detail = request.POST['detail']
			subject = str(email) + ', ' + str(choices) + ', ' + str(phone) + ', ' + str(detail)
			from_email = settings.EMAIL_HOST_USER
			send_mail(name, subject, from_email, ['vikki.azevedo@gmail.com'])


			messages.success(request, 'Form submission successful')
			return redirect(reverse_lazy('vikki'))

			
	context = {'form': form}
	return render(request, 'blog/home.html', context)