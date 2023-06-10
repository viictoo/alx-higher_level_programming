#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head node of a linked list
 * Return: 1 if is a palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *kobe;
	int len = 0, i, j, *arr;

	if (!head)
		return (0);
	if (!((*head)->next) || !(*head))
		return (1);

	kobe = *head;
	while (kobe)
	{
		arr = realloc(arr, sizeof(int) * len);
		arr[len] = kobe->n;
		kobe = kobe->next;
		len++;
	}
	i = 0;
	j = len - 1;
	while (i < j)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
		i++;
		j--;
	}
	free(arr);
	return (1);
}
