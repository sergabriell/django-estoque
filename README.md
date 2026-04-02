# 🧩 Projeto Django Admin com Jazzmin — Guia Completo (Windows)

Este guia mostra **do zero** como preparar o ambiente, criar a venv, usar `requirements.txt`, rodar migrations e utilizar o Django Admin com o tema Jazzmin **sem bugs**.

> Stack estável recomendada:
>
> - Python **3.12**
> - Django **4.2.13 (LTS)**
> - django-jazzmin **3.0.4**

---

## ✅ 1) Instalar o Python 3.12 corretamente

Baixe no site oficial e **marque** a opção:

- ☑️ Add Python to PATH

Depois confirme no terminal:

```bash
python --version
```

Deve aparecer: `Python 3.12.x`

---

## ✅ 2) Criar a pasta do projeto

```bash
mkdir django-product
cd django-product
```

---

## ✅ 3) Criar a Virtual Environment (venv)

```bash
python -m venv .venv
```

### Ativar a venv

**PowerShell**

```bash
.venv\Scripts\activate
```

**Git Bash**

```bash
source .venv/Scripts/activate
```

Você verá `(.venv)` no início da linha.

---

## ✅ 4) Criar o `requirements.txt`

Crie um arquivo na raiz:

```txt
Django==4.2.13
django-jazzmin==3.0.4
```

Instale:

```bash
pip install -r requirements.txt
```

---

## ✅ 5) Criar o projeto Django

```bash
django-admin startproject core .
```

---

## ✅ 6) Configurar o Jazzmin no `settings.py`

Edite `core/settings.py`:

```python
INSTALLED_APPS = [
    "jazzmin",  # sempre antes do admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

---

## ✅ 7) Primeiras migrations

```bash
python manage.py migrate
```

---

## ✅ 8) Criar superusuário

```bash
python manage.py createsuperuser
```

---

## ✅ 9) Rodar o servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/admin

---

# 🏗️ Criando Apps

```bash
python manage.py startapp products
```

Adicione no `INSTALLED_APPS`:

```python
"products",
```

---

# 🧱 Criando Models

`products/models.py`

```python
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

---

# 🛠️ Registrar no Admin

`products/admin.py`

```python
from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
```

---

# 🔁 Migrations sempre que alterar models

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 📦 Congelar dependências (muito importante)

Sempre que instalar algo novo e estiver funcionando:

```bash
pip freeze > requirements.txt
```

---

# 🧹 Resetar banco (desenvolvimento)

```bash
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

# 🧪 Comandos úteis do dia a dia

| Ação | Comando |
|---|---|
| Ativar venv | `.venv\\Scripts\\activate` |
| Rodar servidor | `python manage.py runserver` |
| Criar app | `python manage.py startapp nome` |
| Migrations | `makemigrations && migrate` |
| Criar superuser | `createsuperuser` |
| Shell Django | `python manage.py shell` |

---

# 🎨 Jazzmin UI Builder

No admin, acesse:

`/admin/jazzmin/ui_builder/`

---

# ⚠️ Problemas comuns

## Filtros / FK / M2M não abrem
- Verifique se está usando Django 4.2
- Verifique se `jazzmin` está antes do admin

## `python` não funciona no terminal
- Verifique PATH
- Desative aliases da Microsoft Store

---

# ✅ Checklist final

- [ ] Python 3.12 funcionando no terminal
- [ ] venv ativa
- [ ] requirements instalado
- [ ] Jazzmin antes do admin
- [ ] Migrations rodadas
- [ ] Superuser criado

Pronto. Ambiente estável, reproduzível e profissional.

