from nose.tools import assert_equal

def uni_char(s):

    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True

class TestUnique(object):
    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestUnique()
t.test(uni_char)
