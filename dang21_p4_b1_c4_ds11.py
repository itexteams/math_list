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


def bt_dang21_p4_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random thông số đầu vào
                # Tử số là căn của tổng cấp số cộng: 1 + ... + (dn + c)
                u1 = 1                         # Số hạng đầu
                d = random.choice([2, 4, 6, 8]) # Công sai (chọn chẵn để chia 2 cho đẹp)

                # Mẫu số: a*n - b
                a_mau = random.randint(2, 5)   # Hệ số của n dưới mẫu
                b_mau = random.randint(1, 3)   # Hệ số tự do dưới mẫu

                # 2. Xử lý logic toán học (Sympy)
                n_sym = symbols('n')

                # Xác định số hạng tổng quát un = u1 + (n-1)d
                const_tu = u1 - d
                u_n_expr = d * n_sym + const_tu

                # Số hạng thứ 2 (để hiển thị trong đề bài: 1 + u2 + ...)
                u2 = u1 + d

                # Tính tổng Sn = n(u1 + un)/2
                tong_sn = (n_sym * (u1 + u_n_expr)) / 2

                # Biểu thức giới hạn: Limit(sqrt(Sn) / (an - b))
                bieuthuc = sqrt(tong_sn) / (a_mau * n_sym - b_mau)

                # Tính kết quả chính xác bằng Sympy
                ket_qua = limit(bieuthuc, n_sym, oo)
                kq_latex = latex(ket_qua)

                # 3. Tạo các đáp án nhiễu (Distractors)
                distractors = set()

                # Nhiễu 1: Đáp án vô cùng (giống bẫy trong ảnh gốc)
                distractors.add(oo) 

                # Nhiễu 2: Quên căn bậc 2 (Lấy hệ số n^2 chia hệ số n) -> (d/2)/a
                fake2 = Rational(d, 2) / a_mau
                if fake2 != ket_qua: distractors.add(fake2)

                # Nhiễu 3: Quên chia 2 trong công thức tổng -> sqrt(d)/a
                fake3 = sqrt(d) / a_mau
                if fake3 != ket_qua: distractors.add(fake3)

                # Nhiễu 4: Lấy ngẫu nhiên một số nguyên
                fake4 = random.randint(1, 5)
                if fake4 != ket_qua: distractors.add(fake4)

                # Chuyển set thành list để xử lý
                list_nhieu = list(distractors)
                while len(list_nhieu) < 3:
                    list_nhieu.append(random.randint(10, 20)) # Bổ sung nếu thiếu

                # Định dạng đáp án LaTeX
                da = '$%s$' % kq_latex
                da_s1 = '$%s$' % latex(list_nhieu[0])
                da_s2 = '$%s$' % latex(list_nhieu[1])
                da_s3 = '$%s$' % latex(list_nhieu[2])

                # 4. Xử lý hiển thị chuỗi (String Formatting) cho Đề bài & Lời giải

                # --- Hiển thị u_n (số hạng cuối) ---
                if const_tu < 0:
                    str_un_display = f"{d}n - {abs(const_tu)}"
                elif const_tu > 0:
                    str_un_display = f"{d}n + {const_tu}"
                else:
                    str_un_display = f"{d}n"

                # --- Hiển thị S_n (Tổng) ---
                # Sn = (d/2)n^2 + ((u1 + const_tu)/2)n
                he_so_n2 = Rational(d, 2)            
                he_so_n1 = Rational(u1 + const_tu, 2) 

                str_Sn = f"{latex(he_so_n2)}n^2"
                if he_so_n1 > 0:
                    str_Sn += f" + {latex(he_so_n1)}n"
                elif he_so_n1 < 0:
                    str_Sn += f" - {latex(abs(he_so_n1))}n"

                # --- Hiển thị biểu thức trong căn khi rút n^2 ---
                str_inside_limit = f"{latex(he_so_n2)}"
                if he_so_n1 > 0:
                    str_inside_limit += f" + \\frac{{{latex(he_so_n1)}}}{{n}}"
                elif he_so_n1 < 0:
                    str_inside_limit += f" - \\frac{{{latex(abs(he_so_n1))}}}{{n}}"

                # 5. Nội dung Đề bài
                noidungcauhoi = (
                    'Tính giới hạn $L = \\lim \\frac{\\sqrt{1 + %s + \\dots + (%s)}}{%sn - %s}$.'
                    % (u2, str_un_display, a_mau, b_mau)
                )

                # 6. Nội dung Lời giải
                loigiai = (
                    "Ta có dãy số ở tử số: $1, %s, \\dots, (%s)$ là một cấp số cộng với số hạng đầu $u_1 = %s$ và công sai $d = %s$. \\\\\n"
                    "Số hạng tổng quát: $u_n = %s$. \\\\\n"
                    "Tổng của $n$ số hạng đầu là: \n"
                    "$$ S_n = \\frac{n(u_1 + u_n)}{2} = \\frac{n[%s + (%s)]}{2} = \\frac{n(%sn %s %s)}{2} = %s $$\n"
                    "Khi đó giới hạn cần tính trở thành:\n"
                    "$$ \\begin{aligned} "
                    "L &= \\lim \\frac{\\sqrt{%s}}{%sn - %s} \\\\"
                    "&= \\lim \\frac{\\sqrt{n^2\\left(%s\\right)}}{n\\left(%s - \\frac{%s}{n}\\right)} \\\\"
                    "&= \\lim \\frac{n\\sqrt{%s}}{n\\left(%s - \\frac{%s}{n}\\right)} \\\\"
                    "&= \\frac{\\sqrt{%s}}{%s} = %s "
                    "\\end{aligned} $$"
                    % (
                        u2, str_un_display, u1, d,                      
                        str_un_display,                                 
                        u1, str_un_display,                             
                        d, "+" if (u1+const_tu)>=0 else "-", abs(u1+const_tu), 
                        str_Sn,                                         
                        str_Sn, a_mau, b_mau,                           
                        str_inside_limit, a_mau, b_mau,                 
                        str_inside_limit, a_mau, b_mau,                 
                        latex(he_so_n2), a_mau, kq_latex                
                    )
                )

                # 7. Trộn đáp án và Tạo chuỗi Content duy nhất
                da_d = '\\True ' + str(da)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tạo chuỗi các lựa chọn (choices)
                str_choices = ""
                for item in list_1:
                    str_choices += '{' + item + '}\n'

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

