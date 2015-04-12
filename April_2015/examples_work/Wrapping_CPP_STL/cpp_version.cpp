#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> page( )
{ 
    vector<string> content;
    
    content.push_back("He took his vorpal sword in hand:");
    content.push_back("Long time the manxome foe he sought --");
    content.push_back("So rested he by the Tumtum tree,");
    content.push_back("And stood a while in thought.");
    content.push_back(" ");
    content.push_back("One two! One two! And through and through");
    content.push_back("The vorpal blade went snicker-snack!");
    content.push_back("He left it dead, and with its head");
    content.push_back("He went galumphing back.");

    return content;
}

int main ()
{
    vector<string> output = page( );

    cout << "-----------------"  << endl;     
    cout << "Original ordering:" << endl;
    cout << "-----------------"  << endl;

    for (size_t i = 0; i < output.size(); i++)
    
        cout << output[i] << endl;
    
    sort(output.begin(), output.end() );

    cout << "-----------------" << endl;
    cout << "Sorted lines:"     << endl;
    cout << "-----------------" << endl;

    for (size_t i = 0; i < output.size(); i++)
    
        cout << output[i] << endl;
        
    return 0;
}
