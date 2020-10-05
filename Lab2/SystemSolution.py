import numpy as np
from numpy import linalg as LA
from math import *
from colorama import Fore

n = 99
round_width = 6
zero_elem = 0
tau = 0.000002

def print_vec(u):
    print(Fore.CYAN + "U = [")
    for i in range(0, n + 1):
        print(Fore.LIGHTCYAN_EX + str(round(u[i], round_width)))
    print(Fore.CYAN + "]\n\n")


def print_matrix(A, F):
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            print(Fore.CYAN + round(A[i][j], round_width), end="   ")
        print("|  ", end='')
        print(round(F[i], round_width))


def fill_f():
    f = [(i + 1) / n for i in range(0, n + 1)]
    return f


def fill_matrix():
    A = np.zeros((n + 1, n + 1))
    a_idx = -1
    b_idx = 0
    c_idx = 1
    for i in range(0, n + 1):
        if a_idx >= 0:
            A[i][a_idx] = 1
        A[i][b_idx] = 10 + i + 1  # idx in matrix begins with 1
        if c_idx < n + 1:
           A[i][c_idx] = 1
        a_idx += 1
        b_idx += 1
        c_idx += 1

    for j in range(0, n + 1):
        if j == 0 or j == n:
            A[n][j] = 1
        else:
            A[n][j] = 2

    return A


""" Gauss method """
def exclude_ui(A, F, begin_idx):
    coef = A[begin_idx][begin_idx]
    for i in range(begin_idx + 1, n + 1):
        nu = (A[i][begin_idx] + 0.0) / coef
        for j in range(0, n + 1):
            A[i][j] -= nu * A[begin_idx][j]
        F[i] -= nu * F[begin_idx]


""" Gauss method """
def find_answer(A, F):
    U = [0 for _ in range(0, n + 1)]
    U[n] = F[n] / A[n][n]
    for i in range(n - 1, -1, -1):
        sum = F[i]
        for j in range(n - 1, i - 1, -1):
            sum -= A[i][j + 1] * U[j + 1]
        U[i] = sum / A[i][i]
    return U


""" Zeidel method """
def fill_uk(A, F, Uk):
    for i in range(0, n + 1):
        sum = F[i]
        for j in range(0, n + 1):
            if j != i:
                sum -= A[i][j] * Uk[j]
        Uk[i] = sum / A[i][i]


""" Begin of Gauss method """
def Gauss():
    print(Fore.LIGHTMAGENTA_EX + "Gauss method:")
    F = fill_f()
    A = fill_matrix()
    for i in range(0, n + 1):
        exclude_ui(A, F, i)
    U = find_answer(A, F)
    print_vec(U)
""" End of Gauss method """


""" Begin of Zeidel method """
def Zeidel():
    print(Fore.LIGHTMAGENTA_EX + "Zeidel method:")
    F = fill_f()
    A = fill_matrix()
    U = [0 for _ in range(0, n + 1)]
    r = np.ones(n + 1)  # discrepancy
    while LA.norm(r, ord=np.inf) > tau:  # criteria for stopping iterations
        fill_uk(A, F, U)
        r = A.dot(U) - F
    print_vec(U)
    print(Fore.LIGHTBLUE_EX + "Discrepancy:")
    print(Fore.LIGHTYELLOW_EX + str(LA.norm(r, ord=np.inf)))
""" End of Zeidel method """


def condition_number(A):
    inversedA = LA.inv(A)
    normA = LA.norm(A, ord=np.inf)
    norminversedA = LA.norm(inversedA, ord=np.inf)
    mu = normA * norminversedA
    return round(mu, round_width)


def eigenvalues(A):  # returns lambda_min & lambda_max
    eigenvalues = LA.eigvals(A)
    return {'min': round(min(eigenvalues), round_width),
            'max': round(max(eigenvalues), round_width)}


if __name__ == '__main__':
    Gauss()
    Zeidel()

    A = fill_matrix()
    print(Fore.LIGHTBLUE_EX + "Condition_number of matrix A:")
    print(Fore.LIGHTYELLOW_EX + str(condition_number(A)))
    print(Fore.LIGHTBLUE_EX + "Eigenvalues of matrix A:")
    print(Fore.LIGHTYELLOW_EX + str(eigenvalues(A)))
