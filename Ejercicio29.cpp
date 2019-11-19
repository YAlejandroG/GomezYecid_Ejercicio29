#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double D = 1;
double S = 1;
double T = 1;
double Xmin = -1;
double Xmax = 1;
int Nt = 100;
int Nx = 10;
double dT = T/Nt;
double dX = (Xmax-Xmin)/Nx;

int FTCS(double **PSI);

int main(){
    double **PSI = new double *[Nt];
    for (int i=0;i<Nt;i++){
        PSI[i] =new double[Nx];
    }
    FTCS(PSI);
    
    return 0;
}

int FTCS(double **PSI){
    for(int i=0; i<Nt; i++){
        for(int j=0; j<Nx; j++){
            if(i==0){
                PSI[i][j] = 0;
            }
            
            if(j==0 | j==Nx-1){
                PSI[i][j] = 0;
            }
        }
    }
    
    for(int i=0; i<Nt-1; i++){
        for(int j=1; j<Nx-1; j++){
            PSI[i+1][j] = PSI[i][j]+D*dT*(PSI[i][j+1]-2*PSI[i][j]+PSI[i][j-1])/pow(dX,2)+dT*S;
        }
    }
    
    for(int i=0; i<Nt; i++){
        for(int j=0; j<Nx; j++){
            cout<<PSI[i][j]<<"\t";
        }
        cout<<endl;
    }
    
    return 0;
}