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


def bt_dang27_p4_b1_c4_ds11(self):
            # Khai báo biến
            # --- Phần cấu hình bài toán ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random hệ số
                # Chọn e là số chính phương để mẫu số đẹp (4, 9, 16, 25)
                n=symbols('n')
                e_sqrt_val = randint(2, 5) 
                e = e_sqrt_val ** 2
                f = randint(-9, 9)

                # Chọn a và c sao cho a > c để kết quả dương (hoặc a != c) và số nhỏ để dễ nhìn
                c = randint(1, 3)
                a = c + randint(1, 4) # Đảm bảo a > c

                b = randint(1, 5)
                d = randint(1, 5)

                # 2. Tính toán kết quả chính xác bằng Sympy
                # Biểu thức: (sqrt(an+b) - sqrt(cn+d)) / sqrt(en+f)
                expr = (sqrt(a*n + b) - sqrt(c*n + d)) / sqrt(e*n + f)

                # Tính giới hạn
                kq_chinh_xac = limit(expr, n, oo)

                # 3. Tạo các đáp án nhiễu (Distractors)
                # Đáp án đúng
                da_dung = latex(simplify(kq_chinh_xac))

                # Tạo đáp án sai bằng cách cộng trừ hoặc đổi dấu
                # Sai 1: Đảo dấu kết quả
                da_sai1 = latex(simplify(-kq_chinh_xac))
                # Sai 2: Kết quả + 1/2
                da_sai2 = latex(simplify(kq_chinh_xac + Rational(1, 2)))
                # Sai 3: Kết quả nhân 2 (lỗi thường gặp khi quên chia mẫu)
                da_sai3 = latex(simplify(kq_chinh_xac * 2))

                # Nếu random vô tình trùng nhau thì gán giá trị cố định để tránh lỗi hiển thị
                ds_dap_an = set([da_dung, da_sai1, da_sai2, da_sai3])
                while len(ds_dap_an) < 4:
                    da_sai_them = latex(simplify(kq_chinh_xac + randint(1,5)))
                    ds_dap_an.add(da_sai_them)

                list_dap_an = list(ds_dap_an)
                # Đảm bảo đáp án đúng có trong list và loại bỏ nó để trộn các đáp án sai
                if da_dung in list_dap_an:
                    list_dap_an.remove(da_dung)

                # Lấy 3 đáp án sai từ set
                s = list_dap_an[:3]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Xây dựng nội dung câu hỏi và lời giải

                # Câu hỏi
                noidungcauhoi = (
                    "Tính giới hạn $L = \\lim_{n \\to +\\infty} \\dfrac{\\sqrt{%sn %s} - \\sqrt{%sn %s}}{\\sqrt{%sn %s}}$."
                    % (a, "+" + str(b) if b >= 0 else str(b), 
                       c, "+" + str(d) if d >= 0 else str(d), 
                       e, "+" + str(f) if f >= 0 else str(f))
                )

                # Lời giải chi tiết (Mô phỏng theo ảnh)
                # Bước 1: Nhân liên hợp -> Tử số: (an+b) - (cn+d) = (a-c)n + (b-d)
                tu_so_sau_lh_heso_n = a - c
                tu_so_sau_lh_heso_td = b - d
                str_tu_so = latex(tu_so_sau_lh_heso_n * n + tu_so_sau_lh_heso_td)

                # Mẫu số khi đặt n ra ngoài
                # Tử số rút n: n( (a-c) + (b-d)/n )
                str_tu_so_rut_n = "n \\left(%s - \\frac{%s}{n}\\right)" % (tu_so_sau_lh_heso_n, abs(tu_so_sau_lh_heso_td)) 
                if tu_so_sau_lh_heso_td >= 0:
                    str_tu_so_rut_n = "n \\left(%s + \\frac{%s}{n}\\right)" % (tu_so_sau_lh_heso_n, tu_so_sau_lh_heso_td)

                # Mẫu số rút n: n * sqrt(e + f/n) * (sqrt(a + b/n) + sqrt(c + d/n))
                str_mau_rut_n_1 = "\\sqrt{%s %s \\frac{%s}{n}}" % (e, "+" if f>=0 else "-", abs(f))
                str_mau_rut_n_2 = "\\left(\\sqrt{%s %s \\frac{%s}{n}} + \\sqrt{%s %s \\frac{%s}{n}}\\right)" % (
                    a, "+" if b>=0 else "-", abs(b),
                    c, "+" if d>=0 else "-", abs(d)
                )

                # Giá trị thay số cuối cùng
                val_tu = tu_so_sau_lh_heso_n
                val_mau = "\\sqrt{%s}\\left(\\sqrt{%s}+\\sqrt{%s}\\right)" % (e, a, c)

                loigiai = (r'''Nhân cả tử và mẫu với biểu thức liên hợp $\sqrt{%sn %s} + \sqrt{%sn %s}$, ta được:
                \begin{align*}
                L &= \lim_{n \to +\infty} \dfrac{(%sn %s) - (%sn %s)}{\sqrt{%sn %s}\left(\sqrt{%sn %s} + \sqrt{%sn %s}\right)} \\
                &= \lim_{n \to +\infty} \dfrac{%s}{\sqrt{%sn %s}\left(\sqrt{%sn %s} + \sqrt{%sn %s}\right)} \\
                &= \lim_{n \to +\infty} \dfrac{%s}{n %s %s} \\
                &= \lim_{n \to +\infty} \dfrac{%s %s \frac{%s}{n}}{%s %s} \\
                &= \dfrac{%s - 0}{\sqrt{%s+0}\left(\sqrt{%s+0}+\sqrt{%s+0}\right)} = \dfrac{%s}{%s} = %s.
                \end{align*}''' 
                % (
                    a, "+" + str(b) if b >= 0 else str(b), c, "+" + str(d) if d >= 0 else str(d), # Dòng nhân liên hợp
                    a, "+" + str(b) if b >= 0 else str(b), c, "+" + str(d) if d >= 0 else str(d), # Dòng 1: Tử
                    e, "+" + str(f) if f >= 0 else str(f), a, "+" + str(b) if b >= 0 else str(b), c, "+" + str(d) if d >= 0 else str(d), # Dòng 1: Mẫu
                    str_tu_so, # Dòng 2: Tử rút gọn
                    e, "+" + str(f) if f >= 0 else str(f), a, "+" + str(b) if b >= 0 else str(b), c, "+" + str(d) if d >= 0 else str(d), # Dòng 2: Mẫu giữ nguyên
                    str_tu_so_rut_n, str_mau_rut_n_1, str_mau_rut_n_2, # Dòng 3: Rút n
                    tu_so_sau_lh_heso_n, "+" if tu_so_sau_lh_heso_td >=0 else "-", abs(tu_so_sau_lh_heso_td), # Dòng 4: Tử
                    str_mau_rut_n_1, str_mau_rut_n_2, # Dòng 4: Mẫu
                    val_tu, e, a, c, # Dòng 5: Thay số
                    tu_so_sau_lh_heso_n, val_mau, da_dung # Kết quả
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

