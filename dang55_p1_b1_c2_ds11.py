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


def bt_dang55_p1_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a và b trong công thức u_n = a*n^2 + b
                a = random.choice([1, 1, 1, 2])
                b = random.choice([0, 0, 1, -1])

                # Tính 5 số hạng đầu tiên
                t1 = a * (1**2) + b
                t2 = a * (2**2) + b
                t3 = a * (3**2) + b
                t4 = a * (4**2) + b
                t5 = a * (5**2) + b

                # Định dạng công thức tổng quát đúng
                if a == 1:
                    if b == 0:
                        formula_d = 'n^2'
                    elif b > 0:
                        formula_d = 'n^2 + %s' % b
                    else:
                        formula_d = 'n^2 - %s' % abs(b)
                else:
                    if b == 0:
                        formula_d = '%sn^2' % a
                    elif b > 0:
                        formula_d = '%sn^2 + %s' % (a, b)
                    else:
                        formula_d = '%sn^2 - %s' % (a, abs(b))

                # Dãy số dạng khai triển
                day_so = '%s, %s, %s, %s, %s, \\dots' % (t1, t2, t3, t4, t5)

                # Câu hỏi
                noidungcauhoi = ('Cho dãy số viết dưới dạng khai triển là $%s$. Công thức nào là công thức tổng quát của dãy số trên là' % day_so)

                # Đáp án đúng
                da_d = ('\\True $u_n = %s$' % formula_d)

                # Tạo các đáp án sai
                # Sai lầm 1: Coi là cấp số cộng dựa vào u1, u2 -> d = t2 - t1 -> u_n = d*n + (t1 - d)
                d_linear = t2 - t1
                c_linear = t1 - d_linear
                if c_linear == 0:
                    f_s1 = '%sn' % d_linear
                elif c_linear > 0:
                    f_s1 = '%sn + %s' % (d_linear, c_linear)
                else:
                    f_s1 = '%sn - %s' % (d_linear, abs(c_linear))

                # Sai lầm 2: Công thức bậc nhất khác
                f_s2 = 'n + %s' % (t1 + 2)

                # Sai lầm 3: Sai hệ số của n^2
                a_wrong = a + 1
                b_wrong = t1 - a_wrong
                if b_wrong == 0:
                    f_s3 = '%sn^2' % a_wrong
                elif b_wrong > 0:
                    f_s3 = '%sn^2 + %s' % (a_wrong, b_wrong)
                else:
                    f_s3 = '%sn^2 - %s' % (a_wrong, abs(b_wrong))

                # Đảm bảo không trùng nhau với đáp án đúng
                s_candidates = [
                    '$u_n = %s$' % f_s1,
                    '$u_n = %s$' % f_s2,
                    '$u_n = %s$' % f_s3,
                    '$u_n = 2^n + %s$' % (t1 - 2) if t1 - 2 != 0 else '$u_n = 2^n$'
                ]

                correct_str = '$u_n = %s$' % formula_d
                s_list = []
                for s_item in s_candidates:
                    if s_item != correct_str and s_item not in s_list:
                        s_list.append(s_item)

                # Nếu chưa đủ 3 phương án sai thì bổ sung
                while len(s_list) < 3:
                    rand_f = '$u_n = %sn + %s$' % (random.randint(2, 5), random.randint(1, 5))
                    if rand_f != correct_str and rand_f not in s_list:
                        s_list.append(rand_f)

                da_s1 = s_list[0]
                da_s2 = s_list[1]
                da_s3 = s_list[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Thử lần lượt các giá trị $n = 1, 2, 3, \\dots$ vào công thức $u_n = %s$: \\\\ '
                           'Với $n = 1 \\Rightarrow u_1 = %s$. \\\\ '
                           'Với $n = 2 \\Rightarrow u_2 = %s$. \\\\ '
                           'Với $n = 3 \\Rightarrow u_3 = %s$. \\\\ '
                           'Với $n = 4 \\Rightarrow u_4 = %s$. \\\\ '
                           'Với $n = 5 \\Rightarrow u_5 = %s$. \\\\ '
                           'Do đó công thức tổng quát của dãy số là $u_n = %s$.'
                           % (formula_d, t1, t2, t3, t4, t5, formula_d))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

