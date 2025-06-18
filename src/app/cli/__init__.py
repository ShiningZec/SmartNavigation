# __init__.py

__author__ = 'ShiningZec'

from .cli_util import Cli
from .cli_doc import WELC_DOC, HELP_DOC


def main():
    print(Cli.__name__)
    print(WELC_DOC, HELP_DOC)


if __name__ == '__main__':
    main()
