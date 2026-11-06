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


def bt_dang36_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số cho bài toán
                while True:
                    a = randint(-5, 5)
                    b = randint(-8, 8)
                    c = random.choice([2, 3, 4, 5])
                    k = randint(-4, 4)

                    # m = c*k - a
                    m_val = c * k - a

                    # Điều kiện để đồ thị hàm số không suy biến và m_val khác 0
                    if m_val != 0 and b != -k and (m_val + a) != 0 and b != 0:
                        break

                # Đáp án đúng
                kq = m_val

                # Các đáp án trắc nghiệm
                du = ['$m = %s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo các đáp án nhiễu
                s = [
                    '$m = %s$' % (latex(kq + 1)),
                    '$m = %s$' % (latex(kq + 2)),
                    '$m = %s$' % (latex(kq - 1)),
                    '$m = %s$' % (latex(kq - 2)),
                    '$m = %s$' % (latex(-kq if kq != 1 else 3)),
                    '$m = %s$' % (latex(kq + 3)),
                ]

                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Định dạng biểu thức chứa tham số m
                if a > 0:
                    tu_m = "(m + %s)x" % a
                    m_plus_a = "m + %s" % a
                elif a < 0:
                    tu_m = "(m - %s)x" % abs(a)
                    m_plus_a = "m - %s" % abs(a)
                else:
                    tu_m = "mx"
                    m_plus_a = "m"

                if b > 0:
                    tu_m += " + %sm" % b if b != 1 else " + m"
                elif b < 0:
                    tu_m += " - %sm" % abs(b) if abs(b) != 1 else " - m"

                mau_m = "%sx - m" % c

                # Biểu thức sau khi thay giá trị m cụ thể vào để thử lại trong lời giải
                tu_sub = latex((kq + a)*x + b*kq)
                mau_sub = latex(c*x - kq)

                # Câu hỏi
                noidungcauhoi = ('''Giá trị $m$ để đồ thị hàm số $y = \\frac{%s}{%s}$ có tiệm cận ngang là $y = %s$ bằng bao nhiêu?'''
                                 % (tu_m, mau_m, latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Đồ thị hàm số $y = \\frac{%s}{%s}$ có tiệm cận ngang khi hệ số của $x$ ở tử số khác $0$ ($%s \\ne 0$) và mẫu số có bậc nhất theo $x$ ($c = %s \\ne 0$).\\\\
            Ta có $\\lim_{x \\to \\pm\\infty} y = \\lim_{x \\to \\pm\\infty} \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\
            Do đó, đường tiệm cận ngang của đồ thị hàm số là $y = \\frac{%s}{%s}$.\\\\
            Theo bài ra, đồ thị hàm số có tiệm cận ngang là $y = %s$, suy ra:\\\\
            $$\\frac{%s}{%s} = %s \\iff %s = %s \\iff m = %s.$$\\\\
            Thử lại với $m = %s$, hàm số trở thành $y = \\frac{%s}{%s}$.\\\\
            Tử số và mẫu số không có nghiệm chung nên đồ thị hàm số nhận đường thẳng $y = %s$ làm tiệm cận ngang.\\\\
            Vậy $m = %s$.'''
                           % (tu_m, mau_m, m_plus_a, c,
                              tu_m, mau_m, m_plus_a, c,
                              m_plus_a, c,
                              latex(k),
                              m_plus_a, c, latex(k), m_plus_a, latex(c * k), latex(kq),
                              latex(kq), tu_sub, mau_sub,
                              latex(k),
                              latex(kq)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

