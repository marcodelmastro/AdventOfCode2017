# Advent Of Code 2017

## ChangeLog

* **Day 1**: 2021-02-05
* **Day 2**: 2021-02-05
* **Day 3**: 2021-02-05
* **Day 4**: 2021-02-05
* **Day 5**: 2021-02-05
* **Day 6: 2021-02-05
* **Day 7**: 2021-02-06
  * Part 1: Simple tree navigation using dictionary
  * Part 2: Recursive function to compute tower weight + tree searching
* **Day 8**: 2021-02-06
  * Programming instructions to increase and decrease register values. 
  * Using `defaultdict` to store values in order to avoid having to pre-process register names.
* **Day 9**: 2021-02-07
  * String processing. Use raw string `r''` to avoid missing special characters.
* **Day 10**: 2021-02-08
  * Array slicing and manipulation (simple circular list), ASCII codes, `hex` decoding. Boring.
* **Day 11**: 2021-02-08
  * Hexe grid representation on square grid, with distance calculation.
* **Day 12**: 2021-02-08
  * Recursive connections to be sorted out.
* **Day 13**: 2021-02-09
  * Multiple modular calculations to match criterion.
* **Day 14**: 2021-02-09
  * Recursive implementation of flood-fill algorithm algorithm. Uses Day 10 hashing algorihtm to generate initial matrix.
* **Day 15**: 2021-02-09
  * Linear congruent generators. Using `yield` to align generators with different period.
* **Day 16**: 2021-02-10
  * More string manipulation. Part 2 was a HUGE loop, to be solved looking for a shorter period.
* **Day 17**: 2021-02-10
  * Simple array manipulation for Part 1. Part 2 could not be solved with Part 1 code (too large array size), but it was enough to keep track of one array position and and total (virtual) array lenght.
* **Day 18**: 2021-02-10
  * Part 1: another pseudo-assembly program
  * Part 2: asyncrounous execution of two programs with mutual I/O
* **Day 19**: 2021-02-10
  * Path navigation using complex numbers for coordinates and (change of) directions.
* **Day 20**: 2021-02-11
  * Simplified 3D particle simulation (distances, collisions).
* **Day 21**: 2021-02-11
  * A sort of Conway's Game of Life with pre-ritten evolution/expansion rules. `numpy` to rotate and flip, a lot array broadcasting. 
* **Day 22**: 2021-02-11
  * Another sort of Conway's Game of Life, now with a vector changing the grid status and moving accoridng to it. Again, using complex numbers for position and (change or) direction proves very handy! Grid status saved in a dictionary since the grid size is infininte.
* **Day 23**:
  * Part 1: 2021-02-11. Again a pseudo-assembly interpreter.
  * Part 2: 2021-02-12. In order to do this I had to figure out what the program was doing in Part 2, and then coding in a more efficient way... I manage to do it by looking at the registers and studying the program starting from the end instructions and going backward. Very difficult!

