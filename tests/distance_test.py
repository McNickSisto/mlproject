# tests/distance_test.py
from mlproject.distance import haversine

def test_haversine_is_number():
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 37.15537033159167, -8.736309635176545
    distance = haversine(lon1, lat1, lon2, lat2)
    assert distance == 1581.4024221112622
