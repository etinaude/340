/*
    The sorting program to use for Operating Systems Assignment 1 2020
    written by Robert Sheehan

    Modified by: Etienne Naude
    UPI: enau831

    By submitting a program you are claiming that you and only you have made
    adjustments and additions to this code.

    clear;cc   -O2   a1.1.c -o   1 -pthread;time ./1 10
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/resource.h>
#include <stdbool.h>
#include <sys/times.h>
#include <pthread.h>

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

    int rc;
    size_t s1;
    s1 = 4096;
    pthread_attr_t attr;
    rc = pthread_attr_init(&attr);
    rc = pthread_attr_setstacksize(&attr, s1);
    pthread_t ptid;
    int e = 0;

    struct block *my_data = value;

    //printf("\n\n\n %d \n\n\n\n", (*my_data).size);
    if ((*my_data).size < 2)
        return value;
    int pivot_pos = split_on_pivot(*my_data);

    struct block left_side, right_side;

    left_side.size = pivot_pos;
    left_side.data = (*my_data).data;
    right_side.size = (*my_data).size - pivot_pos - 1;
    right_side.data = (*my_data).data + pivot_pos + 1;
    int a;
    e = pthread_create(&ptid, &attr, &quick_sort, (void *)&left_side);
    if (e)
    {
        //printf("\n1,%d ", e);
        quick_sort((void *)&left_side);
        quick_sort((void *)&right_side);
        a = 0;
    }
    else
    {
        quick_sort((void *)&right_side);
        a = 1;
        e = pthread_join(ptid, NULL);
        if (e)
        {
            //printf("\n3,%d ", e);
        }
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
    exit(EXIT_SUCCESS);
}