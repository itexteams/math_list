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


def bt_dang23_p3_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Chọn hệ số a, b ngẫu nhiên cho đường thẳng (ax + by + c = 0)
            a = random.randint(2, 8)
            b = random.randint(2, 8)

            # Chọn hệ số tự do c1 và c2 khác nhau để tạo 2 đường thẳng song song
            c1 = random.randint(-15, 15)
            c2 = random.randint(-15, 15)
            while c1 == c2:
                c2 = random.randint(-15, 15)

            # Đảm bảo c1, c2 được gán cho Delta và Delta' giống logic đề bài (ví dụ c1=-5, c2=8)
            # Ở đây ta lấy đúng các giá trị trong ảnh làm mặc định nếu muốn fix, 
            # nhưng code này sẽ sinh số mới mỗi lần chạy.

            # Tìm một điểm M(x0, y0) thuộc Delta: a*x + b*y + c1 = 0
            # Để đơn giản, chọn y0 = 0 => x0 = -c1/a. Để tọa độ đẹp, ta dùng Rational.
            x0 = Rational(-c1, a)
            y0 = 0

            # Tính khoảng cách d = |a*x0 + b*y0 + c2| / sqrt(a^2 + b^2)
            # Thay M vào Delta': |a*(-c1/a) + b*0 + c2| = |c2 - c1|
            tu_so = abs(c2 - c1)
            mau_so_binh_phuong = a**2 + b**2
            mau_so = sqrt(mau_so_binh_phuong)

            kq_bieu_thuc = tu_so / mau_so

            # --- TẠO ĐÁP ÁN NHIỄU ---
            da_dung = f"${latex(kq_bieu_thuc)}$"
            nhieu1 = f"${latex(Rational(tu_so + random.randint(1,3), mau_so_binh_phuong))}$"
            nhieu2 = f"${latex(tu_so + random.randint(1,5))}$"
            nhieu3 = f"${latex(Rational(tu_so, a+b))}$"

            list_ans = ['\\True ' + da_dung, nhieu1, nhieu2, nhieu3]
            random.shuffle(list_ans)

            # --- NỘI DUNG CÂU HỎI ---
            # Định dạng đường thẳng: ax + by + c = 0 (xử lý dấu cộng trừ của c)
            def format_line(a, b, c):
                sign = "+" if c >= 0 else ""
                return f"{a}x + {b}y {sign} {c} = 0"

            line_delta = format_line(a, b, c1)
            line_delta_prime = format_line(a, b, c2)

            noidungcauhoi = (f"Cho đường thẳng $\\Delta: {line_delta}$. "
                             f"Khoảng cách giữa hai đường thẳng song song $\\Delta$ và "
                             f"$\\Delta': {line_delta_prime}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).")

            # --- NỘI DUNG LỜI GIẢI ---
            h1=kq_bieu_thuc
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.',',')

            loigiai = (f"Chọn điểm $M({latex(x0)}; {y0}) \\in \\Delta$.\\\\ "
                       f"Khoảng cách giữa hai đường thẳng song song là: "
                       f"$d(\\Delta, \\Delta') = d(M, \\Delta') = "
                       f"\\frac{{|{a} \\cdot \\left({latex(x0)}\\right) + {b} \\cdot {y0} + ({c2})|}}{{\\sqrt{{{a}^2 + {b}^2}}}} = "
                       f"\\frac{{{tu_so}}}{{\\sqrt{{{mau_so_binh_phuong}}}}} = {latex(kq_bieu_thuc)}$.")
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kqz)
            # --- XUẤT KẾT QUẢ ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content 


