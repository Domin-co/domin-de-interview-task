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


def plot_arcs(position, flow, arcs=None, title="", ax=None):
    """Plot a recording, optionally colouring the arcs you produced.

    `arcs`, if given, is a list of index-lists: one list of integer indices
    (into `position`/`flow`) per arc, e.g. [[...], [...], [...], [...]].
    Anything not assigned to an arc is drawn faintly in grey so gaps show up.
    """
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots(figsize=(11, 7))

    ax.scatter(position, flow, s=6, color="lightgrey", label="(unassigned)")
    if arcs:
        for n, idx in enumerate(arcs):
            idx = list(idx)
            if not idx:
                continue
            ax.plot([position[i] for i in idx], [flow[i] for i in idx],
                    marker="o", ms=3, lw=0.8, label=f"arc {n + 1}")
    ax.set_xlabel("position")
    ax.set_ylabel("flow")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.legend()
    return ax


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    pos, flow, t = load_recording("data/sweep_01.json")
    print(f"loaded {len(pos)} samples; "
          f"position [{min(pos):.1f}, {max(pos):.1f}], "
          f"flow [{min(flow):.3f}, {max(flow):.3f}]")
    plot_arcs(pos, flow, title="sweep_01 (raw)")
    plt.show()
