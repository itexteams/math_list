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


def bt_dang12_p3_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn mẫu số cho xác suất màu xanh (p1) và màu vàng (p2)
                # Đảm bảo tổng xác suất < 1 vì còn 2 màu đỏ và trắng
                p1_den = random.randint(3, 6) # ví dụ: 1/3, 1/4, 1/5, 1/6
                p2_den = random.randint(2, 4) # ví dụ: 1/2, 1/3, 1/4

                # Đảm bảo tổng không vượt quá hoặc bằng 1 để bài toán logic
                while (1/p1_den + 1/p2_den) >= 0.9:
                    p1_den = random.randint(3, 8)
                    p2_den = random.randint(2, 5)

                p1 = Rational(1, p1_den)
                p2 = Rational(1, p2_den)

                # Tính kết quả
                kq_chinh_xac = p1 + p2
                kq_float = float(kq_chinh_xac)

                # Làm tròn đến hàng phần chục theo quy tắc ROUND_HALF_UP
                kq_round = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_round).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                da = '$%s$' % (kq_str)

                s = []
                while len(s) < 3:
                    # Tạo các phương án sai quanh đáp án đúng
                    sai_so = random.choice([-0.2, -0.1, 0.1, 0.2, 0.3])
                    val_sai = float(kq_round) + sai_so
                    if val_sai > 0 and val_sai < 1:
                        val_sai_str = str(Decimal(str(val_sai)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        formatted_sai = '$%s$' % (val_sai_str)
                        if formatted_sai != da and formatted_sai not in s:
                            s.append(formatted_sai)

                das1, das2, das3 = s

                # B2: Viết lại nội dung đề bài
                noidungcauhoi = ('''Một hộp có chứa một số quả cầu gồm bốn màu xanh, vàng, đỏ, trắng (các quả cầu cùng màu thì khác nhau về bán kính). Lấy ngẫu nhiên một quả cầu từ hộp, biết xác suất để lấy được một quả cầu màu xanh bằng $%s$, xác suất để lấy được một quả cầu màu vàng bằng $%s$. Xác suất để lấy được một quả cầu xanh hoặc một quả cầu vàng bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).'''
                                 % (latex(p1), latex(p2)))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B1 & B2: Nội dung lời giải chi tiết theo mẫu ảnh
                loigiai = ('''Gọi biến cố $A$: "Lấy được một quả cầu màu xanh" và $B$: "Lấy được một quả cầu màu vàng". Ta có $A, B$ là hai biến cố xung khắc. \\\\
                             Xác suất để lấy được một quả cầu màu xanh hoặc một quả cầu màu vàng là: \\\\
                             $P\\left( A \\cup B \\right) = P\\left( A \\right) + P\\left( B \\right) = %s + %s = %s \\approx %s$.'''
                           % (latex(p1), latex(p2), latex(kq_chinh_xac), kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # Xuất câu trắc nghiệm (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

