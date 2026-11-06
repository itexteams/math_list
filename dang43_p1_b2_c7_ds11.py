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


def bt_dang43_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Thiết lập tham số random ---
                # Ta chọn các số nguyên sao cho Delta của đạo hàm là số không chính phương để có căn
                # y' = x^2 - a*x - b
                a_val = random.randint(1, 3) 
                b_val = random.randint(3, 6)
                c_val = random.randint(2000, 2026)

                # Thiết lập hàm số y = 1/3*x^3 - (a/2)*x^2 - b*x + c
                f = Rational(1, 3)*x**3 - Rational(a_val, 2)*x**2 - b_val*x + c_val

                # Tính đạo hàm y'
                f_prime = diff(f, x)

                # Giải phương trình y' = 0 để tìm nghiệm chính xác (dạng căn thức)
                roots = solve(f_prime, x)
                x1, x2 = min(roots), max(roots)

                # --- Xác định tập hợp nghiệm nguyên S ---
                # Sử dụng evalf() để lấy giá trị xấp xỉ chỉ phục vụ việc xác định biên nguyên
                start_int = int(ceiling(x1.evalf()))
                end_int = int(floor(x2.evalf()))
                S_set = list(range(start_int, end_int + 1))

                # Tính tổng các phần tử của S
                tong_S = sum(S_set)

                # --- B2: Viết nội dung câu hỏi và lời giải ---

                noidungcauhoi = (r'Cho hàm số $y = %s$. Gọi $S$ là tập hợp tất cả các nghiệm nguyên của bất phương trình $y^\prime \le 0$. Tổng tất cả các phần tử của $S$ bằng' 
                                 % (latex(f)))

                # Đáp án đúng
                da_d = '\\True $%s$' % latex(tong_S)

                # Tạo đáp án nhiễu
                s_wrong = [
                    '$%s$' % latex(tong_S + 1),
                    '$%s$' % latex(tong_S - 1),
                    '$%s$' % latex(tong_S + 2)
                ]
                random.shuffle(s_wrong)

                list_1 = [da_d, s_wrong[0], s_wrong[1], s_wrong[2]]
                random.shuffle(list_1)

                # Nội dung lời giải (Hiển thị nghiệm đúng dạng phân số/căn thức)
                str_S = '\\{' + '; '.join(map(str, S_set)) + '\\}'

                loigiai = (r'''Ta có $y^\prime = %s$. \\
                           Xét bất phương trình $y^\prime \le 0 \Leftrightarrow %s \le 0$. \\
                           Giải phương trình $y^\prime = 0$ ta được các nghiệm: \\
                           $x_1 = %s$; $x_2 = %s$. \\
                           Do đó $y^\prime \le 0 \Leftrightarrow %s \le x \le %s$. \\
                           Vì $x \in \mathbb{Z}$ nên $S = %s$. \\
                           Vậy tổng các phần tử của tập hợp $S$ bằng: %s.''' 
                           % (latex(f_prime), latex(f_prime), 
                              latex(x1), latex(x2), 
                              latex(x1), latex(x2), 
                              str_S, latex(tong_S)))

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

