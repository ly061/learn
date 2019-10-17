class Person(object):


    def work(self):
        print('work hard')


def study(s):
    print('study-------{}'.format(s))


Person.test = study
p = Person()
p.work()
p.test()
