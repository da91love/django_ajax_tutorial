from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .forms import ProfileForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        print(id(form))

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('formtest:success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()
        print(id(form))

    print(id(form))
    return render(request, 'formtest/form.html', {'profile_form': form})

def get_success(request):
    return render(request, 'formtest/success.html')