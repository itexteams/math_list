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


def bt_dang32_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khởi tạo các biến ký hiệu
            x, y = symbols('x y')

            # --- BƯỚC 1: RANDOM BÀI TOÁN ---
            # Để đảm bảo 2 đường tròn cắt nhau và số đẹp, ta chọn tâm và bán kính chủ động
            # Đường tròn C1: tâm I1(a1, b1), bán kính R1
            a1, b1 = random.randint(-3, 3), random.randint(-3, 3)
            r1 = random.randint(3, 5)
            c1_expr = expand((x - a1)**2 + (y - b1)**2 - r1**2)

            # Đường tròn C2: tâm I2(a2, b2), bán kính R2
            # Chọn I2 sao cho khoảng cách I1I2 < R1 + R2 và > |R1 - R2|
            a2, b2 = a1 + random.choice([-2, -1, 1, 2]), b1 + random.choice([-2, -1, 1, 2])
            r2 = random.randint(3, 5)
            c2_standard = (x - a2)**2 + (y - b2)**2 # Dạng vế trái của C2
            r2_sq = r2**2

            # Phương trình khai triển của C2 để tính toán
            c2_expr = expand(c2_standard - r2_sq)

            # Tính khoảng cách tâm để đưa vào lời giải
            d_sq = (a2 - a1)**2 + (b2 - b1)**2
            d_val = sqrt(d_sq)

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Trong mặt phẳng $Oxy$, cho hai đường tròn: $(C_1): %s = 0$ và 
            $(C_2): (x %s)^2 + (y %s)^2 = %s$. Phương trình đường thẳng đi qua giao điểm của hai đường tròn đó là'''
                             % (latex(c1_expr), 
                                latex(-a2) if -a2 < 0 else "+ " + latex(-a2),
                                latex(-b2) if -b2 < 0 else "+ " + latex(-b2),
                                latex(r2_sq)))

            # Phương trình đường thẳng (Trục đẳng phương): C1 - C2 = 0 hoặc C2 - C1 = 0
            dt_chua_rut_gon = simplify(c1_expr - c2_expr)
            # Rút gọn để hệ số x dương cho đẹp (nếu cần)
            if dt_chua_rut_gon.coeff(x) < 0:
                dt_final = simplify(-dt_chua_rut_gon)
            else:
                dt_final = dt_chua_rut_gon

            # Đáp án
            da_d = r'\True $%s = 0$' % latex(dt_final)
            s = [
                '$%s = 0$' % latex(simplify(dt_final + x + 1)),
                '$%s = 0$' % latex(simplify(dt_final - y + 2)),
                '$%s = 0$' % latex(simplify(dt_final + 2*x - 3))
            ]
            random.shuffle(s)
            list_1 = [da_d, s[0], s[1], s[2]]
            random.shuffle(list_1)

            # --- BƯỚC 3: LỜI GIẢI CHI TIẾT ---
            loigiai = (r'''$(C_1)$ có tâm $I_1(%s;%s)$ và bán kính $R_1 = %s$ \\
            $(C_2)$ có tâm $I_2(%s;%s)$ và bán kính $R_2 = %s$ \\
            $I_1I_2 = \sqrt{(%s - %s)^2 + (%s - %s)^2} = \sqrt{%s}$. \\
            Ta thấy $|R_1 - R_2| < I_1I_2 < R_1 + R_2$ suy ra hai đường tròn cắt nhau. \\
            Gọi điểm $M(x;y)$ thuộc đường thẳng cần tìm. \\
            Tọa độ $M$ thỏa mãn hệ: 
            $\begin{cases} %s = 0 \\ (x %s)^2 + (y %s)^2 = %s \end{cases} \Leftrightarrow \begin{cases} %s = 0 \quad (1) \\ %s = 0 \quad (2) \end{cases}$ \\
            Lấy $(1) - (2)$ (hoặc ngược lại) ta được: \\
            $%s = 0$. \\
            Nhận thấy $M(x;y)$ luôn thỏa mãn phương trình trên. \\
            Suy ra đường thẳng qua giao điểm của hai đường tròn là: $%s = 0$.'''
                       % (latex(a1), latex(b1), latex(r1),
                          latex(a2), latex(b2), latex(r2),
                          latex(a2), latex(a1), latex(b2), latex(b1), latex(d_sq),
                          latex(c1_expr), 
                          latex(-a2) if -a2 < 0 else "+ " + latex(-a2),
                          latex(-b2) if -b2 < 0 else "+ " + latex(-b2),
                          latex(r2_sq),
                          latex(c1_expr), latex(c2_expr),
                          latex(dt_chua_rut_gon),
                          latex(dt_final)))

            # --- BƯỚC 4: XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+')
            return content

