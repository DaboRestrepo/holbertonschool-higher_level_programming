#include "lists.h"
/**
 * @brief 
 * 
 */
int is_palindrome(listint_t **head)
{
    listint_t *h = head, *current = NULL;
    int index = 0;

    (void)*h;
    (void)index;

    while (*head)
    {
        current = *head->next;
        *head = current;
    }
    printf("%d\n", *head->n);
    return (1);
}