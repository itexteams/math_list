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


def bt_dang5_p3_b4_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random kích thước (từ 5.0 đến 12.0)
                h_val = random.randint(50, 120) / 10.0
                a_val = random.randint(50, 120) / 10.0
                b_val = random.randint(50, 120) / 10.0

                # Tính toán
                # a_val tương ứng A'B' (cạnh D'C'), b_val tương ứng A'D' (cạnh B'C'), h_val tương ứng AA' (chiều cao)
                ah_val = (a_val * b_val) / math.sqrt(a_val**2 + b_val**2)
                tan_alpha = h_val / ah_val
                alpha_rad = math.atan(tan_alpha)
                alpha_deg = math.degrees(alpha_rad)

                kq = round(alpha_deg, 1)

                # Các đáp án trắc nghiệm
                da = str(kq).replace('.', ',') + '^\\circ'

                # Tạo các phương án nhiễu sai khác nhau
                s_set = set()
                while len(s_set) < 3:
                    offset = random.choice([1.5, -1.5, 2.3, -2.3, 3.1, -3.1, 4.5, -4.5, 5.2, -5.2])
                    dist_val = round(alpha_deg + offset, 1)
                    if dist_val > 0 and dist_val != kq:
                        s_set.add(str(dist_val).replace('.', ',') + '^\\circ')

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Format chuỗi hiển thị số
                h_str = str(h_val).replace('.', ',')
                a_str = str(a_val).replace('.', ',')
                b_str = str(b_val).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''Một hộp phấn không bụi có dạng hình hộp chữ nhật, chiều cao hộp phấn bằng $%s$ cm và đáy của nó có hai kích thước là $%s$ cm; $%s$ cm (xem hình vẽ). Tìm số đo góc phẳng nhị diện $[A, B'D', A']$ (Tính theo đơn vị độ và làm tròn kết quả đến hàng phần chục).
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=0.8]
            \\coordinate (Dp) at (0,0);
            \\coordinate (Cp) at (5,0);
            \\coordinate (Bp) at (7,1.5);
            \\coordinate (Ap) at (2,1.5);
            \\coordinate (D) at (0,3);
            \\coordinate (C) at (5,3);
            \\coordinate (B) at (7,4.5);
            \\coordinate (A) at (2,4.5);
            \\draw (D) -- (C) -- (B) -- (A) -- cycle;
            \\draw (Dp) -- (Cp) -- (Bp);
            \\draw (D) -- (Dp);
            \\draw (C) -- (Cp);
            \\draw (B) -- (Bp);
            \\draw[dashed] (A) -- (Ap);
            \\draw[dashed] (Ap) -- (Dp);
            \\draw[dashed] (Ap) -- (Bp);
            \\node[above] at (A) {$A$};
            \\node[above right] at (B) {$B$};
            \\node[above right] at (C) {$C$};
            \\node[above left] at (D) {$D$};
            \\node[below] at (Dp) {$D'$};
            \\node[below] at (Cp) {$C'$};
            \\node[right] at (Bp) {$B'$};
            \\node[above right] at (Ap) {$A'$};
            \\node[left] at (0, 1.5) {$%s$ cm};
            \\node[below] at (2.5, 0) {$%s$ cm};
            \\node[below right] at (6, 0.75) {$%s$ cm};
            \\end{tikzpicture}
            \\end{center}''' % (h_str, a_str, b_str, h_str, a_str, b_str))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải
                ah_str = str(round(ah_val, 2)).replace('.', ',')
                tan_str = str(round(tan_alpha, 2)).replace('.', ',')

                loigiai = ('''Trong mặt phẳng $(A'B'C'D')$, kẻ $A'H \\perp B'D'$ tại $H$. \\\\
            Ta có: $\\begin{cases} B'D' \\perp A'H \\\\ B'D' \\perp AA' \\text{ (do } AA' \\perp (A'B'C'D')) \\end{cases} \\Rightarrow B'D' \\perp (AA'H) \\Rightarrow B'D' \\perp AH$ \\\\
            Do đó $\\widehat{AHA'}$ là góc phẳng nhị diện $[A, B'D', A']$. \\\\
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=0.8]
            \\coordinate (Dp) at (0,0);
            \\coordinate (Cp) at (5,0);
            \\coordinate (Bp) at (7,1.5);
            \\coordinate (Ap) at (2,1.5);
            \\coordinate (D) at (0,3);
            \\coordinate (C) at (5,3);
            \\coordinate (B) at (7,4.5);
            \\coordinate (A) at (2,4.5);
            \\coordinate (H) at (2.5, 0.55);
            \\draw (D) -- (C) -- (B) -- (A) -- cycle;
            \\draw (Dp) -- (Cp) -- (Bp);
            \\draw (D) -- (Dp);
            \\draw (C) -- (Cp);
            \\draw (B) -- (Bp);
            \\draw[dashed] (A) -- (Ap);
            \\draw[dashed] (Ap) -- (Dp);
            \\draw[dashed] (Ap) -- (Bp);
            \\draw[dashed] (Dp) -- (Bp);
            \\draw[dashed] (A) -- (H);
            \\draw[dashed] (Ap) -- (H);
            \\node[above] at (A) {$A$};
            \\node[above right] at (B) {$B$};
            \\node[above right] at (C) {$C$};
            \\node[above left] at (D) {$D$};
            \\node[below] at (Dp) {$D'$};
            \\node[below] at (Cp) {$C'$};
            \\node[right] at (Bp) {$B'$};
            \\node[above left] at (Ap) {$A'$};
            \\node[below right] at (H) {$H$};
            \\node[left] at (0, 1.5) {$%s$ cm};
            \\node[below] at (2.5, 0) {$%s$ cm};
            \\node[below right] at (6, 0.75) {$%s$ cm};
            \\end{tikzpicture}
            \\end{center}
            Tam giác $A'B'D'$ vuông tại $A'$ có đường cao $A'H$ nên ta có: \\\\
            $\\frac{1}{A'H^2} = \\frac{1}{A'B'^2} + \\frac{1}{A'D'^2} \\Rightarrow A'H = \\frac{A'B' \\cdot A'D'}{\\sqrt{A'B'^2 + A'D'^2}} = \\frac{%s \\cdot %s}{\\sqrt{%s^2 + %s^2}} \\approx %s$ \\\\
            Tam giác $AHA'$ vuông tại $A'$ có $\\tan \\widehat{AHA'} = \\frac{AA'}{A'H} \\approx \\frac{%s}{%s} \\approx %s \\Rightarrow \\widehat{AHA'} \\approx %s^{\\circ}$.'''
                % (h_str, a_str, b_str, a_str, b_str, a_str, b_str, ah_str, h_str, ah_str, tan_str, str(kq).replace('.', ',')))
                dapan='\\shortans[0]{$%s$}\n'%(str(kq).replace('.', ','))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

