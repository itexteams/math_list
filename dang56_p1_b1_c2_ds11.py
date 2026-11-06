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


def bt_dang56_p1_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                def format_expr(a, b):
                    if a == 0:
                        return str(b)
                    elif a == 1:
                        res = "n"
                    elif a == -1:
                        res = "-n"
                    else:
                        res = "%sn" % a

                    if b > 0:
                        res += "+%s" % b
                    elif b < 0:
                        res += "-%s" % abs(b)
                    return res

                def format_frac(a, b, c, d):
                    num = format_expr(a, b)
                    den = format_expr(c, d)
                    if den == "1":
                        return num
                    return "\\frac{%s}{%s}" % (num, den)

                def get_seq(a1, b1, c1, d1):
                    seq = []
                    for i in range(1, 5):
                        if c1*i + d1 == 0:
                            return None
                        seq.append(sp.Rational(a1*i + b1, c1*i + d1))
                    return seq

                # Lặp để tìm bộ số a, b, c, d hợp lệ
                while True:
                    a = random.randint(1, 3)
                    b = random.randint(-2, 3)
                    c = random.randint(1, 3)
                    d = random.randint(-2, 3)
                    # Đảm bảo mẫu số luôn dương với n >= 1
                    if c + d > 0 and c*2 + d > 0 and c*3 + d > 0 and c*4 + d > 0:
                        # Đảm bảo dãy số không phải là hằng số
                        if a*d - b*c != 0:
                            # Đảm bảo số hạng đầu tiên có tử số dương để đẹp
                            if a + b > 0:
                                break

                # Tính 4 số hạng đầu của dãy số
                terms = []
                for i in range(1, 5):
                    val = sp.Rational(a*i + b, c*i + d)
                    if val.q == 1:
                        terms.append(str(val.p))
                    else:
                        terms.append("\\frac{%s}{%s}" % (val.p, val.q))

                seq_str = ", ".join(terms) + ", \\dots"

                ans_d = format_frac(a, b, c, d)
                correct_seq = get_seq(a, b, c, d)

                # Khởi tạo các phương án nhiễu
                s_params = [
                    (a, b+1, c, d),
                    (a, b, c, d+1),
                    (c, d, a, b),
                    (a, -b, c, d),
                    (a+1, b, c, d),
                    (a, b, c+1, d),
                    (1, 0, 1, 1), # u_n = n/(n+1)
                    (2, 0, 2, 1)  # u_n = 2n/(2n+1)
                ]

                s_list_str = []
                for p in s_params:
                    sq = get_seq(*p)
                    # Bỏ qua nếu phương án nhiễu vô nghĩa hoặc trùng dãy số với đáp án đúng
                    if sq is not None and sq != correct_seq:
                        s_str = format_frac(*p)
                        if s_str != ans_d and s_str not in s_list_str:
                            s_list_str.append(s_str)

                random.shuffle(s_list_str)

                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $%s \\forall n \\in \\mathbb{N}^*$. Công thức tổng quát của dãy số trên là' % seq_str)

                # Các đáp án
                da_d = ('\\True $u_n = %s$' % ans_d)
                da_s1 = ('$u_n = %s$' % s_list_str[0])
                da_s2 = ('$u_n = %s$' % s_list_str[1])
                da_s3 = ('$u_n = %s$' % s_list_str[2])

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Thử lần lượt các giá trị $n = 1, 2, 3, 4$ vào công thức $u_n = %s$ ta được: \\\\ '
                           'Với $n = 1 \\Rightarrow u_1 = %s$. \\\\ '
                           'Với $n = 2 \\Rightarrow u_2 = %s$. \\\\ '
                           'Với $n = 3 \\Rightarrow u_3 = %s$. \\\\ '
                           'Với $n = 4 \\Rightarrow u_4 = %s$. \\\\ '
                           'Các giá trị này hoàn toàn trùng khớp với dãy số đã cho. \\\\ '
                           'Vậy công thức tổng quát của dãy số là $u_n = %s$.' 
                           % (ans_d, terms[0], terms[1], terms[2], terms[3], ans_d))

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

