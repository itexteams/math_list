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


def bt_dang39_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Bước 1 & 3: Thiết lập tham số ngẫu nhiên cho bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn hệ số 'a' (Trong đề gốc a=1)
                a = random.choice([1, 2, 3]) 

                # Giả thiết f(1) = 1
                x0 = 1
                f_x0 = 1

                # Giá trị k cần tính f(k) (Trong đề gốc k=2)
                k = random.choice([2, 3, 4, 5])

                # Tính toán các giá trị trung gian
                # C = x0/f_x0 - (a * x0^2)/2
                C = Rational(x0, f_x0) - Rational(a * x0**2, 2)

                # Tính f(k) = 2k / (a*k^2 + 2C)
                f_k = Rational(2*k, a*k**2 + 2*C)
                kq_final = simplify(f_k)

                # Bước 4: Tạo các phương án sai (Sử dụng sp.fraction để tránh lỗi)
                def generate_distractors(correct_val):
                    s = set()
                    # Sử dụng sp.fraction thay vì .as_numer_den()
                    num, den = fraction(correct_val)

                    # Các kiểu nhiễu toán học thường gặp
                    options = [
                        Rational(den, num),              # Nghịch đảo
                        correct_val + Rational(1, 2),    # Sai lệch hằng số
                        correct_val - Rational(1, 3),
                        Rational(num + 1, den),          # Sai tử số
                        Rational(num, den + 1),          # Sai mẫu số
                        Rational(num * 2, den),          # Quên chia hệ số
                        Rational(num, den * 2)
                    ]

                    for opt in options:
                        if opt != correct_val and opt > 0:
                            s.add('$%s$' % latex(opt))

                    # Đảm bảo luôn có ít nhất 3 phương án sai
                    while len(s) < 3:
                        random_val = Rational(random.randint(1, 9), random.randint(2, 9))
                        if random_val != correct_val:
                            s.add('$%s$' % latex(random_val))

                    return list(s)

                wrong_answers = generate_distractors(kq_final)
                random.shuffle(wrong_answers)

                das1 = wrong_answers[0]
                das2 = wrong_answers[1]
                das3 = wrong_answers[2]

                # Nội dung câu hỏi
                expr_right = "f(x) - xf^2(x)" if a == 1 else "f(x) - %s xf^2(x)" % a
                noidungcauhoi = (r"Cho hàm số $f(x)$ thỏa mãn $x \cdot f'(x) = %s$ với mọi $x \in (0; +\infty)$. Biết $f(%s) = %s$. Tính giá trị của $f(%s)$."
                                 % (expr_right, x0, f_x0, k))

                # Đáp án đúng
                da_d = r'\True $%s$' % latex(kq_final)

                # Trộn đáp án
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (r"Xét $x \in (0; +\infty)$.\\"
                           r"Ta có: $x \cdot f'(x) = f(x) %s xf^2(x) \Leftrightarrow \frac{f(x) - x \cdot f'(x)}{f^2(x)} = %s x$\\"
                           r"$\Leftrightarrow \left[ \frac{x}{f(x)} \right]' = %s x \Rightarrow \frac{x}{f(x)} = \frac{%s x^2}{2} + C$.\\"
                           r"Do $f(%s) = %s \Rightarrow \frac{%s}{%s} = \frac{%s \cdot %s^2}{2} + C \Rightarrow C = %s$.\\"
                           r"Khi đó: $\frac{x}{f(x)} = \frac{%s x^2}{2} + %s \Rightarrow f(x) = \frac{2x}{%s x^2 + %s}$.\\"
                           r"Vậy $f(%s) = \frac{2 \cdot %s}{%s \cdot %s^2 + %s} = %s$."
                           % ("-" if a == 1 else "- %s" % a, 
                              "" if a == 1 else a,
                              "" if a == 1 else a,
                              "" if a == 1 else a,
                              x0, f_x0, x0, f_x0, a, x0, latex(C),
                              "" if a == 1 else a, latex(C),
                              "" if a == 1 else a, latex(2*C),
                              k, k, "" if a == 1 else a, k, latex(2*C), latex(kq_final)))

            # Xuất câu trắc nghiệm định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

