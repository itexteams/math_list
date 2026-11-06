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


def bt_dang43_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            x = symbols('x')

            # Khai báo danh sách các dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM THAM SỐ ---
                n = random.randint(1, 3) 
                k = random.randint(2, 6)

                # Giá trị f(1) - Để kết quả lẻ, ta có thể dùng số lẻ
                tu_f1 = random.randint(1, 9)
                mau_f1 = 2
                val_f1 = Rational(tu_f1, mau_f1)

                # Giá trị x cần tìm, chọn số không quá lớn để kết quả gọn
                x_find = random.choice([2, 3, 4, 5])

                # --- BƯỚC 2: GIẢI TOÁN BẰNG SYMPY ---
                ve_phai_sau_chia = Rational(k, 2) * x**n
                nguyen_ham = integrate(ve_phai_sau_chia, x)

                nguyen_ham_tai_1 = nguyen_ham.subs(x, 1)
                C = val_f1 - nguyen_ham_tai_1

                # Biểu thức f(x)
                f_x_bieu_thuc = (nguyen_ham + C) / sqrt(x)

                # Tính giá trị chính xác trước
                kq_chinh_xac = f_x_bieu_thuc.subs(x, x_find)

                # --- BƯỚC 3: LÀM TRÒN KẾT QUẢ ---
                # Chuyển sang float để làm tròn
                val_float = float(kq_chinh_xac.evalf())
                # Sử dụng Decimal để làm tròn chuẩn hàng phần chục (0.1)
                kq_rounded = Decimal(str(val_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Định dạng chuỗi hiển thị (thay dấu chấm bằng dấu phẩy)
                da_hien_thi = str(kq_rounded).replace('.', ',')
                da = '$%s$' % da_hien_thi

                # --- BƯỚC 4: TẠO ĐÁP ÁN NHIỄU (Cũng làm tròn) ---
                s = []
                while len(s) < 3:
                    # Tạo sai số ngẫu nhiên
                    sai_so = random.choice([0.5, 1.2, 2.3, 3.1, 0.8, 1.5])
                    huong = random.choice([1, -1])
                    temp_val = float(kq_rounded) + (huong * sai_so)

                    # Làm tròn phương án sai
                    ans_rounded = Decimal(str(temp_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    ans_str = '$%s$' % str(ans_rounded).replace('.', ',')

                    if ans_str != da and ans_str not in s:
                        s.append(ans_str)

                das1, das2, das3 = s[0], s[1], s[2]

                # --- BƯỚC 5: NỘI DUNG CÂU HỎI ---
                ve_phai_goc = k * x**n * sqrt(x)
                noidungcauhoi = (r'''Cho hàm số $y=f(x)$ liên tục trên $(0;+\infty)$ thỏa mãn $2x \cdot f'(x) + f(x) = %s, \forall x \in (0;+\infty)$. Biết $f(1) = %s$, giá trị $f(%s)$ làm tròn đến hàng phần chục bằng bao nhiêu?'''
                                 % (latex(ve_phai_goc), latex(val_f1), latex(x_find)))

                # --- BƯỚC 6: NỘI DUNG LỜI GIẢI ---
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                loigiai = (r'''Phương trình tương đương: \\
                           $\sqrt{x} \cdot f'(x) + \frac{1}{2\sqrt{x}} f(x) = \frac{%s}{2\sqrt{x}}$ \\
                           $\Leftrightarrow \left[ \sqrt{x} \cdot f(x) \right]' = %s$ \\
                           $\Leftrightarrow \sqrt{x} \cdot f(x) = \int %s dx = %s + C$ \\
                           Thay $x=1, f(1)=%s \Rightarrow C = %s$. \\
                           Khi đó $f(x) = \frac{%s %s %s}{\sqrt{x}}$. \\
                           Tại $x=%s$: $f(%s) = \frac{%s %s %s}{\sqrt{%s}} \approx %s$.'''
                           % (latex(ve_phai_goc), latex(ve_phai_sau_chia),
                              latex(ve_phai_sau_chia), latex(nguyen_ham), 
                              latex(val_f1), latex(C),
                              latex(nguyen_ham), '+' if C >= 0 else '', latex(C),
                              latex(x_find), latex(x_find),
                              latex(nguyen_ham.subs(x, x_find)), '+' if C >= 0 else '', latex(C),
                              latex(x_find), da_hien_thi
                             ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(str(da_hien_thi)) 

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

