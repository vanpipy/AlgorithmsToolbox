// Unity tests for singly linked list
#include "unity.h"

// Forward declarations of the API exposed by slist.c
typedef struct SList SList;
SList* slist_create(void);
void slist_destroy(SList* list);
void slist_clear(SList* list);
void slist_push_front(SList* list, int value);
void slist_push_back(SList* list, int value);
int slist_pop_front(SList* list, int* out_value);
size_t slist_size(const SList* list);
int slist_find(const SList* list, int value);

// setUp/tearDown provided by the unified test runner

void test_empty_list_behaviour(void)
{
    SList* list = slist_create();
    TEST_ASSERT_NOT_NULL(list);
    TEST_ASSERT_EQUAL_UINT(0u, slist_size(list));

    int value = 42;
    TEST_ASSERT_EQUAL_INT(0, slist_pop_front(list, &value));
    TEST_ASSERT_EQUAL_UINT(0u, slist_size(list));
    slist_destroy(list);
}

void test_push_and_pop_order(void)
{
    SList* list = slist_create();
    TEST_ASSERT_NOT_NULL(list);

    slist_push_back(list, 1);
    slist_push_back(list, 2);
    slist_push_front(list, 0);

    TEST_ASSERT_EQUAL_UINT(3u, slist_size(list));

    int v;
    TEST_ASSERT_EQUAL_INT(1, slist_pop_front(list, &v));
    TEST_ASSERT_EQUAL_INT(0, v);
    TEST_ASSERT_EQUAL_UINT(2u, slist_size(list));

    TEST_ASSERT_EQUAL_INT(1, slist_pop_front(list, &v));
    TEST_ASSERT_EQUAL_INT(1, v);
    TEST_ASSERT_EQUAL_UINT(1u, slist_size(list));

    TEST_ASSERT_EQUAL_INT(1, slist_pop_front(list, &v));
    TEST_ASSERT_EQUAL_INT(2, v);
    TEST_ASSERT_EQUAL_UINT(0u, slist_size(list));

    TEST_ASSERT_EQUAL_INT(0, slist_pop_front(list, &v));
    slist_destroy(list);
}

void test_find_and_clear(void)
{
    SList* list = slist_create();
    TEST_ASSERT_NOT_NULL(list);

    slist_push_back(list, 10);
    slist_push_back(list, 20);
    slist_push_back(list, 30);

    TEST_ASSERT_EQUAL_INT(1, slist_find(list, 20));
    TEST_ASSERT_EQUAL_INT(0, slist_find(list, 99));

    slist_clear(list);
    TEST_ASSERT_EQUAL_UINT(0u, slist_size(list));
    TEST_ASSERT_EQUAL_INT(0, slist_find(list, 10));
    slist_destroy(list);
}

// main is provided by the unified test runner