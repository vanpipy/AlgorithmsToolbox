#include "unity.h"
#include "string.h"

void setUp(void) {}
void tearDown(void) {}

void test_string_placeholder(void) {
    TEST_ASSERT_TRUE(1);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_string_placeholder);
    return UNITY_END();
}