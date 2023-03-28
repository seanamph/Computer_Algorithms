#include<iostream>
using namespace std;

main(){
    int n = 10; 
    int *p = &n ; 
    /*n 變數的位址：0x5ffe94
    p 儲存的位址：0x5ffe94
    n：10
    *p：10
    &n：0x5ffe94*/
    cout << "n 變數的位址：" << &n << endl
         << "p 儲存的位址：" << p << endl
         << "n：" << n << endl
         << "*p：" << *p << endl
         << "&n：" << &n << endl; 

    return 0; 
}