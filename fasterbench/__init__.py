"""Comprehensive benchmarking toolkit for deep learning models"""

__version__ = "0.1.0"

from .benchmark import benchmark, BenchmarkResult
from .size import SizeMetrics, compute_size, get_model_size, get_num_parameters
from fasterbench.speed import (
    SpeedMetrics, compute_speed, compute_speed_multi, 
    sweep_threads, sweep_latency, sweep_batch_sizes,
)
from .profiling import LayerProfiler
from .compute import ComputeMetrics, compute_compute
from .memory import MemoryMetrics, compute_memory, compute_memory_multi
from .energy import EnergyMetrics, compute_energy, compute_energy_multi
from fasterbench.roofline import (
    HardwarePeaks, RooflinePoint, measure_peaks, clear_peaks_cache, RooflineAnalyzer,
)
from .plot import create_radar_plot, SPECS
from .utils import parse_metric_value

__all__ = [
    # Main entry point
    'benchmark', 'BenchmarkResult',
    # Size
    'SizeMetrics', 'compute_size', 'get_model_size', 'get_num_parameters',
    # Speed
    'SpeedMetrics', 'compute_speed', 'compute_speed_multi', 
    'sweep_threads', 'sweep_latency', 'sweep_batch_sizes',
    # Profiling
    'LayerProfiler',
    # Compute
    'ComputeMetrics', 'compute_compute',
    # Memory
    'MemoryMetrics', 'compute_memory', 'compute_memory_multi',
    # Energy
    'EnergyMetrics', 'compute_energy', 'compute_energy_multi',
    # Roofline
    'HardwarePeaks', 'RooflinePoint', 'measure_peaks', 'clear_peaks_cache', 'RooflineAnalyzer',
    # Plot
    'create_radar_plot', 'SPECS',
    # Report
    'Report', 'ComparisonReport', 'ReportMetricDelta',
    # Utils
    'parse_metric_value',
]
from .report import Report, ComparisonReport, ReportMetricDelta

