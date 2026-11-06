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


def bt_dang28_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3 - Logic Random bài toán: 
                # Random độ dài 2 cạnh AB, AC (đảm bảo AB khác AC để không trùng lặp)
                AB = random.randint(3, 9)
                AC = random.randint(3, 9)
                while AB == AC:
                    AC = random.randint(3, 9)

                # Chọn góc A là các góc đặc biệt (60, 90, 120)
                goc_A = random.choice([60, 90, 120])
                goc_A_half = goc_A // 2

                # Tính toán chính xác bằng dạng phân số (Rational) và căn thức của Sympy
                phan_so_truoc_cos = Rational(2 * AB * AC, AB + AC)
                cos_A_half = cos(goc_A_half * pi / 180)
                AD_exact = simplify(phan_so_truoc_cos * cos_A_half)

                # Tính ra số thập phân và làm tròn đến hàng phần chục
                AD_decimal = float(AD_exact)
                AD_round = Decimal(str(AD_decimal)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Đổi dấu chấm thành phẩy cho chuẩn Việt Nam
                kq_str = str(AD_round).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ có $AB=%s$, $AC=%s$, $\\widehat{A}=%s^\\circ$. Tính độ dài đường phân giác trong góc $A$ của tam giác $ABC$ (kết quả làm tròn đến hàng phần chục).'''
                                 %(AB, AC, goc_A))

                # Các đáp án trắc nghiệm (đáp án đúng)
                da = kq_str

                # Tạo các đáp án gây nhiễu bằng cách cộng trừ thêm 0.1, 0.2
                s = [
                    str(Decimal(str(AD_decimal + 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(AD_decimal - 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(AD_decimal + 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(AD_decimal - 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                ]
                # Lọc bỏ trùng lặp và đảm bảo khác đáp án đúng
                s = list(set([val for val in s if val != kq_str]))
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Định dạng LaTeX cho các đáp án
                da_d = ('\\True $%s$.' % da)
                da_s1 = ('$%s$.' % das1)
                da_s2 = ('$%s$.' % das2)
                da_s3 = ('$%s$.' % das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Đã ép hiển thị phân số và căn thức đẹp mắt, KHÔNG hiển thị số thập phân)
                loigiai = ('''Giả sử đường phân giác trong góc $A$ của $\\Delta ABC$ cắt cạnh $BC$ tại điểm $D$.\\\\
            Với $S$ là kí hiệu diện tích tam giác ta có\\\\
            $S_{ABC} = S_{ADB} + S_{ADC} \\Leftrightarrow \\frac{1}{2}AB \\cdot AC \\cdot \\sin A = \\frac{1}{2}AD \\cdot AB \\sin \\frac{A}{2} + \\frac{1}{2}AD \\cdot AC \\cdot \\sin \\frac{A}{2}$.\\\\
            $\\Leftrightarrow AD = \\frac{2 \\cdot AB \\cdot AC}{AB + AC} \\cdot \\cos \\frac{A}{2} = \\frac{2 \\cdot %s \\cdot %s}{%s + %s} \\cdot \\cos %s^\\circ = %s \\approx %s$.'''
                           %(AB, AC, AB, AC, goc_A_half, latex(AD_exact), kq_str))

            # Xử lý chuỗi hiển thị tránh lỗi dấu + - hoặc - - theo lưu ý
            noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')
            loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

