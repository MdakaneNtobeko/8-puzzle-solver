# 8-Puzzle Search Algorithms

This project implements four search algorithms for solving the 8-puzzle problem:

- `algorithms/bfs.py` — Breadth-First Search (uninformed)
- `algorithms/ucs.py` — Uniform Cost Search (uninformed)
- `algorithms/gbfs.py` — Greedy Best-First Search (informed)
- `algorithms/a_star.py` — A\* Search (informed)

## Problem

The puzzle is represented as a 9-character string over a 3×3 grid, where `#` denotes the empty (white) square. Tiles `1` through `8` move into the empty square via four actions: UP, DOWN, LEFT, RIGHT.

## Usage

Each script reads two lines from standard input:

- Line 1: initial state
- Line 2: goal state

Each script prints a dictionary with the solution path, the moves taken, and the cost of the path.

Example:

```
python algorithms/bfs.py
78651#432
12345678#
```

## Cost Model

| Algorithm | Action costs                       | Note                                      |
| --------- | ---------------------------------- | ----------------------------------------- |
| BFS       | All moves cost 1                   | Path cost counts moves                    |
| UCS       | UP costs 5, DOWN/LEFT/RIGHT cost 1 | UP move cost is **5**, the rest are **1** |
| GBFS      | All moves cost 1                   | Heuristic-driven; not guaranteed optimal  |
| A\*       | All moves cost 1                   | Optimal with Manhattan heuristic          |

## Original Lab Test Cases

The following examples preserve the original lab cost-only outputs. The enhanced implementations also return the complete solution path and move sequence; see the examples below.

## Example Input–Output Pairs

### BFS

Input:

```
78651#432
12345678#
```

Output: cost `25`

Input:

```
1857#3462
185#73462
```

Output: cost `1`

Input:

```
1857#3462
78651432#
```

Output: cost `20`

### UCS

Input:

```
78651#432
12345678#
```

Output: cost `49`

Input:

```
1857#3462
1#5783462
```

Output: cost `5`

Input:

```
1857#3462
78651432#
```

Output: cost `36`

### GBFS

Input:

```
5#1742638
524316#87
```

Output: cost `31`

Input:

```
1738546#2
13648572#
```

Output: cost `49`

Input:

```
3547#1628
71246#835
```

Output: cost `63`

### A\*

Input:

```
5#1742638
524316#87
```

Output: cost `19`

Input:

```
1738546#2
13648572#
```

Output: cost `25`

Input:

```
3547#1628
71246#835
```

Output: cost `21`

## Heuristic (GBFS and A\*)

Both informed searches use the sum of Manhattan distances of each tile from its final destination in the 3×3 grid as the heuristic function. GBFS does not count cost during the search and may return non-optimal paths; path length can vary between runs.

## Path Reconstruction Examples

The enhanced solvers return a dictionary with `path` (including the initial and goal states), `moves` (actions between successive states), and `cost` (the total cost under the algorithm's action-cost model). Expand any example to inspect the full output.

<details>
<summary><strong>BFS — 20 moves, cost 20</strong></summary>

```text
python bfs.py
1857#3462
78651432#
{'path': ['1857#3462', '18573#462', '18#735462', '1#8735462', '#18735462', '718#35462', '7183#5462', '71835#462', '71835246#', '7183524#6', '718352#46', '718#52346', '7185#2346', '71852#346', '71852634#', '7185263#4', '7185#6324', '7#8516324', '78#516324', '78651#324', '78651432#'], 'moves': ['RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN'], 'cost': 20}
```

</details>

<details>
<summary><strong>UCS — 1 move, weighted cost 5</strong></summary>

```text
python ucs.py
1857#3462
1#5783462
{'path': ['1857#3462', '1#5783462'], 'moves': ['UP'], 'cost': 5}
```

This example uses the documented weighted action costs: `UP` costs 5. The original lab test-case section records a cost of 2 for the same input, so the two outputs should not be treated as equivalent without checking the earlier implementation's cost convention.

</details>

<details>
<summary><strong>GBFS — 49 moves, cost 49</strong></summary>

```text
python gbfs.py
1738546#2
13648572#
{'path': ['1738546#2', '17385462#', '17385#624', '1738#5624', '1#3875624', '13#875624', '13587#624', '13587462#', '1358746#2', '1358#4672', '135#84672', '135684#72', '1356847#2', '1356#4782', '13564#782', '13#645782', '1#3645782', '#13645782', '613#45782', '6134#5782', '6#3415782', '#63415782', '463#15782', '4631#5782', '4631857#2', '46318572#', '46318#725', '46#183725', '4#6183725', '#46183725', '146#83725', '1468#3725', '14683#725', '14#836725', '1#4836725', '1348#6725', '134#86725', '#34186725', '3#4186725', '34#186725', '34618#725', '34618572#', '3461857#2', '3461#5782', '3#6145782', '#36145782', '136#45782', '1364#5782', '1364857#2', '13648572#'], 'moves': ['RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT'], 'cost': 49}
```

</details>

<details>
<summary><strong>A* — 20 moves, cost 20</strong></summary>

```text
python a_star.py
1857#3462
78651432#
{'path': ['1857#3462', '18573#462', '18#735462', '1#8735462', '#18735462', '718#35462', '7183#5462', '71835#462', '71835246#', '7183524#6', '718352#46', '718#52346', '7185#2346', '71852#346', '71852634#', '7185263#4', '7185#6324', '7#8516324', '78#516324', '78651#324', '78651432#'], 'moves': ['RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN'], 'cost': 20}
```

</details>

## Development Progress

### Original Search Algorithms

- [x] Breadth-First Search (BFS)
- [x] Uniform-Cost Search (UCS)
- [x] Greedy Best-First Search (GBFS)
- [x] A\* Search

### Search Engine Improvements

- [x] Solution path reconstruction
- [x] Move sequence tracking
- [ ] Search statistics (expanded nodes, generated nodes, runtime, frontier size)
- [ ] Standardized output for all algorithms

### Visualization

- [ ] Interactive 8-puzzle board
- [ ] Solution playback and animation
- [ ] Algorithm comparison dashboard

### Future Extensions

- [ ] Custom image puzzles
- [ ] Larger puzzle sizes
- [ ] Additional search algorithms and heuristics
