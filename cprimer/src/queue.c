#include <stdlib.h>
#include "array.h"
#include "queue.h"

struct Queue *create_queue() {
  struct Queue *queue = malloc(sizeof(struct Queue));
  queue->arr = create_array();
  return queue;
}

int enqueue(struct Queue *queue, int *value) {
  push(queue->arr, value);
  return queue->arr->size;
}

int dequeue(struct Queue *queue) {
  int *v = shift(queue->arr);
  return *v;
}