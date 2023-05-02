import yaml
from collections import OrderedDict
from functools import reduce
import os


def get_build(build_name):
    data_tasks = open_task()
    data_builds = open_builds()
    way = []
    result = []
    tasks = get_task_from_build(data_builds, build_name)
    if tasks is not None:
        for task in tasks:
            get_list(way, task, data_tasks, result)
            result = list(OrderedDict.fromkeys(result[::-1]))
    return result


def print_build(build_name):
    print("Build info:")
    print(" * name: {}".format(build_name))
    l_tasks = get_build(build_name)
    if len(l_tasks) > 0:
        print(" * tasks: {}".format(reduce(list_to_str, l_tasks)))
    else:
        print(" * tasks: {}".format(''))
    # print('\n')


def list_to_str(el_prev, el):
    return str(el_prev) + ", " + str(el)


def get_task(task_name):
    data_tasks = open_task()
    way = []
    result = []
    get_list(way, task_name, data_tasks, result)
    if isinstance(result, list):
        if len(result) > 0:
            result = list(OrderedDict.fromkeys(result[::-1]))
    return result


def get_task_from_build(data, builds_name):
    if isinstance(data, list):
        if len(data) > 0:
            for el in data:
                if el['name'] == builds_name:
                    return el['tasks']
    return []


def print_for(builds):
    if isinstance(builds, list):
        for build in builds:
            if isinstance(builds, dict):
                if 'name' in build:
                    print(build['name'])


def get_list_dependencies(data, tasks):
    result = []
    if isinstance(data, list):
        for el in data:
            if isinstance(el, dict):
                if 'name' in el:
                    if el['name'] in tasks:
                        find_dependencies = el['dependencies']
                        result.extend(find_dependencies)
                        # result.extend(get_list_dependencies(data, find_dependencies))
    return result


def is_duplicates(arr):
    set_arr = set(arr)
    result = True
    if len(arr) == len(set_arr):
        result = False
    return result


def get_list(way, tasks, data, result):
    if is_duplicates(way):
        raise IOError("""Error: cyclical dependencies
                            {}""".format(way))
    if len(tasks) > 0:
        result.append(tasks)
    dependencies = get_list_dependencies(data, tasks)

    for dep in dependencies:
        get_list(way + [dep], dep, data, result)


def list_builds():
    builds = open_builds()
    print('List of available builds:')
    for build in builds:
        print(" * {}".format(build['name']))


def list_tasks():
    tasks = open_task()
    print('List of available tasks:')
    for task in tasks:
        print(" * {}".format(task['name']))


def print_task(task_name):
    print("Task info:")
    print(" * name: {}".format(task_name))
    s = " * tasks: {}"
    l_tasks = get_task(task_name)
    len_list_tasks = len(l_tasks)
    if len_list_tasks > 0:
        l_tasks.pop(-1)
        len_list_tasks -= 1

    if len_list_tasks > 2:
        print(s.format(reduce(list_to_str, l_tasks)))
    elif len_list_tasks == 1:
        print(s.format(l_tasks))
    else:
        print(s.format(""))


tasks_file = 'tasks.yaml'
builds_file = 'builds.yaml'
directory = ""


def open_task():
    with open(os.path.join(directory, tasks_file)) as f:
        data_tasks = yaml.load(f, Loader=yaml.FullLoader)['tasks']
        return data_tasks


def open_builds():
    with open(os.path.join(directory, builds_file)) as f:
        data_builds = yaml.load(f, Loader=yaml.FullLoader)['builds']
        return data_builds
