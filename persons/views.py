from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Country, State, District, City

def home(request):
    return render(request, 'persons/home.html')

    
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'persons/add_person.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})


# AJAX
def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).all()
    return render(request, 'persons/state_dropdown_list_options.html', {'states': states})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def load_districts(request):
    state_id = request.GET.get('state_id')
    districts = District.objects.filter(state_id=state_id).all()
    return render(request, 'persons/district_dropdown_list_options.html', {'districts': districts})

def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
