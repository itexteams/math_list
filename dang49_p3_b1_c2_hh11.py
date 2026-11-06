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


def bt_dang49_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số của SA, SB, SC (SA = m*a, SB = n*a, SC = p*a)
                # Để bài toán đẹp, ta chọn các số nguyên nhỏ
                m = random.randint(1, 2)
                n = random.randint(2, 4)
                p = random.randint(3, 5)
                while n == m: n = random.randint(2, 4)
                while p == n or p == m: p = random.randint(3, 5)

                # Các góc cố định để giữ logic lời giải như hình: ASB = BSC = 60, CSA = 90
                cos60 = Rational(1, 2)
                cos90 = 0

                # Tính độ dài BC: BC^2 = SB^2 + SC^2 - 2*SB*SC*cos(BSC)
                # BC = a * sqrt(n^2 + p^2 - 2*n*p*cos60)
                bc_sq_coeff = n**2 + p**2 - 2*n*p*cos60
                bc_val_latex = "a\\sqrt{%s}" % latex(bc_sq_coeff) if not sqrt(bc_sq_coeff).is_integer else "%sa" % latex(sqrt(bc_sq_coeff))

                # Tính tích vô hướng SA.BC = SA.(SC - SB) = SA.SC - SA.SB
                # SA.SC = SA*SC*cos90 = 0
                # SA.SB = SA*SB*cos60 = m*n*a^2 * (1/2)
                sa_dot_sb_coeff = Rational(m * n, 2)
                numerator_coeff = abs(0 - sa_dot_sb_coeff)

                # cos(alpha) = |SA.BC| / (SA * BC)
                # cos(alpha) = (numerator_coeff * a^2) / (m * a * a * sqrt(bc_sq_coeff))
                # cos(alpha) = numerator_coeff / (m * sqrt(bc_sq_coeff))
                final_cos = numerator_coeff / (m * sqrt(bc_sq_coeff))

                # Rút gọn và hiển thị LaTeX
                da_dung = "$ \\cos \\alpha = %s $" % latex(final_cos)

                # Tạo đáp án nhiễu
                s = [
                    "$ \\cos \\alpha = %s $" % latex(final_cos * Rational(1, 2)),
                    "$ \\cos \\alpha = %s $" % latex(Rational(1, 2)),
                    "$ \\cos \\alpha = 0 $",
                    "$ \\cos \\alpha = %s $" % latex(final_cos / 2 + Rational(1, 3)),
                    "$ \\cos \\alpha = %s $" % latex(sqrt(bc_sq_coeff) / (m*n*p) if m*n*p != 0 else 1)
                ]

                # Loại bỏ nếu trùng đáp án đúng
                s = [item for item in s if item != da_dung]
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $SA = %sa$, $SB = %sa$, $SC = %sa$, $\\widehat{ASB} = \\widehat{BSC} = 60^\\circ$, $\\widehat{CSA} = 90^\\circ$. Gọi $\\alpha$ là góc giữa hai đường thẳng $SA$ và $BC$. Giá trị $\\cos \\alpha$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % ('' if m == 1 else latex(m), latex(n), latex(p)))

                # Hình vẽ TikZ
                hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
                \coordinate (S) at (0,3);
                \coordinate (A) at (-1.5,0.5);
                \coordinate (B) at (0.5,-1);
                \coordinate (C) at (3,0);
                \draw (S)--(A)--(B)--(C)--cycle;
                \draw (S)--(B);
                \draw [dashed] (A)--(C);
                \foreach \p/\pos in {S/above, A/left, B/below, C/right} \fill (\p) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}'''

                # Nội dung lời giải
                h1=final_cos
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                loigiai = ('''Ta có $\\cos \\alpha = |\\cos(\\vec{SA}, \\vec{BC})| = \\frac{|\\vec{SA} \\cdot \\vec{BC}|}{SA \\cdot BC}$. \\\\
                             Xét tích vô hướng: $\\vec{SA} \\cdot \\vec{BC} = \\vec{SA} \\cdot (\\vec{SC} - \\vec{SB}) = \\vec{SA} \\cdot \\vec{SC} - \\vec{SA} \\cdot \\vec{SB}$. \\\\
                             Trong đó: \\\\
                             $\\vec{SA} \\cdot \\vec{SC} = SA \\cdot SC \\cdot \\cos 90^\\circ = %sa \\cdot %sa \\cdot 0 = 0$. \\\\
                             $\\vec{SA} \\cdot \\vec{SB} = SA \\cdot SB \\cdot \\cos 60^\\circ = %sa \\cdot %sa \\cdot \\frac{1}{2} = %sa^2$. \\\\
                             Suy ra $|\\vec{SA} \\cdot \\vec{BC}| = |0 - %sa^2| = %sa^2$. \\\\
                             Độ dài cạnh $BC$: \\\\
                             $BC = \\sqrt{SB^2 + SC^2 - 2SB \\cdot SC \\cdot \\cos 60^\\circ} = \\sqrt{(%sa)^2 + (%sa)^2 - 2 \\cdot %sa \\cdot %sa \\cdot \\frac{1}{2}} = %s$. \\\\
                             Vậy $\\cos \\alpha = \\frac{%sa^2}{%sa \\cdot %s} = %s \\approx %s$.'''
                           % (latex(m), latex(p), latex(m), latex(n), latex(sa_dot_sb_coeff), 
                              latex(sa_dot_sb_coeff), latex(sa_dot_sb_coeff),
                              latex(n), latex(p), latex(n), latex(p), bc_val_latex,
                              latex(sa_dot_sb_coeff), latex(m), bc_val_latex, latex(final_cos),str(kqz)
                             ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.',','))

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + str(da_dung)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'  + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

