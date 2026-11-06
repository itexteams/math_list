import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang38_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Hàm định dạng số để chuyển dấu chấm thành phẩy
            def format_num(num, decimal_places=None):
                if decimal_places is not None:
                    formatted = format(num, f".{decimal_places}f")
                    # Xóa các số 0 thừa ở cuối nếu phần thập phân toàn 0
                    if float(formatted) == int(float(formatted)):
                        return str(int(float(formatted)))
                    return formatted.replace('.', ',')
                else:
                    if isinstance(num, (int, float)):
                        if num == int(num):
                            return str(int(num))
                        else:
                            return str(num).replace('.', ',')
                return str(num).replace('.', ',')

            # Random dữ liệu bài toán
            while True:
                a = random.randint(2, 8) # Chi phí cố định (triệu)
                b_val = random.choice([1, 2, 3, 4, 5])
                b = b_val / 10.0         # Chi phí trên mỗi m3 (0.1 -> 0.5)
                c_val = random.choice([1, 2, 4, 5])
                c = c_val / 1000.0       # Hệ số chi phí bảo dưỡng (0.001 -> 0.005)
                max_x = random.choice([100, 120, 150, 200, 250]) # Sản lượng tối đa

                # Tính toán để đảm bảo cực trị nằm trong khoảng (0, max_x)
                x2_val = a / c
                x0_val = math.sqrt(x2_val)

                if x0_val < max_x:
                    break

            # Tính các giá trị
            C_max = a + b * max_x + c * (max_x ** 2)
            C_max_false = C_max + random.choice([10, -10, 5, -5])

            min_C = b + 2 * math.sqrt(a * c)
            min_C_false = min_C + random.choice([0.1, 0.2, -0.1])
            C_bar_max = a / max_x + b + c * max_x

            # Chuẩn bị chuỗi định dạng
            a_str = format_num(a)
            b_str = format_num(b)
            c_str = format_num(c)
            max_x_str = format_num(max_x)

            C_max_str = format_num(C_max)
            C_max_false_str = format_num(C_max_false)

            x2_str = format_num(x2_val)
            x0_str = format_num(x0_val, 3)

            min_C_rounded = format_num(min_C, 3)
            min_C_false_rounded = format_num(min_C_false, 3)
            C_bar_max_str = format_num(C_bar_max, 3)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tại một xí nghiệp chuyên sản xuất vật liệu xây dựng, nếu trong một ngày xí nghiệp sản xuất $x (\\text{m}^3)$ sản phẩm thì phải bỏ ra các khoản chi phí bao gồm: $%s$ triệu đồng chi phí cố định; $%s$ triệu đồng chi phí cho mỗi mét khối sản phẩm và $%sx^2$ triệu đồng chi phí bảo dưỡng máy móc. Biết rằng, mỗi ngày xí nghiệp sản xuất được tối đa $%s \\text{m}^3$ sản phẩm. Gọi $C(x)$ là tổng chi phí để xí nghiệp sản xuất $x (\\text{m}^3)$ sản phẩm trong một ngày và $\\overline{C}$ là chi phí trung bình trên mỗi mét khối sản phẩm.''' 
                             % (a_str, b_str, c_str, max_x_str))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $C(x) = %s + %sx + %sx^2$ với $0 \\le x \\le %s$' % (a_str, b_str, c_str, max_x_str)
            nb_da_1_s = '$C(x) = %sx + %sx^2$ với $0 \\le x \\le %s$' % (b_str, c_str, max_x_str)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Tổng chi phí sản xuất $C(x)$ bao gồm chi phí cố định, chi phí cho mỗi mét khối và chi phí bảo dưỡng máy móc. \\\\ Do đó, $C(x) = %s + %sx + %sx^2$. \\\\ Vì mỗi ngày xí nghiệp sản xuất tối đa $%s \\text{m}^3$ nên điều kiện là $0 \\le x \\le %s$.''' % (a_str, b_str, c_str, max_x_str, max_x_str))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tổng chi phí sản xuất $%s \\text{m}^3$ sản phẩm là $%s$ triệu đồng' % (max_x_str, C_max_str)
            th_da_1_s = 'Tổng chi phí sản xuất $%s \\text{m}^3$ sản phẩm là $%s$ triệu đồng' % (max_x_str, C_max_false_str)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Thay $x = %s$ vào hàm chi phí $C(x)$, ta có: \\\\ $C(%s) = %s + %s \\cdot %s + %s \\cdot %s^2 = %s$ (triệu đồng).''' % (max_x_str, max_x_str, a_str, b_str, max_x_str, c_str, max_x_str, C_max_str))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $\\overline{C} = %sx + \\frac{%s}{x} + %s$ với $0 < x \\le %s$' % (c_str, a_str, b_str, max_x_str)
            vd_da_1_s = '$\\overline{C} = %sx + \\frac{%s}{x}$ với $0 < x \\le %s$' % (c_str, a_str, max_x_str)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Chi phí trung bình trên mỗi mét khối sản phẩm là: \\\\ $\\overline{C}(x) = \\frac{C(x)}{x} = \\frac{%s + %sx + %sx^2}{x} = \\frac{%s}{x} + %s + %sx$. \\\\ Điều kiện là $0 < x \\le %s$ (do $x$ ở dưới mẫu).''' 
            % (a_str, b_str, c_str, a_str, b_str, c_str, max_x_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $\\overline{C}$ có giá trị thấp nhất bằng $%s$ triệu đồng (kết quả làm tròn ba chữ số thập phân)' % (min_C_rounded)
            vdc_da_1_s = '$\\overline{C}$ có giá trị thấp nhất bằng $%s$ triệu đồng (kết quả làm tròn ba chữ số thập phân)' % (min_C_false_rounded)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét hàm số $\\overline{C}(x) = \\frac{%s}{x} + %s + %sx$ với $0 < x \\le %s$. \\\\
            Ta có $\\overline{C}'(x) = -\\frac{%s}{x^2} + %s$. \\\\
            Cho $\\overline{C}'(x) = 0 \\Leftrightarrow \\frac{%s}{x^2} = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x \\approx %s$ (do $x > 0$). \\\\
            Bảng biến thiên:
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\tkzTabInit[lgt=1.5,espcl=3]{$x$/1,$\\overline{C}'(x)$/1,$\\overline{C}(x)$/2}{$0$,{$%s$},$%s$}
            \\tkzTabLine{,-,0,+,}
            \\tkzTabVar{+/ $+\\infty$ ,-/ {$%s$} ,+/ {$%s$}}
            \\end{tikzpicture}
            \\end{center}
            Dựa vào bảng biến thiên, hàm số đạt giá trị nhỏ nhất tại $x \\approx %s$. \\\\
            Vậy chi phí trung bình thấp nhất là $\\overline{C} \\approx %s$ triệu đồng.''' 
            % (a_str, b_str, c_str, max_x_str, a_str, c_str, a_str, c_str, x2_str, x0_str, x0_str, max_x_str, min_C_rounded, C_bar_max_str, x0_str, min_C_rounded))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

