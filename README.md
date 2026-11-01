# cad-mesh-analyzer

`cad-mesh-analyzer` is an open-source Python toolkit and CLI for automated 3D CAD/STL mesh validation, manifold geometry verification, and engineering automation.

## Key Features
- **Manifold Verification**: Detect non-manifold edges, open boundaries, and watertight violations.
- **Topology & Geometry Quality**: Evaluate facet aspect ratios, surface normal consistency, and degenerated triangles.
- **Automated CI Integration**: Seamlessly run mesh validation inside GitHub Actions or automated pre-processing pipelines.

## Installation
```bash
pip install numpy
cd cad-mesh-analyzer
```

## Usage
Run the analysis tool on any STL file or sample test data:
```bash
python analyzer.py
```

## License
Distributed under the MIT License.
