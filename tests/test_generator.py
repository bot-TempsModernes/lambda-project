from buzz import generator


def test_sample_single_word():
    alist = ('foo', 'bar', 'foobar')
    word = generator.sample(alist)
    assert word in alist


def test_sample_multiple_words():
    alist = ('foo', 'bar', 'foobar')
    words = generator.sample(alist, 2)
    assert len(words) == 2
    assert words[0] in alist
    assert words[1] in alist
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
