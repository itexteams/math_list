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


def bt_dang30_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Parabol có dạng y = ax^2 + bx + c. Trong ảnh c = 2.
                # Ta sẽ random a, b nguyên để bài toán đẹp
                a_val = random.randint(-5, 5)
                if a_val == 0: a_val = 1 # Đảm bảo là parabol
                b_val = random.randint(-5, 5)
                c_val = 2 # Giữ cố định theo đề bài trong ảnh

                # Chọn ngẫu nhiên 2 giá trị x để tạo điểm M và N
                x1 = random.randint(-3, 3)
                x2 = random.randint(-3, 3)
                while x1 == x2: # Đảm bảo 2 điểm phân biệt
                    x2 = random.randint(-3, 3)

                y1 = a_val * x1**2 + b_val * x1 + c_val
                y2 = a_val * x2**2 + b_val * x2 + c_val

                # Tọa độ điểm
                M = (x1, y1)
                N = (x2, y2)

                # Đáp án đúng
                kq_a = a_val
                kq_b = b_val
                da = '$y = %sx^2 %s x + 2$' % (
                    latex(kq_a) if kq_a != 1 else "",
                    ("+ " + latex(kq_b)) if kq_b > 0 else (latex(kq_b)) if kq_b < 0 else ""
                )
                # Xử lý trường hợp b=0 hoặc a=1/-1 cho đẹp (tối ưu hóa hiển thị)
                da = da.replace(' 1x', ' x').replace(' -1x', ' -x').replace(' + 0x', '')

                # Bước 4: Tạo phương án sai không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    wa = random.randint(-5, 5)
                    wb = random.randint(-5, 5)
                    if wa == 0: wa = 2
                    if (wa, wb) != (kq_a, kq_b):
                        wrong_str = '$y = %sx^2 +%s x + 2$' % (
                            latex(wa) if wa != 1 else "",
                            ("+ " + latex(wb)) if wb > 0 else (latex(wb)) if wb < 0 else ""
                        )
                        wrong_str = wrong_str.replace(' 1x', ' x').replace(' -1x', ' -x').replace(' + 0x', '').replace('++', '+').replace('+-', '-')
                        if wrong_str not in s:
                            s.append(wrong_str)

                # Câu hỏi
                noidungcauhoi = ('''Xác định parabol $y = ax^2 + bx + 2$, biết rằng parabol đó đi qua hai điểm $M(%s;%s)$ và $N(%s;%s)$.'''
                                 %(latex(x1), latex(y1), latex(x2), latex(y2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B1-Viết lại y hệt cấu trúc lời giải trong ảnh)
                # Hệ phương trình: 
                # a(x1)^2 + b(x1) + 2 = y1
                # a(x2)^2 + b(x2) + 2 = y2
                eq1_lhs = "%sa + %sb + 2" % (latex(x1**2), latex(x1))
                eq2_lhs = "%sa + %sb + 2" % (latex(x2**2), latex(x2))
                # Dọn dẹp dấu cho hệ phương trình
                eq1_lhs = eq1_lhs.replace(' 1b', ' b').replace(' -1b', ' -b').replace('+ -', '- ')
                eq2_lhs = eq2_lhs.replace(' 1b', ' b').replace(' -1b', ' -b').replace('+ -', '- ')

                loigiai=('''Vì $(P)$ đi qua hai điểm $M(%s;%s)$ và $N(%s;%s)$ nên ta có $\\begin{cases} %s = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$. \\\\
                           Vậy $(P): %s$.'''
                         %(latex(x1), latex(y1), latex(x2), latex(y2), 
                           eq1_lhs, latex(y1), eq2_lhs, latex(y2),
                           latex(kq_a), latex(kq_b), da.replace('$', '')))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

