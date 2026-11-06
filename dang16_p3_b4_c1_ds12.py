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


def bt_dang16_p3_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của hàm số bậc ba y = A*x^3 + B*x^2 + C*x + D
                A = random.choice([-2, -1, 1, 2])
                B = random.choice([-3, -2, -1, 0, 1, 2, 3])
                C = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
                D_coef = random.choice([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

                # Chọn hoành độ 2 điểm P và Q (a và c) sao cho a != c và (a + c) là số chẵn
                a_val = random.choice([-3, -2, -1, 0, 1, 2])
                c_val = a_val + 2 * random.choice([1, 2, 3])

                # Trung điểm M(x_M, y_M)
                x_M = (a_val + c_val) // 2

                # Đảm bảo phương trình tìm hoành độ giao điểm có nghiệm duy nhất
                while (6 * A * x_M + 2 * B) == 0:
                    a_val = random.choice([-3, -2, -1, 0, 1, 2])
                    c_val = a_val + 2 * random.choice([1, 2, 3])
                    x_M = (a_val + c_val) // 2

                # Tính tung độ b và d của hai điểm P và Q
                b_val = A * (a_val**3) + B * (a_val**2) + C * a_val + D_coef
                d_val = A * (c_val**3) + B * (c_val**2) + C * c_val + D_coef

                y_M = (b_val + d_val) // 2

                # Biểu thức hàm số
                f_x = A * x**3 + B * x**2 + C * x + D_coef

                # Ký hiệu biến cho SymPy
                a_sym = sp.Symbol('a')
                c_sym = sp.Symbol('c')

                f_a = A * a_sym**3 + B * a_sym**2 + C * a_sym + D_coef
                f_c = A * c_sym**3 + B * c_sym**2 + C * c_sym + D_coef

                c_expr = 2 * x_M - a_sym
                d_expr = 2 * y_M - f_a

                Q_y = f_x.subs(x, c_expr)

                eq_lhs = sp.expand(d_expr)
                eq_rhs = sp.expand(Q_y)
                eq_diff = sp.expand(d_expr - Q_y)

                # Tính giá trị biểu thức T = a + b + c + d
                T_val = a_val + b_val + c_val + d_val

                # Đáp án đúng
                du = ['$%s$' % (latex(T_val))]
                da = random.choice(du)

                # Khởi tạo các phương án sai không trùng với đáp án đúng
                s_set = set()
                for delta in [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]:
                    val = T_val + delta
                    if val != T_val:
                        s_set.add(val)

                s = ['$%s$' % (latex(v)) for v in s_set]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = %s$ có đồ thị $(C)$. Trên đồ thị hàm số $(C)$ lấy $2$ điểm $P(a;b); Q(c;d)$ ($a,b,c,d \\in \\mathbb{Z}$) sao cho chúng đối xứng nhau qua điểm $M(%s;%s)$. Giá trị của biểu thức $T = a + b + c + d$ bằng bao nhiêu?'''
                    % (latex(f_x), latex(x_M), latex(y_M))
                )

                # Định dạng các phương án trả lời
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Tập xác định: $D = \\mathbb{R}$. \\\\
            Giả sử $P(a;b)$ và $Q(c;d)$ là hai điểm phân biệt thuộc đồ thị $(C)$ với $a,b,c,d \\in \\mathbb{Z}$. \\\\
            Vì $P(a;b) \\in (C)$ nên $b = %s$. \\\\
            Do $P(a;b)$ và $Q(c;d)$ đối xứng nhau qua điểm $M(%s;%s)$ nên $M$ là trung điểm của $PQ$, suy ra: \\\\
            $\\begin{cases} c = 2 \\cdot (%s) - a = %s - a \\\\ d = 2 \\cdot (%s) - b = %s - (%s) \\end{cases}$ \\\\
            Mặt khác, $Q(c;d) \\in (C)$ nên $d = %s$. \\\\
            Thay $c = %s - a$ và $d = %s - (%s)$ vào phương trình trên, ta được: \\\\
            $%s = %s$ \\\\
            $\\Leftrightarrow %s = 0$ \\\\
            $\\Leftrightarrow \\left[\\begin{array}{l} a = %s \\\\ a = %s \\end{array}\\right.$ \\\\
            * Với $a = %s \\Rightarrow b = %s$. Khi đó $c = %s, d = %s$, ta được hai điểm $P(%s;%s)$ và $Q(%s;%s)$. \\\\
            * Với $a = %s \\Rightarrow b = %s$. Khi đó $c = %s, d = %s$, ta được hai điểm $P(%s;%s)$ và $Q(%s;%s)$. \\\\
            (Cả hai trường hợp đều ứng với cùng một cặp điểm $P, Q$ trên đồ thị $(C)$). \\\\
            Vậy $T = a + b + c + d = %s + (%s) + (%s) + (%s) = %s$.'''
                    % (
                        latex(f_a),
                        latex(x_M), latex(y_M),
                        latex(x_M), latex(2 * x_M),
                        latex(y_M), latex(2 * y_M), latex(f_a),
                        latex(f_c),
                        latex(2 * x_M), latex(2 * y_M), latex(f_a),
                        latex(eq_lhs), latex(eq_rhs),
                        latex(eq_diff),
                        latex(a_val), latex(c_val),
                        latex(a_val), latex(b_val), latex(c_val), latex(d_val), latex(a_val), latex(b_val), latex(c_val), latex(d_val),
                        latex(c_val), latex(d_val), latex(a_val), latex(b_val), latex(c_val), latex(d_val), latex(a_val), latex(b_val),
                        latex(a_val), latex(b_val), latex(c_val), latex(d_val), latex(T_val)
                    )
                )
            dapan='\\shortans[0]{$%s$}\n'%(latex(T_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

