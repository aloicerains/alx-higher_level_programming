/**
 * check_cycle - function checks if a loop is present in the linked list
 * @list: pointer to linked list
 *
 * Return: 1 success, 0 failure
 */
#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *toto = list;
	listint_t *hare = list;

	while (toto && hare && hare->next)
	{
		toto = toto->next;
		hare = hare->next->next;
		if (toto == hare)
			return (1);
	}
	return (0);
}
