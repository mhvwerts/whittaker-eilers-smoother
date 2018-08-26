# Whittaker-Eilers smoother in Python

Here's an implementation in Python-numpy-scipy of the Whittaker-Eilers smoother described in:
P. H. C. Eilers, "A perfect smoother", *Anal. Chem.* **2003**, *75*, 3631-3636. Use of 
specific sparse matrix routines makes the smoother fast and memory-efficient.

The original Matlab program by Eilers uses the sparse Cholesky solver for solving
the matrix equation involved in the smoothing procedure, but since a sparse Cholesky solver
is not available in the 'scipy' sparse matrix library, we chose the sparse LU-decomposition
based solver instead ('scipy.sparse.linalg.splu'). Our Python implementation was tested with
the data provided with the original publication, and gave identical smoothing results. The test
is included here as an example script.

We have used the Whittaker-Eilers smoother in our recent work, *e.g.* J. Midelet et al.,
*ChemPhysChem* **2018**, *19*, 827-836. https://doi.org/10.1002/cphc.201701228

It is easy and intuitive to use, often gives better results faster than the venerable Savitsky-Golay smoother, 
and far better results than boxcar-smoothing.

This impementation is distributed under the CeCILL-B license (a BSD-like license). See: http://www.cecill.info/
