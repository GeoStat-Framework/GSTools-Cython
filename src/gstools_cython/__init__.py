"""
Purpose
=======

GSTools is a library providing geostatistical tools
for random field generation, conditioned field generation,
kriging and variogram estimation
based on a list of provided or even user-defined covariance models.

This package provides the Cython backend implementations for GSTools.

Subpackages
===========

.. autosummary::
   :toctree: api

    field
    krige
    variogram
"""

# Hooray!
from . import field, krige, variogram

try:
    from ._version import __version__
except ModuleNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = "unknown"

__all__ = ["__version__"]
__all__ += ["field", "krige", "variogram"]
