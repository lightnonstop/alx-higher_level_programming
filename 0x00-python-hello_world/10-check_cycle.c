#include "lists.h"
#include <stdio.h>
#include <unistd.h>
/**
  * check_cycle - Checks if a singly linked list has a cycle in it.
  * @list: Linked list
  * Return: 1 if there is a cycle, 0 if there is no cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *fast;

	fast = malloc(sizeof(listint_t));
	/*
	 * Moves twice as fast as the list pointer from
	 * one node to another
	 */
	fast = list->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (fast == list)
			return (1);
		fast = fast->next->next;
		list = list->next;
	}
	return (0);
}
