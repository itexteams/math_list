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


def bt_dang28_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            x = symbols('x')

            # Bước 1 & 3: Nghiên cứu đề bài và tạo hàm random thông số
            def generate_problem():
                while True:
                    # Random hệ số m và n trong căn (mx^2 - n)
                    m = randint(2, 5)
                    n = randint(1, 5)

                    # Random cận x = a và x = b
                    a = randint(1, 2)
                    b = a + randint(1, 3)

                    # Kiểm tra điều kiện để biểu thức dưới căn dương trên [a, b]
                    if m * a**2 - n > 0:
                        break

                # Thiết diện là hình chữ nhật cạnh 1: k*x, cạnh 2: sqrt(m*x^2 - n)
                # Để tính toán đẹp, ta lấy k = m (như đề bài gốc 3x và 3x^2)
                k = m 

                # Diện tích thiết diện S(x)
                S_expr = k * x * sqrt(m * x**2 - n)

                # Tính thể tích V = tích phân từ a đến b của S(x)dx
                # Sử dụng phương pháp đổi biến u = mx^2 - n => du = 2mx dx
                # V = integral( k/2m * sqrt(u) du ) = k/3m * (mx^2 - n)^(3/2)
                V_val = integrate(S_expr, (x, a, b))

                return m, n, a, b, k, V_val

            m, n, a, b, k, V_val = generate_problem()

            # Bước 2: Viết lại nội dung theo mẫu code Python
            # Nội dung câu hỏi
            noidungcauhoi = (r'''Tính thể tích $V$ của phần vật thể giới hạn bởi hai mặt phẳng $x=%s$ và $x=%s$, biết rằng khi cắt vật thể bởi mặt phẳng vuông góc với trục $Ox$ tại điểm có hoành độ $x$ ($%s \le x \le %s$) thì được thiết diện là một hình chữ nhật có độ dài hai cạnh là $%sx$ và $\sqrt{%sx^2 - %s}$.'''
                             %(latex(a), latex(b), latex(a), latex(b), latex(k), latex(m), latex(n)))

            # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
            kq_dung = '$%s$' % (latex(V_val))

            # Tạo danh sách các giá trị nhiễu
            s_list = []
            offsets = [Rational(1, 2), Rational(1, 3), 1, 2, 5, 10]
            for off in offsets:
                # Sai số bằng cách cộng/trừ hoặc nhân hệ số
                s1 = V_val + off
                s2 = V_val - off
                if s1 != V_val: s_list.append('$%s$' % latex(s1))
                if s2 != V_val and s2 > 0: s_list.append('$%s$' % latex(s2))

            # Chọn ngẫu nhiên 3 đáp án sai từ danh sách nhiễu
            random.shuffle(s_list)
            das1 = s_list[0]
            das2 = s_list[1]
            das3 = s_list[2]

            # Đưa vào list_1 theo mẫu
            da_d = ('\\True ' + str(kq_dung))
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Nội dung lời giải (Sử dụng \text{d}x theo yêu cầu)
            loigiai = (r'''Diện tích thiết diện là: $S(x) = %sx \cdot \sqrt{%sx^2 - %s}$. \\
                         Thể tích vật thể là: $V = \int_{%s}^{%s} %sx \sqrt{%sx^2 - %s} \text{d}x = %s$.'''
                       %(latex(k), latex(m), latex(n), 
                         latex(a), latex(b), latex(k), latex(m), latex(n), 
                         latex(V_val)))

            # Xuất câu trắc nghiệm đúng 100% định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

