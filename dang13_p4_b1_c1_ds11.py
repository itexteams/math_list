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


def bt_dang13_p4_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Biểu thức dạng S = [A*sin(m*pi/2 - x) - B*cos(x - pi)] / [cos(p*pi/2 - x)]
                # Random các hệ số
                A = randint(1, 3)
                B = randint(2, 5)

                # Góc m lẻ ở tử số dạng 4n + 3 (ví dụ 7, 11, 15) -> sin(m*pi/2 - x) = -cos(x)
                n1 = randint(1, 3)
                m = 4 * n1 + 3

                # Góc p lẻ ở mẫu số dạng 4n + 1 (ví dụ 5, 9, 13) -> cos(p*pi/2 - x) = sin(x)
                n2 = randint(1, 3)
                p = 4 * n2 + 1

                # Tính toán k: Tử số = A*(-cos(x)) - B*(-cos(x)) = (B - A)*cos(x)
                # Mẫu số = sin(x)
                # S = (B - A)*cot(x) -> k = B - A
                k_val = B - A

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(k_val))]
                da = random.choice(du)

                # Tạo phương án nhiễu (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = k_val + randint(-4, 4)
                    if sai != k_val:
                        s.add('$%s$' % (latex(sai)))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Định dạng chuỗi hiển thị biểu thức trong câu hỏi
                # Nếu A = 1 thì không cần in số 1 phía trước sin
                A_str = '' if A == 1 else latex(A)

                # Câu hỏi
                noidungcauhoi = ('''Biểu thức sau: $S = \\frac{%s\\sin\\left(\\frac{%s\\pi}{2} - x\\right) - %s\\cos(x - \\pi)}{\\cos\\left(\\frac{%s\\pi}{2} - x\\right)} = k\\cot x$. Tính giá trị $k$.'''
                                 % (A_str, latex(m), latex(B), latex(p)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                m_chu_ky = 2 * (n1 + 1)
                p_chu_ky = 2 * n2
                loigiai = ('''Ta sử dụng các công thức góc liên kết để rút gọn từng thành phần lượng giác: \\\\
                           + $\\sin\\left(\\frac{%s\\pi}{2} - x\\right) = \\sin\\left(%s\\pi - \\frac{\\pi}{2} - x\\right) = \\sin\\left(-\\frac{\\pi}{2} - x\\right) = -\\cos x$. \\\\
                           + $\\cos(x - \\pi) = \\cos(\\pi - x) = -\\cos x$. \\\\
                           + $\\cos\\left(\\frac{%s\\pi}{2} - x\\right) = \\cos\\left(%s\\pi + \\frac{\\pi}{2} - x\\right) = \\cos\\left(\\frac{\\pi}{2} - x\\right) = \\sin x$. \\\\
                           Thay vào biểu thức $S$, ta được: \\\\
                           $S = \\frac{%s \\cdot (-\\cos x) - %s \\cdot (-\\cos x)}{\\sin x} = \\frac{(%s - %s)\\cos x}{\\sin x} = %s \\cdot \\frac{\\cos x}{\\sin x} = %s\\cot x$. \\\\
                           Đối chiếu với giả thiết $S = k\\cot x$, ta suy ra $k = %s$.'''
                           % (latex(m), latex(m_chu_ky), latex(p), latex(p_chu_ky),
                              latex(A), latex(B), latex(B), latex(A), latex(k_val), latex(k_val), latex(k_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

