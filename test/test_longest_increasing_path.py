import pytest

from src.longest_increasing_path import longest_increasing_path

@pytest.mark.parametrize(('input, expected'), [
    ([[9,9,4], [6,6,8], [2,1,1]], 4),
    ([[3,4,5], [3,2,6], [2,2,1]], 4),
    ([], 0),
    ([[7,7,5],[2,4,6],[8,2,0]], 4),
    ([[19,2,8,6,4,14,1,0,17],
      [0,1,9,10,11,4,12,14,5],
      [14,12,16,0,15,8,5,2,8],
      [5,4,1,17,9,18,8,5,2],
      [9,5,4,8,16,7,11,5,0],
      [5,7,14,18,10,0,14,14,0],
      [9,14,4,13,18,16,9,12,10],
      [18,13,9,18,11,4,12,10,10],
      [7,14,16,19,10,19,11,6,4],
      [16,2,3,7,15,9,7,1,1],
      [1,6,16,15,18,6,6,1,14],
      [9,5,2,9,8,3,2,3,10],
      [2,3,16,8,7,7,0,18,16],
      [11,0,16,8,13,13,11,3,8],
      [17,11,0,12,11,15,12,17,0]], 8)
])
def test_long_non_repeat(input, expected):
    assert longest_increasing_path(input) == expected
