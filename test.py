from models.dev import Dev
from models.project import Project
from models.task import Task
from models.task_list import TaskList
from models.dev_list import DevList


def main():
    """get all task_test"""
    project_bosh = Project('Bosh')
    dev1 = Dev('developerMitya@mail.ru', '111111', 'Oleg', 'Fomin', 22)

    task2 = Task('second_task', 15, project_bosh)

    dev2 = Dev('developerMitya@bbmail.ru', '111111', 'Oleg', 'Fomin', 22, task=task2)
    task3 = Task('second_task', 5, executor=dev1)
    task4 = Task('fourth', 10, executor=dev1)
    task_list = TaskList([task2, task3, task4])
    dev_list = DevList(dev1)
    dev_list.add_dev(dev2)
    print(task2.show_full__info_task())

    # print(task_list.get_all_task())
    """del_task_from_list(use get all task_test)"""
    # task_list.del_task(task2.uid)
    # print(task_list.get_all_task())
    """sort_task_list(use get all task_test)"""
    # print(task_list.sort_priority_task())
    """change task"""
    # task2.change_task(new_priority=5)
    # print(task2)
    """change password"""
    # print(dev1.password)
    # dev1.change_password('123123123')
    # print(dev1.password)
    # print(dev1)
    # dev2.change_email('aaa@mail.rrr')
    # dev2.add_task(task2)
    # print(dev2)
    # task2.change_task(task_executor=dev2)
    # print(task2)
    print(dev_list.get_all_email())
    dev1.add_task(task2)
    dev1.add_task(task4)

    print(dev1)
    print(dev1.show_accepted_task())


if __name__ == '__main__':
    main()