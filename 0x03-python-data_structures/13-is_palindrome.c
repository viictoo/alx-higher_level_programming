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
	listint_t *current = *head;

	return (recursive_tree(&current, current));
}

/**
 * recursive_tree - recursive helper function
 * @right: pointer to the right node
 * @left: pointer to the left node
 * Return: 1 if it is a palindrome, otherwise 0
 */
int recursive_tree(listint_t **right, listint_t *left)
{
	int current_match, is_sublist_palindrome;

	if (left == NULL)
		return (1);

	is_sublist_palindrome = recursive_tree(right, left->next);
	if (!is_sublist_palindrome)
		return (0);

	current_match = ((*right)->n == left->n);
	*right = (*right)->next;

	return (current_match);
}
