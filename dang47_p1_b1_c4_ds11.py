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


def bt_dang47_p1_b1_c4_ds11(self):
            # Khai báo biến
            # --- CẤU HÌNH BÀI TOÁN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                # Chọn b (cơ số của số hạng thứ 2 trong căn)
                b = randint(3, 9) # Ví dụ: b=4 (như hình gốc), hoặc 3, 5, 6...

                # Tính a (cơ số chính)
                a = b**2  # Ví dụ: b=4 -> a=16

                # Chọn c (cơ số của số hạng thứ 2 trong căn thứ 2), c phải nhỏ hơn b
                c = randint(2, b - 1) # Ví dụ: b=4 -> c có thể là 2 hoặc 3


                kq_chinh_xac = Rational(1, 2 * b)

                # B2 - Viết lại y hệt bài toán (tạo string LaTeX)

                # --- Tạo nội dung câu hỏi ---
                noidungcauhoi = (
                    "Giới hạn $T = \\lim_{n\\to+\\infty} \\left(\\sqrt{%s^{n+1}+%s^n} - \\sqrt{%s^{n+1}+%s^n}\\right)$ bằng"
                    % (a, b, a, c)
                )

                # --- Tạo các đáp án nhiễu (Distractors) ---
                # Đáp án đúng
                da_dung = '$%s$' % latex(kq_chinh_xac)

                # Tạo đáp án sai dựa trên các lỗi sai phổ biến
                ds = []

                # Sai lầm 1: Quên nhân 2 ở mẫu -> 1/b
                ds.append(Rational(1, b))

                # Sai lầm 2: Tính sai mẫu số cộng trừ -> 1/(2b + 2) hoặc 1/(2b - 2)
                ds.append(Rational(1, 2*b + 2))
                ds.append(Rational(1, 2*b - 2))

                # Sai lầm 3: Kết quả là 0 hoặc 1 hoặc vô cực (lấy ngẫu nhiên vài mẫu số lạ)
                ds.append(Rational(1, b + 3))
                ds.append(Rational(1, a)) # 1/16 chẳng hạn

                # Lọc trùng và chọn 3 đáp án sai
                ds_unique = list(set(ds))
                if kq_chinh_xac in ds_unique: ds_unique.remove(kq_chinh_xac) # Đảm bảo không trùng đáp án đúng

                random.shuffle(ds_unique)
                wrong_choices = ds_unique[:3]

                # Format đáp án sai sang LaTeX
                list_answers = ['\\True ' + da_dung] + ['$%s$' % latex(w) for w in wrong_choices]
                random.shuffle(list_answers)

                # --- Tạo nội dung lời giải chi tiết (Bám sát hình ảnh) ---
                # Bước 1: Nhân liên hợp
                # Bước 2: Chia cả tử và mẫu cho b^n (tức là căn(a^n))

                tu_so_lien_hop = "%s^n - %s^n" % (b, c)
                mau_so_lien_hop = "\\sqrt{%s^{n+1} + %s^n} + \\sqrt{%s^{n+1} + %s^n}" % (a, b, a, c)

                mau_so_tach_nhan_tu = "\\sqrt{%s \\cdot %s^n + %s^n} + \\sqrt{%s \\cdot %s^n + %s^n}" % (a, a, b, a, a, c)

                # Phân số trong căn sau khi chia
                phan_so_b = "\\left(\\frac{1}{%s}\\right)" % (b) if b == a/b else "\\left(\\frac{%s}{%s}\\right)" % (b, a) # Thực tế 1/b^n trong căn là (1/b)^n nếu rút a^n ra
                # Tuy nhiên code đơn giản theo mẫu hình: rút 16^n -> còn (4/16)^n = (1/4)^n
                # Trong hình: rút 16^n ra ngoài thành 4^n. Bên trong còn 16 + (4/16)^n = 16 + (1/4)^n

                frac_b_inside = Rational(b, a) # Ví dụ 4/16 = 1/4
                frac_c_inside = Rational(c, a) # Ví dụ 3/16

                mau_so_gioi_han = "\\sqrt{%s + \\left(%s\\right)^n} + \\sqrt{%s + \\left(%s\\right)^n}" % (a, latex(frac_b_inside), a, latex(frac_c_inside))

                # Dòng cuối cùng của lời giải
                ket_qua_mau = "%s + %s" % (latex(sqrt(a)), latex(sqrt(a))) # 4 + 4

                loigiai = ('''Ta có $T = \\lim_{n\\to+\\infty} \\left(\\sqrt{%s^{n+1}+%s^n} - \\sqrt{%s^{n+1}+%s^n}\\right) = \\lim_{n\\to+\\infty} \\frac{%s}{%s}$ \\\\
                    $= \\lim_{n\\to+\\infty} \\frac{%s}{%s} = \\lim_{n\\to+\\infty} \\frac{1 - \\left(\\frac{%s}{%s}\\right)^n}{%s}$ \\\\
                    $= \\frac{1}{%s} = %s.$''' 
                    % (
                        a, b, a, c, 
                        tu_so_lien_hop, mau_so_lien_hop,
                        tu_so_lien_hop, mau_so_tach_nhan_tu, 
                        c, b, mau_so_gioi_han,
                        ket_qua_mau, latex(kq_chinh_xac)
                      )
                )

                # --- Xuất kết quả ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choice \n'
                    '{' + str(list_answers[0]) + '}\n'
                    '{' + str(list_answers[1]) + '}\n'
                    '{' + str(list_answers[2]) + '}\n'
                    '{' + str(list_answers[3]) + '}\n'
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content

