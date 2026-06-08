"""Helpers for the sweep-splitting task.

You are given these so you can spend your time on the algorithm rather than on
parsing JSON. You are free to use, ignore, or modify anything here.

Each data file is the raw response from a valve test rig. The measurement we
care about lives under data -> edge_tests. An "edge" is one flow channel; in
these files only one channel ("p_s1") is populated, and it records, for every
sample, the spool `normalised_position` and the measured `flow`.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple

EDGE = "p_s1"  # the populated channel in every provided file


def load_sweep(path: str | Path, edge: str = EDGE) -> Tuple[List[float], List[float]]:
    """Return (position, flow) lists for one sweep file, in sample order.

    `position` is `normalised_position`; `flow` is the measured flow.
    The two lists are aligned: position[i] was measured at the same instant
    as flow[i], and the order is the order the samples were taken in.
    """
    with open(path, "r") as f:
        blob = json.load(f)
    rows = blob["data"]["edge_tests"][edge]["data"]
    position = [r["normalised_position"] for r in rows]
    flow = [r["flow"] for r in rows]
    return position, flow


def plot_split(position, flow, segments=None, title="", ax=None):
    """Plot a sweep, optionally colouring the segments you produced.

    `segments`, if given, is a dict mapping a segment name to a list of
    integer indices into `position`/`flow`, e.g.
        {"left": [...], "deadband": [...], "right": [...]}
    Anything not in a segment is drawn faintly in grey so you can spot gaps.
    """
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots(figsize=(11, 7))

    ax.scatter(position, flow, s=6, color="lightgrey", label="(unassigned)")
    if segments:
        for name, idx in segments.items():
            idx = list(idx)
            if not idx:
                continue
            ax.scatter([position[i] for i in idx], [flow[i] for i in idx],
                       s=8, label=name)
    ax.set_xlabel("normalised_position")
    ax.set_ylabel("flow")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.legend()
    return ax


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    pos, flow = load_sweep("data/sweep_01.json")
    print(f"loaded {len(pos)} samples; "
          f"position range [{min(pos):.1f}, {max(pos):.1f}], "
          f"flow range [{min(flow):.3f}, {max(flow):.3f}]")
    plot_split(pos, flow, title="sweep_01 (raw)")
    plt.show()
