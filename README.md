# Technical task: splitting a valve recording into arcs

Thanks for taking the time to do this. We are more interested in how you reason
about messy real data than in a perfect answer, so please don't over-invest —
something that works and that you can explain is exactly what we are after.

## Background

One of our machines performs a routine where a valve is moved while its linear
position and flow rate are measured continuously. This produces a stream of
position and flow readings that, when plotted against each other, form a
figure-of-eight shape. The routine is run twice in succession, with the second
pass producing a similar figure-of-eight but with inverted flow values. You are
given the full recording as a single continuous dataset.

## The task

Take the raw data and split it into four arcs — two from each pass. Each arc
should represent one lobe of a figure-of-eight.

### Splitting logic

The split point for each figure-of-eight is at the minimum flow region: the area
where the two lobes of the eight meet. Because of noise, the flow reaches its
minimum across a range of position values rather than at a single clean point.
Determine the split point using the median position value within that low-flow
region.

### Arc structure

The machine can begin recording at any point along a pass (at positive flow), so
the raw data will not necessarily start or end at a split point. After splitting,
join any partial segments so that each of the four arcs is contiguous and:

- starts at the centre position (minimum flow region),
- rises to peak flow and position (roughly the middle of the arc),
- returns to the centre position.

In other words, every arc should share its two tails with the minimum flow
region, with the highest flow values sitting in the middle of the arc.

## Requirements

- Use Python. You may use any libraries you like (NumPy, Pandas, SciPy,
  Matplotlib).
- Produce a visualisation of the data before and after the split so your result
  can be verified.
- Keep your code readable and well-commented. We value clarity over cleverness.
- A Jupyter notebook is perfectly fine.

## Assumptions

- Each data file contains two passes (one normal, one flow-inverted), giving four
  arcs in total.
- "Minimum flow" refers to the lowest flow values in each pass.
- You do not need to label or classify the arcs — just split, restructure and
  visualise.

## Tips

- Start by visualising and understanding the shape of the raw data.
- Think about edge cases: what if the recording starts or ends outside the
  minimum flow region?
- There is no single correct threshold for defining minimum flow.
- Focus on something that works and that you can justify. It does not have to be
  perfect.

## What we provide

- `data/` — six recordings (`sweep_01.json` … `sweep_06.json`). A good solution
  should cope with the awkward ones, not only the tidy ones.
- `sweep_tools.py` — `load_recording(path)` returns aligned
  `(position, flow, timestamp)` lists, and `plot_arcs(...)` will draw a recording
  and colour a set of arcs you pass in. Use, change or ignore these as you like.
  (`load_recording` needs only the standard library; `plot_arcs` requires `matplotlib`.)

## Example

The image below shows what a correct result looks like, using `sweep_01.json`.
Left: the raw recording as given. Right: the same data split into four
contiguous arcs, each running centre → peak → centre. The ★ marks the start
of each arc.

![Illustrative example on synthetic data](example/target_example.png)

## What to hand back

1. Your code, runnable, with a short note on how to run it.
2. Before/after visualisations across the recordings.
3. A short write-up (half a page is plenty): the idea behind your method, which
   recordings it handles well and where it struggles, and what you would do with
   more time.
