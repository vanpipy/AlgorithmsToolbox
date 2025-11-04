#ifndef ARRAY_H
#define ARRAY_H

#define DEFAULT_CAPACITY 8
#define EMPTY_VALUE -1
#define CANNOT_DONE -1

struct DynamicArray {
  int *data;
  int size;
  int capacity;
};

struct DynamicArray *create_array();
int push(struct DynamicArray* arr, int value);
int pop(struct DynamicArray* arr);
int shift(struct DynamicArray* arr);

#endif // ARRAY_H
