# -*- coding: utf-8 -*-

import pytest
import hello


@pytest.fixture
def client(request):
    client = hello.app.test_client()
    return client

def test_logout(client):
    rv = client.get('/redir', follow_redirects=True)
    assert b'Hello' in rv.data

def test_local_redirect(client):
    rv = client.get('/redir_local', follow_redirects=True)
    assert b'Hello' in rv.data
