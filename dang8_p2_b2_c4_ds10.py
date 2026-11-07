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


def bt_dang8_p2_b2_c4_ds10(self):
                # Khai báo biến
                # Khai báo biến Sympy
                x = symbols('x')
                
                # --- SINH DỮ LIỆU NGẪU NHIÊN ---
                # Giả sử đỉnh I(x0, y0) và đi qua điểm A(x_pass, y_pass)
                x0 = 1 
                y0 = random.randint(2, 5) 
                x_pass = x0 + 1
                y_pass = y0 - random.randint(1, 2) # Để đồ thị quay bề lõm xuống (a < 0)
                
                # Tính toán hệ số a, b, c cho f(x) = ax^2 + bx + c
                # f(x) = a(x - x0)^2 + y0
                a_val = (y_pass - y0)
                b_val = -2 * a_val * x0
                c_val = a_val * x0**2 + y0
                f_x = a_val*x**2 + b_val*x + c_val
                
                # Các giá trị tính toán hỗ trợ
                f_0 = c_val
                f_minus_1 = a_val*(-1)**2 + b_val*(-1) + c_val
                
                # Nội dung câu hỏi
                noidungcauhoi = r'''Cho hàm số bậc hai $y = f(x)$ có $f(%s) = %s$ và bảng biến thiên như sau:
\begin{center}
\begin{tikzpicture}
\tkzTabInit[espcl=2.5,lgt=1.5]
{$x$/1,$f(x)$/2}
{$-\infty$,$%s$,$+\infty$}
\tkzTabVar{-/$-\infty$,+/$%s$,-/$-\infty$}
\end{tikzpicture}
\end{center}''' % (latex(x_pass), latex(y_pass), latex(x0), latex(y0))
                
                ########################################################################
                # a) NHẬN BIẾT: Giá trị lớn nhất
                a_d = r'\True Hàm số đạt giá trị lớn nhất bằng %s' % (latex(y0))
                a_s = r'Hàm số đạt giá trị lớn nhất bằng %s' % (latex(x0))
                list_a = [a_d, a_s]
                loigiai_a = r'Dựa vào bảng biến thiên, hàm số đạt giá trị lớn nhất bằng %s tại $x = %s$.' % (latex(y0), latex(x0))
                
                ########################################################################
                # b) THÔNG HIỂU: Công thức hàm số
                b_d = r'\True Hàm số bậc hai là $y = %s$' % (latex(f_x))
                b_s = r'Hàm số bậc hai là $y = %sx^2 + %sx + %s$' % (latex(a_val*2), latex(b_val), latex(c_val))
                list_b = [b_d, b_s]
                loigiai_b = (r'Gọi $f(x) = ax^2 + bx + c$. Từ BBT và giả thiết ta có hệ: '
                             r'$\begin{cases} f(%s) = %s \\ -\frac{b}{2a} = %s \\ f(%s) = %s \end{cases} \Rightarrow \begin{cases} a = %s \\ b = %s \\ c = %s \end{cases}$. '
                             r'Vậy $f(x) = %s$.' 
                             % (latex(x_pass), latex(y_pass), latex(x0), latex(x0), latex(y0), latex(a_val), latex(b_val), latex(c_val), latex(f_x)))
                
                ########################################################################
                # c) VẬN DỤNG: Giá trị tại x = 0
                c_d = r'\True Giá trị của hàm số tại $x = 0$ là %s' % (latex(f_0))
                c_s = r'Giá trị của hàm số tại $x = 0$ là %s' % (latex(f_0 + 1))
                list_c = [c_d, c_s]
                loigiai_c = r'Thay $x = 0$ vào biểu thức hàm số: $f(0) = %s(0)^2 + %s(0) + %s = %s$.' % (latex(a_val), latex(b_val), latex(c_val), latex(f_0))
                
                ########################################################################
                # d) VẬN DỤNG CAO: Giá trị tại x = -1
                d_d = r'\True Giá trị của hàm số tại $x = -1$ là %s' % (latex(f_minus_1))
                d_s = r'Giá trị của hàm số tại $x = -1$ là %s' % (latex(f_minus_1 - 2))
                list_d = [d_d, d_s]
                loigiai_d = r'Thay $x = -1$ vào biểu thức hàm số: $f(-1) = %s(-1)^2 + %s(-1) + %s = %s$.' % (latex(a_val), latex(b_val), latex(c_val), latex(f_minus_1))
                
                ########################################################################
                # Kiểm soát số lượng câu đúng từ 1 đến 3
                def count_true(answers):
                    return sum('\\True' in ans for ans in answers)
                
                while True:
                    ans_a = random.choice(list_a)
                    ans_b = random.choice(list_b)
                    ans_c = random.choice(list_c)
                    ans_d = random.choice(list_d)
                    if 1 <= count_true([ans_a, ans_b, ans_c, ans_d]) <= 3:
                        break
                
                # Xuất nội dung theo mẫu dang19
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + 
                    str(noidungcauhoi) + '\n' +
                    '\\choiceTFn \n'
                    '{' + ans_a + '}\n'
                    '{' + ans_b + '}\n'
                    '{' + ans_c + '}\n'
                    '{' + ans_d + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + loigiai_a + '\n'
                    '\\item ' + loigiai_b + '\n'
                    '\\item ' + loigiai_c + '\n'
                    '\\item ' + loigiai_d + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n')
                return content