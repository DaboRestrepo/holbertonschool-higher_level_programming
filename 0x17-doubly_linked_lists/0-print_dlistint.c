#include "lists.h"
/**
 * print_dlistint - Print the values in the double list
 * @h: the head of the double list
 * Return: size_t count
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
