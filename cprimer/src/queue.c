#include <stdlib.h>
#include "queue.h"
#include "array.h"

struct Queue *create_queue() {
  struct Queue *queue = malloc(sizeof(struct Queue));
  queue->arr = create_array();
  return queue;
}

int enqueue(struct Queue *queue, int value) {
  push(queue->arr, value);
  return queue->arr->size;
}

int dequeue(struct Queue *queue) {
  return shift(queue->arr);
}