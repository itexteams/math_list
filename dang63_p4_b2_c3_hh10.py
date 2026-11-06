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


def bt_dang63_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Random tọa độ điểm M(xm, ym)
                xm = randint(-8, 8)
                ym = randint(-8, 8)
                # Tránh trường hợp điểm M nằm trên các trục tọa độ hoặc gốc tọa độ
                while xm == 0 or ym == 0 or abs(xm) == abs(ym):
                    xm = randint(-8, 8)
                    ym = randint(-8, 8)

                om2 = xm**2 + ym**2

                # Phương trình tổng quát: xm*x + ym*y - (xm^2 + ym^2) = 0
                # Chuẩn hóa để hệ số x dương cho đẹp (nếu cần)
                a_val, b_val, c_val = xm, ym, -om2
                if a_val < 0:
                    a_val, b_val, c_val = -a_val, -b_val, -c_val

                def format_eq(a, b, c):
                    expr = a*symbols('x') + b*symbols('y') + c
                    return '$' + latex(expr) + ' = 0$'

                # Đáp án đúng
                kq = format_eq(a_val, b_val, c_val)

                # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
                s_set = set()
                # Các biến thể sai: đổi dấu, hoán vị hệ số
                variations = [
                    (a_val, -b_val, c_val),
                    (b_val, a_val, c_val),
                    (a_val, b_val, -c_val),
                    (-a_val, b_val, c_val),
                    (b_val, -a_val, -c_val)
                ]

                for v_a, v_b, v_c in variations:
                    eq_s = format_eq(v_a, v_b, v_c)
                    if eq_s != kq:
                        s_set.add(eq_s)

                s = list(s_set)
                random.shuffle(s)

                da_d = ('\\True ' + str(kq))
                da_s1 = str(s[0])
                da_s2 = str(s[1]) 
                da_s3 = str(s[2]) 

                # Câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, lập phương trình đường thẳng $d$ đi qua $M(%s;%s)$ và cắt các trục $Ox$, $Oy$ lần lượt tại $A$ và $B$ khác $O$ sao cho $\\frac{1}{OA^2} + \\frac{1}{OB^2}$ nhỏ nhất.'''
                                 %(latex(xm), latex(ym)))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Nội dung lời giải chi tiết (không viết tắt)
                # Chú ý: Không dùng tiền tố r (raw string), sử dụng double backslash \\ cho LaTeX
                loigiai = ('''Gọi $H$ là hình chiếu vuông góc của $O$ trên đường thẳng $d$. Tam giác $OAB$ vuông tại $O$ nên ta có hệ thức lượng: \\\\
                             $\\frac{1}{OA^2} + \\frac{1}{OB^2} = \\frac{1}{OH^2}$. \\\\
                             Mặt khác, vì $H$ là hình chiếu của $O$ lên $d$ và $M \\in d$ nên $OH \\le OM$. \\\\
                             Suy ra $\\frac{1}{OH^2} \\ge \\frac{1}{OM^2} = \\frac{1}{%s^2 + %s^2} = \\frac{1}{%s}$. \\\\
                             Dấu "=" xảy ra khi và chỉ khi $H \\equiv M$. \\\\
                             Khi đó đường thẳng $d$ đi qua $M(%s;%s)$ và vuông góc với $OM$ nên nhận $\\vec{OM} = (%s;%s)$ làm vectơ pháp tuyến. \\\\
                             Vậy phương trình đường thẳng $d$ là: \\\\
                             $%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %s$.'''
                             %(latex(xm), latex(ym), latex(om2),
                               latex(xm), latex(ym), latex(xm), latex(ym),
                               latex(xm), latex(xm), latex(ym), latex(ym),
                               latex(simplify(xm*(symbols('x')-xm) + ym*(symbols('y')-ym))) + ' = 0'
                              ))

            # Xuất câu trắc nghiệm đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content 

