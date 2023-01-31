import pytest
from modules.api.clients.gihub import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    api = GitHub()
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    api = GitHub()
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def tesdt_repo_can_be_found(github_api):
    r = github_api.search_repo('became-qa-auto')
    assert r['total_count'] == 13
    assert 'become-qa-auto'  in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0