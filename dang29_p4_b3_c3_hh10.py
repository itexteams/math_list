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


def bt_dang29_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Tìm bộ số sao cho nghiệm R^2 và tọa độ tâm là số hữu tỉ (không có căn)
                while True:
                    x1, y1 = random.randint(-3, 3), random.randint(-3, 3)
                    x2, y2 = x1 + random.choice([-4, -2, 2, 4]), y1 + random.choice([-2, 2, 4])

                    A = Point(x1, y1)
                    B = Point(x2, y2)

                    # Chọn d sao cho mẫu số sqrt(a^2 + b^2) là số nguyên (bộ ba Pytago)
                    # Các cặp (a,b) phổ biến: (3,4), (4,3), (1,0), (0,1), (5,12)...
                    a_d, b_d = random.choice([(3, 4), (4, -3), (3, -4), (1, 0), (0, 1), (8, 6)])
                    c_d = random.randint(-10, 10)

                    # --- Giải toán ---
                    M = A.midpoint(B)
                    dx, dy = x2 - x1, y2 - y1
                    x_s, y_s = symbols('x y')
                    pt_delta = simplify(dx*(x_s - M.x) + dy*(y_s - M.y))

                    t = symbols('t', real=True)
                    if dy != 0:
                        xi, yi = t, solve(pt_delta.subs(x_s, t), y_s)[0]
                    else:
                        yi, xi = t, solve(pt_delta.subs(y_s, t), x_s)[0]

                    I_t = Point(xi, yi)
                    dist_sq = (a_d*xi + b_d*yi + c_d)**2 / (a_d**2 + b_d**2)
                    ia_sq = I_t.distance(A)**2

                    t_sol = solve(Eq(dist_sq, ia_sq), t)

                    # ĐIỀU KIỆN QUAN TRỌNG: t phải là số hữu tỉ và R^2 phải là số hữu tỉ
                    if t_sol:
                        valid = True
                        for v in t_sol:
                            R2 = simplify(ia_sq.subs(t, v))
                            # Kiểm tra nếu R2 hoặc tọa độ tâm vẫn còn chứa căn (sqrt)
                            if 'sqrt' in str(R2) or 'sqrt' in str(xi.subs(t, v)) or 'sqrt' in str(yi.subs(t, v)):
                                valid = False
                                break
                        if valid: break

                # --- Xây dựng lời giải và đáp án ---
                list_ans = []
                details = []
                for val in t_sol:
                    tâm_I = Point(xi.subs(t, val), yi.subs(t, val))
                    bk_sq = simplify(ia_sq.subs(t, val))
                    pt_c = Eq((x_s - tâm_I.x)**2 + (y_s - tâm_I.y)**2, bk_sq)
                    list_ans.append("$%s$" % latex(pt_c))

                    details.append(
                        "$\\square$ Với $t = %s \\Rightarrow I(%s; %s)$. Bán kính $R^2 = %s$. \\\\ "
                        "Phương trình $(C): %s$." 
                        % (latex(val), latex(tâm_I.x), latex(tâm_I.y), latex(bk_sq), latex(pt_c))
                    )

                # Nội dung câu hỏi
                pt_d_str = "%sx %sy %s = 0" % (a_d, ('+ ' + str(b_d) if b_d >= 0 else '- ' + str(abs(b_d))), ('+ ' + str(c_d) if c_d >= 0 else '- ' + str(abs(c_d))))
                noidungcauhoi = "Trong mặt phẳng $Oxy$ cho $A(%s; %s), B(%s; %s)$ và $d: %s$. Lập phương trình đường tròn $(C)$ qua $A, B$ và tiếp xúc $d$." % (x1, y1, x2, y2, pt_d_str.replace('+ -', '- ').replace('- -', '+ '))

                da_d = '\\True ' + list_ans[0]
                da_s1 = list_ans[1] if len(list_ans) > 1 else "$x^2+y^2=%s$" % (random.randint(1, 20))
                da_s2 = "$(x-1)^2+(y+1)^2=%s$" % (random.randint(1, 20))
                da_s3 = "$(x+2)^2+y^2=%s$" % (random.randint(1, 20))
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                loigiai = (
                    "Đường trung trực $\\Delta$ của $AB$ qua $M(%s; %s)$ có phương trình: $%s = 0$. \\\\ "
                    "Gọi $I \\in \\Delta \\Rightarrow I(%s; %s)$. \\\\ "
                    "Ta có $d(I, d) = IA \\Leftrightarrow d^2(I, d) = IA^2$. \\\\ "
                    "$\\Leftrightarrow \\frac{(%s)^2}{%s} = %s$ \\\\ "
                    "$\\Leftrightarrow \\left[ \\begin{aligned} %s \\end{aligned} \\right.$ \\\\ %s"
                    % (latex(M.x), latex(M.y), latex(pt_delta), latex(xi), latex(yi),
                       latex(a_d*xi + b_d*yi + c_d), a_d**2 + b_d**2, latex(simplify(ia_sq)),
                       " \\\\ ".join(["t = " + latex(v) for v in t_sol]), " \\\\ ".join(details))
                )

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai).replace('+-', '-').replace('- -', '+')+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

