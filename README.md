# Whittaker-Eilers smoother in Python

Here's an implementation in Python-numpy-scipy of the Whittaker-Eilers smoother described in: P. H. C. Eilers, "A perfect smoother", *Anal. Chem.* **2003**, *75*, 3631-3636 ([doi:10.1021/ac034173t](https://doi.org/10.1021/ac034173t)). Use of specific sparse matrix routines makes the smoother fast and memory-efficient. The present implementation only covers evenly-spaced data (*i.e.* data sampled at equal distances) without missing values.

The original Matlab program by Eilers uses the sparse Cholesky solver for solving
the matrix equation involved in the smoothing procedure, but since a sparse Cholesky solver is not available in the 'scipy' sparse matrix library, we chose the sparse LU-decomposition based solver instead ('scipy.sparse.linalg.splu'). Our Python implementation was tested with the data provided with the original publication, and gave identical smoothing results. The test is included here as an example script.

The example script demonstrates how the smoothing routine is used. The only parameter that needs to be tuned (manually, for now) is `lmbd` ('λ' in the Eilers paper), which determines the strength of the smoothing. Note that `lmbd` needs 
tuning over several orders of magnitude (10, 100, 1000, ...). As an optional second parameter, the default 2nd-order smoother (`d = 2`) will work fine for almost all signals. 

We have used the Whittaker-Eilers smoother in our recent work, *e.g.* J. Midelet et al., *ChemPhysChem* **2018**, *19*, 827-836. [doi:10.1002/cphc.201701228](https://doi.org/10.1002/cphc.201701228)

It is easy and intuitive to use, often gives better results faster than the venerable Savitsky-Golay smoother, and far better results than boxcar-smoothing.

This impementation is distributed under the CeCILL-B license (a BSD-like license). See: http://www.cecill.info/

Many thanks go to Simon Bordeyne who pioneered a first (non-sparse) version
of the smoother in Python.


## Suggestions for further work

- Add support for missing values and unevenly spaced data, following the indications in Eilers' paper.
- Explore 'auto-tuning' of the λ parameter, as explained in that same paper, and how this would best be implemented.
