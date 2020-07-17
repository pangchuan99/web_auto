import win32gui
import win32con


#谷歌浏览器
class js:
    def upload_file(filepath):
        # 一级窗口
        dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框

        # 二级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # 三级窗口
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)

        # 文本的输入窗口-四级
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄

        # 打开按钮一二级窗口
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开($0)")  # 确定按钮Button

        # 输入文件地址
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filepath)  # 往输入框输入绝对地址
        # 点击 打开按钮 提交文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

    upload_file('E:\资料\测试资料(1).xlsx')
