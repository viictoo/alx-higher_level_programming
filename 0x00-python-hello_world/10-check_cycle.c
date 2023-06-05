#include "lists.h"

/**
 * check_cycle - bool singly linked list for a cycl
 * @list: singly linked list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *hare, *kobe;

	if (!list)
		return (0);
	hare = kobe = list;
	for (; hare && hare->next;)
	{
		kobe = kobe->next;
		hare = hare->next->next;
		if (hare == kobe)
			return (1);
	}
	return (0);
}
