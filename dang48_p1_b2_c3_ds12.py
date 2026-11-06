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


def bt_dang48_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            t = symbols('t')

            # Khai báo danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                a = 3 * random.randint(1, 4)  # Ví dụ: 3, 6, 9, 12
                b = 2 * random.randint(1, 5)  # Ví dụ: 2, 4, 6, 8, 10
                x0 = random.randint(1, 10)    # Tọa độ ban đầu
                t_val = random.randint(1, 3)  # Thời điểm xét (giây)

                # Biểu thức vận tốc
                v_expr = a*t**2 + b*t

                # Tính quãng đường S = tích phân từ 0 đến t_val của v(t)
                S_val = integrate(v_expr, (t, 0, t_val))

                # Tọa độ cuối cùng x = x0 + S
                kq_dung = x0 + S_val

                # --- B4: Điều chỉnh các phương án sai không được trùng ---
                da_dung_str = f'$x = {latex(kq_dung)}$'

                options = set()
                while len(options) < 3:
                    # Các phương án sai phổ biến:
                    # 1. Quên cộng x0
                    # 2. Tính sai nguyên hàm (không chia hệ số)
                    # 3. Cộng nhầm x0
                    sai = random.choice([
                        S_val,                          # Quên x0
                        x0 + (a*t_val**2 + b*t_val),    # Nhầm công thức vận tốc
                        kq_dung + random.randint(1, 5), # Lệch đơn vị
                        kq_dung - random.randint(1, 3)
                    ])
                    if sai != kq_dung and sai > 0:
                        options.add(f'$x = {latex(sai)}$')

                list_sai = list(options)
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Một chất điểm chuyển động thẳng trên trục $Ox$ với vận tốc cho bởi công thức $v(t) = %s \text{ (m/s)}$ ($t$ là thời gian). Biết rằng tại thời điểm bắt đầu của chuyển động, chất điểm đang ở vị trí có tọa độ $x = %s$. Tọa độ của chất điểm sau $%s$ giây chuyển động là'''
                                 % (latex(v_expr), latex(x0), latex(t_val)))

                # Các đáp án
                da_d = ('\\True ' + da_dung_str)

                # Trộn đáp án
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải (B2: Viết lại y hệt logic bài mẫu)
                # Nguyên hàm của v(t)
                V_antideriv = integrate(v_expr, t)

                loigiai = (r'''Quãng đường mà vật đi được sau $%s$ giây là: \\
                           $S = \int_{0}^{%s} v(t) \text{d}t = \int_{0}^{%s} (%s) \text{d}t = \left. \left( %s \right) \right|_{0}^{%s} = %s \text{ (m)}$. \\
                           Vậy tọa độ của chất điểm sau $%s$ giây chuyển động là $x = %s + %s = %s$.'''
                           % (latex(t_val), latex(t_val), latex(t_val), latex(v_expr), 
                              latex(V_antideriv), latex(t_val), latex(S_val),
                              latex(t_val), latex(x0), latex(S_val), latex(kq_dung)))

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

