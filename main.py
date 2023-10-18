from typing import List
from typing import Sequence

def bitonic_sort(array: Sequence[int]) -> None:
    """バイトニックソート
    :param array: ソート対象の配列
    """
    if len(array) <= 1 or (len(array) & (len(array) - 1)) != 0:
        raise ValueError('The length of the array must be a power of 2.')
    result = _bitonic_sort(True, array)
    array[:] = result

def _bitonic_sort(up: bool, array: Sequence[int]) -> List[int]:
    """バイトニックソート
    :param up: 昇順にソートするかどうかのフラグ
    :param array: ソート対象の配列
    """
    if len(array) <= 1:
        return array
    else:
        first = _bitonic_sort(True, array[:len(array) // 2])
        second = _bitonic_sort(False, array[len(array) // 2:])
        return bitonic_merge(up, first + second)

def bitonic_merge(up: bool, array) -> List[int]:
    """マージ処理
    :param up: 昇順にソートするかどうかのフラグ
    :param array: ソート対象の配列
    """
    if len(array) == 1:
        return array
    else:
        bitonic_compare(up, array)
        first = bitonic_merge(up, array[:len(array) // 2])
        second = bitonic_merge(up, array[len(array) // 2:])
        return first + second

def bitonic_compare(up: bool, array) -> None:
    """比較交換処理
    :param up: 昇順にソートするかどうかのフラグ
    :param array: ソート対象の配列
    """
    dist = len(array) // 2
    for i in range(dist):
        if (array[i] > array[i + dist]) == up:
            array[i], array[i + dist] = array[i + dist], array[i]

def shuffle(array: List[int]) -> None:
    """シャッフル
    :param array: シャッフル対象の配列
    """
    import random
    random.shuffle(array)

if __name__ == '__main__':
    array = [i for i in range(16)]
    shuffle(array)
    print(f'before: {array}')
    bitonic_sort(array)
    print(f'after : {array}')
