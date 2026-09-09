"""
Autonomous Agent Butterworth IIR Digital Filter Skill
Pure Python Standard Library implementation using bilinear transform.
"""
import math
from typing import List, Dict, Any

class ButterworthLowpass:
    """
    Bilinear-transformed 1st-order Butterworth Lowpass digital filter.
    """
    def __init__(self, cutoff_freq: float, sampling_rate: float):
        wc = 2 * math.pi * cutoff_freq
        T = 1.0 / sampling_rate
        wa = (2 / T) * math.tan(wc * T / 2)
        k = wa * T / 2
        norm = 1.0 + k
        self.b0 = k / norm
        self.b1 = k / norm
        self.a1 = (k - 1.0) / norm

    def filter_signal(self, data: List[float]) -> List[float]:
        filtered = []
        prev_x = 0.0
        prev_y = 0.0
        for x in data:
            y = self.b0 * x + self.b1 * prev_x - self.a1 * prev_y
            filtered.append(round(y, 4))
            prev_x = x
            prev_y = y
        return filtered
