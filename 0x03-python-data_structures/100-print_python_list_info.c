#define PY_SSIZE_T_CLEAN
#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Print basic info about Python lists.
 * @p: PyObject.
 * Return: nothing.
 */

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    size = PyList_GET_SIZE(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(void)
{
    Py_Initialize();

    PyObject *pyList = PyList_New(5);
    PyList_SetItem(pyList, 0, PyLong_FromLong(10));
    PyList_SetItem(pyList, 1, PyFloat_FromDouble(3.14));
    PyList_SetItem(pyList, 2, PyUnicode_DecodeUTF8("Hello", 5, "strict"));
    PyList_SetItem(pyList, 3, PyBool_FromLong(1));
    PyList_SetItem(pyList, 4, PyTuple_Pack(2, PyLong_FromLong(1), PyLong_FromLong(2)));

    print_python_list_info(pyList);

    Py_DECREF(pyList);

    Py_Finalize();

    return 0;
}
