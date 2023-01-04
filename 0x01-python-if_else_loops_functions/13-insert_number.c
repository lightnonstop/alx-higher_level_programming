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
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (((*head)->n) > number)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (*head);
	}
	temp = *head;
	while (1)
	{
		if ((temp->n) > number)
		{
			new->next = malloc(sizeof(listint_t));
			if (new->next == NULL)
				return (NULL);
			(new->next)->n = number;
			(new->next)->next = temp;
			return (*head);
		}
		if ((temp->next) == NULL)
		{
			temp->next = malloc(sizeof(listint_t));
			if (temp->next == NULL)
				return (NULL);
			(temp->next)->n = number;
			(temp->next)->next = NULL;
			return (*head);
		}
		new = temp;
		temp = temp->next;
	}
	return (NULL);
}
