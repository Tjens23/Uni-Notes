
# Counting Sort Algorithm - Detailed Notes

## Overview

Counting Sort is a non-comparison based sorting algorithm that works by counting the occurrences of each distinct element in the input array. It's particularly efficient when the range of possible values (k) is not significantly larger than the number of elements (n).

## Time Complexity

- **Time Complexity:** O(n + k)
- **Space Complexity:** O(k)
- **Stable:** Yes (maintains relative order of equal elements)

## Step-by-Step Walkthrough

### Given Input Array

$$A = [2, 4, 1, 2, 5, 0, 4, 1]$$

### Step 1: Find the Range (k)

First, we need to determine the range of values in our input array.

- **Maximum value:** $\max(A) = 5$
- **Minimum value:** $\min(A) = 0$
- **Range calculation:** $k = \max - \min + 1 = 5 - 0 + 1 = 6$

The range k = 6 means we need to track counts for values 0, 1, 2, 3, 4, and 5.

### Step 2: Initialize Counting Array C

Create a counting array C of size k, initialized with zeros:

$$C = [0, 0, 0, 0, 0, 0]$$

**Index mapping:**

- C[0] → count of value 0
- C[1] → count of value 1
- C[2] → count of value 2
- C[3] → count of value 3
- C[4] → count of value 4
- C[5] → count of value 5

### Step 3: Count Occurrences

Iterate through the input array A and count occurrences of each value:

**Counting process:**

- Value 2 appears at indices 0, 3 → C[2] += 2
- Value 4 appears at indices 1, 6 → C[4] += 2
- Value 1 appears at indices 2, 7 → C[1] += 2
- Value 5 appears at index 4 → C[5] += 1
- Value 0 appears at index 5 → C[0] += 1

**Result after counting:** $$C = [1, 2, 2, 0, 2, 1]$$

**Interpretation:**

- 0 appears 1 time
- 1 appears 2 times
- 2 appears 2 times
- 3 appears 0 times
- 4 appears 2 times
- 5 appears 1 time

### Step 4: Calculate Cumulative Sums

Transform the counting array into a cumulative sum array. Each C[i] will represent the number of elements ≤ i.

**Cumulative sum calculation:**

- $C[0] = 1$ (unchanged)
- $C[1] = C[0] + C[1] = 1 + 2 = 3$
- $C[2] = C[1] + C[2] = 3 + 2 = 5$
- $C[3] = C[2] + C[3] = 5 + 0 = 5$
- $C[4] = C[3] + C[4] = 5 + 2 = 7$
- $C[5] = C[4] + C[5] = 7 + 1 = 8$

**Final cumulative array:** $$C = [1, 3, 5, 5, 7, 8]$$

**Interpretation of cumulative sums:**

- C[0] = 1: There is 1 element ≤ 0
- C[1] = 3: There are 3 elements ≤ 1
- C[2] = 5: There are 5 elements ≤ 2
- C[3] = 5: There are 5 elements ≤ 3
- C[4] = 7: There are 7 elements ≤ 4
- C[5] = 8: There are 8 elements ≤ 5

### Step 5: Build Output Array (Final Sorting)

The cumulative sums tell us the final positions of elements in the sorted array. For each element in the original array (processing right to left for stability):

**Process:** For each element `x` in A:

- C[x] gives the position where x should be placed
- Place x at position C[x] - 1 (0-indexed)
- Decrement C[x]

**Final sorted array:** $$\text{Sorted } A = [0, 1, 1, 2, 2, 4, 4, 5]$$

## Algorithm Properties

### Advantages
<
- **Linear time complexity** O(n + k) when k = O(n)
- **Stable sorting** algorithm
- **Not in-place** but predictable space usage
- **No comparisons** needed between elements

### Disadvantages

- **Space complexity** increases with range k
- **Only works** with integers or objects that can be mapped to integers
- **Inefficient** when k >> n (range much larger than input size)

### Best Use Cases

- Sorting integers with small range
- Counting frequencies of elements
- As a subroutine in radix sort
- When stability is required and range is manageable