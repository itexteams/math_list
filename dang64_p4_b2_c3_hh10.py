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


def bt_dang64_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # B2, B3, B4 - Lập trình và Random bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập tham số dựa trên biểu thức y = (m^2 - a)x + bm + c
                a = 7 
                b = 4
                c = -1

                # Chọn m sao cho m^2 - a là một số nguyên (VD: chọn m=3 => 3^2 - 7 = 2)
                # Để bài toán hay, ta cho m ngẫu nhiên là 3 hoặc -3
                m_chuan = random.choice([3, -3])
                k = m_chuan**2 - a # Hệ số góc của đường thẳng thứ hai

                # Để loại 1 giá trị m (giả sử loại m = -3), ta tính d dựa trên m = -3
                m_loai = -m_chuan
                d = b * m_loai + c # Điều kiện bm + c = d sẽ làm hai đường trùng nhau

                # Đáp án đúng là giá trị m không bị trùng
                kq_dung = m_chuan

                # Xử lý dấu của b và c để tránh lỗi hiển thị "x4m" hoặc "+ -1"
                # Sửa lỗi "x4m" bằng cách ép buộc có dấu cách và toán tử
                b_val = abs(b)
                b_sign = "+" if b >= 0 else "-"

                c_str = "+ " + str(latex(abs(c))) if c >= 0 else "- " + str(latex(abs(c)))
                d_str = "+ " + str(latex(abs(d))) if d >= 0 else "- " + str(latex(abs(d)))

                # Các phương án trắc nghiệm
                da_dung_str = '$m = %s$' % (latex(kq_dung))
                s = [
                    '$m = \\pm %s$' % (latex(abs(m_chuan))),
                    '$m = %s$' % (latex(m_loai)),
                    '$m = \\pm \\sqrt{%s}$' % (latex(abs(k))),
                    '$m = 0$',
                    '$m = 1$',
                    '$m = -1$'
                ]

                random.shuffle(s)
                list_sai = []
                for item in s:
                    if item != da_dung_str and len(list_sai) < 3:
                        list_sai.append(item)

                # Nội dung câu hỏi (Đã sửa lỗi x4m bằng cách thêm b_sign)
                noidungcauhoi = ('''Tìm giá trị thực của tham số $m$ để đường thẳng $y = (m^2 - %s)x %s %sm %s$ song song với đường thẳng $y = %sx %s$.'''
                                % (latex(a), b_sign, latex(b_val), c_str, latex(k), d_str))

                # Các đáp án
                da_d = '\\True ' + da_dung_str
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Để đường thẳng $y = (m^2 - %s)x %s %sm %s$ song song với đường thẳng $y = %sx %s$ thì điều kiện là:
                            \\\\[0.5pt] $\\begin{cases} m^2 - %s = %s \\\\ %sm %s \\neq %s \\end{cases} 
                            \\Leftrightarrow \\begin{cases} m^2 = %s \\\\ %sm \\neq %s \\end{cases}
                            \\Leftrightarrow \\begin{cases} m = \\pm %s \\\\ m \\neq %s \\end{cases} 
                            \\Leftrightarrow m = %s$.'''
                          % (latex(a), b_sign, latex(b_val), c_str, latex(k), d_str,
                             latex(a), latex(k), latex(b), c_str, latex(d),
                             latex(a + k), latex(b), latex(d - c),
                             latex(abs(m_chuan)), latex(m_loai), latex(kq_dung)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

