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


def bt_dang59_p1_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo danh sách dạng (ở đây có 1 dạng bài)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- Bước 3: Tìm cách random bài toán ---
                # k là khoảng cách giữa 2 giá trị f (trong đề bài là 2019 - 2009 = 10)
                k = random.choice([10, 20, 5]) 

                # b là giá trị nhỏ (năm hoặc số thứ tự, ví dụ 2009)
                b = random.randint(2000, 2025)
                a = b + k

                # f(k) theo công thức n(n+1)/2
                fk = k * (k + 1) // 2
                bk = b * k

                # Chọn kết quả bài toán T (ví dụ T = 2, 3, 4)
                # Sao cho T là số nguyên để log ra đẹp
                T_kq = random.choice([2, 3, 4])

                # Tính toán hằng số C trong đề bài
                # T = log10( (fk + bk - C) / 2 ) => 10^T = (fk + bk - C) / 2
                # => C = fk + bk - 2 * (10^T)
                target_power = 10**T_kq
                C = fk + bk - 2 * target_power

                # Đảm bảo C > 0 để bài toán thực tế, nếu không thì lấy mặc định như hình
                if C <= 0:
                    k, b, T_kq = 10, 2009, 4
                    fk, bk = 55, 20090
                    C = 145

                # Đáp án đúng
                kq = T_kq
                da_d = ('\\True $%s$' % (latex(kq)))

                # --- Bước 4: Điều chỉnh phương án sai ---
                s = [kq + 1, kq - 1, kq + 2, kq - 2, 0, 1]
                # Loại bỏ giá trị trùng với đáp án đúng
                s = list(set([x for x in s if x != kq and x >= 0]))
                random.shuffle(s)

                da_s1 = '$%s$' % (latex(s[0]))
                da_s2 = '$%s$' % (latex(s[1]))
                da_s3 = '$%s$' % (latex(s[2]))

                # Nội dung câu hỏi
                noidungcauhoi = (
                    r'Cho $f(1)=1$; $f(m+n) = f(m) + f(n) + mn$ với mọi $m, n \in N^*$. '
                    r'Giá trị của biểu thức $T = \log \left[ \frac{f(%s) - f(%s) - %s}{2} \right]$ bằng'
                    % (latex(a), latex(b), latex(C))
                )

                # Nội dung lời giải
                sum_k_minus_1 = (k-1)*k // 2
                loigiai = (
                    r'Ta có $f(%s) = f(%s + %s) = f(%s) + f(%s) + %s \cdot %s = f(%s) + f(%s) + %s$. \\'
                    r'Do đó $f(%s) - f(%s) - %s = f(%s) + %s - %s = f(%s) + %s$. \\'
                    r'Mặt khác, từ $f(n) = f(n-1) + f(1) + (n-1)$, ta suy ra: \\'
                    r'$f(%s) = %s \cdot f(1) + (1 + 2 + \dots + %s) = %s \cdot 1 + %s = %s$. \\'
                    r'Vậy $T = \log \left[ \frac{%s + %s}{2} \right] = \log %s = %s$.'
                    % (latex(a), latex(b), latex(k), latex(b), latex(k), latex(b), latex(k), latex(b), latex(k), latex(bk),
                       latex(a), latex(b), latex(C), latex(k), latex(bk), latex(C), latex(k), latex(bk - C),
                       latex(k), latex(k), latex(k-1), latex(k), latex(sum_k_minus_1), latex(fk),
                       latex(fk), latex(bk - C), latex(target_power * 2 // 2), latex(kq))
                )

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\choice \n'
                           '{' + str(list_1[0]) + '}\n'
                           '{' + str(list_1[1]) + '}\n'
                           '{' + str(list_1[2]) + '}\n'
                           '{' + str(list_1[3]) + '}\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

