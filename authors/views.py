from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from authors.forms.login import LoginForm
from games.models import Games, List, ReviewRating

from .forms import AuthorListForm, RegisterForm, ReviewForm
from .models import Profile

# Create your views here.


def register_view(request):
    # messages.success(request, 'Cadastro efetuado com sucesso.')
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Cadastro efetuado com sucesso.')
        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))
    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    # login_url = reverse('authors:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(reverse('authors:home'))


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def games(request):
    # games = Games.objects.filter(
    #     author=request.user
    # )
    games = Games.objects.all().order_by('title')
    return render(
        request, 
        'games/pages/home.html', 
        context={
            'games': games,
        })


@login_required(login_url='authors:login', redirect_field_name='next')
def list_view(request):
    # games = Games.objects.filter(
    #     author=request.user
    # )
    lists = List.objects.all()
    return render(
        request, 
        'games/pages/lists.html', 
        context={
            'lists': lists,
        })


@login_required(login_url='authors:login', redirect_field_name='next')
def list_edit(request, id):
    lists = List.objects.filter(
        author=request.user,
        pk=id,
    ).first()

    if not lists:
        raise Http404()

    form = AuthorListForm(
        request.POST or None,
        instance=lists
    )

    if form.is_valid():
        lists = form.save(commit=False)
        lists.author = request.user

        lists.save()
        messages.success(request, 'Edição salva.')
        return redirect(reverse('authors:lists'))

    allgames = Games.objects.all()
    listas = List.objects.get(id=id)
    gamelists = listas.games.all()
    listaas = List.objects.all()
    return render(
        request, 
        'games/pages/lista-edit.html', 
        context={
            'form': form,
            'gamelists': gamelists,
            'allgames': allgames,
            'listaas': listaas,
            'listas': listas
        })


@login_required(login_url='authors:login', redirect_field_name='next')
def addgame(request, id):
    url = request.META.get('HTTP_REFERER')
    lists = List.objects.filter(
        author=request.user,
        pk=id,
    )

    if not lists:
        raise Http404()

    print(lists)
     
    for li in lists:
        gamesel = request.POST['gameSelect']
        game = Games.objects.get(id=gamesel)
        li.games.add(game)
    return redirect(url)


@login_required(login_url='authors:login', redirect_field_name='next')
def delete_item(request, id, games_id):
    
    url = request.META.get('HTTP_REFERER')
    lists = List.objects.filter(
        author=request.user,
        pk=id,
    )

    for li in lists:
        game = Games.objects.get(id=games_id)
        li.games.remove(game)

    return redirect(url)


@login_required(login_url='authors:login', redirect_field_name='next')
def favorites_add(request, games_id):
    author = request.user
    fave = Games.objects.get(id=games_id)
    profile = Profile.objects.get(author=author)
    if profile.favourite.filter(id=games_id).exists():
        profile.favourite.remove(fave)
    else:
        profile.favourite.add(fave)
        return redirect(reverse('authors:home'))
    return redirect('authors:home')


@login_required(login_url='authors:login', redirect_field_name='next')
def favorites_view(request):
    author = request.user
    profile = Profile.objects.get(author=author)
    fave = profile.favourite.all()

    return render(
        request, 
        'games/pages/favorites.html', 
        context={
            'faves': fave,
        })


@login_required(login_url='authors:login', redirect_field_name='next')
def newlist_view(request, id):
    return render(
        request, 
        'games/pages/register-list.html', 
        )

@login_required(login_url='authors:login', redirect_field_name='next')
def newlist_add(request):
    allgames = Games.objects.all()
    author = request.user
    profile = Profile.objects.get(author=author)

    print(author)

    form = AuthorListForm(
        request.POST or None,
    )

    if form.is_valid():
        form.instance.author = request.user
        lists = form.save()
        profile.my_lists.add(lists)
        messages.success(request, 'Lista Criada!')
        return redirect('authors:home')
    else: 
        form = AuthorListForm()

    return render(
        request, 
        'games/pages/register-list.html', 
        context={
            'form': form,
            'allgames': allgames,
        })

@login_required(login_url='authors:login', redirect_field_name='next')
def details(request, id):

    game = Games.objects.get(id=id)

    return render(
        request, 
        'games/pages/lista-detail.html', 
        context={
            'game': game
        })


@login_required(login_url='authors:login', redirect_field_name='next')
def game_details(request, id):

    game = Games.objects.get(id=id)

    if request.method == 'POST':

        form = ReviewForm(
            request.POST or None,
        )

        if form.is_valid():
            form.instance.author = request.user
            form.instance.game = game
            form.save()
            messages.success(request, 'Review Feito!')
            return redirect('authors:home')
    else: 
        form = ReviewForm()
    reviewList = ReviewRating.objects.filter(game=id)

    print(reviewList)

    reviews = ReviewRating.objects.all()
    return render(
        request, 
        'games/pages/details.html', 
        context={
            'form': form,
            'reviewList': reviewList,
            'reviews': reviews,
            'game': game
        })

@login_required(login_url='authors:login', redirect_field_name='next')
def lists_details(request, id):

    lists = List.objects.get(id=id)
    gamelists = lists.games.all()

    return render(
        request, 
        'games/pages/lista-detail.html', 
        context={
            'lists': lists,
            'gamelists': gamelists
        })

@login_required(login_url='authors:login', redirect_field_name='next')
def my_list(request):
    author = request.user
    profile = Profile.objects.get(author=author)
    lists = profile.my_lists.all()

    print(lists)

    return render(
        request, 
        'games/pages/mylists.html', 
        context={
            'lists': lists,
        })

@login_required(login_url='authors:login', redirect_field_name='next')
def delete_list(request, id): 
    
    author = request.user
    profile = Profile.objects.get(author=author)
    profile.my_lists.remove(id)

    lists = List.objects.get(id=id)
    lists.delete()

    return redirect('authors:lists')
