from pathlib import Path


class POSCARWriter:

    def __init__(self, structure):
        self.structure = structure

    def write(self, filename):

        filename = Path(filename)

        with open(filename, "w") as f:

            f.write(f"{self.structure.comment}\n")
            f.write(f"{self.structure.scale:.16f}\n")

            for vec in self.structure.lattice:
                f.write(
                    "{:20.16f} {:20.16f} {:20.16f}\n".format(*vec)
                )

            f.write(" ".join(self.structure.species) + "\n")
            f.write(" ".join(map(str, self.structure.counts)) + "\n")

            f.write("Direct\n")

            for x, y, z in self.structure.frac_coords:
                f.write(
                    "{:20.16f} {:20.16f} {:20.16f}\n".format(x, y, z)
                )

        return filename
