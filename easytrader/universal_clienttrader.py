# -*- coding: utf-8 -*-
import time

import pywinauto
import pywinauto.clipboard

from easytrader import grid_strategies
from . import clienttrader


class UniversalClientTrader(clienttrader.BaseLoginClientTrader):
    grid_strategy = grid_strategies.Xls

    @property
    def broker_type(self):
        return "universal"

    def login(self, user, password, exe_path, comm_password=None, **kwargs):
        """
        :param user: 用户名
        :param password: 密码
        :param exe_path: 客户端路径, 类似
        :param comm_password:
        :param kwargs:
        :return:
        """
        self._editor_need_type_keys = True
        try:
            self._app = pywinauto.Application().connect(path=self._run_exe_path(exe_path), timeout=0.2)
        # pylint: disable=broad-except
        except Exception:
            start_time = time.time()
            self._app = pywinauto.Application().start(exe_path)
            print("耗时: {:.2f}秒".format(time.time() - start_time))
            # wait login window ready
        login_code = self.do_login(user, password, exe_path, comm_password)
        if login_code == 1:
            raise Exception("密码错误")
        self.close_login_pop(self.find_login_window_id())

        self._main = self._app.window(title=self.config.TITLE)

    def do_login(self, user, password, exe_path, comm_password=None):
        while True:
            try:
                login_window_id = self.find_login_window_id()
                if login_window_id:
                    user_name_edit = self._app.window(handle=login_window_id) \
                        .window(class_name="ComboBox", control_id=0x3F3)
                    user_name_edit.type_keys(user)

                    password_edit = self._app.window(handle=login_window_id) \
                        .window(class_name="Edit", control_id=0x3F4)
                    password_edit.type_keys(password)

                    comm_password_edit = self._app.window(handle=login_window_id).Edit3
                    comm_password_edit.type_keys(comm_password)

                    self._app.window(handle=login_window_id) \
                        .window(class_name="Button", control_id=0x3EE, title="登录").click()
                    self.wait(0.2)
                    # detect login is success or not
                    # self._app.top_window().wait_not("exists", 100)
                    if self._app.top_window().child_window(control_id=0x3EC).exists() \
                            and self._app.top_window().child_window(control_id=0x3EC).window_text() == "交易密码有误":
                        return 1
                elif self.get_main_win().exists():
                    return 0
            except Exception as err:
                self.wait(0.1)

    def find_login_window_id(self):
        window_list = pywinauto.findwindows.find_windows(class_name='#32770', title="")
        for win in window_list:
            if self._app.window(handle=win).window(class_name="Button", control_id=0x3EE, title="登录").exists():
                return win

    def get_main_win_handle_id(self):
        return pywinauto.findwindows.find_window(title=self.config.TITLE)

    def get_main_win(self):
        return self._app.window(handle=self.get_main_win_handle_id())

    def close_login_pop(self, login_window):
        main_win = self.get_main_win()
        if login_window and self._app.window(handle=login_window).exists() \
                and self._app.top_window().wrapper_object() == self._app.window(handle=login_window).wrapper_object():
            pass
        elif main_win.exists() and main_win.wrapper_object() == self._app.top_window().wrapper_object():
            pass
        else:
            self._app.top_window().close()
