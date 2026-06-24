"""Helpers for the arc-splitting task.

You are given these so you can spend your time on the splitting logic rather
than on file parsing. You are free to use, ignore, or modify anything here.

Each file in data/ is one continuous recording from the machine: aligned
`position`, `flow` and `timestamp` readings, in the order they were sampled.
A single recording contains two passes of the routine, so plotting flow against
position shows two figure-of-eight shapes (the second pass has inverted flow).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple


def load_recording(path: str | Path) -> Tuple[List[float], List[float], List[float]]:
    """Return (position, flow, timestamp) lists for one recording.

    The three lists are aligned and in sample order: position[i], flow[i] and
    timestamp[i] were all recorded at the same instant.
    """
    with open(path, "r") as f:
        rec = json.load(f)
    return rec["position"], rec["flow"], rec["timestamp"]
