from src.bingo import carton

def test_matrix():
    mi_carton = (
        (1,1,0,1,1,1,1,0,1),
        (0,0,1,1,0,1,0,1,0),
        (0,1,0,0,1,0,0,1,1)
    )
    rows = len(mi_carton)
    assert rows == 3
    for i in range(0, 3):
        columns = len(mi_carton[i])
        assert columns == 9
