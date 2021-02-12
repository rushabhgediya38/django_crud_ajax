from django.shortcuts import render
from .forms import UserRegistrationForm
from django.http import JsonResponse, HttpResponse
from .models import crud_post


# Create your views here.


def index(request):
    form = UserRegistrationForm()
    da = crud_post.objects.all()
    return render(request, 'index.html', {'form': form, 'st': da})


def save(request):
	if request.method == 'POST':
		name = request.POST['name_1']
		email = request.POST['email_1']
		description = request.POST['description_1']

		ab = crud_post(name=name, email=email, description=description)
		ab.save()

		crud_data = crud_post.objects.values()
		all_data = list(crud_data) 

		return JsonResponse({'status': 'Save', 'crud_data': all_data})
	

