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


def bt_dang40_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo điểm A và B trước để đảm bảo nghiệm nguyên cho bài toán
                # Để trung điểm I là số nguyên, tổng tọa độ A và B phải là số chẵn
                xa = randint(-5, 5)
                ya = randint(-5, 5)
                xb = randint(-5, 5)
                yb = randint(-5, 5)

                # Kiểm tra điều kiện để I nguyên và A khác B
                while (xa == xb and ya == yb) or (xa + xb) % 2 != 0 or (ya + yb) % 2 != 0:
                    xb = randint(-5, 5)
                    yb = randint(-5, 5)

                # Tọa độ trung điểm I
                xi = (xa + xb) // 2
                yi = (ya + yb) // 2

                # Đường thẳng d1: x + y + c1 = 0 đi qua A(xa, ya)
                # => ya = -xa - c1 => c1 = -xa - ya
                c1 = -xa - ya
                # Đường thẳng d2: x - 2y + c2 = 0 đi qua B(xb, yb)
                # => xb = 2yb - c2 => c2 = 2*yb - xb
                c2 = 2*yb - xb

                # Vectơ BA = (xa - xb; ya - yb)
                v_x = xa - xb
                v_y = ya - yb

                # Rút gọn vectơ chỉ phương
                u_gcd = abs(gcd(v_x, v_y))
                ux = v_x // u_gcd
                uy = v_y // u_gcd

                # Đáp án đúng
                da = '\\vec{u}_1 = (%s; %s)' % (latex(ux), latex(uy))
                da_d = ('\\True $' + str(da) + '$')

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                s = []
                candidates = [
                    (uy, ux), (ux, -uy), (-ux, uy), 
                    (uy, -ux), (-uy, ux), (ux + 1, uy), (ux, uy + 1)
                ]
                for cx, cy in candidates:
                    # Kiểm tra xem có cùng phương với (ux, uy) không
                    if cx * uy != cy * ux:
                        item = '$ \\vec{u} = (%s; %s) $' % (latex(cx), latex(cy))
                        if item not in s:
                            s.append(item)

                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Nội dung câu hỏi
                # d1: x + y + c1 = 0
                # d2: x - 2y + c2 = 0
                # Viết lại dưới dạng chuẩn ax + by + c = 0
                str_d1 = 'x + y %s = 0' % (('+' + str(c1)) if c1 > 0 else (str(c1) if c1 < 0 else '+ 0'))
                str_d2 = 'x - 2y %s = 0' % (('+' + str(c2)) if c2 > 0 else (str(c2) if c2 < 0 else '+ 0'))

                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho điểm $I(%s; %s)$ và hai đường thẳng $d_1: %s$, $d_2: %s$. Hai điểm $A, B$ lần lượt thuộc hai đường thẳng $d_1, d_2$ sao cho $I$ là trung điểm của đoạn thẳng $AB$. Đường thẳng $AB$ có một vectơ chỉ phương là'''
                                 % (latex(xi), latex(yi), str_d1, str_d2))

                # Danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # A thuộc d1 => A(a; -c1 - a)
                # B thuộc d2 => B(2b - c2; b)
                val_y_a = -c1 # y = -c1 - x
                val_x_b = -c2 # x = 2y - c2

                loigiai = ('''Vì $A \\in d_1$, giả sử $A(a; %s - a)$; Vì $B \\in d_2$, giả sử $B(2b %s; b)$.\\\\
                             $I$ là trung điểm của đoạn thẳng $AB$ khi và chỉ khi $\\begin{cases} \\dfrac{a + 2b %s}{2} = %s \\\\ \\dfrac{%s - a + b}{2} = %s \\end{cases}$\\\\
                             $\\Leftrightarrow \\begin{cases} a + 2b = %s \\\\ a - b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases} \\Rightarrow A(%s; %s); B(%s; %s) \\Rightarrow \\overrightarrow{BA} = (%s; %s)$.\\\\
                             Vậy đường thẳng $AB$ có một vectơ chỉ phương là $\\vec{u}_1 = (%s; %s)$.'''
                           % (latex(val_y_a), 
                              ('+' + str(val_x_b)) if val_x_b >= 0 else str(val_x_b),
                              ('+' + str(val_x_b)) if val_x_b >= 0 else str(val_x_b), latex(xi),
                              latex(val_y_a), latex(yi),
                              latex(2*xi - val_x_b), latex(val_y_a - 2*yi),
                              latex(xa), latex(yb),
                              latex(xa), latex(ya), latex(xb), latex(yb),
                              latex(v_x), latex(v_y),
                              latex(ux), latex(uy)
                             ))

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

