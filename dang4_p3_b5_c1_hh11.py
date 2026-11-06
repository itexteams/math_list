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


def bt_dang4_p3_b5_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hàm chuyển đổi số sang chuỗi hiển thị chuẩn tiếng Việt (dấu phẩy)
        def fmt_num(val):
            if isinstance(val, (int, Integer)):
                return str(val)
            val_float = float(val)
            if val_float.is_integer():
                return str(int(val_float))
            # Định dạng tối đa 2 chữ số thập phân gọn gàng
            s = ('%.2f' % val_float).rstrip('0').rstrip('.')
            return s.replace('.', ',')

        # Sinh các thông số sao cho kết quả đẹp, phong phú
        # Có thể là số nguyên hoặc số thập phân có phần thập phân .5
        k = choice([1, 2, 3, 4, 5, 0.5, 1.5, 2.5])
        ab_val = choice([2, 3, 4, 5, 6, 8, 10, 2.5, 3.5, 4.5, 7.5])
        bc_val = choice([2, 4, 6, 8, 10, 12, 14, 16])

        # A'B' = k * AB, do đó B'C' = k * BC
        ab_prime_val = round(k * ab_val, 2)
        if float(ab_prime_val).is_integer():
            ab_prime_val = int(ab_prime_val)

        bc_prime_val = round(k * bc_val, 2)
        if float(bc_prime_val).is_integer():
            bc_prime_val = int(bc_prime_val)

        # Làm tròn và chuẩn hóa đáp số theo yêu cầu
        number = Decimal(str(bc_prime_val))
        if number == number.to_integral():
            kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        else:
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        str_ab = fmt_num(ab_val)
        str_bc = fmt_num(bc_val)
        str_ab_prime = fmt_num(ab_prime_val)
        str_bc_prime = fmt_num(bc_prime_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Ba điểm $A,B,C$ thẳng hàng theo thứ tự $A,B,C$, với $AB=%s\\text{ cm}$ và $BC=%s\\text{ cm}$. Đường thẳng $ABC$ không cùng phương với phương chiếu. Sau phép chiếu song song, $A'B'=%s\\text{ cm}$. Độ dài $B'C'$ (đơn vị cm) là'''
                         % (str_ab, str_bc, str_ab_prime))

        # Nội dung lời giải (sử dụng \\dfrac{}{})
        loigiai = ('''Ba đoạn $AB,BC$ cùng nằm trên một đường thẳng, nên phép chiếu song song bảo toàn tỉ số: \\\\
                   $\\dfrac{A'B'}{B'C'}=\\dfrac{AB}{BC}=\\dfrac{%s}{%s}$. \\\\
                   Thay $A'B'=%s$, ta được $\\dfrac{%s}{B'C'}=\\dfrac{%s}{%s}$. Suy ra \\\\
                   $B'C'=\\dfrac{%s\\cdot %s}{%s}=%s$.'''
                   % (str_ab, str_bc,
                      str_ab_prime, str_ab_prime, str_ab, str_bc,
                      str_ab_prime, str_bc, str_ab, str_bc_prime))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

