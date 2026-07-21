from pathlib import Path
import numpy as np


class ProfileWriter:
    """
    Export 1D profile data to text files.
    """

    @staticmethod
    def write(filename, profile, header="Index Value"):

        filename = Path(filename)

        data = np.column_stack(
            (
                np.arange(len(profile)),
                profile,
            )
        )

        np.savetxt(
            filename,
            data,
            fmt="%8d %18.10f",
            header=header,
        )
