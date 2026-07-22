from pathlib import Path
import numpy as np


class BandStructureWriter:
    """
    Export band structure to a text file.

    Columns:
        k-index   band-1   band-2 ...
    """

    @staticmethod
    def write(filename, bandstructure):

        filename = Path(filename)

        nkpts = bandstructure.nkpts
        nbands = bandstructure.nbands

        data = np.zeros((nkpts, nbands + 1))

        data[:, 0] = np.arange(nkpts)

        data[:, 1:] = bandstructure.eigenvalues

        header = "k-index " + " ".join(
            f"band{i+1}" for i in range(nbands)
        )

        np.savetxt(
            filename,
            data,
            fmt="%.10f",
            header=header,
        )
