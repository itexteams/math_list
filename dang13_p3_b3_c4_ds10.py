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


def bt_dang13_p3_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Bước 1 & 3: Nghiên cứu đề bài và lập logic random
            # Mục tiêu: Tập nghiệm S = (-inf; a] U (b; c]
            # Chọn b = 1/2 cố định (mẫu là 2x - 1)
            # Chọn a < 1/2 và c > 1/2 để cấu trúc tập nghiệm không đổi
            lis_a = [-5, -4, -3, -2, -1] 
            lis_c = [1, 2, 3, 4, 5]
            a_val = random.choice(lis_a)
            c_val = random.choice(lis_c)
            k_val = random.randint(1, 3) # Vế phải là x + k

            # Tính toán các hệ số B, C cho tử số vế trái: x^2 + Bx + C
            # Biểu thức quy đồng: [-x^2 + (B - 2k + 1)x + (C + k)] / (2x - 1) >= 0
            # Để có nghiệm a và c, tử số phải là -(x - a)(x - c) = -x^2 + (a+c)x - ac
            B_val = a_val + c_val + 2*k_val - 1
            C_val = -a_val * c_val - k_val

            # Biểu thức vế trái và vế phải
            tu_vt = x**2 + B_val*x + C_val
            mau_vt = 2*x - 1
            vp = x + k_val
            tu_rut_gon = -x**2 + (a_val + c_val)*x - (a_val * c_val)

            # Tính giá trị biểu thức yêu cầu: T = a + 2b + c (với b = 1/2)
            # T = a + 2*(1/2) + c = a + 1 + c
            kq_val = a_val + 1 + c_val

            # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
            du = [kq_val]
            s = []
            while len(s) < 3:
                nhieu = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4])
                if nhieu not in du and nhieu not in s:
                    s.append(nhieu)

            # Chuyển sang định dạng LaTeX cho các đáp án
            da_dung = '$%s$' % (latex(kq_val))
            da_sai1 = '$%s$' % (latex(s[0]))
            da_sai2 = '$%s$' % (latex(s[1]))
            da_sai3 = '$%s$' % (latex(s[2]))

            # Nội dung câu hỏi
            noidungcauhoi = ('Biết tập nghiệm của bất phương trình $\\frac{%s}{%s} \\ge %s$ là $S=(-\\infty; a] \\cup (b; c]$, giá trị của $a + 2b + c$ bằng bao nhiêu?'
                            % (latex(tu_vt), latex(mau_vt), latex(vp)))

            # Nội dung lời giải với bảng xét dấu tabular
            loigiai = ('Điều kiện: $%s \\neq 0 \\Leftrightarrow x \\neq \\frac{1}{2}$.\\\\\n'
                       '            Ta có: $\\frac{%s}{%s} \\ge %s \\Leftrightarrow \\frac{%s}{%s} - (%s) \\ge 0$ \\\\\n'
                       '            $\\Leftrightarrow \\frac{%s - (%s)(%s)}{%s} \\ge 0 \\Leftrightarrow \\frac{%s}{%s} \\ge 0 \\quad (1)$ \\\\\n'
                       '            Xét dấu vế trái $VT(1)$:\n'
                       '            \\begin{center}\n'
                       '            \\begin{tabular}{|c|lrcrcrcr|}\n'
                       '            \\hline\n'
                       '            $x$ & $-\\infty$ & & $%s$ & & $\\frac{1}{2}$ & & $%s$ & $+\\infty$ \\\\ \\hline\n'
                       '            Tử số & & $-$ & $0$ & $+$ & $|$ & $+$ & $0$ & $-$ \\\\ \\hline\n'
                       '            Mẫu số & & $-$ & $|$ & $-$ & $0$ & $+$ & $|$ & $+$ \\\\ \\hline\n'
                       '            $VT(1)$ & & $+$ & $0$ & $-$ & $||$ & $+$ & $0$ & $-$ \\\\ \\hline\n'
                       '            \\end{tabular}\n'
                       '            \\end{center}\n'
                       '            Từ bảng xét dấu, ta chọn các khoảng mà $VT(1) \\ge 0$, suy ra tập nghiệm:\n'
                       '            $S = (-\\infty; %s] \\cup \\left( \\frac{1}{2}; %s \\right]$. \\\\\n'
                       '            $\\Rightarrow a = %s; b = \\frac{1}{2}; c = %s \\Rightarrow a + 2b + c = %s + 2 \\cdot \\frac{1}{2} + %s = %s$.'
                       % (latex(mau_vt), latex(tu_vt), latex(mau_vt), latex(vp), 
                          latex(tu_vt), latex(mau_vt), latex(vp), 
                          latex(tu_vt), latex(vp), latex(mau_vt), latex(mau_vt), 
                          latex(tu_rut_gon), latex(mau_vt),
                          latex(a_val), latex(c_val),
                          latex(a_val), latex(c_val), 
                          latex(a_val), latex(c_val), latex(a_val), latex(c_val), latex(kq_val)))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

            # Đưa các đáp án vào danh sách và xáo trộn
            da_d = '\\True ' + da_dung
            list_ans = [da_d, da_sai1, da_sai2, da_sai3]
            random.shuffle(list_ans)

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n'
                       '\\end{minipage} \n\n')
            return content

