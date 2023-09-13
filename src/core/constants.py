DICE_DICT = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5}
TILES = list(range(21, 37))
NUMBER_OF_DICE = 8


def compute_title_value(title_index: int) -> int:
    """
    Compute the value of a title based on its index.
    """
    return (title_index - 17) // 4
