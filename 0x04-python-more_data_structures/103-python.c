
#include <Python.h>
/**
 * print_python_bytes - Fn that prints bytes information in given format
 * @p: PyBytesObject
 * Return: (void)
 */
void print_python_bytes(PyObject *p)
{
	unsigned char iter;
    unsigned char size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);

    printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);

	for (iter = 0; iter < size; iter++)
    {
	printf("%02hhx%s", bytes->ob_sval[iter], iter == size - 1 ? "\n" : " ");
    }
}
/**
 * print_python_list - fn that print some basic info about Python lists
 * @p: PyBytesObject.
 * Return: (void)
 */
void print_python_list(PyObject *p)
{
	int size, allocated;
	const char *obj_type;
    int i;

	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

    allocated = list->allocated;
	size = var->ob_size;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		obj_type = list->ob_item[i]->ob_type->tp_name;

		printf("Element %d: %s\n", i, obj_type);

		if (!strcmp(obj_type, "bytes"))
        {
			print_python_bytes(list->ob_item[i]);
        }
	}
}
