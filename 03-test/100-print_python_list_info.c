#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int list_len, alloc_size;
	int i;
	PyObject *obj;


	list_len = Py_SIZE(p);
	alloc_size = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", alloc_size);

	for (i = 0; i < list_len; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
