from pathlib import Path


def scan_vasp_directories(root):
    """
    Scan recursively for directories containing an OUTCAR file.
    """

    root = Path(root)

    calculations = []

    for outcar in root.rglob("OUTCAR"):
        calculations.append(outcar.parent)

    return sorted(calculations)
