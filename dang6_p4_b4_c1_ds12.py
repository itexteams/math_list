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


def bt_dang6_p4_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dùng vòng lặp để đảm bảo kết quả kq_m luôn < 9999 và là số nguyên
                while True:
                    # Khởi tạo tham số ngẫu nhiên
                    a_num = randint(1, 3)
                    a_den = randint(1, 4)
                    a = Rational(a_num, a_den)
                    k = randint(1, 4)  # Thời điểm t đạt độ cao lớn nhất
                    b = Rational(3 * a * k, 2)

                    t = symbols('t')
                    h_func = -a * t**3 + b * t**2
                    dh_func = sp.diff(h_func, t)

                    # Tính các giá trị
                    val_k = h_func.subs(t, k)
                    kq_m = val_k * 1000  # Đổi ra mét

                    if 0 < kq_m < 9999 and kq_m.is_Integer:
                        t_end = Rational(3 * k, 2)  # Thời điểm kết thúc (độ cao trở về 0)
                        break

                # Đáp án đúng
                du = ['$%s$' % (latex(kq_m))]
                da = random.choice(du)

                # Tạo danh sách các phương án sai (có điều kiện để tránh sinh ra số âm khi trừ)
                s = [
                    '$%s$' % (latex(kq_m + 1000)),
                    '$%s$' % (latex(kq_m - 1000)) if kq_m > 1000 else '$%s$' % (latex(kq_m + 1500)),
                    '$%s$' % (latex(kq_m + 2000)),
                    '$%s$' % (latex(kq_m - 2000)) if kq_m > 2000 else '$%s$' % (latex(kq_m + 2500)),
                    '$%s$' % (latex(kq_m + 500)),
                    '$%s$' % (latex(kq_m - 500)) if kq_m > 500 else '$%s$' % (latex(kq_m + 750)),
                    '$%s$' % (latex(val_k)),  # Nhầm lẫn đơn vị km thay vì m
                ]

                # Lọc đáp án trùng với đáp án đúng và loại bỏ trùng lặp
                s = [ans.replace('.', ',') for ans in s if ans != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Ngày khai giảng năm học $2026 - 2027$. Học sinh khối 12 trường THPT Lý Tự Trọng thả chùm bóng bay gắn thông điệp "Học sinh khối 12 sẽ đậu đại học". Ước tính độ cao $h$ (tính bằng $km$) của chùm bóng bay so với mặt đất vào thời điểm $t$ (đơn vị giờ) được cho bởi công thức $h(t) = %s, (0 \\le t \\le %s)$. Tính độ cao lớn nhất của chùm bóng bay đạt độ cao lớn nhất so với mặt đất.'''
                                 % (latex(h_func).replace('.', ','),
                                    latex(t_end).replace('.', ',')
                                   ))

                # Các đáp án
                da_d = ('\\True ' + str(da).replace('.', ','))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số $h(t) = %s$ xác định và liên tục trên đoạn $[0; %s]$.\\\\
            Ta có $h'(t) = %s$.\\\\
            $h'(t) = 0 \\iff %s = 0 \\iff \\left[ \\begin{array}{l} t = 0 \\\\ t = %s \\end{array} \\right.$ (đều thuộc đoạn $[0; %s]$).\\\\
            Tính các giá trị:\\\\
            $h(0) = 0$ (km);\\\\
            $h(%s) = %s$ (km);\\\\
            $h(%s) = 0$ (km).\\\\
            So sánh các giá trị trên, ta thấy độ cao lớn nhất của chùm bóng bay đạt được tại thời điểm $t = %s$ giờ và độ cao lớn nhất đó là $%s$ km = $%s$ mét.'''

                           % (latex(h_func).replace('.', ','),
                              latex(t_end).replace('.', ','),
                              latex(dh_func).replace('.', ','),
                              latex(dh_func).replace('.', ','),
                              latex(k),
                              latex(t_end).replace('.', ','),
                              latex(k),
                              latex(val_k).replace('.', ','),
                              latex(t_end).replace('.', ','),
                              latex(k),
                              latex(val_k).replace('.', ','),
                              latex(kq_m).replace('.', ',')
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

