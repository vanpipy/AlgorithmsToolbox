#include "single_linked_list.h"

struct SingleLinkedListNode *node;

void setUp(void) {
  node = create_single_linked_node(1);
}

void tearDown(void) {
  free(node);
}

void test_node_val_equals_1(void) {
  TEST_ASSERT_EQUAL_INT(1, node->val);
}

void test_node_next_equals_null(void) {
  TEST_ASSERT_EQUAL_INT(NULL, node->next);
}

void test_node_linked_next_node(void) {
  struct SingleLinkedListNode *new_node = create_single_linked_node(2);
  node->next = new_node;
  TEST_ASSERT_EQUAL_INT(2, node->next->val);
  free(new_node);
}