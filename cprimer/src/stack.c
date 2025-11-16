#include <stdlib.h>
#include "array.h"
#include "stack.h"

struct Stack *create_stack(void) {
  struct Stack *stack = malloc(sizeof(struct Stack));
  stack->arr = create_array();
  return stack;
}

void stack_append(struct Stack *stack, int *value) {
  push(stack->arr, value);
}

int *stack_remove(struct Stack *stack) {
  return pop(stack->arr);
}
