#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - A function that inserts a node in a sorted list
 * @head: head pointer in a linked list
 * @number: number to be inserted to the linked list
 * Return: node pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *swap = NULL, *check = NULL, *current = NULL;

	if (!*head || !head)
		return (NULL);
	if ((*head)->next == NULL || (*head)->n > number)
	{
		swap = malloc(sizeof(listint_t));
		if (!swap)
			return (NULL);
		swap->n = number;
		swap->next = (*head);
		(*head) = swap;
		return (swap);
	}
	swap = malloc(sizeof(listint_t));
	if (!swap)
		return (NULL);
	swap->n = number;

	for (check = current = *head; check && check->n < number;
			current = check, check = check->next)
	{
	}
	swap->next = current->next;
	current->next = swap;

	return (swap);
}
