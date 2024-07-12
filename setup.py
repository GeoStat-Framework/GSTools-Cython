"""GSTools-Cython: Cython backend for GSTools."""

import os

import numpy as np
from Cython.Build import cythonize
from extension_helpers import add_openmp_flags_if_available
from setuptools import Extension, setup

# cython extensions
CY_MODS = [
    Extension(
        name=f"gstools_cython.{ext}",
        sources=[os.path.join("src", "gstools_cython", ext) + ".pyx"],
        include_dirs=[np.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    )
    for ext in ["field", "krige", "variogram"]
]
# you can set GSTOOLS_BUILD_PARALLEL=0 or GSTOOLS_BUILD_PARALLEL=1
open_mp = False
if int(os.getenv("GSTOOLS_BUILD_PARALLEL", "0")):
    added = [add_openmp_flags_if_available(mod) for mod in CY_MODS]
    open_mp = any(added)
    print(f"## GSTools-Cython setup: OpenMP used: {open_mp}")
else:
    print("## GSTools-Cython setup: OpenMP not wanted by the user.")

compiler_directives = {}
if int(os.getenv("GSTOOLS_CY_DOCS", "0")):
    print(f"## GSTools-Cython setup: embed signatures for documentation")
    compiler_directives["embedsignature"] = True
if int(os.getenv("GSTOOLS_CY_COV", "0")):
    print(f"## GSTools-Cython setup: enable line-trace for coverage")
    compiler_directives["linetrace"] = True
    for mod in CY_MODS:
        mod.define_macros.append(("CYTHON_TRACE_NOGIL", "1"))

options = {
    "compile_time_env": {"OPENMP": open_mp},
    "compiler_directives": compiler_directives,
}
# setup - do not include package data to ignore .pyx files in wheels
setup(ext_modules=cythonize(CY_MODS, **options), include_package_data=False)
