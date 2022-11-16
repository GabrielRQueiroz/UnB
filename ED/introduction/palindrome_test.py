from palindrome import palindrome


def test_palindrome():
    assert palindrome("ovo") == "POSSÍVEL"

    assert palindrome("abccaa") == "POSSÍVEL"

    assert palindrome("lua") == "POSSÍVEL"

    assert palindrome("abcda") == "POSSÍVEL"

    assert palindrome("abbcca") == "IMPOSSÍVEL"

    assert palindrome("fccf") == "IMPOSSÍVEL"

    assert palindrome("afcfa") == "POSSÍVEL"

    assert palindrome("afccfa") == "IMPOSSÍVEL"

    assert palindrome("a") == "POSSÍVEL"
