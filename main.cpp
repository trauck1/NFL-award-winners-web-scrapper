#include <iostream>
#include <fstream>
using namespace std;
int main(){
    int choice = 0;
    bool exit = false;
    while(exit == false){
      cout << "NFL award winners and player draft position!" << endl;
      cout << "1. AP MVPs" << endl;
      cout << "2. AP DPOYs" << endl;
      cout << "3. SUPERBOWL WINNERs" << endl;
      cout << "4. Draft Position" << endl;
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
          system("python playerFinder.py");
          break;
        case 5:
          exit = true;
          break;
      }
    
    }
    return 0;
}
