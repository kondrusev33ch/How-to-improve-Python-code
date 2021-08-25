int fib(int a); // prototype
int fib(int a)
{
    if(a <= 0)
        return -1;
    else if (a == 1)
        return 0;
    else if ((a == 2) || (a == 3))
        return 1;
    else
        return fib(a - 2) + fib(a - 1);
}