from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import RegistroForm, LoginForm
from django.contrib import messages
from django.contrib.auth import logout



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Criar o usuário mas não salvar ainda
            user.set_password(form.cleaned_data["password1"])  # Garantir que a senha é hash
            user.save()  # Agora salva no banco
            messages.success(request, 'Conta criada com sucesso!')
            login(request, user)  # Loga o usuário automaticamente
            return redirect('dashboard')  
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados.')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')  # Redireciona para a página do dashboard
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')
