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


def bt_dang35_p1_b1_c2_hh12(self):
            x, y, z = symbols('x y z')

            # Bước 1: Chọn bộ số đẹp
            triples = [[1, 2, 2], [2, 3, 6], [1, 4, 8], [4, 4, 7], [2, 6, 9]]
            abc = random.choice(triples)
            a, b, c = abc[0], abc[1], abc[2]

            dist = random.randint(1, 3)
            dq = random.randint(-10, 10)
            while dq == 0: dq = random.randint(-10, 10)

            denom = int(math.sqrt(a**2 + b**2 + c**2))
            k = dist * denom
            d1 = dq + k
            d2 = dq - k

            # Bước 2: Kiểm tra điều kiện loại nghiệm (nếu trùng O hoặc trùng Q)
            valid_d = []
            if d1 != 0 and d1 != dq: valid_d.append(d1)
            if d2 != 0 and d2 != dq: valid_d.append(d2)

            def format_plane(d_val):
                return latex(a*x + b*y + c*z + d_val) + " = 0"

            # --- TẠO CÁC PHƯƠNG ÁN ---

            # 1. Đáp án ĐÚNG (da_d)
            da_d_str = " \\text{ hoặc } ".join(["$%s$" % format_plane(d) for d in valid_d])
            da_d = '\\True ' + da_d_str

            # 2. Nhiễu 1: Sai dấu của dq trong công thức khoảng cách (d + dq thay vì d - dq)
            # dẫn đến nghiệm d = -dq + k và d = -dq - k
            ds1_val = [-dq + k, -dq - k]
            da_s1 = " \\text{ hoặc } ".join(["$%s$" % format_plane(d) for d in ds1_val])

            # 3. Nhiễu 2: Sai hằng số k (ví dụ quên không nhân với mẫu số denom)
            # dẫn đến nghiệm d = dq + dist và d = dq - dist
            ds2_val = [dq + dist, dq - dist]
            da_s2 = " \\text{ hoặc } ".join(["$%s$" % format_plane(d) for d in ds2_val])

            # 4. Nhiễu 3: Chỉ lấy 1 phương trình (thường học sinh hay quên dấu trị tuyệt đối)
            # Hoặc lấy nghiệm d1 nhưng đổi dấu hằng số
            da_s3 = '$%s$' % format_plane(d1 + random.choice([-1, 1, 2]))

            # Bước 4: Trộn đáp án và kiểm tra trùng lặp
            # (Đảm bảo các chuỗi phương án không giống hệt nhau)
            list_ans = list(set([da_d, da_s1, da_s2, da_s3]))
            while len(list_ans) < 4:
                extra_d = dq + random.randint(15, 30)
                list_ans.append('$%s$' % format_plane(extra_d))

            random.shuffle(list_ans)

            # --- NỘI DUNG CÂU HỎI & LỜI GIẢI ---
            plane_q = format_plane(dq)
            noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(Q): %s$ và mặt phẳng $(P)$ không đi qua gốc tọa độ $O$, song song với mặt phẳng $(Q)$ sao cho $d((P);(Q)) = %s$. Phương trình mặt phẳng $(P)$ là'''
                            % (plane_q, latex(dist)))

            loigiai = ('''Mặt phẳng $(P)$ song song với $(Q)$ nên có dạng: $%s + d = 0$ ($d \\neq %s$). \\\\
                         Vì $(P)$ không đi qua $O(0;0;0)$ nên $d \\neq 0$. \\\\
                         Khoảng cách giữa hai mặt phẳng song song là: \\\\
                         $d((P);(Q)) = %s \\Leftrightarrow \\frac{|d - (%s)|}{\\sqrt{%s^2 + %s^2 + %s^2}} = %s$ \\\\
                         $\\Leftrightarrow |d %s| = %s \\cdot %s = %s$ \\\\
                         $\\Leftrightarrow \\left[ \\begin{aligned} d %s &= %s \\\\ d %s &= -%s \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} d &= %s \\\\ d &= %s \\end{aligned} \\right.$. \\\\
                         Đối chiếu điều kiện $d \\neq 0$ và $d \\neq %s$, ta nhận cả hai giá trị. \\\\
                         Vậy phương trình mặt phẳng $(P)$ là: %s.'''
                       % (latex(a*x + b*y + c*z), str(dq), str(dist), str(dq), str(a), str(b), str(c), str(dist),
                          ('+' + str(-dq) if -dq > 0 else str(-dq)), str(dist), str(denom), str(k),
                          ('+' + str(-dq) if -dq > 0 else str(-dq)), str(k), 
                          ('+' + str(-dq) if -dq > 0 else str(-dq)), str(k),
                          str(d1), str(d2), str(dq), da_d_str))

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

