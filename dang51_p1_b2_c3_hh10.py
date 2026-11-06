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


def bt_dang51_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Mỗi bộ gồm: (xA, yA, xB, yB, k)
            data_sets = [
                (0, -1, 2, 1, 1),   # Bài gốc: t=0, t=2
                (1, 0, 3, 2, 3),    # t=1, t=3
                (-1, 0, 1, 2, 1),   # t=-1, t=1
                (2, 0, 4, 2, 4),    # t=2, t=4
                (0, 0, 2, 2, 2),    # t=0, t=2
                (1, -2, 3, 0, 1),   # t=1, t=3
            ]

            # Chọn ngẫu nhiên một bộ dữ liệu
            data = random.choice(data_sets)
            xA, yA, xB, yB, k_val = data

            # Tính toán các thành phần cho lời giải
            # I(t; k-t)
            # vec{AI} = (t - xA; k - t - yA)
            # vec{BI} = (t - xB; k - t - yB)
            # Tích vô hướng: (t - xA)(t - xB) + (k - yA - t)(k - yB - t) = 0
            # 2t^2 - (xA + xB + 2k - yA - yB)t + [xA*xB + (k-yA)(k-yB)] = 0

            t = symbols('t')
            expr = (t - xA)*(t - xB) + (k_val - yA - t)*(k_val - yB - t)
            expr_expanded = expand(expr)
            sol_t = solve(expr, t)

            # Lấy tọa độ C cho từng giá trị t
            list_C = []
            for val_t in sol_t:
                xI = val_t
                yI = k_val - val_t
                # I là trung điểm AC => C = 2I - A
                xC = 2*xI - xA
                yC = 2*yI - yA
                list_C.append((xC, yC))

            # Sắp xếp để tạo đáp án thống nhất
            list_C.sort()
            c1_x, c1_y = list_C[0]
            c2_x, c2_y = list_C[1]

            # Đáp án đúng
            kq_dung = '$C(%s; %s)$ hoặc $C(%s; %s)$' % (latex(c1_x), latex(c1_y), latex(c2_x), latex(c2_y))

            # Tạo các đáp án sai bằng cách biến đổi tọa độ
            du = ['\\True ' + kq_dung]
            s = [
                '$C(%s; %s)$ hoặc $C(%s; %s)$' % (latex(c1_x+1), latex(c1_y), latex(c2_x-1), latex(c2_y)),
                '$C(%s; %s)$ hoặc $C(%s; %s)$' % (latex(c1_x), latex(c1_y+1), latex(c2_x), latex(c2_y-1)),
                '$C(%s; %s)$ hoặc $C(%s; %s)$' % (latex(c1_x-2), latex(c1_y), latex(c2_x+2), latex(c2_y)),
                '$C(%s; %s)$ hoặc $C(%s; %s)$' % (latex(c1_x), latex(c1_y-1), latex(c2_x), latex(c2_y+2)),
                '$C(%s; %s)$' % (latex(c1_x), latex(c1_y)),
                '$C(%s; %s)$' % (latex(c2_x), latex(c2_y))
            ]

            # Trộn đáp án
            random.shuffle(s)
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            list_ans = [du[0], da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ('Trong mặt phẳng với hệ tọa độ $Oxy$, cho hình thoi $ABCD$ có $A(%s;%s), B(%s;%s)$ và tâm $I$ thuộc đường thẳng $d: x + y - %s = 0$. Tọa độ điểm $C$ là'
                            % (latex(xA), latex(yA), latex(xB), latex(yB), latex(k_val)))

            # Chi tiết các bước cho lời giải
            # vec{AI} = (t - xA; (k-yA) - t)
            # vec{BI} = (t - xB; (k-yB) - t)
            vec_AI_x = t - xA
            vec_AI_y = (k_val - yA) - t
            vec_BI_x = t - xB
            vec_BI_y = (k_val - yB) - t

            # Phương trình tích vô hướng
            eq_str = '(%s)(%s) + (%s)(%s) = 0' % (latex(vec_AI_x), latex(vec_BI_x), latex(vec_AI_y), latex(vec_BI_y))
            eq_final = latex(expr_expanded) + ' = 0'

            # Lời giải chi tiết
            loigiai = ('''Do $I \\in d$ nên $I(t; %s - t)$. Ta có $\\vec{AI} = (%s; %s), \\vec{BI} = (%s; %s)$. \\\\
                        Vì $ABCD$ là hình thoi, suy ra $AI \\perp BI$ nên $\\vec{AI} \\cdot \\vec{BI} = 0 \\Leftrightarrow %s \\Leftrightarrow %s \\Leftrightarrow \\left[ \\begin{aligned} & t = %s \\\\ & t = %s \\end{aligned} \\right. $. \\\\
                        Với $t = %s$ thì $I(%s; %s)$. Do $I$ là trung điểm của $AC$ nên suy ra $C(%s; %s)$. \\\\
                        Với $t = %s$ thì $I(%s; %s)$. Do $I$ là trung điểm của $AC$ nên suy ra $C(%s; %s)$.'''
                        % (latex(k_val), latex(vec_AI_x), latex(vec_AI_y), latex(vec_BI_x), latex(vec_BI_y),
                           eq_str, eq_final, latex(sol_t[0]), latex(sol_t[1]),
                           latex(sol_t[0]), latex(sol_t[0]), latex(k_val - sol_t[0]), latex(2*sol_t[0] - xA), latex(2*(k_val - sol_t[0]) - yA),
                           latex(sol_t[1]), latex(sol_t[1]), latex(k_val - sol_t[1]), latex(2*sol_t[1] - xA), latex(2*(k_val - sol_t[1]) - yA)
                        ))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

