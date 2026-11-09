import pytest


# Stars 1 and 5 are saved with 200. Stars 0 and 6 are refused with 400
# and leave the rating as it was (3 stars).
@pytest.mark.parametrize(
    "stars, status, saved",
    [(0, 400, 3), (1, 200, 1), (5, 200, 5), (6, 400, 3)],
)
def test_update_stars_boundaries(api, auth, rating, stars, status, saved):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == status
    res = api.get(path, headers=auth)
    assert res.json()["stars"] == saved
