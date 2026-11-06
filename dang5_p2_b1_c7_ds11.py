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


def bt_dang5_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1 & 2: Nghiên cứu đề bài và thiết lập thông số random
            # Hàm số có dạng f(x) = (x - m) / (x + n).
            m = randint(2, 5)
            n = 1
            # f(0) = -m/n = -m
            f_0 = -m
            # f'(0) = (n+m)/n^2 = m+1 (với n=1)
            a_val = m + 1

            # Định nghĩa hàm số để hiển thị
            f_x_tex = "\\frac{x-%s}{x+%s}" % (m, n)

            # Nội dung câu hỏi
            noidungcauhoi = ("""Dùng định nghĩa để tính đạo hàm của hàm số $f\\left(x\\right)=%s$ tại điểm $x_0=0$ ta được $f'\\left(0\\right)=a$.""" 
                             % (f_x_tex))

            ########################################################################
            # (a) Nhận biết: Định nghĩa đạo hàm
            nb_da_1_d = "\\True $f'\\left(0\\right)=\\lim_{x\\to 0} \\frac{f\\left(x\\right)-f\\left(0\\right)}{x-0}$"
            nb_da_1_s = "$f'\\left(0\\right)=\\lim_{x\\to \\infty} \\frac{f\\left(x\\right)-f\\left(0\\right)}{x-0}$"
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ("""Theo định nghĩa đạo hàm của hàm số tại một điểm $x_0$, ta có \\\\ $f'\\left(x_0\\right)=\\lim_{x\\to x_0} \\frac{f\\left(x\\right)-f\\left(x_0\\right)}{x-x_0}$. \\\\ Với $x_0=0$, ta được $f'\\left(0\\right)=\\lim_{x\\to 0} \\frac{f\\left(x\\right)-f\\left(0\\right)}{x-0}$.""")

            ########################################################################
            # (b) Thông hiểu: Tính toán giới hạn
            k_true = m + 1
            k_false = m + 2
            th_da_1_d = "\\True $f'\\left(0\\right)=\\lim_{x\\to 0} \\frac{%s}{x+1}$" % (k_true)
            th_da_1_s = "$f'\\left(0\\right)=\\lim_{x\\to 0} \\frac{%s}{x+1}$" % (k_false)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ("""Ta có $f\\left(0\\right)=%s$. \\\\ Xét giới hạn: $\\lim_{x\\to 0} \\frac{f\\left(x\\right)-f\\left(0\\right)}{x} = \\lim_{x\\to 0} \\frac{\\frac{x-%s}{x+1}-\\left(%s\\right)}{x} = \\lim_{x\\to 0} \\frac{\\frac{x-%s+%s\\left(x+1\\right)}{x+1}}{x} = \\lim_{x\\to 0} \\frac{%s x}{x\\left(x+1\\right)} = \\lim_{x\\to 0} \\frac{%s}{x+1}$.""" 
                            % (f_0, m, f_0, m, -f_0, k_true, k_true))

            ########################################################################
            # (c) Vận dụng: Phương trình liên quan đến a
            c_val = m
            vd_da_1_d = "\\True Phương trình $3^x=3$ có nghiệm bằng $x=a-%s$" % (c_val)
            vd_da_1_s = "Phương trình $3^x=3$ có nghiệm bằng $x=a+%s$" % (c_val)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ("""Từ kết quả câu b, ta có $f'\\left(0\\right)=%s$, suy ra $a=%s$. \\\\ Phương trình $3^x=3 \\Leftrightarrow x=1$. \\\\ Thử lại với $x=a-%s=%s-%s=1$.""" 
                            % (a_val, a_val, c_val, a_val, c_val))

            ########################################################################
            # (d) Vận dụng cao: Logarit - Đã sửa lỗi chưa random theo a
            vdc_da_1_d = "\\True $\\log_{a} %s = 2$" % (a_val**2)
            vdc_da_1_s = "$\\log_{a} 9 = 3$"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            def get_loigiai_vdc(chosen_ans, a_val):
                if "\\True" in chosen_ans:
                    return ("""Với $a=%s$, ta có $\\log_{a} %s = \\log_{%s} \\left(%s^2\\right) = 2$. """ 
                            % (a_val, a_val**2, a_val, a_val))
                else:
                    # Giải thích tại sao log_a(9) = 3 là sai dựa trên a_val thực tế
                    return ("""Với $a=%s$, ta có $\\log_{a} 9 = \\log_{%s} 9$. \\\\ Vì $a=%s \\geq 3$ nên $\\log_{%s} 9 \\leq 2 < 3$. """ 
                            % (a_val, a_val, a_val, a_val))

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

            # Cập nhật lời giải d) dựa trên lựa chọn ngẫu nhiên
            loigiai_vdc_1 = get_loigiai_vdc(vdc_da_1, a_val)

            # Gán lại vào list để đóng gói
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

