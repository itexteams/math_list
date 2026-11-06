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


def bt_dang48_p1_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập thông số random bài toán
                # Chọn ngẫu nhiên mẫu số (thường gặp 3, 4, 6)
                mau = random.choice([3, 4, 6])

                # Chọn một góc cơ bản đẹp alpha_0 (ở góc phần tư thứ nhất hoặc bất kỳ)
                # Ví dụ mẫu bằng 4, chọn tử bằng 7, ta được 7pi/4
                if mau == 4:
                    tu_goc = random.choice([3, 5, 7])
                elif mau == 3:
                    tu_goc = random.choice([2, 4, 5])
                else:
                    tu_goc = random.choice([5, 7, 11])

                goc_de_bai = Rational(tu_goc, mau) # Hệ số của pi

                # Tính góc cùng điểm cuối bằng cách cộng/trừ k*2*pi (chọn k = -1 hoặc 1 ngẫu nhiên)
                k_chon = random.choice([-1, 1])
                goc_dung = goc_de_bai + k_chon * 2

                # Hàm định dạng phân số pi sang LaTeX đẹp mắt
                def format_latex_pi(f):
                    if f.p == 1:
                        return '\\frac{\\pi}{%s}' % latex(f.q)
                    elif f.p == -1:
                        return '-\\frac{\\pi}{%s}' % latex(f.q)
                    elif f.q == 1:
                        if f.p == 1: return '\\pi'
                        if f.p == -1: return '-\\pi'
                        return '%s\\pi' % latex(f.p)
                    else:
                        if f.p > 0:
                            return '\\frac{%s\\pi}{%s}' % (latex(f.p), latex(f.q))
                        else:
                            return '-\\frac{%s\\pi}{%s}' % (latex(abs(f.p)), latex(f.q))

                str_de_bai = format_latex_pi(goc_de_bai)
                str_dung = format_latex_pi(goc_dung)

                # Đáp án đúng
                da = '$%s$' % str_dung
                da_chon = da

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s = set()
                # Tạo các phương án nhiễu bằng cách lấy các tử số khác xung quanh mẫu số đó
                tu_sai_list = [-tu_goc, tu_goc - 2, tu_goc - 4, tu_goc + 2, 1, -1]
                for ts in tu_sai_list:
                    g_sai = Rational(ts, mau)
                    if g_sai != goc_de_bai and g_sai != goc_dung:
                        s.add('$%s$' % format_latex_pi(g_sai))

                list_sai = list(s)
                # Trích xuất 3 đáp án sai ngẫu nhiên từ tập hợp mẫu nhiễu
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Góc lượng giác nào sau đây có cùng điểm cuối với góc $%s$?''' % str_de_bai)

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Biến đổi biểu diễn toán học cho lời giải chi tiết
                dau_k = '+' if k_chon < 0 else '-'
                k_tri_tuyet = abs(k_chon)

                # Nội dung lời giải chi tiết từng bước theo định nghĩa
                loigiai = ('''Hai góc lượng giác có cùng điểm cuối khi và chỉ khi hiệu số đo của chúng bằng một bội nguyên của $2\\pi$, tức là có dạng $k2\\pi$ với $k \\in \\mathbb{Z}$. \\\\
            Ta có góc lượng giác đề bài cho là: $%s$. \\\\
            Thực hiện biến đổi hiệu số đo giữa góc đề bài và phương án đúng: \\\\
            $%s = %s %s %s \\cdot 2\\pi$. \\\\
            Hiệu số đo là: $\\left(%s\\right) - \\left(%s\\right) = %s \\cdot 2\\pi$ (là một bội nguyên của $2\\pi$). \\\\
            Vậy góc lượng giác có cùng điểm cuối với góc $%s$ là $%s$.'''
                           % (str_de_bai, str_de_bai, str_dung, dau_k, latex(k_tri_tuyet), str_de_bai, str_dung, latex(-k_chon), str_de_bai, str_dung))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

