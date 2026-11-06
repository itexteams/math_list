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


def bt_dang72_p1_b2_c7_ds11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        x = symbols('x')

        # Random tham số k để đảm bảo nghiệm đẹp (khác 0 để hàm có cực trị y')
        k_val = random.choice([-3, -2, -1, 1, 2, 3])

        # Random giá trị hệ số góc nhỏ nhất (đáp án đúng)
        min_slope = random.randint(-5, 10)

        # Tính toán các hệ số của hàm bậc 3: y = x^3 + bx^2 + cx + d
        # Đạo hàm: y' = 3x^2 + 2bx + c = 3(x^2 + 2kx + k^2) + min_slope
        b_val = 3 * k_val
        c_val = min_slope + 3 * (k_val**2)
        d_val = random.randint(-10, 10)

        # Khởi tạo biểu thức
        y_expr = x**3 + b_val*x**2 + c_val*x + d_val
        y_prime_expr = 3*x**2 + 2*b_val*x + c_val
        perfect_square_expr = x**2 + 2*k_val*x + k_val**2
        x_plus_k = x + k_val

        # Đáp án đúng
        da = '$%s$' % latex(min_slope)

        # Sinh các đáp án sai (đảm bảo không trùng đáp án đúng)
        s = set()
        while len(s) < 3:
            delta = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            sai = min_slope + delta
            if sai != min_slope:
                s.add('$%s$' % latex(sai))

        s_list = list(s)
        das1 = s_list[0]
        das2 = s_list[1]
        das3 = s_list[2]

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $y = %s$ có đồ thị là $(C)$. Hệ số góc nhỏ nhất của tiếp tuyến tại một điểm $M$ thuộc đồ thị $(C)$ là''' 
                         % latex(y_expr))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Xử lý chuỗi phần đuôi của bình phương để định dạng LaTeX chuẩn dấu (+ / -)
        tail = ""
        if min_slope > 0:
            tail = " + " + latex(min_slope)
        elif min_slope < 0:
            tail = " - " + latex(abs(min_slope))

        # Nội dung lời giải
        loigiai = ('''Đạo hàm của hàm số: $y' = %s$.\\\\
    Gọi $x$ là hoành độ của điểm $M$ thuộc đồ thị $(C)$, hệ số góc của tiếp tuyến tại $M$ là:\\\\
    $k = y' = %s = 3\\left(%s\\right)%s = 3(%s)^2%s$.\\\\
    Vì $3(%s)^2 \\ge 0, \\forall x \\in \\mathbb{R}$ nên $k \\ge %s$.\\\\
    Dấu "=" xảy ra khi $x = %s$.\\\\
    Vậy hệ số góc nhỏ nhất của tiếp tuyến là $%s$.''' %
        (latex(y_prime_expr), 
         latex(y_prime_expr), latex(perfect_square_expr), tail, latex(x_plus_k), tail,
         latex(x_plus_k), latex(min_slope),
         latex(-k_val), 
         latex(min_slope)))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

