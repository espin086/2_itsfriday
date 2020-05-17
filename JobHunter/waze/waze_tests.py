"""
Checks to make sure that Waze Calculator returned correct values
"""

import waze

OUTPUT = waze.calc_route(
    "10757 Longworth Ave Santa Fe Springs, CA", "Disneyland")


def test_list_is_not_empty():
    """
    Function must return a non-empty list
    """
    assert OUTPUT is True, 'list is empty'


if __name__ == "__main__":
    test_list_is_not_empty()
