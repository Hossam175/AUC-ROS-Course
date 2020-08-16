#include <iostream>
#include <math.h>

using namespace std;
/*
* Prereq: include math.h
* Function that calculates the probability according to a gaussian distribution
* Param:
*   mu: the mean of the sample
*   sigma2: the variance of the sample
*   x: the event variable
*
* Returns:
*   prob: the probability of the variable x happening
*/
double f(double mu, double sigma2, double x)
{
  double prob = (exp(-(pow((x-mu),2))/(2*sigma2)))/(sqrt(2*M_PI*sigma2));
  return (prob);
}


int main(){
//function call
  cout << f(10.0,4.0,8.0) << endl;
  return 0;
}
