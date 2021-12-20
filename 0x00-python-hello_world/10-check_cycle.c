#include "lists.h"
/**
 * check_cycle - Check if the list has a loop.
 * @list: The list of elements.
 * Return: 0 if false and 1 if true.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	if (list == NULL || list->next == NULL)
		return (0);
	fast = fast->next;
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
