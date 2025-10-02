import pytest
from unittest.mock import MagicMock, patch
from jose import jwt, JWTError
from fastapi import HTTPException
from datetime import datetime, timedelta, timezone

from todolist_fastapi.functions import get_session, create_token, authenticate_user, verify_token

@patch('todolist_fastapi.functions.sessionmaker')
def test_get_session(mock_sessionmaker):
    mock_session = MagicMock()
    mock_sessionmaker.return_value = MagicMock(return_value=mock_session)

    gen = get_session()
    session = next(gen)

    mock_sessionmaker.assert_called_once()
    assert session == mock_session

    try:
        next(gen)
    except StopIteration:
        pass

    mock_session.close.assert_called_once()

@patch('todolist_fastapi.functions.SECRET_KEY', 'test_secret')
@patch('todolist_fastapi.functions.ALGORITHM', 'HS256')
def test_create_token_generates_valid_jwt():
    id_user = 42
    duration = timedelta(minutes=1)
    token = create_token(id_user, duration_token=duration)
    decoded = jwt.decode(token, 'test_secret', algorithms=['HS256'])
    assert decoded['sub'] == str(id_user)
    assert 'exp' in decoded

def test_authenticate_user_success(monkeypatch):
    mock_user = MagicMock()
    mock_user.email = "test@example.com"
    mock_user.password = "hashed"
    mock_session = MagicMock()
    mock_session.query().filter().first.return_value = mock_user
    monkeypatch.setattr('src.todolist_fastapi.settings.bcrypt_context.verify', lambda pw, hpw: True)
    from todolist_fastapi.functions import authenticate_user
    result = authenticate_user("test@example.com", "password", mock_session)
    assert result == mock_user

def test_authenticate_user_user_not_found():
    mock_session = MagicMock()
    mock_session.query().filter().first.return_value = None
    from todolist_fastapi.functions import authenticate_user
    result = authenticate_user("notfound@example.com", "password", mock_session)
    assert result is False

def test_authenticate_user_wrong_password(monkeypatch):
    mock_user = MagicMock()
    mock_user.email = "test@example.com"
    mock_user.password = "hashed"
    mock_session = MagicMock()
    mock_session.query().filter().first.return_value = mock_user
    monkeypatch.setattr('src.todolist_fastapi.settings.bcrypt_context.verify', lambda pw, hpw: False)
    from todolist_fastapi.functions import authenticate_user
    result = authenticate_user("test@example.com", "wrongpassword", mock_session)
    assert result is False

@patch('todolist_fastapi.functions.ModelUser')
@patch('todolist_fastapi.functions.jwt.decode')
def test_verify_token_success(mock_jwt_decode, mock_ModelUser):
    mock_user = MagicMock()
    mock_session = MagicMock()
    mock_session.query().filter().first.return_value = mock_user
    mock_jwt_decode.return_value = {'sub': '1'}
    from todolist_fastapi.functions import verify_token
    result = verify_token(token="sometoken", session=mock_session)
    assert result == mock_user

@patch('todolist_fastapi.functions.jwt.decode', side_effect=JWTError("JWTError"))
def test_verify_token_jwt_error(mock_jwt_decode):
    mock_session = MagicMock()
    from todolist_fastapi.functions import verify_token
    with pytest.raises(HTTPException) as excinfo:
        verify_token(token="badtoken", session=mock_session)
    assert excinfo.value.status_code == 401

@patch('todolist_fastapi.functions.ModelUser')
@patch('todolist_fastapi.functions.jwt.decode')
def test_verify_token_user_not_found(mock_jwt_decode, mock_ModelUser):
    mock_session = MagicMock()
    mock_session.query().filter().first.return_value = None
    mock_jwt_decode.return_value = {'sub': '1'}
    from todolist_fastapi.functions import verify_token
    with pytest.raises(HTTPException) as excinfo:
        verify_token(token="validtoken", session=mock_session)
    assert excinfo.value.status_code == 401

