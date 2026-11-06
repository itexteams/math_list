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


def bt_dang16_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # B3: Random bài toán
        p = random.choice([2, 3, 4, 5])

        # Tính toán các giá trị phân số
        tan_bae = Rational(1, p)
        tan_daf = Rational(p - 1, p + 1)
        ag_as = tan_daf
        ga_gs_rational = Rational(p - 1, 2)

        # Chuyển đổi kết quả cuối cùng sang số thập phân (làm tròn đến hàng phần mười / phần trăm)
        ga_gs_float = float(ga_gs_rational)
        kq_dec = Decimal(str(ga_gs_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq = str(kq_dec).replace('.', ',')

        # B4: Điều chỉnh các phương án sai dưới dạng số thập phân, không trùng với đáp án đúng
        s_set = set()
        offsets = [Decimal('0.2'), Decimal('-0.2'), Decimal('0.3'), Decimal('-0.3'),
                   Decimal('0.4'), Decimal('-0.4'), Decimal('0.5'), Decimal('-0.5'),
                   Decimal('0.6'), Decimal('0.7'), Decimal('0.8'), Decimal('1.0')]
        for off in offsets:
            val = kq_dec + off
            if val > 0 and val != kq_dec:
                s_set.add(str(val).replace('.', ','))

        s = ['$%s$' % v for v in s_set]
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tọa độ tỉ lệ phục vụ vẽ hình TikZ (100% như mẫu ảnh, nét 1pt, điểm 1pt, màu black)
        t_df = round(float(tan_daf), 3)
        t_ag = round(float(ag_as), 3)
        t_be = round(float(tan_bae), 3)

        # B1 & B2: Đề bài
        if p == 2:
            mo_ta_e = 'Gọi $E$ là trung điểm của $BC$'
            giai_thich_e = 'Mà $\\tan \\widehat{BAE} = \\frac{BE}{BA} = \\frac{1}{2}$'
        else:
            mo_ta_e = 'Gọi $E$ là điểm thuộc cạnh $BC$ sao cho $BC = %sBE$' % (p)
            giai_thich_e = 'Mà $\\tan \\widehat{BAE} = \\frac{BE}{BA} = \\frac{1}{%s}$' % (p)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông. %s, $F$ là điểm thuộc cạnh $CD$ sao cho $\\widehat{EAF} = 45^\\circ$ và $G$ thuộc cạnh $SA$. Biết $FG$ song song với mặt phẳng $(SBC)$. Khi đó tỉ số $\\frac{GA}{GS}$ bằng'''
                         % (mo_ta_e))

        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (D) at (0,0);
        \\coordinate (A) at (1.8,1.8);
        \\coordinate (C) at (4.5,0);
        \\coordinate (B) at ($(A)+(C)-(D)$);
        \\coordinate (S) at (0.4,4.5);
        \\coordinate (E) at ($(B)!''' + str(1 - t_be) + '''!(C)$);
        \\coordinate (F) at ($(D)!''' + str(t_df) + '''!(C)$);
        \\coordinate (H) at (intersection of A--F and B--C);
        \\coordinate (G) at ($(A)!''' + str(t_ag) + '''!(S)$);
        \\draw[line width=1pt] (S)--(D)--(F) (C)--(B)--(S)--(C) (S)--(H)--(C);
        \\draw[line width=1pt, dashed] (D)--(A)--(B) (F)--(C) (S)--(A) (A)--(E) (A)--(F)--(H) (F)--(G);
        \\fill (S) circle (1pt) node[above left] {$S$};
        \\fill (D) circle (1pt) node[below left] {$D$};
        \\fill (A) circle (1pt) node[above right] {$A$};
        \\fill (B) circle (1pt) node[right] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (E) circle (1pt) node[below right] {$E$};
        \\fill (F) circle (1pt) node[below] {$F$};
        \\fill (G) circle (1pt) node[above right] {$G$};
        \\fill (H) circle (1pt) node[left] {$H$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    Ta có: $\\widehat{BAE} + \\widehat{EAF} + \\widehat{DAF} = 90^\\circ$ \\\\
    $\\Rightarrow \\widehat{BAE} + \\widehat{DAF} = 45^\\circ$ \\\\
    $\\Rightarrow \\tan(\\widehat{BAE} + \\widehat{DAF}) = 1$ \\\\
    $\\Rightarrow \\frac{\\tan \\widehat{BAE} + \\tan \\widehat{DAF}}{1 - \\tan \\widehat{BAE} \\cdot \\tan \\widehat{DAF}} = 1$ \\\\
    %s \\\\
    Nên $\\tan \\widehat{DAF} = %s \\Rightarrow \\frac{DF}{DA} = %s \\Rightarrow DF = %s DA = %s DC$. \\\\
    Gọi $H$ là giao điểm của $AF$ và $BC$ trong mặt phẳng $(ABCD)$. \\\\
    Ta có: \\\\
    $\\begin{cases} GF \\subset (SAH) \\\\ GF // (SBC) \\\\ (SAH) \\cap (SBC) = SH \\end{cases} \\Rightarrow GF // SH$ \\\\
    $\\Rightarrow \\frac{AG}{AS} = \\frac{AF}{AH}$. \\\\
    Mà $\\frac{AF}{AH} = \\frac{DF}{DC} = %s$. \\\\
    Nên $\\frac{AG}{AS} = %s \\Rightarrow \\frac{GA}{GS} = %s = %s$.'''
                   % (tikz_code,
                      giai_thich_e,
                      latex(tan_daf), latex(tan_daf), latex(tan_daf), latex(tan_daf),
                      latex(tan_daf),
                      latex(ag_as), latex(ga_gs_rational), kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

