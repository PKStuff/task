//============================================================================
// Name        : tree.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : This code includes insertion of element and traversal of element
//               in a binary tree.
//============================================================================

#include <iostream>
#include <queue>

using namespace std;

struct node
{
	int data;
	node *left , *right;
};

node *newnode(int data)
{
	node *temp = new node;
	temp->data = data;
	temp->left = temp->right = NULL;
	return temp;
}

void inorder(node *t){
	if(t!=NULL){
		inorder(t->left);
		cout<<"\t"<<t->data;
		inorder(t->right);
	}
}

void levelorder(node *t){

	queue<node*> q1;

	if(t==NULL)
		return;
	else
	{
		q1.push(t);

		while(!q1.empty())
		{
			node *temp = q1.front();
			cout<<"\t"<<temp->data;
			q1.pop();

			if(temp->left!=NULL){
				q1.push(temp->left);
			}

			if(temp->right!=NULL){
				q1.push(temp->right);
			}

		}
	}
}

void insert(node *root,int data){
	queue<node*> q1;
	q1.push(root);

	while(!q1.empty())
	{
		node *temp1 = q1.front();
		q1.pop();

		if(temp1->left!=NULL){
			q1.push(temp1->left);
		}
		else
		{
			temp1->left = newnode(data);
			break;
		}

		if(temp1->right!=NULL){
			q1.push(temp1->right);
		}
		else
		{
			temp1->right = newnode(data);
			break;
		}
	}
}
int lastnode(node *t)
{
	queue<node *> q1;

	q1.push(t);

	while(!q1.empty())
	{
		node *temp = q1.front();
		q1.pop();

		if(temp->left != NULL){
			q1.push(temp->left);
		}

		if(temp->right != NULL){
			q1.push(temp->right);
		}
	}
return q1.back()->data;

}

void deleteNode(node *t ,int data){
	queue<node *> q1,q2;

	q1.push(t);
	q2.push(t);

	int element = lastnode(t);

	while(!q1.empty())
	{
		node *temp = q1.front();
		q1.pop();
		if(temp->data == data )
		{
			temp->data = element;
			break;
		}
		else
		{
			if(temp->left != NULL){
				q1.push(temp->left);
			}

			if(temp->right != NULL){
				q1.push(temp->right);
			}
		}
	}

	while(!q2.empty())
	{
		node *temp = q2.front();
		q2.pop();

		if(temp->left != NULL)
		{
			if(temp->left->data == element && temp->left->left == NULL && temp->left->right == NULL)
			{
				node *temp1 = temp->left;
				temp->left = NULL;
				delete(temp1);
			}
			else
			{
				q2.push(temp->left);
			}
		}
		if(temp->right != NULL)
		{
			if(temp->right->data == element && temp->right->left == NULL && temp->left->right == NULL)
			{
				node *temp1 = temp->right;
				temp->right = NULL;
				delete(temp1);
			}
			else
			{
				q2.push(temp->right);
			}
		}


	}
}

void preorder(node *t){
	if(t!=NULL){
		cout<<"\t"<<t->data;
		preorder(t->left);
		preorder(t->right);
	}
}

void postorder(node *t){
	if(t!=NULL){
		postorder(t->left);
		postorder(t->right);
		cout<<"\t"<<t->data;
	}
}

int menu()
{
	int result;

	cout<<"1.Inorder Traversal\n";
	cout<<"2.Preorder Traversal\n";
	cout<<"3.Postorder Traversal\n";
	cout<<"4.Levelorder Traversal\n";
	cout<<"5.Insert a element:\n";
	cout<<"6.Last Leaf node\n";
	cout<<"7.Delete a node:\n";

	cout<<"Enter Your Choice:\n";
	cin>>result;

	return result;
}
int main(void){

	node *root=newnode(1);

	int choice,element,last;

	do{
		choice = menu();

		switch (choice) {
			case 1:inorder(root);
					cout<<endl;
				break;
			case 2:preorder(root);
					cout<<endl;
				break;
			case 3:postorder(root);
					cout<<endl;
				break;
			case 4:levelorder(root);
					cout<<endl;
				break;
			case 5:cout<<"Enter the element:\n";
					cin>>element;
					insert(root,element);
				break;
			case 6:last = lastnode(root);
					cout<<"The last leaf node is : "<<last<<endl;
			    break;
			case 7:cout<<"Enter the element to delete:\n";
					cin>>element;
					deleteNode(root,element);
				break;
			default:cout<<"System Exit\n";
				break;
		}
	}while(choice != 8);

	return 0;
}
