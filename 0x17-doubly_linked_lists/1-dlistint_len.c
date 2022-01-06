#include "lists.h"
/**
 * dlistint_len - Print the le of the double list
 * @h: a pointer to the head
 * Return: the elements count
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}
