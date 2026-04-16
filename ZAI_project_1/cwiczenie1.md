# Zaawansowane aplikacje internetowe  
# Projekt nr 1

### Ćwiczenie 1

#### Uwagi wstępne

Do wykonania poniższych zadań niezbędne jest posiadanie zainstalowanego w systemie programu *Python* i pakietu *Django*. Sprawdzamy, czy mamy zainstalowany program *Python*:

<font size="2">

```python
D:\ZAI>python --version
# Python 3.11.0
```

</font>

Uzyskany wynik oznacza, że mamy zainstalowany w systemie program *Python* w wersji 3.11.0. Sprawdzamy, czy mamy zainstalowany w systemie pakiet *Django*:

<font size="2">

```python
D:\ZAI>django-admin --version
# 'django-admin' is not recognized as an internal or external command,
#  operable program or batch file.
```

</font>

Uzyskany wynik oznacza, że nie mamy zainstalowanego w systemie pakietu *Django*.

#### Tworzenie środowiska wirtualnego i instalacja niezbędnych pakietów

<font size="2">

```python
# Tworzenie środowiska wirtualnego
D:\ZAI>python -m venv env

# Aktywacja środowiska wirtualnego:
D:\ZAI>env\Scripts\activate
(env) D:\ZAI>
# (env) widoczne na początku znaku zachęty oznacza, że środowisko wirtualne zostało aktywowane

# instalacja pakietu Django
(env) D:\ZAI>pip install django

# Sprawdzenie, czy mamy już Django (w środowisku wirtualnym)
(env) D:\ZAI>django-admin --version
# 4.2
#
# Uzyskany wynik oznacza, że w środowisku wirtualnym mamy zainstalowaną wersję 4.2 pakietu Django.

```

</font>

#### Tworzenie projektu i aplikacji

W poniższych poleceniach *core* oznacza nazwę projektu, zaś *tasks* to nazwa aplikacji. Pierwsze polecenie tworzy projekt, drugie aplikację.

<font size="2">

```python
# Proszę zwrócić uwagę na kropkę na końcu pierwszego polecenia:
(env) D:\ZAI>django-admin startproject core .
(env) D:\ZAI>django-admin startapp tasks      
```

</font>

Uruchamiamy wbudowany serwer www, aby zobaczyć czy Django zainstalowało się pomyślnie.

<font size="2">

```python
python manage.py runserver
# Teraz w przeglądarce internetowej wpisujemy adres: http://localhost:8000
# Powinna wyświetlić się strona Django.
# Oznacza to prawidłową instalację pakietu.
```

</font>

#### Rejestracja aplikacji w <i>Django</i>

W pliku <code>tasks/settings.py</code> na końcu listy <code>INSTALLED_APPS</code> dopisujemy naszą aplikację:

<font size="2">

```python
INSTALLED_APPS = [
    (...),
    'tasks',
]
```

</font>

#### Pierwszy model

W pliku <code>tasks/models.py</code> tworzymy pierwszy model - <i>Task</i>

<font size="2">

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

```

</font>

#### Migracje

Aby zsynchronizować modele i bazę danych, przygotowujemy i wykonujemy <i>migracje</i>.

<font size="2">

```python
python manage.py makemigrations
python manage.py migrate
```

</font>

#### Tworzenie superużytkownika

<font size="2">

```python
python manage.py createsuperuser
```

</font>

#### Rejestracja modelu <i>Task</i> w panelu admina

W pliku <code>tasks/admin.py</code> rejestrujemy model <i>Task</i>

<font size="2">

```python
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at" )
    list_filter = ("title", )
    search_fields = ("title",)

```

</font>

#### Uruchomienie panelu admina w przeglądarce

<font size="2">

```python
# Uruchamiamy serwer www
python manage.py runserver
# W przeglądarce wpisujemy adres url:
http://localhost:8000/admin/
# Logujemy się danymi utworzonego wcześniej superużytkownika
```

</font>

