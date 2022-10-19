from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from .models import Jugador, Video , Categoria
from django.views.generic.detail import DetailView

def home(request):
    return render(request, 'users/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            genero = form.cleaned_data.get('genero')
            altura = form.cleaned_data.get('altura')
            jugador = Jugador()
            jugador.genero = genero
            jugador.altura = altura
            jugador.user = user
            jugador.save()

            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)

def videos(request):
    template = "videos/videop.html"
    context = {}
    videos = Video.objects.all()
    context ["videos"] = videos
    return render(request, template, context)

def categorias2(request):
    template = "public/categoria.html"
    context = {}
    categorias = Categoria.objects.all()
    context ["categorias"] = categorias
    return render(request, template, context)



class CategoriaDetailView(DetailView):
    model = Categoria