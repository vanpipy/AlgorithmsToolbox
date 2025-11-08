#ifndef STRING_H
#define STRING_H

typedef struct {
  char *data;
  int size;
} String;

String *create_string(char *data, int size);
String *substring(String str, int start, int end);
String *concat(String str1, String str2);

#endif // STRING_H
