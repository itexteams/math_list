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


def bt_dang5_p2_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số sao cho kết quả là số nguyên đẹp
            while True:
                d = random.randint(2, 5)
                t_stop = random.randint(4, 9)
                S = t_stop + d
                C = random.randint(2, 10)

                # Đảm bảo a nguyên
                if (C * (S**2)) % d != 0:
                    continue
                a = (C * (S**2)) // d

                # Đảm bảo N(1) = y1 nguyên
                if a % (1 + d) != 0:
                    continue
                y1 = a // (1 + d)

                # Đảm bảo N(2) = Y2 nguyên
                if (2 * a) % (2 + d) != 0:
                    continue
                Y2 = (2 * a) // (2 + d)

                # y2 là số lượt tải thêm trong ngày 2
                y2 = Y2 - y1
                if y2 <= 0 or y1 <= 0:
                    continue

                # Chọn t3 sao cho tổng số lượt tải sau t3 ngày là số nguyên
                valid_t3 = [t for t in range(3, 8) if (a * t) % (t + d) == 0]
                if not valid_t3:
                    continue
                t3 = random.choice(valid_t3)
                v3_true = (a * t3) // (t3 + d)

                break

            # Sinh các giá trị cho các phương án đúng/sai
            k1 = random.choice([20, 30, 40, 50, 60, 70])
            v1_true = a - k1 * d
            v1_false = v1_true + random.choice([-20, -10, 10, 20])

            v3_false = v3_true + random.choice([-20, -10, 10, 20])

            Lf = a - random.choice([10, 20, 30])
            t_stop_false = t_stop + random.choice([-2, -1, 1, 2])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Số lượt tải xuống (đơn vị: nghìn lượt) của một ứng dụng trò chơi mới ra mắt được mô hình hóa bởi hàm số $N(t)=\\frac{at+b}{t+d}$ (với $t \\ge 0$ là thời gian tính bằng ngày kể từ lúc phát hành). Biết rằng tại thời điểm ra mắt ($t=0$) chưa có lượt tải nào. Sau 1 ngày đầu tiên, ứng dụng đạt $%s$ nghìn lượt tải. Trong ngày thứ 2 (tính riêng ngày thứ 2), có thêm $%s$ nghìn lượt tải mới.''' % (y1, y2))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $a - %s d = %s$' % (k1, v1_true)
            nb_da_1_s = '$a - %s d = %s$' % (k1, v1_false)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Cấu trúc lời giải cơ bản (chưa bao gồm đánh giá đúng sai)
            base_loigiai_nb_1 = ('''Theo đề bài, $N(t)=\\frac{at+b}{t+d}$. \\\\
            Với $t=0 \\Rightarrow N(0)=0 \\Rightarrow \\frac{b}{d}=0 \\Rightarrow b=0$. \\\\
            Với $t=1 \\Rightarrow N(1)=%s \\Rightarrow \\frac{a+b}{1+d}=%s \\Leftrightarrow a+b=%s(1+d) \\Leftrightarrow a-%sd=%s$. \\\\
            Với $t=2 \\Rightarrow N(2)=%s \\Rightarrow \\frac{2a+b}{2+d}=%s \\Leftrightarrow 2a+b=%s(2+d) \\Leftrightarrow 2a-%sd=%s$. \\\\
            Ta có hệ phương trình $\\begin{cases} a-%sd=%s \\\\ 2a-%sd=%s \\end{cases} \\Leftrightarrow \\begin{cases} a=%s \\\\ d=%s \\end{cases}$. \\\\
            Suy ra $a - %sd = %s$''' % (
                y1, y1, y1, y1, y1,
                Y2, Y2, Y2, Y2, 2 * Y2,
                y1, y1, Y2, 2 * Y2, a, d,
                k1, v1_true
            ))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tổng số lượt tải tích lũy sau $%s$ ngày đầu tiên là $%s$ nghìn lượt' % (t3, v3_true)
            th_da_1_s = 'Tổng số lượt tải tích lũy sau $%s$ ngày đầu tiên là $%s$ nghìn lượt' % (t3, v3_false)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_th_1 = ('''Theo câu trên suy ra $N(t)=\\frac{%st}{t+%s}$ suy ra $N(%s)=\\frac{%s \\cdot %s}{%s+%s}=%s$''' % (a, d, t3, a, t3, t3, d, v3_true))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Theo mô hình này, tổng số lượt tải của ứng dụng sẽ không vượt quá $%s$ nghìn lượt' % (a)
            vd_da_1_s = 'Theo mô hình này, tổng số lượt tải của ứng dụng sẽ không vượt quá $%s$ nghìn lượt' % (Lf)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_vd_1 = ('''Ta có: $\\lim\\limits_{t \\to +\\infty} N(t) = \\lim\\limits_{t \\to +\\infty} \\left( \\frac{%st}{t+%s} \\right) = %s$''' % (a, d, a))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Để duy trì đà tăng trưởng, nhà phát hành đang chi $%s$ triệu đồng/ngày cho tiền chạy quảng cáo. Biết rằng mỗi một nghìn lượt tải mới đem lại doanh thu tức thì là 1 triệu đồng. Để tối ưu hóa lợi nhuận, nhà phát hành nên dừng chạy chiến dịch quảng cáo này ngay sau khi kết thúc ngày thứ $%s$' % (C, t_stop)
            vdc_da_1_s = 'Để duy trì đà tăng trưởng, nhà phát hành đang chi $%s$ triệu đồng/ngày cho tiền chạy quảng cáo. Biết rằng mỗi một nghìn lượt tải mới đem lại doanh thu tức thì là 1 triệu đồng. Để tối ưu hóa lợi nhuận, nhà phát hành nên dừng chạy chiến dịch quảng cáo này ngay sau khi kết thúc ngày thứ $%s$' % (C, t_stop_false)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Cấu trúc lời giải cơ bản
            ad = a * d
            S2 = S**2
            base_loigiai_vdc_1 = ('''Ta có hàm tốc độ tăng trưởng: $N'(t)=\\frac{%s}{(t+%s)^2}$. \\\\
            Lợi nhuận thì bằng doanh thu trừ chi phí. Ta nên dừng lại khi lợi nhuận bắt đầu chuyển sang âm. \\\\
            Vậy điểm hòa vốn khi $N'(t)=%s \\Leftrightarrow \\frac{%s}{(t+%s)^2}=%s \\Leftrightarrow (t+%s)^2 = %s \\Leftrightarrow t=%s$ (do $t \\ge 0$). \\\\
            Vậy nhà phát hành nên dừng ngay sau khi kết thúc ngày thứ $%s$''' % (
                ad, d,
                C, ad, d, C, d, S2, t_stop,
                t_stop
            ))

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

            # Sinh lời giải với kết luận đúng/sai linh hoạt tương ứng vào mệnh đề vừa được chọn
            loigiai_nb_1 = base_loigiai_nb_1 + (' nên mệnh đề này đúng.' if '\\True' in nb_da_1 else ' nên mệnh đề này sai.')
            loigiai_th_1 = base_loigiai_th_1 + (' nên mệnh đề này đúng.' if '\\True' in th_da_1 else ' nên mệnh đề này sai.')
            loigiai_vd_1 = base_loigiai_vd_1 + (' nên mệnh đề này đúng.' if '\\True' in vd_da_1 else ' nên mệnh đề này sai.')
            loigiai_vdc_1 = base_loigiai_vdc_1 + (' nên mệnh đề này đúng.' if '\\True' in vdc_da_1 else ' nên mệnh đề này sai.')

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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

