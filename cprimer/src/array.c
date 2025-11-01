#include <stdio.h>

#define MONTHS 12

// Expose a simple API for testing
int days_in_month(int month)
{
  int days[MONTHS] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  if (month < 1 || month > MONTHS) {
    return -1;
  }
  return days[month - 1];
}

#ifndef UNIT_TEST
int main()
{
  int days[MONTHS] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int index = 0;
  for (int index = 0; index < MONTHS; index++) {
    printf("Month %2d has %2d days.\n", index + 1, days[index]);
  }
  return 0;
}
#endif

