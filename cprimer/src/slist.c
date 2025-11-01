// Singly linked list implementation (minimal API)
// No header used to keep consistent with existing project style.

#include <stdlib.h>
#include <stddef.h>

typedef struct SListNode {
    int value;
    struct SListNode* next;
} SListNode;

typedef struct SList {
    SListNode* head;
    size_t size;
} SList;

// Create / Destroy
SList* slist_create(void)
{
    SList* list = (SList*)malloc(sizeof(SList));
    if (!list) return NULL;
    list->head = NULL;
    list->size = 0;
    return list;
}

void slist_destroy(SList* list)
{
    if (!list) return;
    SListNode* cur = list->head;
    while (cur) {
        SListNode* next = cur->next;
        free(cur);
        cur = next;
    }
    free(list);
}

// Clear all nodes but keep list allocated
void slist_clear(SList* list)
{
    if (!list) return;
    SListNode* cur = list->head;
    while (cur) {
        SListNode* next = cur->next;
        free(cur);
        cur = next;
    }
    list->head = NULL;
    list->size = 0;
}

// Push front
void slist_push_front(SList* list, int value)
{
    if (!list) return;
    SListNode* node = (SListNode*)malloc(sizeof(SListNode));
    if (!node) return;
    node->value = value;
    node->next = list->head;
    list->head = node;
    list->size++;
}

// Push back
void slist_push_back(SList* list, int value)
{
    if (!list) return;
    SListNode* node = (SListNode*)malloc(sizeof(SListNode));
    if (!node) return;
    node->value = value;
    node->next = NULL;
    if (!list->head) {
        list->head = node;
    } else {
        SListNode* cur = list->head;
        while (cur->next) cur = cur->next;
        cur->next = node;
    }
    list->size++;
}

// Pop front; returns 1 if popped, 0 if empty
int slist_pop_front(SList* list, int* out_value)
{
    if (!list || !list->head) return 0;
    SListNode* node = list->head;
    if (out_value) *out_value = node->value;
    list->head = node->next;
    free(node);
    list->size--;
    return 1;
}

// Size
size_t slist_size(const SList* list)
{
    return list ? list->size : 0;
}

// Find value; returns 1 if found, 0 if not
int slist_find(const SList* list, int value)
{
    if (!list) return 0;
    SListNode* cur = list->head;
    while (cur) {
        if (cur->value == value) return 1;
        cur = cur->next;
    }
    return 0;
}