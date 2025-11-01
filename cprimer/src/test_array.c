#include "unity.h"

// Function under test (provided by array.c)
int days_in_month(int month);

void setUp(void) {}
void tearDown(void) {}

static void test_valid_months(void)
{
    TEST_ASSERT_EQUAL_INT(31, days_in_month(1));
    TEST_ASSERT_EQUAL_INT(28, days_in_month(2));
    TEST_ASSERT_EQUAL_INT(30, days_in_month(4));
    TEST_ASSERT_EQUAL_INT(31, days_in_month(12));
}

static void test_invalid_months(void)
{
    TEST_ASSERT_EQUAL_INT(-1, days_in_month(0));
    TEST_ASSERT_EQUAL_INT(-1, days_in_month(13));
    TEST_ASSERT_EQUAL_INT(-1, days_in_month(-5));
}

int main(void)
{
    UNITY_BEGIN();
    RUN_TEST(test_valid_months);
    RUN_TEST(test_invalid_months);
    return UNITY_END();
}