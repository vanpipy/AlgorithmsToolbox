#include "array.h"
#include <stdlib.h>

void resize(struct DynamicArray *arr, int scale) {
  if (!arr) {
    return;
  }
  int new_capacity = arr->capacity;
  if (scale > 0) {
    new_capacity = new_capacity << scale;
  } else if (scale < 0) {
    new_capacity = new_capacity >> -scale;
  }
  if (new_capacity < DEFAULT_CAPACITY) {
    new_capacity = DEFAULT_CAPACITY;
  }
  if (new_capacity == arr->capacity) {
    return;
  }

  void **new_data = (void **)realloc(arr->data, new_capacity * sizeof(void *));
  if (!new_data) {
    return;
  }

  if (new_capacity > arr->capacity) {
    for (int i = arr->capacity; i < new_capacity; i++) {
      new_data[i] = NULL;
    }
  }
  arr->data = new_data;
  arr->capacity = new_capacity;
}

struct DynamicArray *create_array() {
  struct DynamicArray *arr =
      (struct DynamicArray *)malloc(sizeof(struct DynamicArray));
  if (!arr) {
    return NULL;
  }
  arr->size = 0;
  arr->capacity = DEFAULT_CAPACITY;
  arr->data =
      (void **)calloc(arr->capacity, sizeof(void *));
  if (!arr->data) {
    free(arr);
    return NULL;
  }
  return arr;
}

int push(struct DynamicArray *arr, void *value) {
  if (!arr) {
    return -1;
  }
  if (arr->size >= arr->capacity) {
    resize(arr, 1);
  }
  arr->data[arr->size] = value;
  arr->size += 1;
  return arr->size;
}

void *pop(struct DynamicArray *arr) {
  if (!arr || arr->size == 0) {
    return NULL;
  }
  void *temp = arr->data[arr->size - 1];
  arr->data[arr->size - 1] = NULL;
  arr->size -= 1;
  if (arr->size < arr->capacity / 2) {
    resize(arr, -1);
  }
  return temp;
}

void *shift(struct DynamicArray *arr) {
  if (!arr || arr->size == 0) {
    return NULL;
  }
  void *temp = arr->data[0];
  for (int i = 0; i < arr->size - 1; i++) {
    arr->data[i] = arr->data[i + 1];
  }
  arr->size -= 1;
  arr->data[arr->size] = NULL;
  if (arr->size < arr->capacity / 2) {
    resize(arr, -1);
  }
  return temp;
}