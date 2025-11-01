// Unified Unity test runner that invokes all test suites
#include "unity.h"

// Array tests
void test_valid_months(void);
void test_invalid_months(void);

// Singly linked list tests
void test_empty_list_behaviour(void);
void test_push_and_pop_order(void);
void test_find_and_clear(void);

void setUp(void) {}
void tearDown(void) {}

int main(void)
{
    UNITY_BEGIN();

    // array.c tests
    RUN_TEST(test_valid_months);
    RUN_TEST(test_invalid_months);

    // slist.c tests
    RUN_TEST(test_empty_list_behaviour);
    RUN_TEST(test_push_and_pop_order);
    RUN_TEST(test_find_and_clear);

    return UNITY_END();
}