#include <stdio.h>
#include <stdlib.h>

struct Qnode {
    int Data;
    struct Qnode *Next;
};

struct Queue {
    struct Qnode *Front, *Rear;
};

struct Qnode* newNode(int k) {
    struct Qnode* temp = (struct Qnode*)malloc(sizeof(struct Qnode));
    temp->Data = k;
    temp->Next = NULL;
    return temp;
}

struct Queue* createQueue() {
    struct Queue* q = (struct Queue*)malloc(sizeof(struct Queue));
    q->Front = q->Rear = NULL;
    return q;
}


void enQueue(struct Queue* q, int k) {
    struct Qnode* temp = newNode(k);
    if (q->Rear == NULL) {
        q->Front = q->Rear = temp;
        return;
    }
    q->Rear->Next = temp;
    q->Rear = temp;
}

void deQueue(struct Queue* q) {
    if (q->Front == NULL)
        return;
    struct Qnode* temp = q->Front;
    q->Front = q->Front->Next;
    if (q->Front == NULL) {
        q->Rear = NULL;
    }
    free(temp);
}

int main() {
    struct Queue* q = createQueue();
    enQueue(q, 10);
    enQueue(q, 20);
    deQueue(q);
    deQueue(q);
    enQueue(q, 30);
    enQueue(q, 40);
    enQueue(q, 50);
    deQueue(q);
    printf("Queue Front : %d \n", ((q->Front != NULL)) ? (q->Front)->Data : -1);
    printf("Queue Rear : %d", ((q->Rear != NULL)) ? (q->Rear)->Data : -1);
    return 0;
}

