import job_hunter


def test_menu_not_empty():
    assert bool(job_hunter.menu()), "Menu is empty"
    return None


if __name__ == "__main__":
    test_menu_print()