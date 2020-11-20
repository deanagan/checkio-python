import pytest

from src.cipher_crossword import cipher

@pytest.mark.parametrize(('puzzle', 'words', 'expected'), [
    ([
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6]
        ],

        ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace'],
     [['h', 'e', 'l', 'l', 'o'],
      ['a', ' ', 'e', ' ', 'z'],
      ['b', 'i', 'm', 'b', 'o'],
      ['i', ' ', 'm', ' ', 'n'],
      ['t', 'r', 'a', 'c', 'e']])
])
def test_cipher_crossword(puzzle, words, expected):
    assert cipher(puzzle, words) == expected
