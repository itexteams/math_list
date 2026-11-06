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


def bt_dang42_p1_b3_c4_ds11(self):
            # Khai báo biến
            # Khởi tạo biến x
            x = symbols('x')

            # Bước 3: Suy nghĩ tìm cách random bài toán
            # Ta sẽ chọn các hệ số a, b sao cho hàm số đồng biến (a, b dương) 
            # Sau đó chọn c sao cho f(x) đổi dấu trong khoảng (-2, -1) hoặc (-1, 0)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số a, b dương để hàm số đơn điệu tăng (dễ kiểm soát nghiệm)
                a = random.randint(2, 9)
                b = random.randint(2, 9)

                # Chọn khoảng xét nghiệm: mẫu trong ảnh là (-2, -1)
                # Ta có thể random giữa các cặp khoảng: (-2, -1), (-1, 0), (0, 1)
                khoang_chon = random.choice([(-2, -1), (-1, 0)])
                x1, x2 = khoang_chon

                # Tính giá trị f(x) tại x1 và x2 (không có c)
                # f(x) = a*x^5 + b*x^3 + c
                val_x1_no_c = a*(x1**5) + b*(x1**3)
                val_x2_no_c = a*(x2**5) + b*(x2**3)

                # Để f(x1)*f(x2) < 0, ta chọn c nằm giữa -val_x1_no_c và -val_x2_no_c
                # Ví dụ: f(-2) < 0 và f(-1) > 0 => c > -val_x1_no_c và c < -val_x2_no_c (nếu val_x1 < val_x2)
                c_min = min(-val_x1_no_c, -val_x2_no_c)
                c_max = max(-val_x1_no_c, -val_x2_no_c)
                c = random.randint(int(c_min) + 1, int(c_max) - 1)

                # Biểu thức hàm số
                f_expr = a*x**5 + b*x**3 + c

                # Tính giá trị cụ thể để đưa vào lời giải
                f_x1 = a*(x1**5) + b*(x1**3) + c
                f_x2 = a*(x2**5) + b*(x2**3) + c
                tich = f_x1 * f_x2

                # Đáp án đúng
                da_dung = f'({x1}; {x2})'

                # Các đáp án sai (random các khoảng khác)
                list_sai = [
                    f'({x1-1}; {x1})',
                    f'({x2}; {x2+1})',
                    f'({x2+1}; {x2+2})',
                    f'(1; 2)',
                    f'(2; 3)'
                ]
                random.shuffle(list_sai)
                da_s1, da_s2, da_s3 = list_sai[:3]

                # Nội dung câu hỏi
                noidungcauhoi = (f'Phương trình ${latex(f_expr)} = 0$ có nghiệm thuộc khoảng nào sau đây?')

                # Các đáp án trắc nghiệm
                da_d = '\\True $' + da_dung + '$'
                list_ans = [da_d, f'${da_s1}$', f'${da_s2}$', f'${da_s3}$']
                random.shuffle(list_ans)

                # Lời giải chi tiết theo mẫu ảnh
                loigiai = (f'''Đặt $f(x) = {latex(f_expr)}$.\\\\
                           $f(x)$ liên tục trên $\\mathbb{{R}}$ nên $f(x)$ liên tục trên $[{x1}; {x2}]$ (1)\\\\
                           Ta có: $\\begin{{cases}} f({x1}) = {f_x1} \\\\ f({x2}) = {f_x2} \\end{{cases}}$\\\\
                           Suy ra $f({x1}) \\cdot f({x2}) = {f_x1} \\cdot {f_x2} = {tich} < 0$ (2)\\\\
                           Từ (1) và (2) suy ra $f(x) = 0$ có nghiệm thuộc khoảng $({x1}; {x2})$.''')

            # Xuất câu trắc nghiệm ra định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

