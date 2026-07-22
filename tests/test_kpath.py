import numpy as np

from dft_toolkit import KPath


def test_kpath():

    coords = np.array(
        [
            [0,0,0],
            [0.5,0,0],
            [1.0,0,0],
        ]
    )

    kp = KPath(coords)

    assert kp.nkpts == 3

    d = kp.distances()

    assert np.allclose(
        d,
        [0.0,0.5,1.0]
    )
