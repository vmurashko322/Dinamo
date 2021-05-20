from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from main.forms import ChangeAdvUserForm, UserRegisterForm
from main.forms import CreateProductModel, ProductForm
from main.models import AdvUser
from movies.models import Movie


def get_first_page(request):
    context = {'name': 'tomas', 'dict': {'id': 1}, 'list': [100, 200, 300]}
    return render(request, 'first_page.html', context)


class UserLogin(LoginView):
    template_name = 'auth/login.html'


@login_required
def profile(request):
    return render(request, 'auth/profile.html')


# через класс
# class AdvLogoutView(LoginRequiredMixin, LogoutView):
#     template_name = 'movies_list.html'

# через функцию
def AdvLogoutView(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000/')


# через функцию второй вариант
# def logout(request):
#     request.session.flush()
#     request.user = AnonymousUser()
#     return render()

class ChangeAdvUserView(LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'auth/update_user.html'
    form_class = ChangeAdvUserForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.request.user.id)


# регистрация через функцию
def register_user(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.instance.set_password(form.cleaned_data['password'])
            form.save()
        else:
            context = {'form': form}
            return render(request, 'auth/register.html', context)
    context = {'form': form}
    return render(request, 'auth/register.html', context)


# регистрация через классс
# class RegisterUserView(CreateView):
#     form_class = UserRegisterForm
#     model = AdvUser
#     template_name = 'auth/register.html'
#     success_url = reverse_lazy('register_done')


def createProduct(request):
    # формы через модели
    form = CreateProductModel()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateProductModel(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['form'] = form
    return render(request, 'createProduct.html', context)

    # просто формы
    # print(request.POST)
    # form=CreateProductForm(request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     prod=Product(**form.cleaned_data)
    #     prod.save()
    # contex={'form':form}
    # return render(request, 'createProduct.html', contex)


# через html
# if request.method == "POST":
#
#     prod = Product()
#     name = request.POST.get('name')
#     price = request.POST.get('price')
#     if len(name) < 100 and len(price.split('.')[0]) <= 3:
#         prod.name = name
#         prod.price = price
#         prod.save()
#     else: return HttpResponse('Ошибка')
#     return HttpResponse('Данные успешно сохранены')
# return render(request, 'createProduct.html')

# 13.04
def new_form(request):
    formS = ProductForm()
    context = {'form': formS}
    if request.method == "POST":
        form = ProductForm({'name': request.POST['name'], 'price': request.POST['price']})
        form.save()
        # if form.is_valid():
        #     print(form.cleaned_data)
    return render(request, 'form_new.html', context)


def show_dict(request):
    array = [2001, 1999, 2015, 2006, 2021]
    film = Movie.objects.all()
    print(film)
    print(film.filter(date_published=2015))
    print(film[:1])
    return HttpResponse(film)
