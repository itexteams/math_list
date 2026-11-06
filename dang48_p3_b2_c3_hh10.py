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


def bt_dang48_p3_b2_c3_hh10(self):
    # Khai báo biến và chọn dạng
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # 1. Sinh ngẫu nhiên các thông số hình học Oxy
        xD = randint(-3, 3)
        yD = randint(-3, 3)

        # Vectơ pháp tuyến của MH: n_MH = (u, v)
        u = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        v = random.choice([-3, -2, -1, 1, 2, 3])
        c1 = randint(-10, 10)

        # AD vuông góc MH => VTPT của AD là (v, -u)
        c_AD = -v * xD + u * yD

        # Tạo điểm A(xA, yA) nguyên thuộc AD
        k_step = randint(-3, 3)
        xA = xD + u * k_step
        yA = yD + v * k_step

        # Đường thẳng d chứa A: a_d * x + b_d * y + c_d = 0
        a_d = randint(-3, 3)
        b_d = randint(-3, 3)
        while a_d * (-u) - b_d * v == 0 or (a_d == 0 and b_d == 0):
            a_d = randint(-3, 3)
            b_d = randint(-3, 3)
        c_d = -(a_d * xA + b_d * yA)

        ans_val = 2 * xA - yA

        # 2. Định dạng chuỗi phương trình các đường thẳng
        # Đường thẳng MH: u*x + v*y + c1 = 0
        pt_MH = ""
        if u == 1:
            pt_MH += "x"
        elif u == -1:
            pt_MH += "-x"
        else:
            pt_MH += "%d x" % u

        if v > 0:
            pt_MH += " + " + ("y" if v == 1 else "%d y" % v)
        else:
            pt_MH += " - " + ("y" if v == -1 else "%d y" % (-v))

        if c1 > 0:
            pt_MH += " + %d = 0" % c1
        elif c1 < 0:
            pt_MH += " - %d = 0" % (-c1)
        else:
            pt_MH += " = 0"

        # Đường thẳng d: a_d*x + b_d*y + c_d = 0
        pt_d = ""
        if a_d == 1:
            pt_d += "x"
        elif a_d == -1:
            pt_d += "-x"
        else:
            pt_d += "%d x" % a_d

        if b_d > 0:
            pt_d += " + " + ("y" if b_d == 1 else "%d y" % b_d)
        else:
            pt_d += " - " + ("y" if b_d == -1 else "%d y" % (-b_d))

        if c_d > 0:
            pt_d += " + %d = 0" % c_d
        elif c_d < 0:
            pt_d += " - %d = 0" % (-c_d)
        else:
            pt_d += " = 0"

        # Đường thẳng AD: v*x - u*y + c_AD = 0
        pt_AD = ""
        if v == 1:
            pt_AD += "x"
        elif v == -1:
            pt_AD += "-x"
        else:
            pt_AD += "%d x" % v

        if -u > 0:
            pt_AD += " + " + ("y" if -u == 1 else "%d y" % (-u))
        else:
            pt_AD += " - " + ("y" if -u == -1 else "%d y" % u)

        if c_AD > 0:
            pt_AD += " + %d = 0" % c_AD
        elif c_AD < 0:
            pt_AD += " - %d = 0" % (-c_AD)
        else:
            pt_AD += " = 0"

        kq_str = str(ans_val).replace('.', ',')

        # Khối vẽ hình TikZ minh họa cố định hình dạng theo yêu cầu
        tikz_fig = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (5,0);
    \\coordinate (A) at (1.5,4);
    \\coordinate (M) at ($(B)!0.5!(C)$);
    \\coordinate (E) at ($(A)!(B)!(C)$); % Chiếu B lên AC
    \\coordinate (F) at ($(A)!(C)!(B)$); % Chiếu C lên AB
    \\coordinate (K) at ($(B)!(A)!(C)$); % Chiếu A lên BC
    \\coordinate (H) at (intersection of B--E and C--F);
    \\coordinate (D) at (intersection of E--F and B--C);
    \\draw[line width=1pt, black] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt, black] (B)--(E);
    \\draw[line width=1pt, black] (C)--(F);
    \\draw[line width=1pt, black] (A)--(K);
    \\draw[line width=1pt, black] (D)--(B);
    \\draw[line width=1pt, black] (D)--(F);
    \\draw[line width=1pt, black] (A)--(D);
    \\draw[line width=1pt, black] (M)--(H);
    \\fill[black] (A) circle (1pt) node[above] {$A$};
    \\fill[black] (B) circle (1pt) node[below] {$B$};
    \\fill[black] (C) circle (1pt) node[below] {$C$};
    \\fill[black] (D) circle (1pt) node[below left] {$D$};
    \\fill[black] (E) circle (1pt) node[above right] {$E$};
    \\fill[black] (F) circle (1pt) node[above left] {$F$};
    \\fill[black] (H) circle (1pt) node[above right] {$H$};
    \\fill[black] (M) circle (1pt) node[below] {$M$};
    \\fill[black] (K) circle (1pt) node[below] {$K$};
    \\end{tikzpicture}
    \\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ nhọn có các đường cao $BE$ và $CF$. Gọi $H$ là trực tâm của tam giác $ABC$ và $M$ là trung điểm cạnh $BC$. Tìm tọa độ đỉnh $A(a;b)$, biết đường thẳng $EF$ cắt đường thẳng $BC$ tại $D(%d;%d)$, đường thẳng $MH$ có phương trình $%s$ và đỉnh $A(a;b)$ thuộc đường thẳng $d: %s$. Giá trị $2a - b$ bằng bao nhiêu?'''
                         % (xD, yD, pt_MH, pt_d))

        # Lời giải chi tiết kèm hình vẽ
        loigiai = ('''%s
    Gọi $K$ là hình chiếu vuông góc của $A$ lên $BC$, suy ra $AK$ là đường cao của tam giác $ABC$ và $H \\in AK$. \\\\
    Tứ giác $BCEF$ nội tiếp đường tròn đường kính $BC$ tâm $M$. \\\\
    Đường thẳng $EF$ cắt $BC$ tại $D$. Theo tính chất chùm điều hòa của tứ giác toàn phần $AFHEBC$, ta có $(D, K, B, C) = -1$. \\\\
    Theo hệ thức Maclaurin đối với trung điểm $M$ của đoạn thẳng $BC$: \\\\
    $\\overline{MD} \\cdot \\overline{MK} = MB^2 = MC^2$. \\\\
    Mặt khác, xét hai tam giác vuông $AKC$ và $BKH$ đồng dạng, ta có: \\\\
    $\\overline{KH} \\cdot \\overline{KA} = \\overline{KB} \\cdot \\overline{KC} = \\overline{KM}^2 - MC^2$. \\\\
    Cộng hai đẳng thức trên, ta được: \\\\
    $\\overline{MD} \\cdot \\overline{MK} + \\overline{KH} \\cdot \\overline{KA} = KM^2 \\Leftrightarrow DH \\perp AM$. \\\\
    Trong tam giác $ADM$, $AK \\perp DM$ và $DH \\perp AM$, mà $H = AK \\cap DH$ nên $H$ chính là trực tâm của tam giác $ADM$. \\\\
    Từ đó suy ra $MH \\perp AD$. \\\\
    Đường thẳng $MH$ có phương trình $%s$ nên vectơ pháp tuyến của $MH$ là $\\vec{n}_{MH} = (%d; %d)$. \\\\
    Vì $AD \\perp MH$ nên đường thẳng $AD$ nhận $\\vec{u}_{MH} = (%d; %d)$ làm vectơ pháp tuyến. \\\\
    Phương trình đường thẳng $AD$ đi qua điểm $D(%d;%d)$ là: \\\\
    $%s$. \\\\
    Tọa độ đỉnh $A$ là giao điểm của đường thẳng $AD$ và đường thẳng $d: %s$. \\\\
    Tọa độ điểm $A$ thỏa mãn hệ phương trình: \\\\
    $\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %d \\\\ y = %d \\end{cases} \\Rightarrow A(%d;%d)$. \\\\
    Do đó $a = %d$ và $b = %d$. \\\\
    Vậy $2a - b = 2 \\cdot (%d) - (%d) = %s$.'''
                   % (tikz_fig, pt_MH, u, v, v, -u, xD, yD, pt_AD, pt_d, pt_AD, pt_d, xA, yA, xA, yA, xA, yA, xA, yA, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content

