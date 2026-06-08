# Take-home task: splitting a valve flow sweep

Thanks for taking the time to do this. We expect it to take roughly two to four
hours. It is deliberately open-ended in places — we are more interested in how
you reason about messy real data than in a perfect answer.

## Background (no valve knowledge needed)

One of the tests on our valve rig sweeps a moving part (the "spool") across its
full travel while measuring the resulting oil flow. For each sample we record
two numbers:

- `normalised_position` — where the spool is, and
- `flow` — the flow at that instant.

If you plot `flow` against `normalised_position` you get a characteristic shape:
two active flow "lobes", one either side, separated by a central band where the
spool is near its null point and almost no flow passes. We call that central
near-zero band the **deadband**. The two boundaries of the deadband — where flow
lifts off from zero on each side — are physically the most important feature of
the test.

You are given six real sweeps in `data/` (`sweep_01.json` … `sweep_06.json`).
They are genuine rig outputs, so they vary: some are clean and roughly centred,
others drift, overshoot, are noisy, or are shifted well off to one side. A good
solution should cope with all of them, not just the tidy ones.

## Your task

Write a function that takes one sweep and splits its samples into three groups:

- `left` — the flow lobe on the low-position side,
- `deadband` — the central near-zero-flow band, and
- `right` — the flow lobe on the high-position side.

```python
def split_sweep(position: list[float], flow: list[float]) -> dict[str, list[int]]:
    """Return {"left": [...], "deadband": [...], "right": [...]},
    where each value is a list of integer indices into the input lists."""
```

Then, as the headline result, report the two **deadband edge positions** for each
sweep — the `normalised_position` at which flow leaves the deadband on the left
and on the right.

## What we provide

- `data/` — the six sweep files.
- `sweep_tools.py` — `load_sweep(path)` returns aligned `(position, flow)` lists,
  and `plot_split(...)` will draw a sweep and colour your segments. Use, change,
  or ignore these as you like. (Plotting needs `matplotlib`; the loader does not.)

## What to hand back

1. Your code, runnable, with a short note on how to run it.
2. A figure per sweep showing your split (the helper makes this easy), or an
   equivalent way for us to see your result on all six.
3. A short write-up (half a page is plenty) covering:
   - the idea behind your method and why you chose it,
   - which sweeps it handles well and which it struggles with, and how you know,
   - what you would do with more time.

## How we will assess it

- **Robustness first.** Does it hold up across the varied sweeps, including the
  awkward ones? A method that is simple but degrades gracefully beats a clever
  one that breaks silently.
- **Reasoning.** Do your choices make sense, and do you understand your method's
  failure modes? Being honest about where it breaks scores well.
- **Clarity.** Readable, sensibly structured code and a clear write-up.

You may use any standard Python libraries. There is no hidden "correct" answer —
show us how you think.
