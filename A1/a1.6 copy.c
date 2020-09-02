/*
    The sorting program to use for Operating Systems Assignment 1 2020
    written by Robert Sheehan

    Modified by: Etienne Naude
    UPI: enau831

    By submitting a program you are claiming that you and only you have made
    adjustments and additions to this code.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/resource.h>
#include <stdbool.h>
#include <sys/times.h>
#include <sys/wait.h>
#include <sys/mman.h>

#define SIZE 10

struct block
{
    int size;
    int *data;
};

void print_data(struct block my_data)
{
    for (int i = 0; i < my_data.size; ++i)
        printf("%d ", my_data.data[i]);
    printf("\n");
}

/* Split the shared array around the pivot, return pivot index. */
int split_on_pivot(struct block my_data)
{
    int right = my_data.size - 1;
    int left = 0;
    int pivot = my_data.data[right];
    //printf("Pivot %d \n", pivot);
    while (left < right)
    {
        int value = my_data.data[right - 1];
        if (value > pivot)
        {
            my_data.data[right--] = value;
        }
        else
        {
            my_data.data[right - 1] = my_data.data[left];
            my_data.data[left++] = value;
        }
    }
    my_data.data[right] = pivot;
    return right;
}

/* Quick sort the data. */
void *quick_sort(void *value)
{
    int protection = PROT_READ | PROT_WRITE;
    int visibility = MAP_SHARED | MAP_ANONYMOUS;
    struct block *my_data = value;
    if ((*my_data).size < 2)
        return value;
    int pivot_pos = split_on_pivot((*my_data));

    struct block left_side, right_side;
    left_side.data = mmap(NULL, left_side.size * sizeof(int), protection, visibility, -1, 0);
    int *delay = mmap(NULL, 4, protection, visibility, -1, 0);
    *delay = 0;
    left_side.size = pivot_pos;
    left_side.data = (*my_data).data;
    //printf("data %d\n", *left_side.data);
    right_side.size = (*my_data).size - pivot_pos - 1;
    right_side.data = (*my_data).data + pivot_pos + 1;
    if (left_side.size > 4)
    {
        int result;
        int *yo;
        //printf("%d,,%p\n", left_side.size, meme);
        int forks = fork();
        if (forks == 0)
        {
            int hi = 123;
            printf("C0: %d\n", *left_side.data);
            quick_sort((void *)&left_side);
            *left_side.data = 111;
            printf("C1: %d\n", *left_side.data);
            *delay = 6;
            exit(0);
        }
        else
        {
            //printf("p0: %d\n", *left_side.data);
            //printf("%d 1delay\n", *delay);
            quick_sort((void *)&right_side);
            wait(NULL);
            /*while (!*delay)
            {
                printf("%d\n", *delay);
            }*/
            /*for (int i = 0; i < 1000; i++)
            {

                printf("%d 2delay\n", *delay);
            }*/
            printf("p1 %d\n", *left_side.data);
            //sleep(50);
            //left_side.data = *meme;
            //printf("|r0|m:%p| d:%p|t:%d|\n", (&meme), &left_side.data, getpid());
            //printf("|r1|m:%p| d:%p|t:%d|\n", meme, left_side.data, getpid());
        }
        /*
    if (pid == 0)
    {
        yo = meme;
        memcpy(meme, &hi[1], 4);
        printf("Child read: %d\n", *yo);
        exit(0);
    }
    else
    {
        //printf("Parent read: %s\n", meme);
        wait(NULL);
        memcpy(&yo, meme, 4);
        printf("parent %d\n", yo);
    }

*/

        //munmap(meme, left_side.size * sizeof(int));
    }
    else
    {
        //printf("3\n");
        quick_sort((void *)&left_side);
        quick_sort((void *)&right_side);
    }
}

/* Check to see if the data is sorted. */
bool is_sorted(struct block my_data)
{
    bool sorted = true;
    for (int i = 0; i < my_data.size - 1; i++)
    {
        if (my_data.data[i] > my_data.data[i + 1])
            sorted = false;
    }
    return sorted;
}

/* Fill the array with random data. */
void produce_random_data(struct block my_data)
{
    srand(1); // the same random data seed every time
    for (int i = 0; i < my_data.size; i++)
    {
        my_data.data[i] = rand() % 1000;
    }
}

int main(int argc, char *argv[])
{
    long size;

    if (argc < 2)
    {
        size = SIZE;
    }
    else
    {
        size = atol(argv[1]);
    }
    struct block start_block;
    start_block.size = size;
    start_block.data = (int *)calloc(size, sizeof(int));
    if (start_block.data == NULL)
    {
        printf("Problem allocating memory.\n");
        exit(EXIT_FAILURE);
    }

    produce_random_data(start_block);

    if (start_block.size < 1001)
        print_data(start_block);

    struct tms start_times, finish_times;
    times(&start_times);
    printf("start time in clock ticks: %ld\n", start_times.tms_utime);
    quick_sort((void *)&start_block);
    times(&finish_times);
    printf("finish time in clock ticks: %ld\n", finish_times.tms_utime);

    if (start_block.size < 1001)
        print_data(start_block);

    printf(is_sorted(start_block) ? "sorted\n" : "not sorted\n");
    free(start_block.data);
    //*/
    exit(EXIT_SUCCESS);
}