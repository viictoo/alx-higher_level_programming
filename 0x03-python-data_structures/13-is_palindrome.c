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
	listint_t *kobe = *head, *hare = *head;
	listint_t *prev = NULL, *next = NULL;

	while (hare && hare->next)
	{
		hare = hare->next->next;
		next = kobe->next;
		kobe->next = prev;
		prev = kobe;
		kobe = next;
	}
	if (hare)
		kobe = kobe->next;

	while (prev && kobe)
	{
		if (prev->n != kobe->n)
			return (0);
		prev = prev->next;
		kobe = kobe->next;
	}
	return (1);
}
