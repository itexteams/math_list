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


def bt_dang14_p2_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến và tạo bài toán ngẫu nhiên cho hàm số dạng f(x) = (Ax^2 + Bx + C) / (x + D)
            x = symbols('x')

            # Tạo ngẫu nhiên các hệ số sao cho phép chia đa thức cho ra tiệm cận xiên y = A*x + b_val
            A = random.randint(2, 3)
            D_val = random.randint(1, 4)
            b_val = random.randint(-4, -1)
            R = random.randint(1, 5) # Phần dư luôn khác 0

            B = A * D_val + b_val
            C_val = b_val * D_val + R

            tu_so = A * x**2 + B * x + C_val
            mau_so = x + D_val

            # Hoành độ giao điểm thực tế của tiệm cận xiên với Ox
            hoanh_do_dung = Rational(-b_val, A)
            hoanh_do_sai = Rational(b_val, A) if b_val != 0 else 2
            if hoanh_do_dung == hoanh_do_sai:
                hoanh_do_sai = hoanh_do_dung + 1

            # Tọa độ giao điểm thực tế với tiệm cận đứng x = -D_val
            y_inter = A * (-D_val) + b_val

            # Diện tích tam giác OAB thực tế
            S_dung = Rational(b_val**2, 2 * A)
            S_sai = Rational(b_val**2, A)

            # Giá trị lớn nhất của y = Ax + b_val trên [0; 3]
            max_dung = 3 * A + b_val
            max_sai = b_val

            # Nội dung câu hỏi sử dụng định dạng %s theo mẫu
            noidungcauhoi = ('''Cho hàm số $(C): y = f(x) = \\frac{%s}{%s}$ biết đồ thị hàm số có đường tiệm cận xiên là đường thẳng $\\Delta: y = ax+b$.''' 
                             % (latex(tu_so), latex(mau_so)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Giao điểm của $\\Delta$ và trục $Ox$ có hoành độ bằng $%s$' % (latex(hoanh_do_dung))
            nb_da_1_s = 'Giao điểm của $\\Delta$ và trục $Ox$ có hoành độ bằng $%s$' % (latex(hoanh_do_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $f(x) = \\frac{%s}{%s} = %s x + %s + \\frac{%s}{%s}$.\\\\
            Suy ra đường tiệm cận xiên của đồ thị hàm số là $\\Delta: y = %s x + %s$.\\\\
            Giao điểm của $\\Delta$ với trục $Ox$ (ứng với $y = 0$) thỏa mãn: $%s x + %s = 0 \\Leftrightarrow x = %s$.\\\\
            Vậy hoành độ giao điểm của $\\Delta$ và trục $Ox$ bằng $%s$.'''
                            % (latex(tu_so), latex(mau_so), latex(A), latex(b_val), latex(R), latex(mau_so),
                               latex(A), latex(b_val), latex(A), latex(b_val), latex(hoanh_do_dung), latex(hoanh_do_dung)))

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
            th_da_1_d = '\\True Giao điểm của $\\Delta$ và tiệm cận đứng của $(C)$ có tọa độ là $\\left(%s; %s\\right)$' % (latex(-D_val), latex(y_inter))
            th_da_1_s = 'Giao điểm của $\\Delta$ và tiệm cận đứng của $(C)$ có tọa độ là $\\left(%s; %s\\right)$' % (latex(-D_val), latex(-y_inter if y_inter != 0 else 5))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Đo thị hàm số $(C)$ có đường tiệm cận đứng là $x = %s$.\\\\
            Giao điểm của đường tiệm cận xiên $\\Delta: y = %s x + %s$ và đường tiệm cận đứng $x = %s$ có tọa độ thỏa mãn hệ phương trình:\\\\
            $\\begin{cases} x = %s \\\\ y = %s x + %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$\\\\
            Vậy tọa độ giao điểm của hai đường tiệm cận là $\\left(%s; %s\\right)$.'''
                            % (latex(-D_val), latex(A), latex(b_val), latex(-D_val),
                               latex(-D_val), latex(A), latex(b_val), latex(-D_val), latex(y_inter),
                               latex(-D_val), latex(y_inter)))

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
            vd_da_1_d = '\\True Gọi $A = \\Delta \\cap Ox, B = \\Delta \\cap Oy$ thì diện tích tam giác $OAB$ bằng $%s$' % (latex(S_dung))
            vd_da_1_s = 'Gọi $A = \\Delta \\cap Ox, B = \\Delta \\cap Oy$ thì diện tích tam giác $OAB$ bằng $%s$' % (latex(S_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Đường thẳng $\\Delta: y = %s x + %s$ cắt các trục tọa độ lần lượt tại:\\\\
            $A = \\Delta \\cap Ox \\Rightarrow A\\left(%s; 0\\right) \\Rightarrow OA = \\left|%s\\right| = %s$.\\\\
            $B = \\Delta \\cap Oy \\Rightarrow B\\left(0; %s\\right) \\Rightarrow OB = \\left|%s\\right| = %s$.\\\\
            Diện tích tam giác vuông $OAB$ được tính bởi công thức: $S = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.'''
                            % (latex(A), latex(b_val),
                               latex(hoanh_do_dung), latex(hoanh_do_dung), latex(hoanh_do_dung),
                               latex(b_val), latex(b_val), latex(-b_val),
                               latex(hoanh_do_dung), latex(-b_val), latex(S_dung)))

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
            vdc_da_1_d = '\\True Giá trị lớn nhất của hàm số $y = ax+b$ trên $\\left[0;3\\right]$ bằng $%s$' % (latex(max_dung))
            vdc_da_1_s = 'Giá trị lớn nhất của hàm số $y = ax+b$ trên $\\left[0;3\\right]$ bằng $%s$' % (latex(max_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Từ phương trình tiệm cận xiên $\\Delta: y = %s x + %s$, ta xét hàm số bậc nhất $g(x) = %s x + %s$ trên đoạn $\\left[0;3\\right]$.\\\\
            Vì hệ số góc của đường thẳng là $a = %s > 0$ nên hàm số $g(x)$ luôn đồng biến trên $\\mathbb{R}$, từ đó hàm số cũng đồng biến trên đoạn $\\left[0;3\\right]$.\\\\
            Do đó, giá trị lớn nhất của hàm số trên đoạn $\\left[0;3\\right]$ đạt được tại đầu mút $x = 3$, giá trị lớn nhất đó bằng: $g(3) = %s \\cdot 3 + %s = %s$.'''
                             % (latex(A), latex(b_val), latex(A), latex(b_val),
                                latex(A), latex(A), latex(b_val), latex(max_dung)))

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
                str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -','-')
            return content

