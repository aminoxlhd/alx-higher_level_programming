#include <Python.h>

/**
 * print_python_list_info - rints some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int total_size, allocated_size, i;
	const char *name;

	if (p == NULL)
		return;

	total_size = PyList_Size(p);
	allocated_size = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", total_size);
	printf("[*] Allocated = %ld\n", allocated_size);
	for (i = 0; i < total_size; i++)
	{
		name = (Py_TYPE(PyList_GetItem(p, i)))->tp_name;
		printf("Element %ld: %s\n", i, name);
	}
}
