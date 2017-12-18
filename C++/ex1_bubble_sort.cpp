#include <vector>
#include <iostream>

/*

Challenge: Given an n-element vector of distinct elements, sort the vector in ascending order using the Bubble Sort algorithm.

g++ -o ex1_bubble_sort ex1_bubble_sort.cpp

Inputs:
1) n, and integer defining the number of elements in the vector
2) n space-separated integers defining the elements of the vector

Example use:
> ./ex1_bubble_sort
Enter number of elements in the vector: 6
Enter elements of the vector: 1000 -1 0 34 67 2
Array is sorted in 7 swaps.
First element   : -1
Last element    : 1000
Sorted vector   : -1 0 2 34 67 1000 

*/

using namespace std;

void bubble_sort_pass(int *total_swap_count_ptr, vector<int> *vec_of_ints_ptr)
{
    // Loop over all elements of the vector
    for (int index = 1; index < vec_of_ints_ptr->size(); index++)
    {
        // If current elements is less than the elements at the prior
        // index, swap the two elements
        if (vec_of_ints_ptr->at(index) < vec_of_ints_ptr->at(index - 1))
        {
            int smaller_val = vec_of_ints_ptr->at(index);
            (*vec_of_ints_ptr)[index] = (*vec_of_ints_ptr)[index-1];
            (*vec_of_ints_ptr)[index-1] = smaller_val;
            (*total_swap_count_ptr)++;
        }
    }
}

int main(){
    // Prompt user for vector size
    cout << "Enter number of elements in the vector: ";
    int n;
    cin >> n;

    // Prompt user for vector elements; store in vector a
    cout << "Enter elements of the vector: ";
    vector<int> vec_of_ints(n);
    for(int vec_of_ints_i = 0; vec_of_ints_i < n; vec_of_ints_i++){
       cin >> vec_of_ints[vec_of_ints_i];
    }
    
    // Initialize counters to help determine when no further sorting
    // passes are required.
    int total_swap_count = 0;
    int last_total_swap_count = 0;
    
    // Call bubble sort function until vector is sorted
    do {
        last_total_swap_count = total_swap_count;
        bubble_sort_pass(&total_swap_count, &vec_of_ints);
    }
    while (last_total_swap_count < total_swap_count);

    // Output results    
    cout << "Array is sorted in " << total_swap_count << " swaps.\n";
    cout << "First element\t: " << vec_of_ints[0] << endl;
    cout << "Last element\t: " << vec_of_ints.back() << endl;
    cout << "Sorted vector\t: ";
    for (int index = 0; index < vec_of_ints.size(); index++)
    {
        cout << vec_of_ints[index] << " ";
    }
    cout << endl;
    
    return 0;
}