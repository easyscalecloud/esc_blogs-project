# -*- coding: utf-8 -*-

from esc_blogs import api


def test():
    _ = api


if __name__ == "__main__":
    from esc_blogs.tests import run_cov_test

    run_cov_test(__file__, "esc_blogs.api", preview=False)
