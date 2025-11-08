#include <stdlib.h>
#include <string.h>
#include "string.h"

static String *allocate_string(int size) {
  if (size < 0) {
    return NULL;
  }
  String *s = (String *)malloc(sizeof(String));
  if (!s) {
    return NULL;
  }
  s->size = size;
  s->data = (char *)malloc((size + 1) * sizeof(char));
  if (!s->data) {
    free(s);
    return NULL;
  }
  s->data[size] = '\0';
  return s;
}

String *create_string(char *data, int size) {
  String *s = allocate_string(size);
  if (!s) {
    return NULL;
  }
  if (data && size > 0) {
    memcpy(s->data, data, (size_t)size);
  }
  return s;
}

String *substring(String str, int start, int end) {
  if (start < 0 || end < start || end > str.size) {
    return NULL;
  }
  if (str.size > 0 && str.data == NULL) {
    return NULL;
  }
  int new_size = end - start;
  String *s = allocate_string(new_size);
  if (!s) {
    return NULL;
  }
  if (new_size > 0) {
    memcpy(s->data, str.data + start, (size_t)new_size);
  }
  return s;
}

String *concat(String str1, String str2) {
  if ((str1.size > 0 && str1.data == NULL) || (str2.size > 0 && str2.data == NULL)) {
    return NULL;
  }
  int total = str1.size + str2.size;
  String *s = allocate_string(total);
  if (!s) {
    return NULL;
  }
  if (str1.size > 0) {
    memcpy(s->data, str1.data, (size_t)str1.size);
  }
  if (str2.size > 0) {
    memcpy(s->data + str1.size, str2.data, (size_t)str2.size);
  }
  return s;
}
