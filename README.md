
Fight.net
===
- Title:  `Fight.net`
- Authors:  `Alfonso Robledo Rangel`

## Install & Dependence
- python
- pytorch
- numpy

## Use
- for train
  ```
  python train.py
  ```
- for test
  ```
  python test.py
  ```


## Directory Hierarchy
```
|—— .env
|—— .env.dev
|—— .env.prod
|—— .gitignore
|—— chromadb.py
|—— db.sqlite3
|—— eventos
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— 0002_usuarios_eventos_usuario.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-313.pyc
|            |—— 0002_usuarios_eventos_usuario.cpython-313.pyc
|            |—— __init__.cpython-313.pyc
|    |—— models.py
|    |—— static
|        |—— css
|            |—— estilos.css
|    |—— templates
|        |—— eventos
|            |—— index.html
|    |—— tests.py
|    |—— views.py
|    |—— __init__.py
|    |—— __pycache__
|        |—— admin.cpython-313.pyc
|        |—— apps.cpython-313.pyc
|        |—— models.cpython-313.pyc
|        |—— views.cpython-313.pyc
|        |—— __init__.cpython-313.pyc
|—— fightnet_eventos
|    |—— asgi.py
|    |—— settings.py
|    |—— urls.py
|    |—— wsgi.py
|    |—— __init__.py
|    |—— __pycache__
|        |—— settings.cpython-313.pyc
|        |—— urls.cpython-313.pyc
|        |—— wsgi.cpython-313.pyc
|        |—— __init__.cpython-313.pyc
|—— manage.py
|—— __pycache__
|    |—— chromadb.cpython-313.pyc
```


## Code Details
### Tested Platform
- software
  ```
  OS: Debian unstable (May 2021), Ubuntu LTS
  Python: 3.8.5 (anaconda)
  PyTorch: 1.7.1, 1.8.1
  ```
  
## 🚀 Instrucciones de Uso

Sigue estos pasos para levantar el proyecto en tu entorno local.

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/nombre-del-proyecto.git
cd nombre-del-proyecto
```


