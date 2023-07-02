#include <Python.h>


/**
 * print_python_string - A function that prints python strings
 *					This code will be compiled with
 * gcc -shared -Wl,-soname,libPython.so -o libPython.so
 * -fPIC -I/usr/include/python3.4 102-python.c
 *
 * @p: python string string
 * Return: (void)
 */

void print_python_string(PyObject *p)
{
	long int count;


	/*flush stdout buffer to ensure accurate printout*/
	fflush(stdout);

	printf("[.] string object info\n");

	/*If p is not a valid string, print an error message*/
	if (!PyUnicode_CheckExact(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	count = PyUnicode_GET_LENGTH(p);
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");

	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", count);
	printf("  value: %S\n", PyUnicode_AsWideCharString(p, &count));
}
