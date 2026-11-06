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


def bt_dang46_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random điểm I và các thông số để đảm bảo tọa độ nguyên
                # Chọn I(xI, yI) là số nguyên
                xI = random.randint(1, 4)
                yI = random.randint(1, 4)
                k_line = xI + yI  # Đường thẳng x + y - k = 0 đi qua I

                # Để AID = 90 độ và ABCD là hình thang cân có B, C nguyên:
                # Ta chọn các vector IA = (-a, a) và ID = (-na, -na)
                a = random.randint(1, 2)
                n = random.randint(2, 3) # Tỷ lệ đáy lớn/đáy nhỏ

                # Tọa độ các đỉnh (đảm bảo tính chất hình thang cân và AB // CD)
                xA, yA = xI - a, yI + a
                xB, yB = xI + a, yI + a
                xD, yD = xI - n*a, yI - n*a
                xC, yC = xI + n*a, yI - n*a

                # Tính các bình phương khoảng cách để đưa vào lời giải
                # AD^2 = (xD-xA)^2 + (yD-yA)^2
                AD2 = (xD - xA)**2 + (yD - yA)**2
                AD_val = sqrt(AD2)

                t_sym = symbols('t', real=True)
                # Tọa độ I(t; k - t)
                IA2_expr = (t_sym - xA)**2 + (k_line - t_sym - yA)**2
                ID2_expr = (t_sym - xD)**2 + (k_line - t_sym - yD)**2

                # Nội dung câu hỏi
                noidungcauhoi = ("Trong mặt phẳng với hệ tọa độ $Oxy$, cho hình thang cân $ABCD$ với $AB$ song song $CD$ và $AB < CD$. Biết các đỉnh $A(%s;%s), D(%s;%s)$, giao điểm $I$ của hai đường chéo $AC$ và $BD$ nằm trên đường thẳng $d: x+y-%s=0$ sao cho $\\widehat{AID}=90^\\circ$. Tìm tọa độ điểm $B$ và $C$." 
                                 % (latex(xA), latex(yA), latex(xD), latex(yD), latex(k_line)))

                # Đáp án đúng
                kq_dung = "B(%s;%s), C(%s;%s)" % (latex(xB), latex(yB), latex(xC), latex(yC))

                # Các đáp án nhiễu (số nguyên gần đó)
                s_options = [
                    "B(%s;%s), C(%s;%s)" % (latex(xB+1), latex(yB), latex(xC+1), latex(yC)),
                    "B(%s;%s), C(%s;%s)" % (latex(xB), latex(yB-1), latex(xC), latex(yC-1)),
                    "B(%s;%s), C(%s;%s)" % (latex(yB), latex(xB), latex(yC), latex(xC)),
                    "B(%s;%s), C(%s;%s)" % (latex(xA), latex(yA), latex(xD), latex(yD))
                ]

                random.shuffle(s_options)

                da_d = ('\\True $' + kq_dung + '$')
                da_s1 = '$' + s_options[0] + '$'
                da_s2 = '$' + s_options[1] + '$'
                da_s3 = '$' + s_options[2] + '$'

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải chi tiết (bám sát cấu trúc ảnh mẫu)
                loigiai = ("Do $I \\in d$ nên $I(t; %s-t)$. Ta có $AD = %s$, $IA = \\sqrt{%s}$, $ID = \\sqrt{%s}$. \\\\"
                           "Áp dụng định lý hàm số cô-sin cho tam giác $AID$ ta được: \\\\"
                           "$\\cos \\widehat{AID} = \\frac{IA^2 + ID^2 - AD^2}{2IA.ID}$ \\\\"
                           "$\\Leftrightarrow 0 = \\frac{IA^2 + ID^2 - AD^2}{2IA.ID} \\Leftrightarrow IA^2 + ID^2 - AD^2 = 0$. \\\\"
                           "Thay tọa độ vào ta tìm được $t = %s$, suy ra $I(%s;%s)$. \\\\"
                           "Khi đó $IA = %s$ và $ID = %s$. \\\\"
                           "Vì $ABCD$ là hình thang cân nên $IA = IB = %s$. \\\\"
                           "Do $\\vec{ID}$ và $\\vec{IB}$ ngược hướng nên $\\vec{ID} = -\\frac{ID}{IB}\\vec{IB} = -%s\\vec{IB}$. \\\\"
                           "Từ đó suy ra tọa độ điểm $B(%s;%s)$ và $C(%s;%s)$. \\\\"
                           % (latex(k_line), latex(AD_val), latex(IA2_expr.subs(t_sym, symbols('t'))), 
                              latex(ID2_expr.subs(t_sym, symbols('t'))), latex(xI), latex(xI), latex(yI), 
                              latex(sqrt(IA2_expr.subs(t_sym, xI))), latex(sqrt(ID2_expr.subs(t_sym, xI))),
                              latex(sqrt(IA2_expr.subs(t_sym, xI))), latex(n),
                              latex(xB), latex(yB), latex(xC), latex(yC)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

