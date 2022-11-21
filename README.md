# [ Django ] Game Reviews WebSite

### 📑 Descrição

Um agregador de notas e críticas de jogos que permite `criar playlists públicas` de temas específicos.

**[ Tecnologias ]**

<samp>
  
- <em>Django</em> | <em>Python</em> | <em>JavaScript</em> | <em>Bootstrap</em>
  
</samp>

![image](https://user-images.githubusercontent.com/99571291/202287918-17c1f6e7-35b6-4a32-b4b9-36ce4f62298a.png)

### 🎲 Iniciando o Projeto

<samp>

> **Warning**
> Comandos descritos para o sistema operacional Windows.

</samp>

**1. Clone o repositório e instale as dependências**

```sh
$ git clone <https://github.com/ellenmariadev/game-reviews-django.git>
$ pip install -r requirements.txt
```

**2. Configure o ambiente virtual**

```sh
$ python -m venv venv

# Windows
$ source venv/Scripts/activate

# Linux/MacOS
$ . venv/bin/activate
```

**3. Crie as migrações e execute a aplicação**

```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

**3. Acesse o localhost**

```sh
$ <http://127.0.0.1:8000/>
```
