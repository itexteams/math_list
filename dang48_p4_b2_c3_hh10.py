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


def bt_dang48_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo các biến ký hiệu cho sympy
            x, y, c, d = symbols('x y c d')

            # Khai báo danh sách các dạng (ở đây có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các hệ số cho đường thẳng d1: x - y + k1 = 0 và d2: m*x + y + k2 = 0
                # Để giải ra số nguyên dễ dàng, ta cố định cấu trúc này
                m = random.randint(1, 3) # Hệ số góc của d2 (trong ảnh là 2)
                k1 = random.randint(-8, 8) # Hệ số tự do d1 (trong ảnh là -4)
                k2 = random.randint(-8, 8) # Hệ số tự do d2 (trong ảnh là -2)

                # Bước 2: Chọn trước tọa độ nguyên cho C và D để đảm bảo bài toán có nghiệm đẹp
                val_c = random.randint(-5, 5)
                val_d = random.randint(-5, 5)
                while val_c == val_d: # Tránh việc C trùng D hoặc các trường hợp suy biến
                    val_d = random.randint(-5, 5)

                # Tọa độ C thuộc d1: y = x + k1
                yc = val_c + k1
                # Tọa độ D thuộc d2: y = -m*x - k2
                yd = -m * val_d - k2

                point_C = (val_c, yc)
                point_D = (val_d, yd)

                # Bước 3: Chọn tọa độ điểm A ngẫu nhiên
                xa = random.randint(-7, 10)
                ya = random.randint(-7, 10)
                point_A = (xa, ya)

                # Bước 4: Tính tọa độ điểm B để ABCD là hình bình hành (vecto AB = vecto DC)
                # vecto DC = (xc - xd, yc - yd)
                v_dc_x = point_C[0] - point_D[0]
                v_dc_y = point_C[1] - point_D[1]

                # B = A + vecto DC
                xb = xa + v_dc_x
                yb = ya + v_dc_y
                point_B = (xb, yb)

                # vecto AB
                v_ab_x = xb - xa
                v_ab_y = yb - ya

                # Chuẩn bị dữ liệu cho nội dung câu hỏi
                # Đường thẳng d1: x - y + k1 = 0 -> Viết lại dạng Latex
                line1_str = "x - y" + (" + " if k1 > 0 else " - ") + str(abs(k1)) + " = 0"
                if k1 == 0: line1_str = "x - y = 0"

                # Đường thẳng d2: mx + y + k2 = 0
                line2_str = (str(m) if m != 1 else "") + "x + y" + (" + " if k2 > 0 else " - ") + str(abs(k2)) + " = 0"
                if k2 == 0: line2_str = (str(m) if m != 1 else "") + "x + y = 0"

                # Đáp án đúng
                da_dung = "C(%s;%s), D(%s;%s)" % (val_c, yc, val_d, yd)

                # Tạo các đáp án nhiễu
                s = [
                    "C(%s;%s), D(%s;%s)" % (val_d, yd, val_c, yc), # Hoán đổi C, D
                    "C(%s;%s), D(%s;%s)" % (val_c + 1, yc - 1, val_d, yd),
                    "C(%s;%s), D(%s;%s)" % (val_c, yc, val_d - 1, yd + 1),
                    "C(%s;%s), D(%s;%s)" % (-val_c, -yc, -val_d, -yd),
                    "C(%s;%s), D(%s;%s)" % (yc, val_c, yd, val_d)
                ]

                # Lọc bỏ nếu ngẫu nhiên trùng đáp án đúng
                s = [i for i in s if i != da_dung]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (
                    "Trong mặt phẳng với hệ tọa độ $Oxy$, cho hai đường thẳng "
                    "$d_1: %s$, $d_2: %s$, và hai điểm $A(%s;%s)$, $B(%s;%s)$. "
                    "Điểm $C$ trên đường thẳng $d_1$ và điểm $D$ trên đường thẳng $d_2$ "
                    "sao cho tứ giác $ABCD$ là hình bình hành. Tìm tọa độ hai điểm $C$ và $D$."
                    % (line1_str, line2_str, xa, ya, xb, yb)
                )

                # Đáp án
                da_d = "\\True $" + da_dung + "$"
                da_s1 = "$" + das1 + "$"
                da_s2 = "$" + das2 + "$"
                da_s3 = "$" + das3 + "$"

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                # Biểu diễn y theo x cho d1 và d2 để tham số hóa
                # d1: y = x + k1 -> C(c; c + k1)
                # d2: y = -m*x - k2 -> D(d; -m*d - k2)
                expr_yc = "c " + ("+ " + str(k1) if k1 > 0 else "- " + str(abs(k1))) if k1 != 0 else "c"
                expr_yd = ("-" + str(m) if m != 1 else "-") + "d " + ("- " + str(k2) if k2 > 0 else "+ " + str(abs(k2))) if k2 != 0 else ("-" + str(m) if m != 1 else "-") + "d"

                # Vecto DC = (c - d; (c+k1) - (-md-k2)) = (c-d; c + md + k1 + k2)
                expr_dc_y = "c + " + (str(m) if m != 1 else "") + "d" + (" + " if (k1+k2) > 0 else " - ") + str(abs(k1+k2))
                if (k1+k2) == 0: expr_dc_y = "c + " + (str(m) if m != 1 else "") + "d"

                loigiai = (
                    "Do $C \\in d_1$ nên $C(c; %s)$ và $D \\in d_2$ nên $D(d; %s)$. \\\\\n"
                    "Ta có $\\vec{AB} = (%s; %s)$, $\\vec{DC} = (c - d; %s)$. \\\\\n"
                    "Tứ giác $ABCD$ là hình bình hành khi và chỉ khi $\\vec{AB} = \\vec{DC}$ \\\\\n"
                    "$\\Leftrightarrow \\begin{cases} c - d = %s \\\\ %s = %s \\end{cases} "
                    "\\Leftrightarrow \\begin{cases} c = %s \\\\ d = %s \\end{cases}$. \\\\\n"
                    "Vậy $C(%s; %s), D(%s; %s)$."
                    % (expr_yc.replace(" ", ""), expr_yd.replace(" ", ""), 
                       v_ab_x, v_ab_y, expr_dc_y.replace(" ", ""),
                       v_ab_x, expr_dc_y.replace(" ", ""), v_ab_y,
                       val_c, val_d,
                       val_c, yc, val_d, yd)
                )

            # Xuất nội dung theo định dạng yêu cầu
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content 

