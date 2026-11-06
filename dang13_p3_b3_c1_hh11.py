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


def bt_dang13_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        cases = [
            (2, 3, 3, 'G là trọng tâm của tam giác $SAB$'),
            (3, 4, 2, 'G là điểm trên đoạn $SE$ (với $E$ là trung điểm của $AB$) thỏa mãn $SG = \\frac{3}{4}SE$'),
            (3, 5, 5, 'G là điểm trên đoạn $SE$ (với $E$ là trung điểm của $AB$) thỏa mãn $SG = \\frac{3}{5}SE$'),
            (4, 7, 7, 'G là điểm trên đoạn $SE$ (với $E$ là trung điểm của $AB$) thỏa mãn $SG = \\frac{4}{7}SE$'),
        ]
        u, v, k, mo_ta_g = random.choice(cases)

        # Đáp án đúng
        kq = k
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        candidate_vals = [k + 1, k + 2, k + 3, k - 1 if k > 1 else k + 4, k - 2 if k > 2 else k + 5]
        for val in candidate_vals:
            if val != k and val > 0:
                s_set.add(str(val))

        s = ['$%s$' % v for v in s_set]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # B1 & B2: Đề bài
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với các cạnh đáy là $AB$ và $CD$. Gọi $I, J$ lần lượt là trung điểm của các cạnh $AD$ và $BC$ và %s. Khi $AB = k \\cdot CD, k \\in \\mathbb{N}^*$ thì tứ giác tạo bởi các giao tuyến của $(IJG)$ với các mặt của hình chóp là một hình bình hành. Giá trị của $k$ bằng bao nhiêu?'''
                         % (mo_ta_g))

        # Tọa độ tỉ lệ phục vụ vẽ hình TikZ (100% như mẫu ảnh, nét 1pt, điểm 1pt, màu black)
        t_mn = round(u / v, 2)

        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (6,0);
        \\coordinate (D) at (1.4,-1.8);
        \\coordinate (C) at (3.8,-1.8);
        \\coordinate (S) at (3,3.6);
        \\coordinate (E) at ($(A)!0.5!(B)$);
        \\coordinate (G) at ($(S)!''' + str(t_mn) + '''!(E)$);
        \\coordinate (M) at ($(S)!''' + str(t_mn) + '''!(A)$);
        \\coordinate (N) at ($(S)!''' + str(t_mn) + '''!(B)$);
        \\coordinate (I) at ($(A)!0.5!(D)$);
        \\coordinate (J) at ($(B)!0.5!(C)$);
        \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (S)--(B) (A)--(D)--(C)--(B) (M)--(I) (N)--(J);
        \\draw[line width=1pt, dashed] (A)--(B) (S)--(E) (I)--(J) (M)--(N) (I)--(G)--(J);
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[right] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[below] {$D$};
        \\fill (E) circle (1pt) node[below] {$E$};
        \\fill (G) circle (1pt) node[left] {$G$};
        \\fill (M) circle (1pt) node[left] {$M$};
        \\fill (N) circle (1pt) node[right] {$N$};
        \\fill (I) circle (1pt) node[left] {$I$};
        \\fill (J) circle (1pt) node[right] {$J$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        if u == 2 and v == 3:
            giai_thich_mn = 'Do $G$ là trọng tâm tam giác $SAB$ và $MN // AB$ nên $\\frac{MN}{AB} = \\frac{SG}{SE} = \\frac{2}{3}$ \\\\ ($E$ là trung điểm của $AB$) $\\Rightarrow MN = \\frac{2}{3}AB$.'
        else:
            giai_thich_mn = 'Do $\\frac{SG}{SE} = \\frac{%s}{%s}$ và $MN // AB$ nên $\\frac{MN}{AB} = \\frac{SG}{SE} = \\frac{%s}{%s}$ \\\\ ($E$ là trung điểm của $AB$) $\\Rightarrow MN = \\frac{%s}{%s}AB$.' % (u, v, u, v, u, v)

        loigiai = ('''%s
    Ta có $ABCD$ là hình thang và $I, J$ là trung điểm của $AD, BC$ nên $IJ // AB$. \\\\
    Vậy $\\begin{cases} G \\in (SAB) \\cap (IJG) \\\\ AB \\subset (SAB) \\\\ IJ \\subset (IJG) \\\\ AB // IJ \\end{cases} \\Rightarrow (SAB) \\cap (IJG) = MN // IJ // AB$ với $M \\in SA, N \\in SB$. \\\\
    Dễ thấy hình đa giác tạo bởi các giao tuyến của $(IJG)$ với các mặt của hình chóp là tứ giác $MNJI$. \\\\
    %s \\\\
    Lại có $IJ = \\frac{1}{2}(AB + CD)$. Vì $MN // IJ$ nên $MNIJ$ là hình thang, do đó $MNIJ$ là hình bình hành khi $MN = IJ$ \\\\
    $\\Leftrightarrow \\frac{%s}{%s} AB = \\frac{1}{2}(AB + CD) \\Leftrightarrow AB = %s CD$. \\\\
    Vậy thiết diện là hình bình hành khi $AB = %s CD$. Suy ra $k = %s$.'''
                   % (tikz_code,
                      giai_thich_mn,
                      latex(u), latex(v),
                      latex(k),
                      latex(k),
                      latex(kq)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

