#include <stdlib.h>
#include "unity.h"
#include "array.h"

struct DynamicArray *arr;

void setUp(void) {
  arr = create_array();
}

void tearDown() {
  free(arr);
}

void test_arr_has_8_capacity_default(void) {
  TEST_ASSERT_EQUAL_INT(8, arr->capacity);
}

void test_push_and_return_arr_size(void) {
  TEST_ASSERT_EQUAL_INT(arr->size, push(arr, 1));
}

void test_pop_and_return_removed_value(void) {
  TEST_ASSERT_EQUAL_INT(1, pop(arr));
}

void test_push_9_times_and_trigger_resize(void) {
  for (int i = 1; i <= 9; i++) {
    push(arr, i);
  }
  TEST_ASSERT_EQUAL_INT(16, arr->capacity);
}

void test_pop_when_size_less_than_8_and_trigger_resize(void) {
  pop(arr);
  pop(arr);
  TEST_ASSERT_EQUAL_INT(8, arr->capacity);
}

void test_pop_and_the_empty_equals_empty_value(void) {
  TEST_ASSERT_EQUAL_INT(EMPTY_VALUE, arr->data[arr->size - 1]);
}

void test_pop_is_blocked_when_size_is_0(void) {
  for (int i = 0; i <= 6; i++) {
    pop(arr, i);
  }
  TEST_ASSERT_EQUAL_INT(CANNOT_POP, pop(arr));
}
