struct Queue {
  struct DynamicArray *arr;
};

struct Queue *create_queue();

int enqueue(struct Queue *queue, int *value);
int dequeue(struct Queue *queue);