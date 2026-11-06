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


def bt_dang21_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các giá trị ngẫu nhiên để đỉnh nằm ngoài khoảng [m, n]
                # Hàm số dạng y = Ax^2 + Bx + C
                A = random.choice([-2, -1, 1, 2])
                # Để x_I = -B/(2A) nằm ngoài khoảng [m, n] dương, ta chọn B sao cho x_I âm
                # Ví dụ: A < 0, B < 0 => x_I = -(-)/( -) = âm
                B = A * random.randint(2, 6) # Đảm bảo x_I = -B/2A là số nguyên hoặc hữu tỉ đẹp
                C = random.randint(-10, 10)

                m = 0
                n = random.randint(3, 6)

                # Định nghĩa hàm số
                x = symbols('x')
                f = A*x**2 + B*x + C

                # Tính toán các giá trị
                x_dinh = Rational(-B, 2*A)
                f_m = f.subs(x, m)
                f_n = f.subs(x, n)

                # Tìm Max, Min trong đoạn [m, n]
                # Vì x_dinh nằm ngoài [m, n], Max/Min chỉ nằm ở 2 đầu mút
                val_max = max(f_m, f_n)
                val_min = min(f_m, f_n)

                # Các đáp án trắc nghiệm
                kq_dung = "\\min y = %s; \\max y = %s" % (latex(val_min), latex(val_max))

                # Tạo các phương án nhiễu (đảm bảo không trùng đáp án đúng)
                s = [
                    "\\min y = %s; \\max y = %s" % (latex(val_min - 1), latex(val_max)),
                    "\\min y = %s; \\max y = %s" % (latex(val_min), latex(val_max + 2)),
                    "\\min y = %s; \\max y = %s" % (latex(val_min - 2), latex(val_max - 1)),
                    "\\min y = %s; \\max y = %s" % (latex(val_min + 1), latex(val_max + 1)),
                    "\\min y = %s; \\max y = %s" % (latex(val_min - 5), latex(val_max + 3)),
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = (r"Giá trị lớn nhất, nhỏ nhất của hàm số $y = %s$ với $%s \le x \le %s$ là"
                                 % (latex(f), latex(m), latex(n)))

                # Các đáp án
                da_d = r'\True $' + kq_dung + '$'
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt cấu trúc trong ảnh)
                huong_be_lom = "xuống" if A < 0 else "lên"
                loigiai = (r"Hàm số $y = %s$ có $a = %s %s 0$ nên bề lõm hướng %s. \\ "
                           r"Hoành độ đỉnh $x_I = -\frac{b}{2a} = %s \notin [%s; %s]$. \\ "
                           r"Ta có $f(%s) = %s; f(%s) = %s$. \\ "
                           r"Vậy $\min y = f(%s) = %s; \max y = f(%s) = %s$."
                           % (latex(f), latex(A), "<" if A < 0 else ">", huong_be_lom,
                              latex(x_dinh), latex(m), latex(n),
                              latex(n), latex(f_n), latex(m), latex(f_m),
                              latex(n if f_n < f_m else m), latex(val_min),
                              latex(m if f_m > f_n else n), latex(val_max)))

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

