// a program to check a string is palindrome or not
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    int len = str.length();
    int flag = 0;
    for(int i = 0; i < len; i++)
    {
        if(str[i] != str[len - i - 1])
        {
            flag = 1;
            break;
        }
    }
    if (flag == 1)
        cout << str << " is not a palindrome";
    else
        cout << str << " is a palindrome";
    return 0;
}