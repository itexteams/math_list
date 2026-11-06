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


def bt_dang31_p3_b2_c1_ds12(self):
            # Khai báo biến
            def round_SA(a): 
                # Kiểm tra nếu a là số nguyên
                if a == int(a):
                    return "", int(a)

                # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                # Xác định cách làm tròn
                if len(integer_part) > 2:
                    number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng đơn vị)."
                elif len(integer_part) == 2 and len(decimal_part) > 1:
                    number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần chục)."
                elif len(decimal_part) <= 2:
                    number = str_a  # Không cần làm tròn thêm
                    cirle = ""
                else:
                    number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần trăm)."

                # Chuyển dấu chấm thành dấu phẩy (nếu có)
                return cirle, str(number).replace('.', ',')

            # ------------------------------------------------------------------------------BÀI TOÁN
            # 1. Sinh ngẫu nhiên các giá trị gốc
            T0_goc = round(random.uniform(3, 15),2)
            T1_goc = round(random.uniform(40, 80),1)
            k = -random.uniform(0.00022, 0.00024)

            # 2. Tính toán và LÀM TRÒN các hệ số
            c3 = round(-k / 3, 6)
            c2 = round(-k * (T0_goc + T1_goc) / 2, 5)
            c1 = round(-k * T0_goc * T1_goc, 5)
            c0 = round(random.uniform(980.85, 999.90), 2)

            # 3. Giải bài toán DỰA TRÊN CÁC SỐ ĐÃ LÀM TRÒN
            a_pt = -3 * c3
            b_pt = 2 * c2
            c_pt = -c1

            he_so_thuc_te = [a_pt, b_pt, c_pt]
            nghiem_thuc_te = np.roots(he_so_thuc_te)

            T0_chinh_xac = [r.real for r in nghiem_thuc_te if 0 < r.real < 30][0]
            ket_qua = round(T0_chinh_xac, 5)

            noidungcauhoi = f""" Một nghiên cứu cho thấy thể tích $V$ của 1 kg nước (tính bằng cm$^3$) ở nhiệt độ $T$ (đơn vị: $^\\circ$C) khi $T$ thay đổi từ $0^\\circ$C đến $30^\\circ$C được cho xấp xỉ bởi công thức:
                    $$V(T) = {c0:.2f} - {c1:.5f}T + {c2:.5f}T^2 - {c3:.6f}T^3.$$
                    Nhiệt độ $T_0 \\in (0; 30)$ nhỏ nhất là bao nhiêu để kể từ nhiệt độ $T_0$ trở lên thì thể tích $V$ tăng?
                        {round_SA(ket_qua)[0]} """
            loigiai = f""" Để thể tích $V$ bắt đầu tăng, ta cần tìm điểm cực tiểu $T_0$ của hàm số $V(T)$ trên khoảng $(0; 30)$. Điều này tương đương với việc tìm nghiệm của phương trình $V'(T) = 0$ trong khoảng đó. \\\\
                        Ta có hàm thể tích:
                        $V(T) = {c0:.2f} - {c1:.5f}T + {c2:.5f}T^2 - {c3:.6f}T^3$ \\\\
                        Lấy đạo hàm theo $T$:
                        $V'(T) = -{c1:.5f} + 2 \\cdot {c2:.5f}T - 3 \\cdot {c3:.6f}T^2$\\\\
                        $V'(T) = {a_pt:.6f}T^2 + {b_pt:.5f}T - {c1:.5f}$  \\\\
                        Giải phương trình bậc hai $V'(T) = 0$ để tìm các điểm cực trị.\\\\
                        Sử dụng máy tính hoặc công cụ giải toán với các hệ số trên, ta tìm được nghiệm trong khoảng $(0; 30)$ là:
                        $T_0 \\approx {T0_chinh_xac:.5f}^\\circ$C.  \\\\
                        Làm tròn kết quả theo yêu cầu đề bài, ta được $T_0 = {latex(ket_qua)}^circ C{'' if len(str(ket_qua)) < 5 else f'\\approx {round_SA(ket_qua)[1]}^\\circ C'}$. """
            #Đáp án
            dapan='\\shortans[0]{$%s$}'%(round_SA(ket_qua)[1])              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content

