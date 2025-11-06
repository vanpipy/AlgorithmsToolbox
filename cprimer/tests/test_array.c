#include "array.h"
#include "unity.h"
#include <stdlib.h>

struct DynamicArray *arr;

void setUp(void) { arr = create_array(); }

void tearDown() {

}

void test_arr_has_8_capacity_default(void) {
  TEST_ASSERT_EQUAL_INT(8, arr->capacity);
}

void test_push_and_return_arr_size(void) {
  int *v = (int *)malloc(sizeof(int));
  *v = 1;
  TEST_ASSERT_EQUAL_INT(1, push(arr, v));
  TEST_ASSERT_EQUAL_INT(1, arr->size);
}

void test_pop_and_return_removed_value(void) {
  int *v = (int *)malloc(sizeof(int));
  *v = 1;
  push(arr, v);
  int *out = (int *)pop(arr);
  TEST_ASSERT_NOT_NULL(out);
  TEST_ASSERT_EQUAL_INT(1, *out);
  free(out);
}

void test_push_9_times_and_trigger_resize(void) {
  for (int i = 1; i <= 9; i++) {
    int *v = &i;
    push(arr, v);
  }
  TEST_ASSERT_EQUAL_INT(16, arr->capacity);
}

void test_pop_when_size_less_than_8_and_trigger_resize(void) {
  for (int i = 1; i <= 9; i++) {
    pop(arr);
  }
  free(pop(arr));
  free(pop(arr));
  TEST_ASSERT_EQUAL_INT(DEFAULT_CAPACITY, arr->capacity);
}

void test_pop_and_the_empty_equals_empty_value(void) {
  int *v = (int *)malloc(sizeof(int));
  *v = 5;
  push(arr, v);
  free(pop(arr));
  TEST_ASSERT_EQUAL_PTR(NULL, arr->data[arr->size]);
}

void test_pop_is_blocked_when_size_is_0(void) {
  for (int i = 0; i <= 6; i++) {
    (void)pop(arr);
  }
  TEST_ASSERT_NULL(pop(arr));
}

void test_shift_and_return_removed_value(void) {
  int *v = (int *)malloc(sizeof(int));
  *v = 1;
  push(arr, v);
  int *out = (int *)shift(arr);
  TEST_ASSERT_NOT_NULL(out);
  TEST_ASSERT_EQUAL_INT(1, *out);
  free(out);
}

void test_shift_and_rest_values_shift_to_preivous(void) {
  int *v2 = (int *)malloc(sizeof(int));
  *v2 = 2;
  int *v3 = (int *)malloc(sizeof(int));
  *v3 = 3;
  int *v4 = (int *)malloc(sizeof(int));
  *v4 = 4;
  push(arr, v2);
  push(arr, v3);
  push(arr, v4);
  int *out = (int *)shift(arr);
  TEST_ASSERT_NOT_NULL(out);
  TEST_ASSERT_EQUAL_INT(2, *out);
  TEST_ASSERT_EQUAL_INT(3, *(int *)arr->data[0]);
  TEST_ASSERT_EQUAL_INT(4, *(int *)arr->data[1]);
  free(out);
}

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_arr_has_8_capacity_default);
  RUN_TEST(test_push_and_return_arr_size);
  RUN_TEST(test_pop_and_return_removed_value);
  RUN_TEST(test_push_9_times_and_trigger_resize);
  RUN_TEST(test_pop_when_size_less_than_8_and_trigger_resize);
  RUN_TEST(test_pop_and_the_empty_equals_empty_value);
  RUN_TEST(test_pop_is_blocked_when_size_is_0);
  RUN_TEST(test_shift_and_return_removed_value);
  RUN_TEST(test_shift_and_rest_values_shift_to_preivous);
  return UNITY_END();
}
