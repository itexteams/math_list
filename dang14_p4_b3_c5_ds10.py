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


def bt_dang14_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Random số mũ n của biểu thức [1 + x^2(1-x)]^n
                n = random.randint(8, 12)

                # Tính toán các hệ số thành phần
                # Hệ số x^8 xuất hiện ở số hạng chứa (x^2(1-x))^3 và (x^2(1-x))^4
                # Số hạng i=3: C(n,3) * x^6 * (1-x)^3 -> cần x^2 từ (1-x)^3 -> C(n,3) * C(3,2) * (-1)^2
                # Số hạng i=4: C(n,4) * x^8 * (1-x)^4 -> cần x^0 từ (1-x)^4 -> C(n,4) * C(4,0) * (-1)^0

                c_n_3 = math.comb(n, 3)
                c_n_4 = math.comb(n, 4)
                c_3_2 = math.comb(3, 2)
                c_4_0 = math.comb(4, 0)

                val1 = c_n_3 * c_3_2
                val2 = c_n_4 * c_4_0
                kq_val = val1 + val2

                # Đáp án đúng
                kq = str(kq_val)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s_vals = set()
                while len(s_vals) < 3:
                    # Tạo các phương án sai dựa trên các sai lầm thường gặp hoặc lân cận
                    distractor = kq_val + random.choice([-1, 1, -10, 10, -20, 20]) * random.randint(1, 5)
                    if distractor != kq_val and distractor > 0:
                        s_vals.add(distractor)

                list_s = ['$%s$' % str(v) for v in s_vals]

                # Câu hỏi
                noidungcauhoi = ('''Tìm hệ số của $x^8$ trong khai triển thành đa thức của $\\left[1 + x^2\\left(1 - x\\right)\\right]^{%s}$.'''
                                 % (latex(n)))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq))
                da_s1 = list_s[0]
                da_s2 = list_s[1]
                da_s3 = list_s[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B1 & B2: Viết lại y hệt cấu trúc lời giải mẫu)
                # Tạo chuỗi khai triển tổng quát cho n
                khai_trien_mau = 'C_{%s}^0 + C_{%s}^1 x^2\\left(1 - x\\right) + C_{%s}^2 x^4\\left(1 - x\\right)^2 + C_{%s}^3 x^6\\left(1 - x\\right)^3 + C_{%s}^4 x^8\\left(1 - x\\right)^4 + \\dots + C_{%s}^{%s} x^{2%s}\\left(1 - x\\right)^{%s}' % (n, n, n, n, n, n, n, n, n)

                loigiai = ('''Ta có: $\\left[1 + x^2\\left(1 - x\\right)\\right]^{%s} = %s$. \\\\
            Nhận xét: \\\\
            Bậc của $x$ trong 3 số hạng đầu luôn nhỏ hơn 8. \\\\
            Bậc của $x$ trong các số hạng từ thứ 6 trở đi luôn lớn hơn 8. \\\\
            Do đó $x^8$ chỉ có trong số hạng thứ tư và thứ năm. \\\\
            Xét trong khai triển $C_{%s}^3 x^6\\left(1 - x\\right)^3$ thì hệ số của $x^8$ là: $C_{%s}^3 \\cdot C_3^2 = %s$. \\\\
            Xét trong khai triển $C_{%s}^4 x^8\\left(1 - x\\right)^4$ thì hệ số của $x^8$ là: $C_{%s}^4 \\cdot C_4^0 = %s$. \\\\
            Vậy hệ số của $x^8$ trong khai triển $\\left[1 + x^2\\left(1 - x\\right)\\right]^{%s}$ là: $%s + %s = %s$.'''
                           % (latex(n), khai_trien_mau,
                              latex(n), latex(n), latex(val1),
                              latex(n), latex(n), latex(val2),
                              latex(n), latex(val1), latex(val2), latex(kq_val)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

