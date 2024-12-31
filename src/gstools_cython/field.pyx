# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True
"""
This is the randomization method summator, implemented in cython.

.. currentmodule:: gstools_cython.field

Functions
^^^^^^^^^

.. autosummary::
   :toctree:

   summate
   summate_incompr
   summate_fourier
"""

import numpy as np
from cython.parallel import prange

if OPENMP:
    cimport openmp

cimport numpy as np
from libc.math cimport cos, sin


def set_num_threads(num_threads):
    cdef int num_threads_c = 1
    if num_threads is None:
        # OPENMP set during setup
        if OPENMP:
            num_threads_c = openmp.omp_get_num_procs()
        else:
            ...
    else:
        num_threads_c = num_threads
    return num_threads_c


def summate(
    const double[:, :] cov_samples,
    const double[:] z_1,
    const double[:] z_2,
    const double[:, :] pos,
    num_threads=None,
):
    """
    Fourier summator for random field generation using the randomization method.

    Parameters
    ----------
    cov_samples : double[:, :]
        samples from the spectral density distribution of the covariance model
    z_1 : double[:]
        random samples from a normal distribution
    z_2 : double[:]
        random samples from a normal distribution
    pos : double[:, :]
        the position (d,n) tuple with d dimensions and n points.
    num_threads : None or int, optional
        number of OpenMP threads, default: None

    Returns
    -------
    summed_modes : double[:]
        summed random modes
    """
    cdef int i, j, d
    cdef double phase
    cdef int dim = pos.shape[0]

    cdef int X_len = pos.shape[1]
    cdef int N = cov_samples.shape[1]

    cdef double[:] summed_modes = np.zeros(X_len, dtype=float)

    cdef int num_threads_c = set_num_threads(num_threads)

    for i in prange(X_len, nogil=True, num_threads=num_threads_c):
        for j in range(N):
            phase = 0.
            for d in range(dim):
                phase += cov_samples[d, j] * pos[d, i]
            summed_modes[i] += z_1[j] * cos(phase) + z_2[j] * sin(phase)

    return np.asarray(summed_modes)


cdef (double) abs_square(const double[:] vec) noexcept nogil:
    cdef int i
    cdef double r = 0.

    for i in range(vec.shape[0]):
        r += vec[i]**2

    return r


def summate_incompr(
    const double[:, :] cov_samples,
    const double[:] z_1,
    const double[:] z_2,
    const double[:, :] pos,
    num_threads=None,
):
    """
    Fourier summator for random vector field generation using the randomization method.

    Parameters
    ----------
    cov_samples : double[:, :]
        samples from the spectral density distribution of the covariance model
    z_1 : double[:]
        random samples from a normal distribution
    z_2 : double[:]
        random samples from a normal distribution
    pos : double[:, :]
        the position (d,n) tuple with d dimensions and n points.
    num_threads : None or int, optional
        number of OpenMP threads, default: None

    Returns
    -------
    summed_modes : double[:, :]
        summed random modes
    """
    cdef int i, j, d
    cdef double phase
    cdef double k_2
    cdef int dim = pos.shape[0]

    cdef double[:] e1 = np.zeros(dim, dtype=float)
    e1[0] = 1.
    cdef double[:] proj = np.empty(dim)

    cdef int X_len = pos.shape[1]
    cdef int N = cov_samples.shape[1]

    cdef double[:, :] summed_modes = np.zeros((dim, X_len), dtype=float)

    for i in range(X_len):
        for j in range(N):
            k_2 = abs_square(cov_samples[:, j])
            phase = 0.
            for d in range(dim):
                phase += cov_samples[d, j] * pos[d, i]
            for d in range(dim):
                proj[d] = e1[d] - cov_samples[d, j] * cov_samples[0, j] / k_2
                summed_modes[d, i] += (
                    proj[d] * (z_1[j] * cos(phase) + z_2[j] * sin(phase))
                )
    return np.asarray(summed_modes)


def summate_fourier(
    const double[:] spectrum_factor,
    const double[:, :] modes,
    const double[:] z_1,
    const double[:] z_2,
    const double[:, :] pos,
    num_threads=None,
):
    """
    Fourier summator for periodic random field generation using the fourier method.

    Parameters
    ----------
    spectrum_factor : double[:, :]
        spectrum factors
    modes : double[:, :]
        modes from the covariance model
    z_1 : double[:]
        random samples from a normal distribution
    z_2 : double[:]
        random samples from a normal distribution
    pos : double[:, :]
        the position (d,n) tuple with d dimensions and n points.
    num_threads : None or int, optional
        number of OpenMP threads, default: None

    Returns
    -------
    summed_modes : double[:]
        summed random modes
    """
    cdef int i, j, d
    cdef double phase
    cdef int dim = pos.shape[0]

    cdef int X_len = pos.shape[1]
    cdef int N = modes.shape[1]

    cdef double[:] summed_modes = np.zeros(X_len, dtype=float)

    cdef int num_threads_c = set_num_threads(num_threads)

    for i in prange(X_len, nogil=True, num_threads=num_threads_c):
        for j in range(N):
            phase = 0.
            for d in range(dim):
                phase += modes[d, j] * pos[d, i]
            summed_modes[i] += (
                spectrum_factor[j] * (z_1[j] * cos(phase) + z_2[j] * sin(phase))
            )

    return np.asarray(summed_modes)
