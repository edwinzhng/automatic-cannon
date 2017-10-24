#include "./include/json.hpp"
#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>

double calcDistX(std::vector<double> &coordinates, double focal_length, double averageHeight);
double calcDistY(double top_right, double top_left, double bottom_right, double bottom_left);
double calculateTime(double dist_x, double dist_y);
std::vector<double> parseJson();

int main() {
  std::vector<double> coordinates = parseJson();
  calcDistX(coordinates, 2570, 0.22);
  return 0;
}

double calcDistX(std::vector<double> &coordinates, double focal_length, double averageWidth) {
  double dist_x = 0;
  dist_x = (averageWidth * focal_length) / (coordinates[0] - coordinates[1]); // horizontal distance = knownWidth * focal_length / pixelWidth
  std::cout << coordinates[0] << std::endl;
  return dist_x;
}

double calcDistY(double top_right, double top_left, double bottom_right, double bottom_left) {
  double dist_y = 0;
  // TODO calculate vertical distance relative to cannon
  return dist_y;
}

double calculateTime(double dist_x, double dist_y) {
  int t = 0;
  // TODO calculate time needed with dist_x
  return t;
}

std::vector<double> parseJson() {
  std::ifstream i("../data/coordinates.json");
  nlohmann::json camera_data;
  i >> camera_data;
  std::cout << camera_data << std::endl;

  std::vector<double> coordinates = {};
  // TODO parse data for all coordinates
  std::cout << coordinates[0] << std::endl;
  return coordinates;
}
