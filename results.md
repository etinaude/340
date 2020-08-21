# Results

- Name: Etienne Naude
- UPI: enau831
- ID: 768485633

## System Information

- Computer 1

  - WSL (Ubuntu 20.04 LTS)
  - 16 Threads, 8 core
  - CPU: i5-10210u
  - RAM: 8GB
  - CC version: 9.3.0

- Computer 2

  - Kubuntu 20.04 LTS Native
  - 4 Threads, 4 core
  - CPU: i5-4590 (similar)
  - RAM: 8GB
  - CC version: 9.2.1

## Summary

Unfortunately I Started compiling and running my programmes on Computer 1 with native Kubuntu but I ran into a hard drive issue and lost my partitions, but from having to move to using WSL I found the time difference and consistency was drastically different so I decided to run all my tests again on a separate Native linux computer. The results are bellow, each test used a 10,000,000 input size, the real time is listed in the first line in seconds and the clock ticks is in the seconds

## Seed 1, Computer 1

| Step | 1         | 2         | 3         | Average |
| ---- | --------- | --------- | --------- | ------- |
| 1    | 79.529 s  | 79.860 s  | 80.613 s  |         |
|      | 7946 t    | 7981 t    | 8053 t    |         |
| 2    | 84.838 s  | 83.398 s  | 83.511 s  |         |
|      | 8803 t    | 8631 t    | 8714 t    |         |
| 3    | 83.768 s  | 83.378 s  | 82.077 s  |         |
|      | 8803 t    | 8631 t    | 8714 t    |         |
| 4    | 84.334 s  | 84.195 s  | 83.586 s  |         |
|      | 8720 t    | 8707 t    | 8612 t    |         |
| 5    | 139.712 s | 141.075 s | 149.215 s |         |
|      | 13939 t   | 8092 t    | 13885t    |         |
| 6    | 59.275 s  | 56.706 s  | 55.929 s  |         |
|      | 2259 t    | 2176 t    | 2218 t    |         |
| 7    | 137.628 s | 136.664 s | 137.140 s |         |
|      | 13734 t   | 13654 t   | 13704 t   |         |
| 8    |           |           |           |         |
|      |           |           |           |         |

## Seed 1, Computer 2

| Step | 1        | 2        | 3        | Average      |
| ---- | -------- | -------- | -------- | ------------ |
| 1    | 41.863 s | 41.860 s | 41.860 s | **41.861 s** |
|      | 4184 t   | 4184 t   | 4184 t   | 4184 t       |
| 2    | 40.642 s | 40.634 s | 40.869 s | **40.715 s** |
|      | 4196 t   | 4195 t   | 4219 t   | 4204 t       |
| 3    | 35.124 s | 35.318 s | 33.188 s | **34.543 s** |
|      | 5732 t   | 5655 t   | 5732 t   | 5706 t       |
| 4    | 40.741 s | 40.738 s | 40.742   | **40.740 s** |
|      | 4201 t   | 4201 t   | 4202 t   | 4201         |
| 5    | 40.641 s | 40.641 s | 40.644 s | **40.643 s** |
|      | 4060 t   | 4060 t   | 4061 t   | 4060 t       |
| 6    | 13.938 s | 14.220 s | 13.523 s | **13.894 s** |
|      | 414 t    | 415 t    | 416 t    | 415 t        |
| 7    | 13.976 s | 14.001 s | 14.104s  | **14.027 s** |
|      | 20 t     | 21 t     | 20 t     | 20 t         |
| 8    |          |          |          |              |
|      |          |          |          |              |

The variation for the WSL was much higher than native linux where native linux was getting around 1 or 2 ticks range (other than the step 3 outlier), the WSL computer would get a variation upwards of 100.

## Step 1

This step was slow since it had no parallelization

## Step 2

This is slightly quicker but not substantially so

## Step 3

AAAH PAIN
AAAH MORE PAIN

## Step 4

## Step 5

## Step 6

| input | seed | split     | 1          |
| ----- | ---- | --------- | ---------- |
|       | 1    |           |            |
|       |      | 8,000,000 | 44.518s    |
|       |      | 5,000,000 | 45.915s    |
|       |      | 1,000,000 | 40.506s    |
|       |      | 800,000   | 41.278s    |
|       |      | 500,000   | 41.824s    |
|       |      | 200,000   | 40.904s    |
|       |      | 80,000    | 43.356s    |
|       |      | 50,000    | 42.531s    |
|       |      | 20,000    | Not Sorted |
|       |      | 18,000    | Not Sorted |
|       | 2    |           |            |
|       |      | 4,000,000 | 43.562s    |
|       |      |           | 56.352s    |
|       |      |           | 56.685s    |
|       |      | 3,000,000 | 39.817s    |
|       |      |           | 40.053s    |
|       |      |           | 40.239s    |
|       |      | 2,500,000 | 40.228s    |
|       |      | 2,000,000 | 40.073s    |
|       |      |           | 40.500s    |
|       |      | 1,500,000 | 44.657s    |
|       |      |           | 41.960s    |
|       |      | 1,200,000 | 42.862s    |
|       |      | 200,000   | 43.768s    |
|       | 3    |           |            |
|       |      | 4,000,000 | 39.219s    |
|       |      |           | 41.101s    |
|       |      | 3,500,000 | 40.663s    |
|       |      |           | 41.338s    |
|       |      | 3,000,000 | 41.723s    |
|       |      |           | 41.771s    |
|       |      | 2,500,000 | 41.336s    |
|       |      |           | 42.434s    |
|       |      | 2,000,000 | 42.123s    |
|       |      |           | 43.097s    |
|       | 4    |           |            |
|       |      | 4,000,000 | 44.334s    |
|       |      | 3,000,000 | 41.226s    |
|       |      | 2,000,000 | 44.656s    |
|       | 5    |           |            |
|       |      | 4,000,000 | 43.081s    |
|       |      | 3,000,000 | 44.727s    |
|       |      | 2,000,000 | 41.533s    |
|       | 6    |           |            |
|       |      | 4,000,000 | 42.860s    |
|       |      |           | 42.871s    |
|       |      |           | 40.128s    |
|       |      | ave       | 41.953s    |
|       |      | range     | 2.743s     |
|       |      |           |            |
|       |      | 3,000,000 | 43.487s    |
|       |      |           | 42.043s    |
|       |      |           | 43.908s    |
|       |      | ave       | 43.146s    |
|       |      | range     | 1.865      |
|       |      |           |            |
|       |      | 2,000,000 | 40.340s    |
|       |      |           | 40.219s    |
|       |      |           | 41.237s    |
|       |      | ave       | 40.599s    |
|       |      | range     | 1.018s     |

kubutnu

| input | seed | split     | 1        |
| ----- | ---- | --------- | -------- |
|       | 1    | 1,000,000 | 12.203 s |
|       |      | 800,000   | 11.525 s |
|       |      | 900,000   | 11.003 s |
|       |      | 950,000   | 11.665 s |

# Step 7

| seed | split     | 1        |
| ---- | --------- | -------- |
| 1    | 5,000,000 | 38,203 s |
|      | 3,000,000 | 20,494 s |
|      | 2,000,000 | 19.013 s |
|      | 1,000,000 | 17.007 s |
|      | 800,000   | 16.994 s |
|      | 500,000   | 15,832 s |
|      | 100,000   | 13.902 s |
|      | 95,000    | 13.765 s |
|      | 90,000    | 13.904 s |
|      | 80,000    | 14.108 s |
| 2    | 105,000   | 13.576 s |
|      | 100,000   | 13.601 s |
|      | 95,000    | 13.605 s |
|      | 90,000    | 12.860 s |
|      | 85,000    | 13,109 s |
| 3    | 100,000   | 14,444 s |
|      | 95,000    | 13.928 s |
|      | 90,000    | 13,631 s |
|      | 85,000    | 13.516 s |
