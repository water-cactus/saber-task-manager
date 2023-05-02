"""Usage:
        main.py [options] list (builds|tasks)
        main.py [options] list (builds|tasks)
        main.py [options] get (builds|tasks) <name>
        main.py [options] get (builds|tasks) <name>


Examples:
    python main.py list builds
    python main.py -d my_directory list builds
    python main.py list tasks
    python main.py get builds approach_important
    python main.py get tasks design_olive_cyclops

Argument:
    list builds     output all builds from the builds.yaml file
    list tasks      output all tasks from the tasks.yaml file
    get builds      output of all dependencies builds   (dependencies do not repeat)
    get tasks       output of all task dependencies     (dependencies do not repeat)

Options:
  -h --help
  -d DIR --directory=DIR selecting a file directory
"""
from docopt import docopt
import task_manager


if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments['--directory'] is not None:
        task_manager.directory = arguments['--directory']

    if arguments['list'] and arguments['builds']:
        task_manager.list_builds()
    if arguments['list'] and arguments['tasks']:
        task_manager.list_tasks()
    if arguments['get'] and arguments['builds']:
        task_manager.print_build(arguments['<name>'])
    if arguments['get'] and arguments['tasks']:
        task_manager.print_task(arguments['<name>'])
