/*
UNIVERSIDAD SERGIO ARBOLEDA
ESCUELA DE CIENCIAS EXACTAS E INGENIERÍA
INGENIERÍA DE SISTEMAS Y TELECOMUNICACIONES
AUTHORS: JUAN JOSÉ MONTENEGRO PULIDO & CAMILO ANDRÉS ROMERO MALDONADO
EMAILS: juan.montenegro@correo.usa.edu.co & camiloa.romero@correo.usa.edu.co
12/03/2021
*/

#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#include "matrix.h"

int main(int argc, char **argv)
{
  if (argc != 3)
  {
    fprintf(stderr, "%s <matrix size> <number of threads>\n", argv[0]);
    return -1;
  }

  int MATRIX_SIZE = atoi(argv[1]);
  argc--;
  argv++;

  int NUM_THREADS = atoi(argv[1]);
  argc--;
  argv++;

  /* Se  crean las variables de doble puntero */
  double **matrixA = NULL, **matrixB = NULL, **result = NULL;

  /* Se reserva de forma dinamica el espacio de memoria para cada una delas matrices N * N */
  if ((matrixA = (double **)malloc(MATRIX_SIZE * sizeof(double *))) == NULL ||
      (matrixB = (double **)malloc(MATRIX_SIZE * sizeof(double *))) == NULL ||
      (result = (double **)malloc(MATRIX_SIZE * sizeof(double *))) == NULL)
  {
    printf("insuficente espacio de memoria\n");
    return -1;
  }

  for (int i = 0; i < MATRIX_SIZE; i++)
  {
    if ((matrixA[i] = (double *)malloc(MATRIX_SIZE * sizeof(double))) == NULL ||
        (matrixB[i] = (double *)malloc(MATRIX_SIZE * sizeof(double))) == NULL ||
        (result[i] = (double *)malloc(MATRIX_SIZE * sizeof(double))) == NULL)
    {
      printf("insuficente espacio de memoria\n");
      return -1;
    }
  }

  omp_set_num_threads(NUM_THREADS); // Sets # of threads to be used
#pragma omp parallel                // Declaration of Open MP pragma
  {

#pragma omp master // Declaration of Open MP master

    initMatrixDynamic(MATRIX_SIZE, matrixA, matrixB, result);
    // printMatrix(MATRIX_SIZE, matrixA, "Matrix A"); // Uncomment to print matrix
    // printMatrix(MATRIX_SIZE, matrixB, "Matrix B"); // Uncomment to print matrix
    sample_start();

    /* Variables iteradoras */
    int j, k, l;

    for (j = 0; j < MATRIX_SIZE; j++)
    {
      for (k = 0; k < MATRIX_SIZE; k++)
      {
        double *auxMatrixA, *auxMatrixB; // Auxiliary Pointers to matrixes (Array) positions
        double sum = 0.0;

        // auxMatrixA = *(matrixA + (i * MATRIX_SIZE)); // Assignment of the position of the matrixA in the main array for looping in it
        auxMatrixA = *(matrixA + j); // Assignment of the position of the matrixA in the main array for looping in it
        auxMatrixB = *(matrixB + k); // Assignment of the position of the matrixB in the main array for looping in it

        // for (k = 0; k < MATRIX_SIZE; k++, auxMatrixA++, auxMatrixB++) // Increasing of the position of the pointers to matrixes
        for (l = MATRIX_SIZE; l > 0; l--, auxMatrixA++, auxMatrixB++) // Increasing of the position of the pointers to matrixes
        {
          sum += (*auxMatrixA * *auxMatrixB);
        }
        *(*(result + k) + j) = sum; // Assignment of sum to the result section of the main array
      }
    }
    // printMatrix(MATRIX_SIZE, result, "Result Matrix"); // Uncomment to print matrix
    sample_stop();
    sample_end();
  }
  matrixDynamicFree(MATRIX_SIZE, matrixA, matrixB, result);
  return 0;
}
