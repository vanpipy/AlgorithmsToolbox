#include "array.h"
#include "queue.h"
#include "unity.h"
#include "unity_internals.h"


struct Queue *queue;

void setUp(void) { queue = create_queue(); }

void tearDown() {}

void test_enqueue_and_return_size_of_queue(void) {
  enqueue(queue, 0);
  TEST_ASSERT_EQUAL_INT(1, queue->arr->size);
}

void test_dequeue_and_return_value(void) {
  int a = 1;
  int b = 2;
  enqueue(queue, &a);
  enqueue(queue, &b);
  TEST_ASSERT_EQUAL_INT(1, dequeue(queue));
}

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_enqueue_and_return_size_of_queue);
  RUN_TEST(test_dequeue_and_return_value);
  return UNITY_END();
}
