from typing import List
from typing import Sequence

def bitonic_sort(array: Sequence[int]) -> None:
    """バイトニックソート
    :param array: ソート対象の配列
    """
    _bitonic_sort(array, 0, len(array), True)

def _bitonic_sort(array: Sequence[int], start: int, size: int, ascending: bool) -> None:
    """バイトニックソート
    :param array: ソート対象の配列
    :param start: ソート対象の開始インデックス
    :param size: ソート対象のサイズ
    :param ascending: 昇順ソートの場合はTrue、降順ソートの場合はFalse
    """
    if size <= 1:
        return
    half = size // 2
    _bitonic_sort(array, start, half, True)
    _bitonic_sort(array, start + half, half, False)
    _bitonic_merge(array, start, size, ascending)

def _bitonic_merge(array: Sequence[int], start: int, size: int, ascending: bool) -> None:
    """バイトニックマージ
    :param array: ソート対象の配列
    :param start: ソート対象の開始インデックス
    :param size: ソート対象のサイズ
    :param ascending: 昇順ソートの場合はTrue、降順ソートの場合はFalse
    """
    if size <= 1:
        return
    half = size // 2
    for i in range(start, start + half):
        if (array[i] > array[i + half]) == ascending:
            array[i], array[i + half] = array[i + half], array[i]
    _bitonic_merge(array, start, half, ascending)
    _bitonic_merge(array, start + half, half, ascending)

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
