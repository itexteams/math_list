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


def bt_dang45_p4_b6_c2_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Cho tứ diện đều cạnh a
        # Random độ dài cạnh a (mặc định a = 1, có thể chọn a nguyên từ 1 đến 3)
        a_val = random.choice([1, 2, 3])


        he_so = Rational(11, 216) * (a_val**3)
        he_so_str = latex(he_so)

        if a_val == 1:
            str_canh = '1'
            da = '$V = \\frac{11\\sqrt{2}}{216}$'
            s = [
                '$V = \\frac{\\sqrt{2}}{108}$',
                '$V = \\frac{7\\sqrt{2}}{216}$',
                '$V = \\frac{\\sqrt{2}}{18}$',
                '$V = \\frac{13\\sqrt{2}}{216}$',
                '$V = \\frac{5\\sqrt{2}}{72}$',
                '$V = \\frac{\\sqrt{2}}{72}$'
            ]
        else:
            str_canh = str(a_val)
            tu = 11 * (a_val**3)
            g = math.gcd(tu, 216)
            tu_rut = tu // g
            mau_rut = 216 // g
            if tu_rut == 1:
                da = '$V = \\frac{\\sqrt{2}}{%s}$' % (mau_rut)
            else:
                da = '$V = \\frac{%s\\sqrt{2}}{%s}$' % (tu_rut, mau_rut)

            s = [
                '$V = \\frac{\\sqrt{2}}{%s}$' % (108 // math.gcd(a_val**3, 108)),
                '$V = \\frac{7\\sqrt{2}}{%s}$' % (216 // math.gcd(7 * a_val**3, 216)),
                '$V = \\frac{\\sqrt{2}}{%s}$' % (18 // math.gcd(a_val**3, 18)),
                '$V = \\frac{13\\sqrt{2}}{%s}$' % (216 // math.gcd(13 * a_val**3, 216)),
                '$V = \\frac{5\\sqrt{2}}{%s}$' % (72 // math.gcd(5 * a_val**3, 72))
            ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện đều $ABCD$ có cạnh bằng $%s$. Gọi $M$ là trung điểm của cạnh $AB$; điểm $N$ nằm trên cạnh $CD$ sao cho $NC = 2ND$. Mặt phẳng $(P)$ chứa $MN$ và song song với $AC$ chia khối tứ diện $ABCD$ thành hai khối đa diện, trong đó khối đa diện chứa đỉnh $A$ có thể tích là $V$. Tính $V$.'''
                         % (str_canh))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # TikZ hình vẽ
        hinhve = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (D) at (5,0);
        \\coordinate (C) at (1.8,-1.8);
        \\coordinate (A) at (2.2,3.8);
        \\coordinate (M) at ($(A)!0.5!(B)$);
        \\coordinate (N) at ($(D)!0.333!(C)$);
        \\coordinate (Q) at ($(B)!0.5!(C)$);
        \\coordinate (P) at ($(A)!0.667!(D)$);
        \\draw[line width=1pt] (A)--(B) (A)--(C) (A)--(D) (P)--(N) (B)--(C) (C)--(D) (M)--(Q);
        \\draw[line width=1pt, dashed] (B)--(D) (M)--(P) (Q)--(N);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (M) circle (1pt) node[above left] {$M$};
        \\fill (N) circle (1pt) node[below right] {$N$};
        \\fill (P) circle (1pt) node[above right] {$P$};
        \\fill (Q) circle (1pt) node[below left] {$Q$};
    \\end{tikzpicture}
    \\end{center}'''

        # Nội dung lời giải
        loigiai = ('''%s
    Trong mặt phẳng $(ABC)$, qua $M$ kẻ đường thẳng song song với $AC$ cắt $BC$ tại $Q$.\\\\
    Vì $M$ là trung điểm của $AB$ nên $Q$ là trung điểm của $BC$ và $MQ // AC$.\\\\
    Trong mặt phẳng $(ACD)$, qua $N$ kẻ đường thẳng song song với $AC$ cắt $AD$ tại $P$.\\\\
    Theo định lí Thales, ta có $\\frac{DP}{DA} = \\frac{DN}{DC} = \\frac{1}{3} \\Rightarrow \\frac{AP}{AD} = \\frac{2}{3}$ và $PN // AC$.\\\\
    Do đó, thiết diện của tứ diện $ABCD$ cắt bởi mặt phẳng $(P)$ là hình thang $MNPQ$ ($MQ // PN // AC$).\\\\
    Mặt phẳng $(P)$ chia khối tứ diện thành hai khối đa diện: khối không chứa $A$ (chứa các đỉnh $B, D$) và khối chứa đỉnh $A$.\\\\
    Thể tích của tứ diện đều $ABCD$ cạnh $%s$ là:
    $$V_{ABCD} = \\frac{(%s)^3\\sqrt{2}}{12}$$
    Ta phân chia khối đa diện không chứa đỉnh $A$ thành hai khối chóp $B.MNQ$ và $D.MNP$ (hoặc dùng tỉ số thể tích):
    Kẻ $BN$ cắt mặt phẳng chứa thiết diện, ta tính được tỉ số thể tích của khối đa diện chứa đỉnh $A$ là $\\frac{V}{V_{ABCD}} = \\frac{11}{18}$.\\\\
    Do đó thể tích khối đa diện chứa đỉnh $A$ là:
    $$V = \\frac{11}{18} V_{ABCD} = %s$$'''
                   % (hinhve, str_canh, str_canh, str(da).replace('$', '')))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[0]) + '}\n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

