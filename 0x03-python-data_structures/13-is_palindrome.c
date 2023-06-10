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

	if (!((*head)->next) || !(*head) || !head)
		return (1);
	hare = kobe = *head;

	while (hare && hare->next)
	{
		kobe = kobe->next;
		hare = hare->next->next;
		len++;
		if (hare == kobe)
			return (0);
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
