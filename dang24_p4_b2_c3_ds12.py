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


def bt_dang24_p4_b2_c3_ds12(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                x = sp.Symbol('x')

                # Random hệ số A và B (Trong ảnh A=2, B=1)
                A = random.randint(1, 5)
                B = random.randint(1, 4)

                # Random cận trên (Trong ảnh là pi/3)
                list_can = [pi/6, pi/4, pi/3]
                a = random.choice(list_can)

                # Hàm số và nguyên hàm
                f = A*sin(x) + B/(cos(x)**2)
                F = -A*cos(x) + B*tan(x)

                # Tính giá trị tại các cận
                val_upper = F.subs(x, a)
                val_lower = F.subs(x, 0)
                kq_final = simplify(val_upper - val_lower)

                # Đáp án đúng
                da_dung = '$%s$' % latex(kq_final)

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo nhiễu bằng cách thay đổi dấu hoặc nhầm lẫn nguyên hàm
                    sai_1 = simplify(val_upper + val_lower) # Sai dấu tích phân
                    sai_2 = simplify(val_upper)             # Quên trừ cận dưới
                    sai_3 = simplify(A*cos(a) + B*tan(a) - A) # Sai dấu nguyên hàm cos
                    sai_4 = simplify(kq_final + random.randint(1, 3))

                    for gia_tri in [sai_1, sai_2, sai_3, sai_4]:
                        temp_latex = '$%s$' % latex(gia_tri)
                        if temp_latex != da_dung:
                            s.add(temp_latex)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Bước 2: Viết lại nội dung câu hỏi
                noidungcauhoi = (r'Tính $\displaystyle \int_{0}^{%s} \left( %s \sin x + \frac{%s}{\cos^2 x} \right) \text{d} x$.'
                                 % (latex(a), latex(A) if A != 1 else "", latex(B) if B != 1 else "1"))

                # Nội dung lời giải chi tiết
                loigiai = (r'''Ta có nguyên hàm của hàm số là:
                             $\displaystyle \int \left( %s \sin x + \frac{%s}{\cos^2 x} \right) \text{d} x = %s + C$. \\
                             Áp dụng công thức Newton-Leibniz: \\
                             $\displaystyle \int_{0}^{%s} \left( %s \sin x + \frac{%s}{\cos^2 x} \right) \text{d} x = \left( %s \right) \bigg|_{0}^{%s}$ \\
                             $= \left( %s \right) - \left( %s \right) = %s$.'''
                           % (latex(A) if A != 1 else "", latex(B) if B != 1 else "1", latex(F),
                              latex(a), latex(A) if A != 1 else "", latex(B) if B != 1 else "1", latex(F), latex(a),
                              latex(val_upper), latex(val_lower), latex(kq_final)
                              ))

                # Trộn đáp án
                da_d = '\\True ' + da_dung
                list_ans = [da_d, das1, das2, das3]
                random.shuffle(list_ans)

                # Xuất kết quả theo mẫu
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

