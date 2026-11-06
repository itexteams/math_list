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


def bt_dang42_p4_b3_c5_ds11(self):
            # Khai báo biến
            # --- BƯỚC 1 & 2: THIẾT LẬP BIẾN VÀ NGẪU NHIÊN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # A_vay: Số tiền vay (triệu đồng) - Random từ 200 đến 800 triệu
                A_vay = random.randint(200, 800)

                # r_lai: Lãi suất hàng tháng (%) - Random từ 0.4% đến 0.9%
                r_lai = round(random.uniform(0.4, 0.9), 1)
                r_decimal = r_lai / 100

                # n_nam: Số năm vay - Random từ 2 đến 6 năm
                n_nam = random.randint(3, 6)
                n_thang = n_nam * 12

                # Tiền tiết kiệm (chỉ mang tính chất làm đề bài phong phú)
                tiet_kiem = random.randint(400, 700)

                # Công thức tính số tiền trả hàng tháng a:
                # a = A * r * (1+r)^n / ((1+r)^n - 1)
                tu_so = A_vay * r_decimal * (1 + r_decimal)**n_thang
                mau_so = (1 + r_decimal)**n_thang - 1
                a_calc = tu_so / mau_so

                # Làm tròn kết quả đến 4 chữ số thập phân để giống mẫu lời giải
                kq_float = round(a_calc, 4)
                kq_str = str(kq_float).replace('.', ',')

                # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI KHÔNG TRÙNG ---
                # Lấy các giá trị xung quanh kết quả đúng
                sai_1 = round(kq_float + random.uniform(0.5, 1.5), 4)
                sai_2 = round(kq_float - random.uniform(0.5, 1.5), 4)
                sai_3 = round(kq_float + random.uniform(1.6, 2.5), 4)

                # Đáp án đúng
                da_dung = '$%s$ triệu đồng' % kq_str

                # Danh sách các đáp án nhiễu
                s = [
                    '$%s$ triệu đồng' % str(sai_1).replace('.', ','),
                    '$%s$ triệu đồng' % str(sai_2).replace('.', ','),
                    '$%s$ triệu đồng' % str(sai_3).replace('.', ','),
                ]

                # Nội dung câu hỏi
                r_lai_vn = str(r_lai).replace('.', ',')
                # Nội dung câu hỏi
                noidungcauhoi = (
                    f"Ba năm trước, An tốt nghiệp Đại học và đi làm ngay. Sau 3 năm tích lũy, An tiết kiệm được ${tiet_kiem}$ triệu đồng. "
                    f"Để mở công ty riêng, An quyết định vay thêm từ ngân hàng số tiền ${A_vay}$ triệu đồng với hình thức trả góp: "
                    f"đều đặn hàng tháng (bắt đầu sau 1 tháng kể từ khi giải ngân), An sẽ trả một khoản tiền cố định cho ngân hàng. "
                    f"Biết lãi suất cho vay là ${r_lai_vn}\\%$ mỗi tháng (không đổi trong suốt quá trình vay) và An hoàn thành trả nợ sau đúng "
                    f"${n_nam}$ năm (tức ${n_thang}$ tháng). Tính số tiền An cần trả hàng tháng cho ngân hàng.")

                # Các đáp án trắc nghiệm
                da_d = '\\True ' + da_dung
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- BƯỚC 3: NỘI DUNG LỜI GIẢI ---
                loigiai = ('''An vay số tiền $A = %s$ triệu đồng, lãi suất $r = %s$ptr. $a$ (triệu đồng) là số tiền mà An trả hàng tháng. \\\\
                            Gọi $T_n$ là số tiền mà An phải trả sau $n$ tháng. \\\\
                            Ta có: \\\\
                            $T_1 = %s(1 + %s\\%%) - a$. \\\\
                            $T_2 = (%s(1 + %s\\%%) - a)(1 + %s\\%%) - a = %s(1 + %s\\%%)^2 - a(1 + %s\\%%) - a$. \\\\
                            ... \\\\
                            $T_n = %s(1 + %s\\%%)^n - a\\frac{(1 + %s\\%%)^n - 1}{%s\\%%}$. \\\\
                            Theo đề bài $T_{%s} = 0 \\Leftrightarrow %s(1 + %s\\%%)^{%s} - a\\frac{(1 + %s\\%%)^{%s} - 1}{%s\\%%} = 0 \\Rightarrow a \\approx %s$ triệu đồng.'''
                           %(latex(A_vay), latex(r_lai), 
                             latex(A_vay), latex(r_lai),
                             latex(A_vay), latex(r_lai), latex(r_lai), latex(A_vay), latex(r_lai), latex(r_lai),
                             latex(A_vay), latex(r_lai), latex(r_lai), latex(r_lai),
                             latex(n_thang), latex(A_vay), latex(r_lai), latex(n_thang), latex(r_lai), latex(n_thang), latex(r_lai),
                             kq_str))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('ptr','\\%')
            return content

