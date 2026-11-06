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


def bt_dang41_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                a = randint(-5, -2) # Nghiệm âm
                b = randint(2, 5)   # Nghiệm dương

                n = a + b
                m = -a * b

                # Thiết lập các hàm số
                # f(x) = -x^3 + mx
                # g(x) = -nx^2
                f_expr = -x**3 + m*x
                g_expr = -n*x**2

                # Biểu thức hiệu (phù hợp với hình ảnh: x^3 - nx^2 - mx)
                h_expr = x**3 - n*x**2 - m*x

                # Tính tích phân từng phần để lấy giá trị số
                # Khoảng 1: [a, 0]
                I1_val = integrate(h_expr, (x, a, 0))
                # Khoảng 2: [0, b]
                I2_val = integrate(h_expr, (x, 0, b))

                kq_chuan = Abs(I1_val) + Abs(I2_val)

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                du = ['$%s$' % latex(kq_chuan)]
                da = du[0]

                s = set()
                while len(s) < 3:
                    # Tạo các phương án sai bằng cách thay đổi tử số hoặc mẫu số của kết quả
                    sai = kq_chuan + random.choice([Rational(1, 2), Rational(1, 3), Rational(2, 3), Rational(-1, 2), Rational(5, 12)])
                    if sai != kq_chuan and sai > 0:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # B2: Viết lại đề bài theo mẫu
                # Nội dung câu hỏi
                # y = -x^3 + mx và y = -nx^2
                # Chỉnh sửa hiển thị nếu n=1 hoặc m=1
                f_tex = latex(f_expr)
                g_tex = latex(g_expr)

                noidungcauhoi = (r'''Tính diện tích $S$ của hình phẳng $(H)$ giới hạn bởi các đường cong $y = %s$ và $y = %s$.'''
                                 % (f_tex, g_tex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng \text{d}x theo yêu cầu)
                # Nguyên hàm của x^3 - nx^2 - mx là x^4/4 - n*x^3/3 - m*x^2/2
                nguyen_ham = Integral(h_expr, x).doit()

                loigiai = (r'''Xét phương trình hoành độ giao điểm 2 đường cong: \\
                            $ %s = %s \Leftrightarrow x(x^2 - %sx - %s) = 0 \Leftrightarrow \left[\begin{aligned} &x = 0 \\ &x = %s \\ &x = %s \end{aligned}\right. $ \\
                            $\Rightarrow$ Diện tích cần tìm là: \\
                                $S = \int_{%s}^{%s} |%s| \text{d}x = \int_{%s}^{0} |%s| \text{d}x + \int_{0}^{%s} |%s| \text{d}x$ \\
                            $= \left| \int_{%s}^{0} (%s) \text{d}x \right| + \left| \int_{0}^{%s} (%s) \text{d}x \right| \\ = \left| \left( %s \right) \bigg|_{%s}^{0} \right| + \left| \left( %s \right) \bigg|_{0}^{%s} \right|$ \\
                            $= \left| %s \right| + \left| %s \right| = %s$.'''
                           % (f_tex, g_tex, latex(n) if n != 1 else "", latex(m), latex(a), latex(b),
                              latex(a), latex(b), latex(h_expr),
                              latex(a), latex(h_expr), latex(b), latex(h_expr),
                              latex(a), latex(h_expr), latex(b), latex(h_expr),
                              latex(nguyen_ham), latex(a), latex(nguyen_ham), latex(b),
                              latex(I1_val), latex(I2_val), latex(kq_chuan)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


