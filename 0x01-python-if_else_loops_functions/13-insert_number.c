/**
 *insert_node - function inserts node at a given index
 * @head: pointer to head argument
 * @n: Data argument for initialization
 *
 * Return: Address of new node or null incase of failure.
 */
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *tmp1 = NULL;
	listint_t *newNode = malloc(sizeof(listint_t));

	if (head != NULL && newNode != NULL)
	{
		tmp1 = (*head);
		while (tmp1 != NULL && tmp1->next != NULL)
		{
			if (tmp1->next->n >= n)
				break;
			tmp1 = tmp1->next;
		}
		if (tmp1 != NULL)
		{
			newNode->n = n;
			newNode->next = tmp1->next;
			tmp1->next = newNode;
			return (newNode);
		}
	}
	return (NULL);
}
