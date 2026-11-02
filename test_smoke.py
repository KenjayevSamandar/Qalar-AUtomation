import pytest
import requests

@pytest.mark.smoke
def test_api_ishlayapti(base_url):
	"""Eng asosiy tekshiruv: API umuman javob bermadimi?"""
	javob=requests.get(f"{base_url}/posts/1/")
	assert javob.status_code==200	
@pytest.mark.smoke
def test_post_mavjud(base_url):
    """Bitta post mavjudligini tekshirish"""
    javob = requests.get(f"{base_url}/posts/1")
    assert javob.json()["id"] == 1


@pytest.mark.smoke
def test_users_api_ishlayapti(base_url):
    """Users endpoint ham ishlayaptimi?"""
    javob = requests.get(f"{base_url}/users")
    assert javob.status_code == 200
