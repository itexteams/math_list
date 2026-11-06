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


def bt_dang9_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến Sympy
            x = symbols('x')
            m = symbols('m')

            # --- SINH DỮ LIỆU NGẪU NHIÊN ---
            # Parabol (P): y = ax^2 + bx + c. Mặc định a=1 để bài toán đẹp.
            a_val = 1
            b_val = random.randint(-5, -2) 
            c_val = random.randint(1, 3)
            f_x = a_val*x**2 + b_val*x + c_val

            # Đường thẳng d: y = x - m
            # Phương trình hoành độ giao điểm chung: x^2 + (b_val-1)x + (c_val+m) = 0
            # Hệ số phương trình bậc hai theo m: A=1, B=(b_val-1), C=(c_val+m)
            B_eq = b_val - 1

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $y = %s$ có đồ thị $(P)$ và đường thẳng $d: y = x - m$.''' % (latex(f_x))

            ########################################################################
            # a) NHẬN BIẾT: Vị trí tương đối của d và Delta: y = x
            a_d = r'\True Đường thẳng $d$ song song hoặc trùng với đường thẳng $\Delta: y = x$'
            a_s = r'Đường thẳng $d$ luôn song song với đường thẳng $\Delta: y = x$'
            list_a = [a_d, a_s]
            loigiai_a = (r'Đường thẳng $d$ và $\Delta$ đều có hệ số góc bằng $1$. '
                         r'Khi $m=0$ thì $d \equiv \Delta$, khi $m \neq 0$ thì $d \parallel \Delta$. '
                         r'Do đó $d$ song song hoặc trùng với $\Delta$.')

            ########################################################################
            # b) THÔNG HIỂU: Thay m cụ thể (m=2)
            m_fix = 2
            # Giải PT: x^2 + B_eq*x + (c_val + m_fix) = 0
            C_eq_b = c_val + m_fix
            delta_b = B_eq**2 - 4*a_val*C_eq_b

            # Tính nghiệm giao điểm
            x_sol = solve(x**2 + B_eq*x + C_eq_b, x)
            if len(x_sol) == 2:
                x1, x2 = x_sol
                y1, y2 = x1 - m_fix, x2 - m_fix
                b_d = r'\True Khi $m = %s$, $d$ cắt $(P)$ tại hai điểm $(%s; %s)$ và $(%s; %s)$' % (m_fix, latex(x1), latex(y1), latex(x2), latex(y2))
                b_s = r'Khi $m = %s$, $d$ cắt $(P)$ tại duy nhất một điểm' % (m_fix)
                loigiai_b = (r'Với $m = %s$, phương trình hoành độ giao điểm là: '
                             r'$%s = x - %s \Leftrightarrow x^2 %s x + %s = 0 \Leftrightarrow \left[\begin{smallmatrix} x=%s \\ x=%s \end{smallmatrix}\right.$. '
                             r'Tọa độ giao điểm là $(%s; %s)$ và $(%s; %s)$.' 
                             % (m_fix, latex(f_x), m_fix, latex(B_eq), latex(C_eq_b), latex(x1), latex(x2), latex(x1), latex(y1), latex(x2), latex(y2)))
            else:
                # Trường hợp delta không đẹp (hiếm với khoảng random này) thì lấy giá trị x=1, x=3 làm chuẩn
                b_d = r'\True Khi $m = 2$, $d$ cắt $(P)$ tại hai điểm phân biệt'
                b_s = r'Khi $m = 2$, $d$ tiếp xúc với $(P)$ tại một điểm'
                loigiai_b = r'Thay $m=2$ vào phương trình hoành độ và giải tìm nghiệm.'

            list_b = [b_d, b_s]

            ########################################################################
            # c) VẬN DỤNG: Điều kiện 2 nghiệm phân biệt (Delta > 0)
            # Delta = B_eq^2 - 4(c_val + m) = B_eq^2 - 4*c_val - 4m
            # Delta > 0 <=> 4m < B_eq^2 - 4*c_val <=> m < (B_eq^2 - 4*c_val)/4
            m_limit = Rational(B_eq**2 - 4*c_val, 4)

            c_d = r'\True Đường thẳng $d$ cắt đồ thị $(P)$ tại hai điểm khi và chỉ khi $m < %s$' % (latex(m_limit))
            c_s = r'Đường thẳng $d$ cắt đồ thị $(P)$ tại hai điểm khi và chỉ khi $m > %s$' % (latex(m_limit))
            list_c = [c_d, c_s]
            loigiai_c = (r'Phương trình hoành độ giao điểm: $x^2 + (%s)x + m + %s = 0$. '
                         r'$d$ cắt $(P)$ tại 2 điểm khi $\Delta = (%s)^2 - 4(m + %s) > 0 \Leftrightarrow %s - 4m > 0 \Leftrightarrow m < %s$.' 
                         % (B_eq, c_val, B_eq, c_val, B_eq**2 - 4*c_val, latex(m_limit)))

            ########################################################################
            # d) VẬN DỤNG CAO: Nghiệm trái dấu (a*c < 0)
            # PT: x^2 + B_eq*x + (m + c_val) = 0. Nghiệm trái dấu <=> 1*(m + c_val) < 0 <=> m < -c_val
            d_d = r'\True Đường thẳng $d$ cắt $(P)$ tại hai điểm có hoành độ trái dấu khi và chỉ khi $m < %s$' % (latex(-c_val))
            d_s = r'Đường thẳng $d$ cắt $(P)$ tại hai điểm có hoành độ trái dấu khi và chỉ khi $m > %s$' % (latex(-c_val))
            list_d = [d_d, d_s]
            loigiai_d = (r'Để hai giao điểm có hoành độ trái dấu thì phương trình hoành độ giao điểm có $ac < 0$. '
                         r'Suy ra $1 \cdot (m + %s) < 0 \Leftrightarrow m < %s$.' % (c_val, latex(-c_val)))

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

