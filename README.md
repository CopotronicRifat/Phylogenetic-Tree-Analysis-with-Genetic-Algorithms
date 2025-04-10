# Phylogenetic Tree Analysis with Genetic Algorithms

## Overview

This project explores the application of Genetic Algorithms (GA) to construct and analyze phylogenetic trees. It was developed as part of my MSc research on metaheuristic approaches for bioinformatics problems. The goal is to automate the inference of evolutionary relationships among species using optimized tree structures.

## Requirements

### Software
- Python 3.4 or above

### Python Packages
Make sure the following packages are installed:

- biopython
- numpy
- matplotlib
- scipy
- fuzzywuzzy
- pandas

You can install them using:

```bash
pip install biopython numpy matplotlib scipy fuzzywuzzy pandas
```

## Data Source

The genome data is obtained from NCBI:

🔗 [NCBI Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/Entrez)

NCBI data is typically in XML format. You may parse it using:
1. `Bio.Entrez` module
2. Python's built-in `xml.dom` or `xml.sax`
3. Manual string-based parsing (not recommended)

### Genome database includes:
- Assembly
- BioCollections
- BioProject
- BioSample
- Clone
- dbVar
- Genome
- GSS
- Nucleotide
- Probe
- SNP
- SRA
- Taxonomy

## Notes

- You may need to modify the code to read specific datasets from the Genome database.
- Parameter tuning is critical for optimal GA performance.
- Modular design supports easy changes to datasets and GA settings.
- Due to the stochastic nature of GA, reproduced results may slightly differ from those reported in the original thesis.

## Citation

If you use this work, please cite:

```
S. M. Rafiuddin, "Estimation of Phylogenetic Tree using Gene Sequencing Data,"
2019 4th International Conference on Electrical Information and Communication Technology (EICT),
Khulna, Bangladesh, 2019, pp. 1-6, doi:10.1109/EICT48899.2019.9068849.
```

## License

This project is open-sourced under the MIT License.

## Author

S. M. Rafiuddin (2020)
