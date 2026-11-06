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


def bt_dang54_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến danh sách dạng (ở đây chỉ có 1 dạng theo yêu cầu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn tọa độ điểm A(xA, yA) và điểm B(xB, yB)
                # Để đảm bảo lời giải giống mẫu (có các trường hợp a=0, b=0), ta chọn dx, dy khác 0
                xA = random.randint(-5, 5)
                yA = random.randint(-5, 5)

                dx = random.randint(1, 4) * random.choice([-1, 1])
                dy = random.randint(1, 4) * random.choice([-1, 1])

                xB = xA + dx
                yB = yA + dy

                # Phương trình đường thẳng d: a(x - xA) + b(y - yA) = 0 <=> ax + by - (a*xA + b*yA) = 0
                # Khoảng cách lớn nhất đạt được khi vecto pháp tuyến n = vecto AB = (dx, dy)
                a_nghiem = dx
                b_nghiem = dy
                constant = - (a_nghiem * xA + b_nghiem * yA)

                # Biểu thức đường thẳng đúng
                expr_dung = Poly(a_nghiem*x + b_nghiem*y + constant, x, y).as_expr()
                da_dung = '$%s = 0$' % (latex(expr_dung))

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    # Tạo các hệ số nhiễu
                    a_sai = random.choice([a_nghiem, -a_nghiem, b_nghiem])
                    b_sai = random.choice([b_nghiem, -b_nghiem, a_nghiem])
                    c_sai = constant + random.randint(-5, 5)

                    if a_sai == 0 and b_sai == 0: continue

                    expr_sai = Poly(a_sai*x + b_sai*y + c_sai, x, y).as_expr()
                    str_sai = '$%s = 0$' % (latex(expr_sai))

                    if str_sai != da_dung:
                        s_set.add(str_sai)

                s = list(s_set)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho hai điểm $A(%s;%s)$ và $B(%s;%s)$. Lập phương trình đường thẳng $d$ đi qua $A$ và cách $B$ một khoảng lớn nhất.'''
                                 % (latex(xA), latex(yA), latex(xB), latex(yB)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Tính toán các giá trị cho lời giải
                dist_a0 = abs(dy) # Khoảng cách khi a=0
                dist_b0 = abs(dx) # Khoảng cách khi b=0
                max_dist_sq = dx**2 + dy**2

                # Nội dung lời giải chi tiết (B2)
                loigiai = ('''Phương pháp đại số: Đường thẳng $d$ đi qua $A(%s;%s)$ và có vectơ pháp tuyến $\\vec{n} = (a;b)$ với $a^2+b^2 \\neq 0$ nên có phương trình
                             $d: a(x-%s)+b(y-%s)=0$ hoặc $ax+by-%s a-%s b=0$. \\\\
                             Khoảng cách từ $B$ đến đường thẳng $d$ được xác định \\\\ $d(B,d) = \\frac{|a(%s-%s) + b(%s-%s)|}{\\sqrt{a^2+b^2}} = \\frac{|%s a + %s b|}{\\sqrt{a^2+b^2}}$. \\\\
                             Nếu $a=0$ thì $d(B,d) = %s$. \\\\
                             Nếu $b=0$ thì $d(B,d) = %s$. \\\\
                             Khi $a \\neq 0$ và $b \\neq 0$ ta chọn $b=1$. \\\\
                             Suy ra $d(B,d) = \\frac{|%s a + %s|}{\\sqrt{a^2+1}} = |f(a)|$, với $f(a) = \\frac{%s a + %s}{\\sqrt{a^2+1}}$. \\\\
                             Áp dụng bất đẳng thức Cauchy – Shwarz, ta có \\\\ $(%s a + %s)^2 \\le ((%s)^2 + (%s)^2)(a^2+1) \\Rightarrow \\frac{|%s a + %s|}{\\sqrt{a^2+1}} \\le \\sqrt{%s}$. \\\\
                             Vậy $\\max_{\\mathbb{R}} f(a) = \\sqrt{%s}$, xảy ra khi $\\frac{a}{%s} = \\frac{1}{%s} \\Rightarrow a = %s$. \\\\
                             So sánh các trường hợp, ta được $d(B,d)$ lớn nhất khi $a=%s, b=%s$. \\\\
                             Vậy phương trình đường thẳng cần tìm $d: %s = 0$.'''
                           % (latex(xA), latex(yA), latex(xA), latex(yA), latex(xA), latex(yA),
                              latex(xB), latex(xA), latex(yB), latex(yA), latex(dx), latex(dy),
                              latex(dist_a0), latex(dist_b0),
                              latex(dx), latex(dy), latex(dx), latex(dy),
                              latex(dx), latex(dy), latex(dx), latex(dy), latex(dx), latex(dy), latex(max_dist_sq),
                              latex(max_dist_sq), latex(dx), latex(dy), latex(Rational(dx, dy)),
                              latex(dx), latex(dy), latex(expr_dung)
                              ))

            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('--', '+').replace('+-', '-')
            return content 

