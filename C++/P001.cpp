#include <iostream>

int main(void){
  int providedNum = 1000;
  int mtpSum = 0;

  for (int i=0; i<providedNum; i++){
    if (i%3 == 0)
      mtpSum += i;
    if (i%5 == 0 && i%3 != 0)
      mtpSum += i;
  }

  std::cout << mtpSum << std::endl;
}