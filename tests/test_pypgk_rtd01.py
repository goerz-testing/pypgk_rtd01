"""Tests for `pypgk_rtd01` package."""

import pytest
from pkg_resources import parse_version

import pypgk_rtd01


def test_valid_version():
    """Check that the package defines a valid ``__version__``."""
    v_curr = parse_version(pypgk_rtd01.__version__)
    v_orig = parse_version("0.1.0-dev")
    assert v_curr >= v_orig
