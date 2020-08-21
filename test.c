#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/wait.h>

int main()
{
    int hi[] = {5, 10, 15};
    int *yo;                          // parent process will write this message
    char child_message[] = "goodbye"; // child process will then write this one

    int protection = PROT_READ | PROT_WRITE;
    int visibility = MAP_SHARED | MAP_ANONYMOUS;
    void *meme = mmap(NULL, 3, protection, visibility, -1, 0);

    //memcpy(meme, hi, __SIZEOF_INT__);

    memcpy(meme, &hi[0], 4);
    int pid = fork();
    if (pid == 0)
    {
        yo = meme;
        memcpy(meme, &hi[1], 4);
        memcpy(yo, meme, 3);
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
}