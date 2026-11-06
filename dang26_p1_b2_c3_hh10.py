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


def bt_dang26_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            x, y, t = symbols('x y t')

            # B3: Suy nghĩ tìm cách random bài toán để kết quả luôn NGUYÊN
            # Bước 1: Chọn bộ ba Pytago (a, b, c) sao cho a^2 + b^2 = c^2
            # Điều này giúp khoảng cách từ O đến đường thẳng và các tọa độ dễ nguyên hơn
            triples = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13)]
            a, b, c_pyt = random.choice(triples)

            # Ngẫu nhiên dấu cho hệ số
            a *= random.choice([-1, 1])
            b *= random.choice([-1, 1])

            # Bước 2: Chọn khoảng cách OA = R (R nên là số nguyên)
            R = random.randint(3, 10)

            # Bước 3: Để A(x,y) nguyên và OA=R, A phải là một bộ Pytago khác hoặc nằm trên trục tọa độ
            # Ta chọn trước 1 điểm A_target nguyên sao cho xA^2 + yA^2 = R^2
            # Ví dụ đơn giản nhất: A_target nằm trên các trục hoặc là bộ số Pytago
            possible_A = []
            for ix in range(-R, R + 1):
                for iy in range(-R, R + 1):
                    if ix**2 + iy**2 == R**2:
                        possible_A.append((ix, iy))

            A1_coords = random.choice(possible_A)
            xA1, yA1 = A1_coords

            # Bước 4: Tính hệ số tự do C sao cho đường thẳng ax + by + C = 0 đi qua A1
            C = -(a * xA1 + b * yA1)

            # --- Giải bài toán theo mẫu ---
            # Tìm điểm M thuộc Delta (chọn xM sao cho yM nguyên)
            # ax + by + C = 0 => y = (-C - ax)/b. Ta tìm xM để tử số chia hết cho b.
            xM = 0
            found_M = False
            for i in range(-20, 20):
                if (-C - a * i) % b == 0:
                    xM = i
                    found_M = True
                    break
            yM = (-C - a * xM) // b

            # Vectơ chỉ phương u = (-b, a)
            u_vec = (-b, a)

            # Phương trình tham số
            xA = xM - b * t
            yA = yM + a * t

            # Phương trình OA^2 = R^2
            eq = (xM - b*t)**2 + (yM + a*t)**2 - R**2
            t_sol = solve(eq, t)

            # Tọa độ các điểm A tìm được
            points = []
            for sol in t_sol:
                points.append((xA.subs(t, sol), yA.subs(t, sol)))

            # --- Xử lý nội dung hiển thị ---
            delta_expr = a*x + b*y + C
            delta_latex = latex(delta_expr)

            noidungcauhoi = (r"Cho đường thẳng $\Delta: %s = 0$. "
                             r"Tọa độ điểm $A$ thuộc đường thẳng $\Delta$ và cách gốc tọa độ một khoảng bằng $%s$ là" 
                             % (delta_latex, latex(R)))

            loigiai = (r"Dễ thấy $M(%s; %s)$ thuộc đường thẳng $\Delta$ và $\vec{u}(%s; %s)$ là một vectơ chỉ phương của $\Delta$ nên có "
                       r"phương trình tham số là $\begin{cases} x = %s \\ y = %s \end{cases}$."
                       r"\\ Điểm $A \in \Delta$ nên tọa độ điểm $A$ có dạng $A(%s; %s)$. "
                       r"\\ Theo giả thiết $OA = %s \iff \sqrt{(%s)^2 + (%s)^2} = %s$."
                       r"\\ Giải phương trình ta được $t = %s$ hoặc $t = %s$."
                       r"\\ Vậy ta tìm được các điểm thỏa mãn là: "
                       % (latex(xM), latex(yM), latex(u_vec[0]), latex(u_vec[1]),
                          latex(xA), latex(yA), latex(xA), latex(yA),
                          latex(R), latex(xA), latex(yA), latex(R),
                          latex(t_sol[0]), latex(t_sol[1] if len(t_sol)>1 else t_sol[0])))

            # Liệt kê kết quả cuối cùng
            for i, p in enumerate(points):
                loigiai += r" $A_{%d}(%s; %s)$" % (i+1, latex(p[0]), latex(p[1]))
                if i < len(points)-1: loigiai += ","
            loigiai += "."

            # Đáp án trắc nghiệm
            da_dung = r"$%s$" % (", ".join([f"A_{i+1}({latex(p[0])}; {latex(p[1])})" for i, p in enumerate(points)]))
            da_sai1 = r"$A(0;0)$"
            da_sai2 = r"$A(1;1)$"
            da_sai3 = r"$A(%s; %s)$" % (latex(xA1 + 1), latex(yA1 - 1))

            list_1 = ['\\True ' + da_dung, da_sai1, da_sai2, da_sai3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

