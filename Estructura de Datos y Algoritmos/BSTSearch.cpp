#include <iostream>

using namespace std;

struct node {
    int key;
    struct node *left, *right;
};

struct node* newNode(int item) {
    struct node* temp = new struct node;
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
};

struct node* insert(struct node* node, int key){
    if (node == NULL) 
        return newNode(key);
    if (key < node->key) 
        node->left = insert(node->left, key);
    else if (key > node->key) 
        node->right = insert(node->right, key);
    
    return node;
};

struct node* search(struct node* root, int key) {
    if (root == NULL || root->key == key) 
        return root;

    if (root->key < key) 
        return search(root->right, key);
    return search(root->left, key);
};


int main(){
    struct node* root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 25);
    insert(root, 45);
    insert(root, 75);
    insert(root, 55);
    insert(root, 85);
    insert(root, 40);
    insert(root, 35);
    insert(root, 28);

    int key = 85;

    if (search(root,key) == NULL) 
        cout << "Key not found" << endl;
    else 
        cout << "Key found" << endl;


    return 0;
}

