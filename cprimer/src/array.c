#include "array.h"
#include <stdlib.h>

struct DynamicArray *create_array() {
  struct DynamicArray *arr;
  arr->size = 0;
  arr->capacity = DEFAULT_CAPACITY;
  arr->data = (int *)malloc(arr->capacity * sizeof(int));
  return arr;
}

void resize(struct DynamicArray *arr, int scale) {
  struct DynamicArray *new_arr;
  new_arr->capacity = arr->capacity * (2^scale);
  new_arr->data = (int *)realloc(arr->data, new_arr->capacity * sizeof(int));
  arr->capacity = new_arr->capacity;
  arr->data = new_arr->data;
  free(new_arr);
}

int push(struct DynamicArray *arr, int value) {
  if (arr->capacity < arr->size + 1) {
    resize(arr, 1);
  }
  arr->data[arr->size + 1] = value;
  arr->size = arr->size + 1;
  return arr->size;
}

int pop(struct DynamicArray *arr) {
  if (arr->size == 0) {
    return CANNOT_DONE;
  }
  if (arr->size - 1 < arr->capacity / 2) {
    resize(arr, -1);
  }
  arr->size = arr->size - 1;
  int temp = arr->data[arr->size - 1];
  arr->data[arr->size - 1] = EMPTY_VALUE;
  return temp;
}

int shift(struct DynamicArray *arr) {
  if (arr->size == 0) {
    return CANNOT_DONE;
  }
  if (arr->size - 1 < arr->capacity / 2) {
    resize(arr, -1);
  }
  arr->size = arr->size - 1;
  int temp = arr->data[0];
  for (int i = 0; i < arr->size; i++) {
    arr->data[i] = arr->data[i + 1];
  }
  arr->data[arr->size - 1] = EMPTY_VALUE;
  return temp;
}