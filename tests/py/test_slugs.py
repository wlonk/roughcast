from roughcast.slugs import slugify


class TestSlugify:
    def test_unicode(self):
        value = "v0.1.0 江湖"
        expected = "v0.1.0-江湖"
        actual = slugify(value, allow_unicode=True)
        assert actual == expected

    def test_non_unicode(self):
        value = "v0.1.0 江湖"
        expected = "v0.1.0"
        actual = slugify(value)
        assert actual == expected
