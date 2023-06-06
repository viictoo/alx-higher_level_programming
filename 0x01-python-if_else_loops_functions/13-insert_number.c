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
	listint_t *swap, *temp, *current;

	if (!*head)
		return (NULL);
	if ((*head)->next == NULL)
	{
		swap = malloc(sizeof(listint_t));
		if (!swap)
			return (NULL);
		swap->n = number;
		swap->next = NULL;
		(*head)->next = swap;
		return (swap);
	}
	for (swap = *head; swap && swap->n < number;
			current = swap, swap = swap->next)
	{
	}
	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);
	temp->n = number;
	temp->next = swap;
	current->next = temp;
	return (temp);
}
