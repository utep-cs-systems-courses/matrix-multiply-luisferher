#Luis F. Hernandez
#!/usr/bin/env python3
import time
import argparse
import numpy as np

def genMatrix(size, value):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

def genMatrix2(size, value):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix

def multMatrix(matA,matB):
    
    """
    Multiply 2 2d square matrices and generates a 2d square matrix with the result of the multiplication operation
    """
    matrix = genMatrix2(256,0)
    for x in range(len(matA)):
        for y in range(len(matB[0])):
            for k in range(len(matB)):
                matrix[x][y] = ((matA[x][k]) * (matB[k][y]))

    return matrix

            



def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')

def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file
    """

    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    """
    Reads a matrix from a file
    """

    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix

def main():
    """
    Used for running as a script
    """

    parser = argparse.ArgumentParser(description=
        'Generate a 2d matrix and save it to  a file.')
    parser.add_argument('-s', '--size', default=256, type=int,
        help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=2, type=int,
        help='The value with which to fill the array with')
    parser.add_argument('-f', '--filename',
        help='The name of the file to save the matrix in (optional)')

    args = parser.parse_args()
    #Get the first Matrix
    mat1 = genMatrix2(args.size, args.value)
    #Get the second Matrix 
    mat2 = genMatrix2(args.size, args.value)
    #Create the resulting Matrix
    mat3 = genMatrix2(256,0)
    totalTime = 0
    for i in range(10):
        print(f'Test '+str(i))
        start = time.time() 
        #Call the multiplication function and store the resulting matrix in mat3
        mat3 = multMatrix(mat1,mat2)
        elapsedTime = time.time() - start
        totalTime += elapsedTime
        printSubarray(mat3)
        print(f'Elapsed Time: '+str(elapsedTime)+' Seconds')
    totalTime = totalTime/10
    print(f'Averaged Time per test: '+str(totalTime))

if __name__ == '__main__':
    # execute only if run as a script
    main()
