#ifndef ARRAY_H
#define ARRAY_H

#define DEFAULT_CAPACITY 8

struct DynamicArray {
  void **data;
  int size;
  int capacity;
};

struct DynamicArray *create_array();
int push(struct DynamicArray* arr, void *value);
void *pop(struct DynamicArray* arr);
void *shift(struct DynamicArray* arr);

#endif // ARRAY_H
