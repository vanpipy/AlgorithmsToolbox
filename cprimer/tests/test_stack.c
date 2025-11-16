#include "unity.h"
#include "array.h"
#include "stack.h"

struct Stack *stack;

void setUp(void) { stack = create_stack(); }
void tearDown(void) {}

void test_append(void) {
  int a = 1;
  int b = 2;
  int c = 3;
  stack_append(stack, &a);
  TEST_ASSERT_EQUAL_INT(1, (*(int *)stack->arr->data[stack->arr->size - 1]));
  stack_append(stack, &b);
  TEST_ASSERT_EQUAL_INT(2, (*(int *)stack->arr->data[stack->arr->size - 1]));
  stack_append(stack, &c);
  TEST_ASSERT_EQUAL_INT(3, (*(int *)stack->arr->data[stack->arr->size - 1]));
}

void test_remove(void) {
  TEST_ASSERT_EQUAL_INT(2, (*(int *)stack_remove(stack)));
  TEST_ASSERT_EQUAL_INT(1, (*(int *)stack_remove(stack)));
  TEST_ASSERT_EQUAL_INT(0, (*(int *)stack_remove(stack)));
}

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_append);
  RUN_TEST(test_remove);
  return UNITY_END();
}