An implementation of the following Deceptive Trap Function:

- For every 1 contained in each population member's bit string, fitness is increased by one point
- However, max fitness is attained when all bits are zero

To handle the deceptive aspect of this problem, a simplified version of Adaptive Group Mutation is used - https://www.cs.le.ac.uk/people/syang/Papers/WSEAS-TS04.pdf - If we find a duplicate string, flip every bit. This does not disrupt the overall logic, handles duplicates throughout the normal course of running the algorithm, and is generalizable to non-deceptive problems.

For tournament selection, given that all population members get to participate, picking the match-ups purely at random produces the best results both for strengthening the available genomes and preserving diversity. Even selecting specifically for Hamming difference performs worse.

Unlike with tournament selection, picking parents to reproduce should be done probabilistically based on score. Picking based on randomness or Hamming difference performs noticeably slower, especially with larger bit strings.

Only one elite is kept in order to promote diversity.

Handling mutation rate on a per string basis promotes convergence for high-scoring strings and exploration for lower-scoring ones. By applying the mutation rate cell by cell, rather than to a set amount of cells per string, additional stochasticity is added into the algorithm.
