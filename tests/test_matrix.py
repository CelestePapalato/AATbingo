from tests.test_1_a_90 import carton

def test_matrix():
    mi_carton = carton
    rows = len(mi_carton)
    assert rows == 3
    for i in range(0, 3):
        columns = len(mi_carton[i])
        assert columns == 9
