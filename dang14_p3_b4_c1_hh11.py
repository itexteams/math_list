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


def bt_dang14_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random tỷ lệ cạnh AC của tam giác đều EAC: AC = k, BD = 2k (với k in [1, 2, 3, 4])
        # Đề bài gốc: BD = 2*AC = 2 (tương ứng k = 1)
        k = random.choice([1, 2, 3, 4])
        bd = 2 * k
        ac = k

        val_max = Decimal(k**2) * Decimal(math.sqrt(3)) / Decimal(3)
        kq = val_max.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ vẽ đúng 100% như ảnh, nét 1pt, điểm 1pt, màu black
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        % Toa do cac dinh cua hinh chop S.ABCD\n"
            "        \\coordinate (A) at (0.0, 0.0);\n"
            "        \\coordinate (B) at (4.2, 0.0);\n"
            "        \\coordinate (D) at (1.4, 1.6);\n"
            "        \\coordinate (C) at (5.6, 1.6);\n"
            "        \\coordinate (S) at (2.0, 4.8);\n"
            "        \\coordinate (O) at ($(A)!0.5!(C)$);\n"
            "        \\coordinate (E) at ($(S)!0.5!(B)$);\n"
            "        \\coordinate (I) at ($(D)!0.67!(O)$);\n"
            "        \\coordinate (M) at ($(D)!0.67!(A)$);\n"
            "        \\coordinate (N) at ($(D)!0.67!(C)$);\n"
            "        \\coordinate (Q) at ($(E)!0.33!(S)$);\n"
            "        \\coordinate (R) at ($(A)!0.33!(S)$);\n"
            "        \\coordinate (P) at ($(C)!0.33!(S)$);\n"
            "        \\fill[green!45] (M)--(N)--(P)--(Q)--(R)--cycle;\n"
            "        \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S) (S)--(B) (E)--(A) (E)--(C) (M)--(R)--(Q)--(P) (E)--(B);\n"
            "        \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D) (A)--(C) (B)--(D) (O)--(E) (I)--(Q) (M)--(N)--(P) (M)--(I)--(N);\n"
            "        \\fill (S) circle (1pt) node[above] {$S$};\n"
            "        \\fill (A) circle (1pt) node[below left] {$A$};\n"
            "        \\fill (B) circle (1pt) node[below right] {$B$};\n"
            "        \\fill (C) circle (1pt) node[right] {$C$};\n"
            "        \\fill (D) circle (1pt) node[below] {$D$};\n"
            "        \\fill (O) circle (1pt) node[below] {$O$};\n"
            "        \\fill (E) circle (1pt) node[above right] {$E$};\n"
            "        \\fill (I) circle (1pt) node[below] {$I$};\n"
            "        \\fill (M) circle (1pt) node[left] {$M$};\n"
            "        \\fill (N) circle (1pt) node[below] {$N$};\n"
            "        \\fill (P) circle (1pt) node[above right] {$P$};\n"
            "        \\fill (Q) circle (1pt) node[above right] {$Q$};\n"
            "        \\fill (R) circle (1pt) node[left] {$R$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Biểu thức hiển thị theo k
        if k == 1:
            str_sd = "\\sqrt{3}"
            str_rm = "(1-x)\\sqrt{3}"
            str_smnpr = "-\\sqrt{3}x^2 + \\sqrt{3}x"
            str_seac = "\\frac{\\sqrt{3}}{4}"
            str_sqrp = "\\frac{\\sqrt{3}}{4}x^2"
            str_fx = "-\\frac{3\\sqrt{3}}{4}x^2 + \\sqrt{3}x"
            str_gtln = "\\frac{\\sqrt{3}}{3}"
        else:
            str_sd = "%d\\sqrt{3}" % k
            str_rm = "%d\\sqrt{3}(1-x)" % k
            str_smnpr = "-%d\\sqrt{3}x^2 + %d\\sqrt{3}x" % (k**2, k**2)
            str_seac = "\\frac{%d\\sqrt{3}}{4}" % (k**2)
            str_sqrp = "\\frac{%d\\sqrt{3}}{4}x^2" % (k**2)
            str_fx = "-\\frac{%d\\sqrt{3}}{4}x^2 + %d\\sqrt{3}x" % (3 * k**2, k**2)
            str_gtln = "\\frac{%d\\sqrt{3}}{3}" % (k**2)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành tâm $O$, $E$ là trung điểm của $SB$. Biết rằng $\\Delta EAC$ đều, $BD = 2AC = %d$. Lấy $I$ trên đoạn $OD$ với $DI = x$ $(0 < x < %d)$. Gọi $(\\alpha)$ là mặt phẳng qua $I$ và song song với $(ACE)$. Mặt phẳng $(\\alpha)$ cắt $AD, CD, SC, SB, SA$ lần lượt tại $M, N, P, Q, R$. Diện tích lớn nhất của ngũ giác $MNPQR$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm). '''
                         % (bd, k)
                         )

        # Nội dung lời giải
        loigiai = (hinhve+'''Qua $I$ dựng đường thẳng song song với $AC$ cắt $AD, CD$ lần lượt tại $M$ và $N$.\\\\
    Qua $I$ dựng đường thẳng song song với $OE$ cắt $SB$ tại $Q$.\\\\
    Qua $Q$ dựng đường thẳng song song với $AE$ cắt $SA$ tại $R$.\\\\
    Qua $Q$ dựng đường thẳng song song với $EC$ cắt $SC$ tại $P$.\\\\
    Khi đó $(\\alpha) \\equiv (MNPQR)$ và $(MNPQR) // (ACE)$.\\\\
    Ta có: $\\frac{QP}{EC} = \\frac{QR}{AE} = \\frac{RP}{AC} = \\frac{SQ}{SE} = \\frac{SP}{SC}$ nên $\\Delta QRP$ đều.\\\\
    Ta có: $IQ // OE // SD$ nên $\\begin{cases} RM // SD \\\\ PN // SD \\end{cases}$. Mặt khác $\\frac{CN}{CD} = \\frac{AM}{AD}$ nên $RM = PN \\Rightarrow MNPR$ là hình bình hành.\\\\
    Lại có $\\Delta EAC$ đều nên $OE \\perp AC \\Rightarrow PN \\perp MN$. Suy ra $MNPR$ là hình chữ nhật.\\\\
    Tam giác $EAC$ đều có cạnh $AC = %d$ nên $EO = \\frac{%d\\sqrt{3}}{2} \\Rightarrow SD = 2EO = %s$.\\\\
    Ta có: $\\frac{MN}{AC} = \\frac{DI}{DO} = \\frac{x}{%d} \\Rightarrow MN = x$;\\\\
    $\\frac{RM}{SD} = \\frac{AM}{AD} = \\frac{OI}{OD} = 1 - \\frac{x}{%d} \\Rightarrow RM = %s$.\\\\
    Diện tích hình chữ nhật $MNPR$ bằng: $S_{MNPR} = %s$.\\\\
    Diện tích tam giác $EAC$ bằng: $S_{\\Delta EAC} = %s$.\\\\
    Lại có: $\\frac{S_{\\Delta QRP}}{S_{\\Delta EAC}} = \\left(\\frac{QR}{AE}\\right)^2 = \\left(\\frac{DI}{DO}\\right)^2 = \\left(\\frac{x}{%d}\\right)^2 \\Rightarrow S_{\\Delta QRP} = %s$.\\\\
    Do đó diện tích ngũ giác $MNPQR$ bằng:\\\\
    $S(x) = S_{\\Delta QRP} + S_{MNPR} = %s$.\\\\
    Xét hàm số $f(x) = %s$ với $0 < x < %d$.\\\\
    Dễ thấy hàm số đạt GTLN bằng $%s \\approx %s$ tại $x = \\frac{2}{3} \\cdot %d$.\\\\
    Vậy diện tích lớn nhất của ngũ giác $MNPQR$ là $%s$.'''
                   % (k, k, str_sd, k, k, str_rm, str_smnpr, str_seac, k, str_sqrp, str_fx, str_fx, k, str_gtln, kq_str, k, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

