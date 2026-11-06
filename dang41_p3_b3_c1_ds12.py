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


def bt_dang41_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp tìm bộ số ngẫu nhiên thỏa mãn
                while True:
                    A = random.choice([1, 2, 3, 4])
                    B = random.choice([-3, -2, -1, 1, 2, 3])
                    D = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
                    S0 = random.choice([4, 6, 8, 10, 12, 15, 16, 20])

                    # Đảm bảo nghiệm của mẫu không trùng làm triệt tiêu tử số
                    if A * D + B != 0:
                        break

                # Xây dựng chuỗi tử số
                if A == 1:
                    tu_str = "mx"
                else:
                    tu_str = "%smx" % A

                if B > 0:
                    tu_str += " + m" if B == 1 else " + %sm" % B
                else:
                    tu_str += " - m" if B == -1 else " - %sm" % abs(B)

                # Xây dựng chuỗi mẫu số
                if D > 0:
                    mau_str = "x - %s" % D
                else:
                    mau_str = "x + %s" % abs(D)

                # Chuỗi tiệm cận ngang y = Am
                Am_str = "m" if A == 1 else "%sm" % A

                # Tính toán các giá trị liên quan
                tu_at_D_val = A * D + B
                abs_AD = abs(A * D)
                m_abs = Rational(S0, abs_AD)

                # Đáp án đúng (luôn có 2 giá trị m phân biệt)
                kq = 2
                du = ['$2$']
                da = random.choice(du)

                # Các đáp án nhiễu
                s = ['$0$', '$1$', '$3$', '$4$', '$Vô số$']
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = \\frac{%s}{%s}$. Có bao nhiêu giá trị thực của tham số $m$ để đường tiệm cận đứng, tiệm cận ngang của đồ thị hàm số cùng với hai trục tọa độ tạo thành một hình chữ nhật có diện tích bằng %s?'''
                                 % (tu_str, mau_str, S0))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Xét hàm số $y = \\frac{%s}{%s}$:\\\\
            - Khi $m = 0$, hàm số trở thành $y = 0$, đồ thị không có đường tiệm cận.\\\\
            - Khi $m \\ne 0$, tử số tại $x = %s$ bằng $%s m \\ne 0$. Do đó, đồ thị hàm số có:\\\\
            + Đường tiệm cận đứng: $x = %s$.\\\\
            + Đường tiệm cận ngang: $y = %s$.\\\\
            Hai đường tiệm cận $x = %s$ và $y = %s$ cùng với hai trục tọa độ $x = 0$ và $y = 0$ tạo thành một hình chữ nhật có diện tích là:\\\\
            $$S = |%s| \\cdot |%s| = %s \\cdot |m|.$$\\\\
            Theo giả thiết, diện tích hình chữ nhật bằng $%s$, ta có:\\\\
            $$%s \\cdot |m| = %s \\iff |m| = %s \\iff m = \\pm %s.$$\\\\
            Cả hai giá trị này đều thỏa mãn $m \\ne 0$.\\\\
            Vậy có $2$ giá trị thực của tham số $m$ thỏa mãn yêu cầu bài toán.'''
                           % (tu_str, mau_str,
                              latex(D), latex(tu_at_D_val),
                              latex(D),
                              Am_str,
                              latex(D), Am_str,
                              latex(D), Am_str, latex(abs_AD),
                              S0,
                              latex(abs_AD), S0, latex(m_abs), latex(m_abs)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(2))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

