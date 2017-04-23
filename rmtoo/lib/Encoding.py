'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Helper class for Encoding - supports python 2 and 3

 (c) 2017 by flonatel

 For licensing details see COPYING
'''
import sys


class Encoding(object):

    @staticmethod
    def is_unicode(s):
        if s is None:
            return False
        if sys.version_info[0] == 2:
            # The noqa is needed to get pep8 run on python3
            if type(s) != unicode:
                print("UNIIIIIIIIIIIIIIIICCCCCCODE [%s]" % s)
            return type(s) == unicode  # noqa: F821
        if sys.version_info[0] == 3:
            return type(s) == str
        assert False

    # This is somewhat hackish - but the only way I found to
    # check if 's' is a unicode string.
    @staticmethod
    def check_unicode(s):
        if s is None:
            return
        if type(s) in [list, dict]:
            print("+++ ERROR: Must be a string not a [%s]" % type(s))
            assert False
        if not Encoding.is_unicode(s):
            print("+++ ERROR: String [%s] must be unicode" % s)
            assert False
        return

    @staticmethod
    def check_unicode_list(l):
        if type(l) != list:
            print("+++ ERROR: Must be a list not a [%s]" % type(l))
            assert False
        for s in l:
            Encoding.check_unicode(s)

    @staticmethod
    def to_unicode(l):
        if sys.version_info[0] == 2:
            # The noqa is needed to get pep8 run on python3
            return unicode(l)  # noqa: F821
        if sys.version_info[0] == 3:
            return str(l)
        assert False
