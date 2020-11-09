/* Matrix Calculator
#
# Can perform various functions
# Matrix Equals
# Matrix Add
# Matrix Multiply
# Matrix Scalar Add
# Matrix Scalar Multiply
# Matrix Trace
# Matrix Transpose
# Matrix Submatrix
# Matrix Determinant
# Matrix Inverse
# Matrix Print
# Test file
*/

#include <stdio.h>
#include <string.h>

void main()
{
    char key;

    // User input
    printf("Welcome to THE MATRIX CALCULATOR!\nPlease select a Function: [E]quals, [A]dd, [M]ultiply, [S]calar, [Tr]ace, [T]ranspose, [Sub]matrix, [D]eterminant, [I]nverse, [P]rint. ");
    scanf("%s", key);

    // Catergorization
    if (key == 'E' | key == 'e')
    {
        MatrixEquals();
    }
    else if (key == 'A' | key == 'a')
    {
        MatrixAdd();
    }
}

void MatrixEquals()
{
}

void MatrixAdd()
{
}

void MatrixMultiply()
{
}

void MatrixScalarAdd()
{
}

void MatrixScalarMultiply()
{
}

void MatrixTrace()
{
}

void MatrixTranspose()
{
}

void MatrixSubmatrix()
{
}

void MatrixDeterminant()
{
}

void MatrixInverse()
{
}

void MatrixPrint()
{
}
