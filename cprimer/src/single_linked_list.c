#include <stdlib.h>

struct SingleLinkedListNode {
  int val;
  struct SingleLinkedListNode *next;
};

struct SingleLinkedListNode *create_single_linked_node(int val) {
  struct SingleLinkedListNode *node =
      malloc(sizeof(struct SingleLinkedListNode));
  node->val = val;
  node->next = NULL;
  return node;
}