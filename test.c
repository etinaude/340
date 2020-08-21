#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

int main()
{
    char parent_message[] = "hello";  // parent process will write this message
    char child_message[] = "goodbye"; // child process will then write this one

    int protection = PROT_READ | PROT_WRITE;
    int visibility = MAP_SHARED | MAP_ANONYMOUS;
    void *meme = mmap(NULL, 1000, protection, visibility, -1, 0);

    memcpy(meme, parent_message, sizeof(parent_message));

    int pid = fork();

    if (pid == 0)
    {
        printf("Child read: %s\n", meme);
        memcpy(meme, child_message, sizeof(child_message));
        printf("Child wrote: %s\n", meme);
        exit(0);
    }
    else
    {
        //printf("Parent read: %s\n", meme);
        wait(NULL);
        printf("After 1s, parent read: %s\n", meme);
    }
}