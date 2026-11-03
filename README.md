<div align="center"><img src="https://raw.githubusercontent.com/pallets/flask/refs/heads/stable/docs/_static/flask-name.svg" alt="" height="150"></div>

# Flask

Flask is a lightweight [WSGI] web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around [Werkzeug]
and [Jinja], and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/

## A Simple Example

```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Donate

The Pallets organization develops and supports Flask and the libraries
it uses. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today].

[please donate today]: https://palletsprojects.com/donate

## Contributing

## Diagrames UML de seqüència — Autenticació

Aquests diagrames representen el procés d'autenticació de l'aplicació web del projecte Blog Flask.

### 1. Esquelet del diagrama de seqüència

Mostra els participants del procés: l'usuari, la interfície web, el servei d'autenticació i la base de dades.

[Veure l'esquelet del login](diagrams/esquelet-login.png)

### 2. Flux principal (happy path)

Representa el procés d'inici de sessió quan les credencials són correctes.

[Veure el flux principal](diagrams/login-happy-path.png)

### 3. Flux alternatiu: credencials invàlides

Representa què passa quan l'usuari introdueix credencials incorrectes.

[Veure el diagrama](diagrams/credencials-incorrectes.png)

### 4. Flux alternatiu: sistema no accessible

Representa què passa quan el sistema no està disponible i es mostra un missatge d'error.

[Veure el diagrama](diagrams/sistema-no-accessible.png)

### 5. Flux alternatiu: format de correu incorrecte

Representa què passa quan l'usuari introdueix un correu electrònic amb un format incorrecte.

[Veure el diagrama](diagrams/format-correu-incorrecte.png)

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/
