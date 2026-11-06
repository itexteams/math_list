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


def bt_dang42_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số cho bài toán
                A = randint(1, 4)
                B = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                N = randint(8, 20)

                # Số các số nguyên trong khoảng (-N; N)
                total_ints = 2 * N - 1

                # Xét phương trình g(m) = A*m^2 + (B + 1)*m = 0
                # Nghiệm m1 = 0
                # Nghiệm m2 = -(B + 1) / A
                m1 = 0
                m2_num = -(B + 1)
                m2_den = A

                excluded_count = 1  # Giá trị m = 0 luôn thuộc (-N; N) do N >= 8

                is_m2_valid = False
                m2_val = None
                if m2_num % m2_den == 0:
                    m2_val = m2_num // m2_den
                    if m2_val != 0 and -N < m2_val < N:
                        is_m2_valid = True
                        excluded_count += 1

                kq = total_ints - excluded_count

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách các đáp án nhiễu
                s = [
                    '$%s$' % (latex(total_ints)),
                    '$%s$' % (latex(total_ints - 1)),
                    '$%s$' % (latex(kq + 1)),
                    '$%s$' % (latex(kq - 1)),
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq - 2))
                ]

                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Chuỗi hiển thị tử số
                if B == 1:
                    bx_str = "+ x"
                elif B == -1:
                    bx_str = "- x"
                elif B > 0:
                    bx_str = "+ %sx" % B
                else:
                    bx_str = "- %sx" % abs(B)

                if A == 1:
                    ax2_str = "x^2"
                else:
                    ax2_str = "%sx^2" % A

                tu_str = "%s %s + m" % (ax2_str, bx_str)

                sum_b1 = B + 1
                if sum_b1 == 0:
                    gm_factor_str = "%sm^2" % A if A > 1 else "m^2"
                    pt_nghiem = "m = 0"
                else:
                    if sum_b1 > 0:
                        b1_str = "+ %sm" % sum_b1 if sum_b1 != 1 else "+ m"
                    else:
                        b1_str = "- %sm" % abs(sum_b1) if abs(sum_b1) != 1 else "- m"

                    if A == 1:
                        gm_factor_str = "m^2 %s" % b1_str
                    else:
                        gm_factor_str = "%sm^2 %s" % (A, b1_str)

                    pt_nghiem = "m = 0 \\text{ hoặc } m = %s" % latex(Rational(m2_num, m2_den))

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu giá trị nguyên $m \\in (-%s; %s)$ sao cho đồ thị hàm số $y = \\frac{%s}{x - m}$ có tiệm cận xiên?'''
                                 % (N, N, tu_str))

                # Nội dung lời giải
                if is_m2_valid:
                    loigiai = ('''Để đồ thị hàm số có tiệm cận xiên thì tử số không chia hết cho mẫu số, tức là $x = m$ không là nghiệm của tử số.\\\\
            Thay $x = m$ vào tử số, ta được $g(m) = %s = 0 \\iff %s$.\\\\
            Do đó, đồ thị hàm số có tiệm cận xiên khi và chỉ khi $m \\ne 0$ và $m \\ne %s$.\\\\
            Số các giá trị nguyên của $m$ thuộc khoảng $(- %s; %s)$ là: $%s$ giá trị.\\\\
            Loại $2$ giá trị $m = 0$ và $m = %s$ (đều thuộc khoảng $(- %s; %s)$), ta được $%s - 2 = %s$ giá trị nguyên của $m$ thỏa mãn.\\\\
            Vậy có %s giá trị nguyên của tham số $m$ thỏa mãn yêu cầu bài toán.'''
                               % (gm_factor_str, pt_nghiem, latex(m2_val),
                                  N, N, total_ints,
                                  latex(m2_val), N, N, total_ints, kq,
                                  kq))
                elif m2_val == 0:
                    loigiai = ('''Để đồ thị hàm số có tiệm cận xiên thì tử số không chia hết cho mẫu số, tức là $x = m$ không là nghiệm của tử số.\\\\
            Thay $x = m$ vào tử số, ta được $g(m) = %s = 0 \\iff m = 0$.\\\\
            Do đó, đồ thị hàm số có tiệm cận xiên khi và chỉ khi $m \\ne 0$.\\\\
            Số các giá trị nguyên của $m$ thuộc khoảng $(- %s; %s)$ là: $%s$ giá trị.\\\\
            Loại $1$ giá trị $m = 0$ thuộc khoảng $(- %s; %s)$, ta được $%s - 1 = %s$ giá trị nguyên của $m$ thỏa mãn.\\\\
            Vậy có %s giá trị nguyên của tham số $m$ thỏa mãn yêu cầu bài toán.'''
                               % (gm_factor_str,
                                  N, N, total_ints,
                                  N, N, total_ints, kq,
                                  kq))
                else:
                    if m2_num % m2_den != 0:
                        reason = "Do $m \\in \\mathbb{Z}$ nên $m \\ne %s$ luôn được thỏa mãn với mọi $m \\in \\mathbb{Z}$" % latex(Rational(m2_num, m2_den))
                    else:
                        reason = "Do $m = %s \\notin (-%s; %s)$ nên giá trị này không thuộc khoảng đang xét" % (latex(m2_val), N, N)

                    loigiai = ('''Để đồ thị hàm số có tiệm cận xiên thì tử số không chia hết cho mẫu số, tức là $x = m$ không là nghiệm của tử số.\\\\
            Thay $x = m$ vào tử số, ta được $g(m) = %s = 0 \\iff %s$.\\\\
            %s.\\\\
            Do đó, ta chỉ cần loại giá trị $m = 0$.\\\\
            Số các giá trị nguyên của $m$ thuộc khoảng $(- %s; %s)$ là: $%s$ giá trị.\\\\
            Loại $1$ giá trị $m = 0$, ta được $%s - 1 = %s$ giá trị nguyên của $m$ thỏa mãn.\\\\
            Vậy có %s giá trị nguyên của tham số $m$ thỏa mãn yêu cầu bài toán.'''
                               % (gm_factor_str, pt_nghiem,
                                  reason,
                                  N, N, total_ints,
                                  total_ints, kq,
                                  kq))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
            dapan='\\shortans[0]{$%s$}\n'%(da)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

