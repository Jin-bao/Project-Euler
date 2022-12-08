#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

bool primeQ(int n);
vector<int>primeDivs(int n);
int phi(int n);

int main(){
  int up_limit = 10000000;
  int phin = 0;
  float ndphin = 0.0;
  float ndphin_min = 10000000.0;
  int min = 0;
  for (int i=2; i<=up_limit; ++i){
    phin = phi(i);
    string i_str = to_string(i);
    sort(i_str.begin(), i_str.end());
    string phin_str = to_string(phin);
    sort(phin_str.begin(), phin_str.end());
    if (i_str == phin_str){
      ndphin = float(i)/phin;
      if (ndphin < ndphin_min){
        ndphin_min = ndphin;
        min = i;
      }
    }
  }
  cout << min << endl;
  return 0;
}

bool primeQ(int n){
  if (n<2){
    return false;
  }
  if (n==2 || n==3){
    return true;
  }
  if (n%6!=1 && n%6!=5){
    return false;
  }
  for (int i=5; i<int(sqrt(n))+1; i+=6){
    if (n%i==0 || n%(i+2)==0){
      return false;
    }
  }
  return true;
}

vector<int>primeDivs(int n){
  vector<int>nVec;
  if (primeQ(n)){
    nVec = {n};
    return nVec;
  }
  int flag;
  flag = int(sqrt(n))+1;
  for (int i=2; i<flag; ++i){
    if (n%i == 0){
      if (primeQ(i)){
        nVec.push_back(i);
      }
      int ndi = n/i;
      if (primeQ(ndi) && ndi!=i){
        nVec.push_back(ndi);
      }
    }
  }
  return nVec;
}

int phi(int n){
  vector<int>nVec = primeDivs(n);
  float phin = n;
  int nVsize = nVec.size();
  for (int d=0; d<nVsize; ++d){
    phin *= 1 - 1./nVec[d];
  }
  return phin;
}