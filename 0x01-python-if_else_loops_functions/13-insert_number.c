#include "lists.h"
/**
 * insert_node - Insert a node in a place of the list
 * @head: list
 * @number: number to add
 * Return: the new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *h = *head;
	/*unsigned int idx = 0;*/

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	if (h == NULL)
		return (NULL);
	new->n = number;
	while ( < new->n)
	{
		if (h->next == NULL)
			return (NULL);
		h = h->next;
		data++;
	}
	new->next = h->next;
	h->next = new;
	return (new);
}
