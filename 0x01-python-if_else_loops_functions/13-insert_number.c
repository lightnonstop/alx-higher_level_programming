#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: Pointer to head node
  * @number: First Operand
  * Return: The address of the new node, or NULL if it failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	if (head == NULL || *head == NULL)
		return (NULL);
	temp = *head;
	while (temp != NULL)
	{
		if ((temp->n) > number)
		{
			new->next = malloc(sizeof(listint_t));
			(new->next)->n = number;
			(new->next)->next = temp;
			return (*head);
		}
		new = temp;
		temp = temp->next;
	}
	return (NULL);
}
