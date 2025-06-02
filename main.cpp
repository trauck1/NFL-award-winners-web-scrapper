#include <iostream>
#include <fstream>
using namespace std;
int main(){
    int choice = 0;
    bool exit = false;
    while(exit == false){
      cout << "NFL award winners by year!" << endl;
      cout << "1. AP MVP" << endl;
      cout << "2. AP DPOY" << endl;
      cout << "3. SUPERBOWL WINNER" << endl;
      cout << "4. IN PROGRESS" << endl;
      cout << "5. Exit" << endl;
      cin >> choice;
      switch(choice){
        case 1:
          system("python mvp.py");
          break;
        case 2:
          system("python dpoy.py");
          break;
        case 3:
          system("python superbowl.py");
          break;
        case 4:
          cout<< "IN PROGRESS" << endl;
          break;
        case 5:
          exit = true;
          break;
      }
    
    }
    return 0;
}
