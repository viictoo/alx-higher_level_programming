#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head node of a linked list
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *hare = *head, *kobe = *head;
	int len = 0, count = 0;

	if (head == NULL)
		return (0);

	if (!(*head))
		return (1);

	while (hare && hare->next)
	{
		kobe = kobe->next;
		hare = hare->next->next;
		len++;
	}
	if (len % 2 != 0)
		len--;
	while (kobe)
	{
		hare = *head;
		len--;
		count = len;
		while (count >= 0)
		{
			hare = hare->next;
			count--;
		}
		if (hare->n != kobe->n)
			return (0);
		kobe = kobe->next;
	}
	return (1);
}
