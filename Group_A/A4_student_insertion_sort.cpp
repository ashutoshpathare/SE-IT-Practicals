#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

struct Student
{
    int id;
    char name[50];
    float cgpa;
};

void addStudent(Student *&s, int &size)
{
    Student *temp = (Student *)realloc(s, (size + 1) * sizeof(Student));
    if (temp == NULL)
    {
        cout << "Memory allocation failed" << endl;
        exit(1);
    }
    s = temp;

    cout << "Enter ID: ";
    cin >> s[size].id;
    cin.ignore();
    cout << "Enter Name: ";
    cin.getline(s[size].name, 50);
    cout << "Enter CGPA: ";
    cin >> s[size].cgpa;
    size++;
}

void display(Student *s, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << "ID: " << s[i].id << "  Name: " << s[i].name << "  CGPA: " << s[i].cgpa << endl;
    }
}

void sortByName(Student *s, int size)
{
    for (int i = 1; i < size; i++)
    {
        Student key = s[i];
        int j = i - 1;
        while (j >= 0 && strcmp(s[j].name, key.name) > 0)
        {
            s[j + 1] = s[j];
            j--;
        }
        s[j + 1] = key;
    }
}

void sortByCgpa(Student *s, int size, int order)
{
    for (int i = 1; i < size; i++)
    {
        Student key = s[i];
        int j = i - 1;
        while (j >= 0 && ((order == 1 && s[j].cgpa > key.cgpa) || (order == 2 && s[j].cgpa < key.cgpa)))
        {
            s[j + 1] = s[j];
            j--;
        }
        s[j + 1] = key;
    }
}

int main()
{
    Student *s = NULL;
    int size = 0;
    int ch;

    do
    {
        cout << "\n1. Add student" << endl;
        cout << "2. Display" << endl;
        cout << "3. Sort by name" << endl;
        cout << "4. Sort by CGPA (ascending)" << endl;
        cout << "5. Sort by CGPA (descending)" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter choice: ";
        cin >> ch;

        if (ch == 1)
            addStudent(s, size);
        else if (ch == 2)
            display(s, size);
        else if (ch == 3)
        {
            sortByName(s, size);
            display(s, size);
        }
        else if (ch == 4)
        {
            sortByCgpa(s, size, 1);
            display(s, size);
        }
        else if (ch == 5)
        {
            sortByCgpa(s, size, 2);
            display(s, size);
        }
    } while (ch != 6);

    free(s);
    return 0;
}
