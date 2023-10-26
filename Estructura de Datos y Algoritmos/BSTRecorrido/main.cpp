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
}

struct node* insert(struct node* node, int key){
    if (node == NULL)
        return newNode(key);
    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);

    return node;
}

struct node* search(struct node* root, int key) {
    if (root == NULL || root->key == key)
        return root;

    if (root->key < key)
        return search(root->right, key);
    return search(root->left, key);
}

void inorder(struct node* root) {
    if (root != NULL) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
    }
}

void preorder(struct node* root) {
    if (root != NULL) {
        cout << root->key << " ";
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(struct node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        cout << root->key << " ";
    }
}

int height(node* root) {
    if (root == NULL)
        return 0;
    int lheight = height(root->left);
    int rheight = height(root->right);
    if (lheight > rheight)
        return lheight + 1;
    else
        return rheight + 1;
}

void printCurrentLevel(struct node* root, int level) {
    if (root == NULL)
        return;
    if (level == 1)
        cout << root->key << " ";
    else if (level > 1) {
        printCurrentLevel(root->left, level - 1);
        printCurrentLevel(root->right, level - 1);
    }
}

void printLevelOrder(struct node* root) {
    int h = height(root);
    for (int i = 1; i <= h; i++) {
        printCurrentLevel(root, i);
        cout << endl;
    }
}

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

    cout << "Inorder: ";
    inorder(root);

    cout << endl;
    cout << "Preorder: ";
    preorder(root);

    cout << endl;
    cout << "Postorder: ";
    postorder(root);

    cout << endl;
    cout << "Height: " << height(root) << endl;

    cout << endl;
    cout << "Current Level: " << endl;
    printCurrentLevel(root, 3);

    cout << endl;
    cout << "Level Order: " << endl;
    printLevelOrder(root);


    return 0;
}