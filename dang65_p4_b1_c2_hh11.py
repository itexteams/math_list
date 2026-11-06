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


def bt_dang65_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Bước 1: Khai báo các thiết lập và chọn dạng toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 2 & 3: Thiết lập các biến số ngẫu nhiên
                # AB = CD = k*a. MN = m*a
                # Trong đề bài gốc: k = 2, m = sqrt(3)

                # Tạo các bộ dữ liệu đẹp (AB, MN, Kết quả góc)
                data_sets = [
                    {'k': 2, 'm_expr': sqrt(3), 'm_latex': r'\sqrt{3}', 'ans': 60},
                    {'k': 2, 'm_expr': sqrt(2), 'm_latex': r'\sqrt{2}', 'ans': 90},
                    {'k': 2, 'm_expr': 1, 'm_latex': '1', 'ans': 60},
                    {'k': 4, 'm_expr': 2*sqrt(3), 'm_latex': r'2\sqrt{3}', 'ans': 60},
                ]

                selected = random.choice(data_sets)
                k = selected['k']
                m_expr = selected['m_expr']
                m_latex = selected['m_latex']
                goc_kq = selected['ans']

                # Tính toán các bước cho lời giải
                # PM = CD/2 = k/2, PN = AB/2 = k/2
                pm_pn_val = k // 2
                # cos(MPN) = (PM^2 + PN^2 - MN^2) / (2*PM*PN)
                cos_val = (pm_pn_val**2 + pm_pn_val**2 - m_expr**2) / (2 * pm_pn_val * pm_pn_val)

                # Chuyển cos_val sang độ
                import math
                try:
                    angle_rad = math.acos(float(cos_val))
                    angle_deg = round(math.degrees(angle_rad))
                except:
                    angle_deg = 120 # Mặc định cho trường hợp mẫu gốc

                # Bước 4: Điều chỉnh các phương án sai
                choices_list = [30, 45, 60, 90]
                if goc_kq in choices_list:
                    choices_list.remove(goc_kq)
                random.shuffle(choices_list)

                da_d = r'\True $' + str(goc_kq) + r'^\circ$'
                da_s1 = '$' + str(choices_list[0]) + r'^\circ$'
                da_s2 = '$' + str(choices_list[1]) + r'^\circ$'
                da_s3 = '$' + str(choices_list[2]) + r'^\circ$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Cho tứ diện $ABCD$ có $AB = CD = ' + str(k) + 'a$. Gọi $M, N$ lần lượt là trung điểm $AD$ và $BC$. '
                    'Biết $MN = a' + m_latex + '$. Tính góc giữa hai đường thẳng $AB$ và $CD$.'
                )

                # Hình vẽ TikZ
                tikz_code = r'''\begin{center}
                \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (0,1);
                \coordinate (C) at (0.5,-1);
                \coordinate (D) at (4,0);
                \coordinate (B) at (1.2,3.5);
                \coordinate (M) at ($(A)!0.5!(D)$);
                \coordinate (N) at ($(B)!0.5!(C)$);
                \coordinate (P) at ($(A)!0.5!(C)$);
                \draw (B)--(A)--(C)--(D)--(B)--(C) (P)--(N);
                \draw[dashed] (A)--(D) (M)--(N) (P)--(M);
                \draw (B)--(D);
                \foreach \p/\pos in {A/left, B/above, C/below, D/right, M/above, N/right, P/left}
                    \fill (\p) node[\pos] {$\p$};
                \end{tikzpicture}
                \end{center}'''

                # Nội dung lời giải chi tiết
                # Xử lý hiển thị phân số cho cos
                tu = pm_pn_val**2 + pm_pn_val**2
                mau = 2 * pm_pn_val * pm_pn_val
                cos_text = r'\frac{' + str(pm_pn_val) + '^2 + ' + str(pm_pn_val) + '^2 - (' + m_latex + ')^2}{2 \\cdot ' + str(pm_pn_val) + ' \\cdot ' + str(pm_pn_val) + '}'

                # Tính góc thực tế của tam giác MPN
                loigiai = (
                    'Gọi $P$ là trung điểm $AC$, ta có $PM // CD$ và $PN // AB$, suy ra $(AB, CD) = (PM, PN)$. \\\\'
                    'Dễ thấy $PM = \\frac{CD}{2} = ' + str(pm_pn_val) + 'a$ và $PN = \\frac{AB}{2} = ' + str(pm_pn_val) + 'a$. \\\\'
                    'Xét $\\Delta PMN$ ta có $\\cos \\widehat{MPN} = ' + cos_text + ' = ' + str(sp.nsimplify(cos_val)) + '$. \\\\'
                    '$\\Rightarrow \\widehat{MPN} = ' + str(angle_deg) + r'^\circ$. \\\\'
                    'Vì góc giữa hai đường thẳng luôn $\\le 90^\\circ$, nên $(AB, CD) = ' + (str(angle_deg) if angle_deg <= 90 else str(180-angle_deg)) + r'^\circ$.'
                       )

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n').replace('a1$','a$')
            return content

