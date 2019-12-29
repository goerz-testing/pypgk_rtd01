"""Set up the environment for doctests

This file is automatically evaluated by py.test. It ensures that we can write
doctests without distracting import statements in the doctest.
"""
import pytest

import pypgk_rtd01


@pytest.fixture(autouse=True)
def set_doctest_env(doctest_namespace):
    doctest_namespace['pypgk_rtd01'] = pypgk_rtd01
