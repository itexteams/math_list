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


def bt_dang21_p3_b3_c2_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Chọn cạnh a và số lần tô màu k
        a_list = [1, 2, 3, 4, 5, 6]
        a = random.choice(a_list)

        k_list = [10, 20, 30, 40, 50]
        k = random.choice(k_list)

        S1 = a**2

        # Tính toán hệ số (2 * a^2) / 3
        # Rút gọn phân số 2*S1 / 3
        if (2 * S1) % 3 == 0:
            he_so_str = f"{(2 * S1) // 3}"
        else:
            he_so_str = f"\\frac{{{2 * S1}}}{{3}}"

        # Đáp án đúng: hệ số * (1 - (1/4)^k)
        da_str = f"{he_so_str}\\left(1 - \\frac{{1}}{{4^{{{k}}}}}\\right)"
        da = f"${da_str}$"

        # Các phương án nhiễu
        s = [
            f"${he_so_str}\\left(1 - \\frac{{1}}{{2^{{{k}}}}}\\right)$",
            f"${he_so_str}\\left(1 + \\frac{{1}}{{4^{{{k}}}}}\\right)$",
            f"\\frac{{{S1}}}{{3}}\\left(1 - \\frac{{1}}{{4^{{{k}}}}}\\right)$",
            f"\\frac{{{S1}}}{{2}}\\left(1 - \\frac{{1}}{{4^{{{k}}}}}\\right)$",
            f"${he_so_str}\\left(1 - \\frac{{1}}{{4^{{{k - 1}}}}}\\right)$",
            f"${he_so_str}\\left(1 - \\frac{{1}}{{4^{{{k + 1}}}}}\\right)$"
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi (Bao gồm cả code vẽ hình TikZ)
        noidungcauhoi = (r'''Một viên gạch hình vuông $A_1B_1C_1D_1$ có cạnh $A_1B_1 = %s$. Người ta bắt đầu trang trí viên gạch bằng cách tô màu như sau: \\
        1. Nối 4 trung điểm $A_2, B_2, C_2, D_2$ theo thứ tự của 4 cạnh $A_1B_1, B_1C_1, C_1D_1, D_1A_1$ ta được hình vuông thứ hai là $A_2B_2C_2D_2$ và 4 tam giác vuông cân, người ta tô màu 4 tam giác vuông cân này (lần tô thứ nhất). \\
        2. Nối 4 trung điểm $A_3, B_3, C_3, D_3$ theo thứ tự của 4 cạnh $A_2B_2, B_2C_2, C_2D_2, D_2A_2$ ta được hình vuông thứ ba là $A_3B_3C_3D_3$. \\
        3. Nối 4 trung điểm $A_4, B_4, C_4, D_4$ theo thứ tự của 4 cạnh $A_3B_3, B_3C_3, C_3D_3, D_3A_3$ ta được hình vuông thứ tư là $A_4B_4C_4D_4$ và 4 tam giác vuông cân, người ta tô màu 4 tam giác vuông cân này (lần tô thứ hai). \\
        4. Tiếp tục quá trình trên cho đến khi hoàn thành xong lần tô thứ $%s$. (Tham khảo hình vẽ) \\
    \begin{center}
        \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            \draw  [line width=1]  (32.2,96.8) -- (120.2,96.8) -- (120.2,184.8) -- (32.2,184.8) -- cycle ;
            \draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 },fill opacity=1 ][line width=1]  (184.46,96.8) -- (272.46,96.8) -- (272.46,184.8) -- (184.46,184.8) -- cycle ;
            \draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 },fill opacity=1 ][line width=1]  (336.73,96.8) -- (424.73,96.8) -- (424.73,184.8) -- (336.73,184.8) -- cycle ;
            \draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 },fill opacity=1 ][line width=1]  (488.99,96.8) -- (576.99,96.8) -- (576.99,184.8) -- (488.99,184.8) -- cycle ;
            \draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 },fill opacity=1 ][line width=1]  (228.46,96.8) -- (272.46,140.8) -- (228.46,184.8) -- (184.46,140.8) -- cycle ;
            \draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 },fill opacity=1 ][line width=1]  (380.73,96.8) -- (424.73,140.8) -- (380.73,184.8) -- (336.73,140.8) -- cycle ;
            \draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 },fill opacity=1 ][line width=1]  (358.73,118.8) -- (402.73,118.8) -- (402.73,162.8) -- (358.73,162.8) -- cycle ;
            \draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 },fill opacity=1 ][line width=1]  (533.4,97.47) -- (577.4,141.47) -- (533.4,185.47) -- (489.4,141.47) -- cycle ;
            \draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 },fill opacity=1 ][line width=1]  (511.4,119.47) -- (555.4,119.47) -- (555.4,163.47) -- (511.4,163.47) -- cycle ;
            \draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 },fill opacity=1 ][line width=1]  (533.4,119.47) -- (555.4,141.47) -- (533.4,163.47) -- (511.4,141.47) -- cycle ;
        \end{tikzpicture}
    \end{center}
        Tổng diện tích phần được tô màu sau lần tô thứ $%s$ bằng bao nhiêu?'''
                         % (latex(a), latex(k), latex(k)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = (r'''Gọi diện tích các hình vuông $A_1B_1C_1D_1, A_2B_2C_2D_2, \dots, A_mB_mC_mD_m$ lần lượt là $S_1, S_2, \dots, S_m$. \\
        Theo giả thiết, cạnh của hình vuông ban đầu là $a = %s \Rightarrow S_1 = %s^2 = %s$. \\
        Hình vuông thứ hai có diện tích $S_2 = \frac{1}{2}S_1 = \frac{%s}{2}$. \\
        Diện tích phần tô màu ở lần thứ nhất là:
        \[ u_1 = S_1 - S_2 = \frac{%s}{2}. \]
        Tương tự, diện tích hình vuông thứ ba là $S_3 = \frac{1}{2}S_2 = \frac{1}{4}S_1$; diện tích hình vuông thứ tư là $S_4 = \frac{1}{2}S_3 = \frac{1}{8}S_1$. \\
        Diện tích phần tô màu ở lần thứ hai là:
        \[ u_2 = S_3 - S_4 = \frac{1}{4}S_1 - \frac{1}{8}S_1 = \frac{1}{8}S_1 = \frac{1}{4}u_1. \]
        Do đó, diện tích phần tô màu ở mỗi lần lập thành một cấp số nhân có số hạng đầu $u_1 = \frac{%s}{2}$ và công bội $q = \frac{1}{4}$. \\
        Tổng diện tích phần được tô màu sau lần tô thứ $%s$ là tổng của $%s$ số hạng đầu tiên của cấp số nhân trên:
        \[ S_{%s} = u_1 \cdot \frac{1 - q^{%s}}{1 - q} = \frac{\frac{%s}{2}\left(1 - \left(\frac{1}{4}\right)^{%s}\right)}{1 - \frac{1}{4}} = %s \left(1 - \frac{1}{4^{%s}}\right). \]'''
                   % (latex(a), latex(a), latex(S1), latex(S1), latex(S1),
                      latex(S1), latex(k), latex(k), latex(k), latex(k),
                      latex(S1), latex(k), he_so_str, latex(k)))

        dapan = '\\shortans[0]{$%s$}\n' % (da_str)

        # Xuất câu trắc nghiệm 4 phương án
        content = ('\\begin{minipage}{\\textwidth} \n'
                   '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                   '\\loigiai{' + str(loigiai) + '}\n'
                   '\\end{ex}\n \\end{minipage} \n\n')
        return content

