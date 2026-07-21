# DFT-Toolkit

**DFT-Toolkit** is an open-source Python library for analyzing Density Functional Theory (DFT) calculations with a primary focus on **VASP**.

The toolkit provides parsers, analysis tools, visualization utilities, and a command-line interface for computational materials science.

---

## Features

### File Parsers

- OUTCAR
- DOSCAR
- EIGENVAL
- PROCAR
- POSCAR / CONTCAR
- XDATCAR
- CHGCAR
- LOCPOT
- INCAR
- KPOINTS
- vasprun.xml
- POTCAR

### Analysis

- Band gap
- Effective mass
- Work function
- Charge density difference
- Density profile

### Visualization

- Band structure
- Density of States (DOS)
- Projected DOS (PDOS)
- Fat band

### Export

- CSV
- JSON
- POSCAR
- Density profile

---

## Installation

### Install from PyPI

```bash
pip install dft-toolkit
git clone https://github.com/YOUR_GITHUB_USERNAME/DFT-Toolkit.git
cd DFT-Toolkit
pip install -e .

Sau khi dán xong, **chỉ gõ đúng một dòng**:

```text

---

## Quick Start

```python
from python.parsers import OUTCARParser

outcar = OUTCARParser().read("OUTCAR").parse()

print(outcar)
pytest -v
cat >> README.md <<'EOF'

---

## Quick Start

```python
from python.parsers import OUTCARParser

outcar = OUTCARParser().read("OUTCAR").parse()

print(outcar)
pytest -v
dft-toolkit --helppython/
├── analysis/
├── cli/
├── core/
├── io/
├── parsers/
├── plotting/
└── writers/

tests/
examples/
docs/
---

## Bước 4. Thêm phần cuối

```bash
cat >> README.md <<'EOF'
---

## Roadmap

### Version 1.0

- Stable VASP parsers
- Electronic structure analysis
- Publication-quality plots
- Command-line interface
- Complete documentation

### Future Versions

- Quantum ESPRESSO support
- Wannier90
- BoltzTraP
- Phonopy
- ASE integration

---

## Contributing

Contributions are welcome through pull requests and issue reports.

---

## Citation

If this project is useful in your research, please cite DFT-Toolkit in your publications.

---

## License

MIT License
