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


def bt_dang22_p1_b4_c2_hh12(self):
            # Vòng lặp để đảm bảo tìm được tọa độ nguyên cho tâm I
            while True:
                xA = random.randint(-5, 5)
                yA = random.randint(-5, 5)
                zA = random.randint(-5, 5)
                xB = random.randint(-6, 6)
                yB = random.randint(-6, 6)
                zB = random.randint(-6, 6)

                if xA == xB: continue # Tránh chia cho 0 khi giải phương trình

                sum_A = xA**2 + yA**2 + zA**2
                sum_B = xB**2 + yB**2 + zB**2

                tu_so = sum_B - sum_A
                mau_so = 2 * (xB - xA)

                # Điều kiện để tọa độ a của tâm I(a; 0; 0) là số nguyên
                if tu_so % mau_so == 0:
                    a = tu_so // mau_so
                    break

            # Tính bán kính bình phương R^2 = IA^2
            R2 = (xA - a)**2 + yA**2 + zA**2

            # Hàm bổ trợ định dạng (x - a)^2 theo chuẩn LaTeX (không dùng f-string)
            def format_term(var, val):
                if val == 0: 
                    return "%s^2" % (var)
                if val > 0:
                    return "\\left(%s - %s\\right)^2" % (var, val)
                else:
                    return "\\left(%s + %s\\right)^2" % (var, abs(val))

            x_term = format_term('x', a)
            kq = "%s + y^2 + z^2 = %s" % (x_term, R2)

            # Tạo các phương án nhiễu (đảm bảo không trùng với đáp án đúng)
            s_set = set()
            while len(s_set) < 3:
                # Nhiễu giá trị bán kính
                nhieu_R = "%s + y^2 + z^2 = %s" % (x_term, abs(R2 + random.choice([-2, -1, 1, 2, 3])))
                # Nhiễu tọa độ tâm (tăng/giảm a)
                nhieu_tam = "%s + y^2 + z^2 = %s" % (format_term("x", a + random.choice([-1, 1])), R2)
                # Nhiễu trục (đưa biến sang y)
                nhieu_truc = "x^2 + %s + z^2 = %s" % (format_term("y", a), R2)

                for opt in [nhieu_R, nhieu_tam, nhieu_truc]:
                    if opt != kq:
                        s_set.add(opt)

            s_list = list(s_set)
            das1, das2, das3 = s_list[0], s_list[1], s_list[2]

            # Nội dung câu hỏi
            noidungcauhoi = "Phương trình mặt cầu $(S)$ đi qua $A(%s; %s; %s)$, $B(%s; %s; %s)$ và có tâm $I$ thuộc trục $Ox$ là" % (xA, yA, zA, xB, yB, zB)

            # Trộn đáp án
            da_d = "\\True $%s$" % (kq)
            list_1 = [da_d, "$%s$" % das1, "$%s$" % das2, "$%s$" % das3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = (
                "Vì tâm $I \\in Ox$ nên $I(a; 0; 0)$.\\\\ "
                "Mặt cầu đi qua $A, B$ nên $IA^2 = IB^2 \\Leftrightarrow (%s-a)^2 + %s^2 + %s^2 = (%s-a)^2 + %s^2 + %s^2$\\\\ "
                "$\\Leftrightarrow -2(%s)a + %s = -2(%s)a + %s$ "
                "$\\Leftrightarrow %sa = %s \\Leftrightarrow a = %s$.\\\\ "
                "Vậy $I(%s; 0; 0)$ và $R^2 = IA^2 = (%s - %s)^2 + %s^2 + %s^2 = %s$.\\\\ "
                "Phương trình: $%s$." 
                % (xA, yA, zA, xB, yB, zB, xA, sum_A, xB, sum_B, 2*(xB-xA), sum_B - sum_A, a, a, xA, a, yA, zA, R2, kq)
            )

            # Xuất nội dung theo mẫu (không dùng f-string, xử lý dấu ngoặc)
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + noidungcauhoi + "\n"
                "\\choice \n"
                "{" + list_1[0] + "}\n"
                "{" + list_1[1] + "}\n"
                "{" + list_1[2] + "}\n"
                "{" + list_1[3] + "}\n"
                "\\loigiai{" + loigiai + "}\n"
                "\\end{ex}\n "
                "\\end{minipage} \n\n").replace('+ -', '-').replace('- -', '+')
            return content

