# -*- coding: utf-8 -*-
from gongyi.trunk.runners.gongyi_runner import gongyiRunner


class Main:
    @staticmethod
    def start_gongyi_test():
        gongyiRunner().run()


if __name__ == '__main__':
    Main.start_gongyi_test()
