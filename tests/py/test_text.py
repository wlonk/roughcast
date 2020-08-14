from roughcast.text import unmark


def test_unmark():
    value = """
# This is a heading

- And this is a list.

But this is _italic_, so it's best.
    """
    expected = (
        "This is a heading\n\nAnd this is a list.\n\nBut this is italic, so it's best."
    )
    actual = unmark(value)
    assert actual == expected
