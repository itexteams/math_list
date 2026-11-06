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


def bt_dang18_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- RANDOM SỐ LIỆU ---
                # a là hệ số trong căn: sqrt(1-ax) - sqrt(1+ax)
                a = randint(1, 5) 
                # b là hằng số phân thức: m + (b-x)/(1+x)
                b = randint(1, 5)

                # --- TÍNH TOÁN KẾT QUẢ ---
                # Lim phải (x -> 0+): m + (b-0)/(1+0) = m + b
                lim_phai_val = b

                # Lim trái (x -> 0-): (sqrt(1-ax) - sqrt(1+ax))/x
                # = -2ax / (x * (sqrt + sqrt)) = -a
                lim_trai_val = -a

                # Kết quả m
                ket_qua_m = -a - b

                # --- HIỂN THỊ ĐỀ BÀI ---
                # Xử lý hiển thị hệ số a (nếu a=1 thì viết x thay vì 1x)
                str_ax = f"{a}x" if a > 1 else "x"

                ham_so_latex = (r"f\left( x \right) = \begin{cases} "
                                r"\dfrac{\sqrt{1-%s} - \sqrt{1+%s}}{x} & \text{khi } x < 0 \\"
                                r" m + \dfrac{%s-x}{1+x} & \text{khi } x \ge 0 "
                                r"\end{cases}" % (str_ax, str_ax, b))

                noidungcauhoi = (r"Giá trị của $m$ để hàm số $%s$ liên tục tại $x=0$ bằng bao nhiêu?" % ham_so_latex)

                # --- TẠO ĐÁP ÁN NHIỄU ---
                kq = ket_qua_m
                wrong_answers = set()
                wrong_answers.add(-kq)     # Sai dấu
                wrong_answers.add(kq + 1)  # Sai lệch đơn vị
                wrong_answers.add(kq - 1)

                # Bổ sung nếu chưa đủ 3 đáp án nhiễu
                while len(wrong_answers) < 3:
                    wrong_answers.add(randint(-10, 10))
                wa_list = list(wrong_answers)

                # Format đáp án
                du = [f"m = {kq}"]
                da = random.choice(du)

                s = [f"m = {wa_list[0]}", f"m = {wa_list[1]}", f"m = {wa_list[2]}"]
                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1); da_s2 = str(das2); da_s3 = str(das3)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- LỜI GIẢI CHI TIẾT (ĐÃ SỬA FORMATTING) ---

                # Bước nhân liên hợp
                tu_so_lien_hop = r"(1-%s) - (1+%s)" % (str_ax, str_ax)
                mau_so_lien_hop = r"x\left(\sqrt{1-%s} + \sqrt{1+%s}\right)" % (str_ax, str_ax)

                # Bước rút gọn tử số: tính toán giá trị thực (-2 * a)
                val_tu_rut_gon = -2 * a
                tu_so_rut_gon = f"{val_tu_rut_gon}x" 

                # Tạo chuỗi lời giải
                # Sử dụng \begin{aligned} để căn thẳng hàng dấu bằng và tránh bị kéo giãn khoảng cách
                # Hoặc ngắt dòng bằng \\ và tách thành các công thức riêng

                loigiai = (r'''Ta có: \\
                $\bullet \lim\limits_{x \to 0^+} f(x) = \lim\limits_{x \to 0^+} \left( m + \dfrac{%s-x}{1+x} \right) = m + %s$. \\
                $\bullet \lim\limits_{x \to 0^-} f(x) = \lim\limits_{x \to 0^-} \dfrac{\sqrt{1-%s} - \sqrt{1+%s}}{x} $ \\
                $= \lim\limits_{x \to 0^-} \dfrac{%s}{%s} $ \\
                $= \lim\limits_{x \to 0^-} \dfrac{%s}{%s} 
                = \dfrac{%s}{2} = %s$. \\
                $\bullet f(0) = m + %s$. \\
                Để hàm số liên tục tại $x=0$ thì $\lim\limits_{x \to 0^+} f(x) = \lim\limits_{x \to 0^-} f(x) = f(0)$ \\
                $\Leftrightarrow m + %s = %s \Leftrightarrow m = %s$.'''
                % (b, b, 
                   str_ax, str_ax, 
                   tu_so_lien_hop, mau_so_lien_hop,
                   tu_so_rut_gon, mau_so_lien_hop,
                   val_tu_rut_gon, lim_trai_val,
                   b,
                   b, lim_trai_val, kq))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content   

