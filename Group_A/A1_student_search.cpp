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

void linearSearch(Student *s, int size)
{
    int key;
    int found = 0;
    cout << "Enter ID to search: ";
    cin >> key;
    for (int i = 0; i < size; i++)
    {
        if (s[i].id == key)
        {
            cout << "Student found" << endl;
            cout << "ID: " << s[i].id << "  Name: " << s[i].name << "  CGPA: " << s[i].cgpa << endl;
            found = 1;
            break;
        }
    }
    if (found == 0)
        cout << "Student not found" << endl;
}

void sortById(Student *s, int size)
{
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - i - 1; j++)
        {
            if (s[j].id > s[j + 1].id)
            {
                Student t = s[j];
                s[j] = s[j + 1];
                s[j + 1] = t;
            }
        }
    }
}

void binarySearch(Student *s, int size)
{
    sortById(s, size);
    int key, low = 0, high = size - 1, found = 0;
    cout << "Enter ID to search: ";
    cin >> key;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (s[mid].id == key)
        {
            cout << "Student found" << endl;
            cout << "ID: " << s[mid].id << "  Name: " << s[mid].name << "  CGPA: " << s[mid].cgpa << endl;
            found = 1;
            break;
        }
        else if (key < s[mid].id)
            high = mid - 1;
        else
            low = mid + 1;
    }
    if (found == 0)
        cout << "Student not found" << endl;
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
        cout << "3. Linear search" << endl;
        cout << "4. Binary search" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter choice: ";
        cin >> ch;

        if (ch == 1)
            addStudent(s, size);
        else if (ch == 2)
            display(s, size);
        else if (ch == 3)
            linearSearch(s, size);
        else if (ch == 4)
            binarySearch(s, size);
    } while (ch != 5);

    free(s);
    return 0;
}
