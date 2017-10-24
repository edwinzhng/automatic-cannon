#include "trajectory.h"
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

double calcDistX(vector<int> coordinates[], double focal_length, double averageHeight);
double calcDistY(double top_right, double top_left, double bottom_right, double bottom_left);
double calculateTime(double dist_x, double dist_y);
double pixels_to_cm(int pixels);

int main() {
  return 0;
}

double calcDistX(vector<int> coordinates[], double focal_length, double averageHeight);

double calculateTime(double dist_x, double dist_y) {
  return dist_x;
}

double pixels_to_cm(int pixels) {
  double conversion_factor = 0.5;
  double cm = (double)pixels * conversion_factor;
  return cm;
}
