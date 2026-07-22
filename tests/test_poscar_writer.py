from pathlib import Path
import numpy as np

from dft_toolkit import POSCARParser
from dft_toolkit import POSCARWriter

DATA = Path(__file__).parent/"data"/"graphene"/"POSCAR"


def test_poscar_writer(tmp_path):

    s = POSCARParser().read(DATA).parse()

    outfile = tmp_path/"POSCAR.out"

    POSCARWriter(s).write(outfile)

    assert outfile.exists()

    s2 = POSCARParser().read(outfile).parse()

    assert s2.comment == s.comment
    assert s2.scale == s.scale
    assert s2.species == s.species
    assert s2.counts == s.counts

    np.testing.assert_allclose(s2.lattice, s.lattice)
    np.testing.assert_allclose(s2.frac_coords, s.frac_coords)
