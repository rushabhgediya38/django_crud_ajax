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
		stu = request.POST.get('stuid')
		name = request.POST['name_1']
		email = request.POST['email_1']
		description = request.POST['description_1']

		if stu == '':
			ab = crud_post(name=name, email=email, description=description)
		else:
			ab = crud_post(id=stu, name=name, email=email, description=description)
		ab.save()

		crud_data = crud_post.objects.values()
		all_data = list(crud_data) 

		return JsonResponse({'status': 'Save', 'crud_data': all_data})
	return JsonResponse({'status': 0})

def data_delete(request):
	if request.method == "POST":
		id = request.POST.get('sid')
		da = crud_post.objects.get(pk=id)
		da.delete()
		return JsonResponse({'status':1})

	return JsonResponse({'status':0})


def data_edit(request):
	if request.method == "POST":
		id = request.POST.get('sid')
		ed = crud_post.objects.get(pk=id)

		ed_data = {"id":ed.id, "name":ed.name, "email":ed.email, "description":ed.description}

		return JsonResponse(ed_data)



