from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from four.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# from four.forms import new_user


# Create your views here.

def index(request):
    return render(request, 'index.html')


def other(request):
    return render(request, 'other.html')


def another(request):
    return render(request, 'another.html')


@login_required
def special(request):
    return HttpResponse('You have loged in!')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')


def form_view(request):
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()

                registered = True
            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()

    return render(request, 'forms.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')

        else:
            print('Someone tried to Login and Failed')
            print('Username: {} and Password {}'.format(username, password))
            return HttpResponse('invalid login details supplied!')

    else:
        return render(request, 'login.html', {})
# def form_view(request):
#     form = new_user()
#
#     if request.method == "POST":
#         form = new_user(request.POST)
#
#         if form.is_valid():
#             # print("VALIDATION SUCCESS!")
#             # print("NAME:" + form.cleaned_data['name'])
#             # print("EMAIL:" + form.cleaned_data['email'])
#             # print("TEXT:" + form.cleaned_data['text'])
#             form.save(commit=True)
#             return render(request, 'index.html')
#         else:
#             print('Error')
#     return render(request, 'forms.html', {'form': form})
