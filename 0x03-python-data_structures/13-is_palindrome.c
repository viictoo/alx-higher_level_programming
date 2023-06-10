#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head node of a linked list
 * Return: 1 if is a palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *hare, *kobe;
	int len = 0, count = 0;

	if (!((*head)->next) || !(*head))
		return (1);
	hare = kobe = *head;
	while (kobe)
	{
		kobe = kobe->next;
		hare = hare->next->next;

		if (hare == kobe)
			return (0);

		if (hare == NULL)
		{
			while (kobe)
			{
				hare = *head;
				count = len;
				while (count > 0)
				{
					hare = hare->next;
					count--;
				}
				len--;
				if (hare->n != kobe->n)
					return (0);
				kobe = kobe->next;
			}
			return (1);
		}
		len++;
	}
	return (0);
}
