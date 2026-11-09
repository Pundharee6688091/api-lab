# The owner makes a rating. Another user tries to read, change or delete it,
# is refused with a status from 400 to 499, and the rating stays as it was.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    assert 400 <= res.status_code <= 499
    assert api.get(path, headers=auth).json() == rating


def test_other_user_cannot_change(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 1}, headers=other_auth)
    assert 400 <= res.status_code <= 499
    assert api.get(path, headers=auth).json() == rating


def test_other_user_cannot_delete(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    assert 400 <= res.status_code <= 499
    assert api.get(path, headers=auth).json() == rating
