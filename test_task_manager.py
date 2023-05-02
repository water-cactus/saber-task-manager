import unittest
import task_manager


class MyTestCase(unittest.TestCase):

    def test_get_build(self):

        self.assertEqual(task_manager.get_build('approach_important'), ['upgrade_blue_centaurs',
                                                                        'design_black_centaurs',
                                                                        'train_silver_centaurs',
                                                                        'read_purple_centaurs',
                                                                        'map_gray_centaurs'])

        self.assertEqual(task_manager.get_build('test_build'), ['test3', 'test2', 'test1'])
        self.assertEqual(task_manager.get_build('test777'), [])
        self.assertEqual(task_manager.get_build('test1'), [])

    def test_list_to_str(self):
        self.assertEqual(task_manager.list_to_str(1, 2), "1, 2")
        self.assertEqual(task_manager.list_to_str('a', 'b'), "a, b")

    def test_get_task(self):
        self.assertEqual(task_manager.get_task(''),[])
        self.assertEqual(task_manager.get_task('test1'), ['test3', 'test2', 'test1'])

    def test_get_task_from_build(self):
        data = task_manager.open_builds()
        self.assertEqual(task_manager.get_task_from_build(data, 'test_build'),['test1'])
        self.assertEqual(task_manager.get_task_from_build(data, 'test_build2'), [])
        self.assertEqual(task_manager.get_task_from_build([], 'test_build2'), [])
        self.assertEqual(task_manager.get_task_from_build('asda', 'test_build2'), [])

    def test_print_for(self):
        self.assertEqual(task_manager.print_for([]),None)
        self.assertEqual(task_manager.print_for([1, 2, 3]), None)

    def get_list_dependencies(self):
        data = task_manager.open_task()
        self.assertEqual(task_manager.get_list_dependencies(data, 'test1'), [])

    def print_task(self):
        self.assertEqual(task_manager.print_task('design_olive_cyclops'),None)
        self.assertEqual(task_manager.print_task('test1'), None)

    def print_task(self):
        self.assertEqual(task_manager.print_task('design_olive_cyclops'),None)
        self.assertEqual(task_manager.print_task('test1'), None)


if __name__ == '__main__':
    unittest.main()
