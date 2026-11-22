import pytest
from flask import g
from flask import session

from flaskr.db import get_db


def test_register(client, app):
    # test that viewing the page renders without template errors
    assert client.get("/auth/register").status_code == 200

    # test that successful registration redirects to the login page
    response = client.post("/auth/register", data={"username": "a", "password": "password123"})
    assert response.headers["Location"] == "/auth/login"

    # test that the user was inserted into the database
    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM user WHERE username = 'a'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("test", "test1234", b"already registered"),
    ),
)
def test_register_validate_input(client, username, password, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password}
    )
    assert message in response.data


def test_login(client, auth):
    # test that viewing the page renders without template errors
    assert client.get("/auth/login").status_code == 200

    # test that successful login redirects to the index page
    response = auth.login()
    assert response.headers["Location"] == "/"

    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["username"] == "test"


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "test", b"Incorrect username."), ("test", "a", b"Incorrect password.")),
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session

# Prueba R2 con contraseña corta (5 caracteres): debe mostrar error y no registrar.
def test_register_pwd_curta(client, app):
    # Envía una petición POST a /auth/register con un usuario nuevo y contraseña de 5 caracteres.
    response = client.post(
        "/auth/register", data={"username": "usuari_curt", "password": "12345"}
    )
    # Comprueba que en la respuesta HTML aparece el mensaje de error por contraseña corta.
    assert b"Password must be at least 8 characters long." in response.data
    # Abre el contexto de la aplicación Flask para consultar la base de datos.
    with app.app_context():
        # Verifica que el usuario NO se ha insertado en la tabla user.
        assert (
            get_db()
            .execute("SELECT * FROM user WHERE username = 'usuari_curt'")
            .fetchone()
            is None
        )


# Prueba R2 con contraseña en el límite exacto (8 caracteres): debe aceptar el registro.
def test_register_pwd_limit(client, app):
    # Envía una petición POST con contraseña de exactamente 8 caracteres ("12345678").
    response = client.post(
        "/auth/register", data={"username": "usuari_limit", "password": "12345678"}
    )
    # Comprueba que redirige a la página de login (/auth/login), señal de registro correcto.
    assert response.headers["Location"] == "/auth/login"
    # Abre el contexto de la aplicación para comprobar la base de datos.
    with app.app_context():
        # Verifica que el usuario SÍ se ha creado en la tabla user.
        assert (
            get_db()
            .execute("SELECT * FROM user WHERE username = 'usuari_limit'")
            .fetchone()
            is not None
        )


# Prueba R2 con contraseña larga (> 8 caracteres): debe aceptar el registro.
def test_register_pwd_llarga(client, app):
    # Envía una petición POST con una contraseña larga de más de 8 caracteres.
    response = client.post(
        "/auth/register",
        data={"username": "usuari_llarg", "password": "contrasenyaLlarga123"},
    )
    # Comprueba que redirige a /auth/login tras registrar correctamente.
    assert response.headers["Location"] == "/auth/login"
    # Abre el contexto de la aplicación para verificar la inserción.
    with app.app_context():
        # Verifica que el usuario existe en la base de datos.
        assert (
            get_db()
            .execute("SELECT * FROM user WHERE username = 'usuari_llarg'")
            .fetchone()
            is not None
        )
