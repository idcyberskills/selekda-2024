#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_BOOKS 100
#define TITLE_SIZE 100
#define AUTHOR_SIZE 100

typedef struct {
    int id;
    char title[TITLE_SIZE];
    char author[AUTHOR_SIZE];
    int quantity;
} Book;

Book bookstore[MAX_BOOKS];
int book_count = 0;

void addBook() {
    if (book_count >= MAX_BOOKS) {
        printf("Bookstore is full!\n");
        return;
    }

    Book new_book;
    new_book.id = book_count + 1;

    printf("Enter title: ");
    gets(new_book.title);
    new_book.title[strcspn(new_book.title, "\n")] = 0; // Remove newline character

    printf("Enter author: ");
    gets(new_book.author);
    new_book.author[strcspn(new_book.author, "\n")] = 0; // Remove newline character

    printf("Enter quantity: ");
    scanf("%d", &new_book.quantity);
    getchar(); // Clear newline character from input buffer

    bookstore[book_count++] = new_book;
    printf("Book added successfully!\n");
}

void removeBook() {
    int id;
    printf("Enter book ID to remove: ");
    scanf("%d", &id);
    getchar(); // Clear newline character from input buffer

    int index = -1;
    for (int i = 0; i < book_count; i++) {
        if (bookstore[i].id == id) {
            index = i;
            break;
        }
    }

    if (index == -1) {
        printf("Book not found!\n");
        return;
    }

    for (int i = index; i < book_count - 1; i++) {
        bookstore[i] = bookstore[i + 1];
    }

    book_count--;
    printf("Book removed successfully!\n");
}

void searchBook() {
    int id;
    printf("Enter book ID to search: ");
    scanf("%d", &id);
    getchar(); // Clear newline character from input buffer
    if (bookstore[id].id) {
        printf("Book found!\n");
        printf("ID: %d\n", bookstore[i].id);
        printf("Title: %s\n", bookstore[i].title);
        printf("Author: %s\n", bookstore[i].author);
        printf("Quantity: %d\n", bookstore[i].quantity);
        return;
    }else{
        printf("Book not found!\n");
    }
}

void listBooks() {
    if (book_count == 0) {
        printf("No books in the bookstore!\n");
        return;
    }

    for (int i = 0; i < book_count; i++) {
        printf("ID: %d\n", bookstore[i].id);
        printf("Title: %s\n", bookstore[i].title);
        printf("Author: %s\n", bookstore[i].author);
        printf("Quantity: %d\n", bookstore[i].quantity);
        printf("\n");
    }
}

void showMenu() {
    printf("1. Add Book\n");
    printf("2. Remove Book\n");
    printf("3. Search Book\n");
    printf("4. List Books\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
}

int main() {
    int choice;

    while (1) {
        showMenu();
        scanf("%d", &choice);
        getchar(); // Clear newline character from input buffer

        switch (choice) {
            case 1:
                addBook();
                break;
            case 2:
                removeBook();
                break;
            case 3:
                searchBook();
                break;
            case 4:
                listBooks();
                break;
            case 5:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }

        printf("\n");
    }

    return 0;
}