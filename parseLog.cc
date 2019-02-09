

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
  string line;
  ifstream fotoapparat_file("fotoapparat_100pictures.txt");
  ifstream googlecamera_file("camera_100pictures.txt");

  if(fotoapparat_file.is_open()){
    while(getline(fotoapparat_file, line)){
    }
    fotoapparat_file.close();
  }

  if(googlecamera_file.is_open()){
    while(getline(fotoapparat_file, line)){
    }
    fotoapparat_file.close();
  }

}
