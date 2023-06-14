#include <Python.h>
/**
 * print_python_list - fn that print some basic info about Python lists
 * @p: PyBytesObject.
 * Return: (void)
 */
void print_python_list(PyObject *p)
{
	const char *pyType;
	int pySize, alloc;
	int i;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	alloc = list->allocated;
	pySize = var->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", pySize);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < pySize; i++)
	{
		pyType = list->ob_item[i]->ob_type->tp_name;

		printf("Element %d: %s\n", i, pyType);

		if (!strcmp(pyType, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}


/**
 * print_python_bytes - Fn that prints bytes information in given format
 * @p: PyBytesObject
 * Return: (void)
 */
void print_python_bytes(PyObject *p)
{
	long int pySize, lim;
	char *byte_as_str;
	long int i = 0;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	pySize = ((PyVarObject *)(p))->ob_size;
	byte_as_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", pySize);
	printf("  trying string: %s\n", byte_as_str);
	if (pySize >= 10)
		lim = 10;
	else
		lim = pySize + 1;

	printf("  first %ld bytes:", lim);
	while (i < lim)
	{
		if (byte_as_str[i] >= 0)
			printf(" %02x", byte_as_str[i]);
		else
			printf(" %02x", 256 + byte_as_str[i]);
		i++;
	}
	putchar("\n");
}
