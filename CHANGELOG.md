# Changelog

## v0.1.0 (2026-03-24)

First stable release of fasterbench.

### Features

- **Unified `benchmark()` API** — Single entry point returning typed `BenchmarkResult` with 5 metric categories
- **Size metrics** — Parameter count, disk size via `compute_size()`
- **Speed metrics** — Latency, throughput, batch/thread/latency sweeps via `compute_speed_multi()`
- **Compute metrics** — MACs/FLOPs via thop and torchprofile backends via `compute_compute()`
- **Memory metrics** — CPU (psutil) and GPU (CUDA) memory tracking via `compute_memory_multi()`
- **Energy metrics** — Power consumption and carbon footprint via codecarbon via `compute_energy_multi()`
- **`LayerProfiler`** — Per-layer profiling with hook-based measurement (speed, memory, size, compute)
- **Radar plots** — Multi-model comparison visualization via `create_radar_plot()`
- **`BenchmarkResult`** — Supports both typed access (`result.size.size_mib`) and dict access (`result["size_mib"]`)
- **Serialization** — `.as_dict()`, `.to_dataframe()`, `.to_json()` on all result types

### Infrastructure

- Migrated to nbdev3 with `pyproject.toml` (PEP 621)
- CI via GitHub Actions (nbdev3-ci workflow)
- Documentation via Quarto + GitHub Pages
- Suppressed spurious logging from thop and codecarbon

## v0.0.1

Initial development release.
