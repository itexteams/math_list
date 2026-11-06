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


def bt_dang68_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số: Ở bài gốc là y = x^2 - 4x + 3 và d = mx + 3
                # Để giữ nguyên dạng x1=0, ta giữ nguyên hệ số tự do của P và d giống nhau.
                c = random.randint(1, 10) # Hệ số tự do (trong ảnh là 3)
                b_p = random.randint(-6, -2) # Hệ số bậc 1 của P (trong ảnh là -4)

                # Biểu thức x1^3 + x2^3 = k. Trong ảnh k = 8.
                # Với x1 = 0, x2 = 4+m, thì (4+m)^3 = k => 4+m = căn bậc 3 của k.
                # Để m nguyên và đẹp, ta chọn k là một số lập phương (1, 8, 27, 64...)
                can_bac_3 = random.randint(1, 5)
                k = can_bac_3**3 

                # Tính toán đáp án đúng m
                # Phương trình: x^2 + (b_p - m)x = 0 => x1=0, x2 = m - b_p
                # x2^3 = k => x2 = can_bac_3 => m - b_p = can_bac_3 => m = can_bac_3 + b_p
                m_correct = can_bac_3 + b_p

                # Đáp án đúng
                da = '$m = %s$' % (m_correct)

                # Tạo các đáp án sai (không trùng đáp án đúng)
                s_values = set()
                while len(s_values) < 3:
                    sai = m_correct + random.choice([-3, -2, -1, 1, 2, 3])
                    if sai != m_correct:
                        s_values.add(sai)

                list_s = ['$m = %s$' % (latex(v)) for v in s_values]
                das1, das2, das3 = list_s[0], list_s[1], list_s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho parabol $(P): y = x^2 %s x + %s$ và đường thẳng $d: y = mx + %s$. Tìm các giá trị của $m$ để $d$ cắt $(P)$ tại hai điểm phân biệt $A, B$ có hoành độ $x_1, x_2$ thỏa mãn $x_1^3 + x_2^3 = %s$ là'''
                                  %(latex(b_p), latex(c), latex(c), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                # Biểu thức (m - b_p) trong code tương ứng với (4+m) trong ảnh nếu b_p = -4
                hieu_m = "m" + (" + " + str(-b_p) if b_p < 0 else " - " + str(b_p))

                loigiai=('''Phương trình hoành độ giao điểm của $(P)$ và $d$ là $x^2 %s x + %s = mx + %s$ \\\\
                          $\\Leftrightarrow x^2 - (%s + m)x = 0 \\Leftrightarrow \\left[\\begin{aligned} &x = 0 \\\\ &x = %s + m \\end{aligned}\\right.$ \\\\
                          Giả sử $x_1 = 0$ và $x_2 = %s + m$. Theo giả thiết, ta có: \\\\
                          $x_1^3 + x_2^3 = %s \\Leftrightarrow 0 + (%s + m)^3 = %s \\Leftrightarrow %s + m = %s \\Leftrightarrow m = %s$. \\\\
                          Vậy $m = %s$ thỏa yêu cầu bài toán.'''
                          %(latex(b_p), latex(c), latex(c), latex(-b_p), latex(-b_p), 
                            latex(-b_p), latex(k), latex(-b_p), latex(k), latex(-b_p), 
                            latex(can_bac_3), latex(m_correct), latex(m_correct)
                          ))

            # Xuất câu trắc nghiệm
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

