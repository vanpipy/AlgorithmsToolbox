#ifndef STACK_H
#define STACK_H

struct Stack {
  struct DynamicArray *arr;
};

struct Stack *create_stack(void);
void stack_append(struct Stack *stack, int *value);
int *stack_remove(struct Stack *stack);

#endif // STACK_H