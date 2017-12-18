#include <iostream>
/*

Challenge: Write a program that, given a number n from STDIN, prints out all numbers from 1 to n (inclusive) to STDOUT, each on their own line. But there's a catch:

    For numbers divisible by 3, instead of n, print Fizz
    For numbers divisible by 5, instead of n, print Buzz
    For numbers divisible by 3 and 5, just print FizzBuzz

g++ -o ex2_fizz_buzz ex2_fizz_buzz.cpp

Example use:
> ./ex2_fizz_buzz
Number of integers to be evaluated : 15
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
*/

using namespace std;

int main() {  
    
    // Prompt user for n, the number of integers to print
    cout << "Number of integers to be evaluated : ";
    int n;
    cin >> n;
    
    // Print out the sequence, obeying the rules
    for (int count = 1; count <= n; count++)
    {
        if ((count % 3 == 0) && (count % 5 == 0))
            cout << "FizzBuzz\n";
        else if (count % 3 == 0)
            cout << "Fizz\n";
        else if (count % 5 == 0)
            cout << "Buzz\n";
        else
            cout << count << endl;
    }
    return 0;
}