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


def bt_dang28_p3_b1_c2_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random kích thước nhà kho
        ab = random.choice([8, 10, 12, 14, 16])
        ad = random.choice([16, 20, 24, 28, 30])
        h_wall = random.choice([5, 6, 7, 8])
        delta_h = random.choice([2, 3, 4])  # phần chóp mái nhô lên
        h_total = h_wall + delta_h

        # Tính toán tọa độ và phương trình mặt phẳng (EFIK):
        val_a = 0
        val_b = -Rational(ad, 2 * delta_h)
        val_c = Rational(ad * h_wall, 2 * delta_h)

        ans_val = val_a - val_b + val_c  # a - b + c

        # Đưa về dạng chuỗi kết quả
        if ans_val.q == 1:
            kq_val = ans_val.p
            kq_str = str(kq_val)
        else:
            number = Decimal(float(ans_val))
            kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq).replace('.', ',')

        # Định dạng các hệ số trong phương trình mặt phẳng
        pt_mp = "y "
        if val_b < 0:
            if val_b == -1:
                pt_mp += "- z "
            else:
                pt_mp += "- %s z " % latex(-val_b)
        else:
            if val_b == 1:
                pt_mp += "+ z "
            else:
                pt_mp += "+ %s z " % latex(val_b)

        if val_c >= 0:
            pt_mp += "+ %s = 0" % latex(val_c)
        else:
            pt_mp += "- %s = 0" % latex(-val_c)

        # TikZ code vẽ hình chính xác 100% như đề có tô màu 2 mái IKEF và HGIK
        tikz_code = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "    \\coordinate (O) at (0,0);\n"
            "    \\coordinate (A) at (0,0.3);\n"
            "    \\coordinate (B) at (-1.8,-1.5);\n"
            "    \\coordinate (C) at (1.4,-1.5);\n"
            "    \\coordinate (D) at (3.2,0.3);\n"
            "    \\coordinate (E) at (0,2.5);\n"
            "    \\coordinate (F) at (-1.8,0.7);\n"
            "    \\coordinate (G) at (1.4,0.7);\n"
            "    \\coordinate (H) at (3.2,2.5);\n"
            "    \\coordinate (I) at (-0.2,1.35);\n"
            "    \\coordinate (K) at (1.6,3.15);\n"
            "    \\fill[red!25] (I)--(K)--(E)--(F)--cycle;\n"
            "    \\fill[red!35] (I)--(K)--(H)--(G)--cycle;\n"
            "    \\draw[line width=1pt, dashed] (B)--(A)--(D);\n"
            "    \\draw[line width=1pt, dashed] (A)--(E);\n"
            "    \\draw[line width=1pt] (F)--(B)--(C)--(G)--cycle;\n"
            "    \\draw[line width=1pt] (C)--(D)--(H)--(G);\n"
            "    \\draw[line width=1pt] (F)--(E)--(K)--(H);\n"
            "    \\draw[line width=1pt] (F)--(I)--(G);\n"
            "    \\draw[line width=1pt] (I)--(K);\n"
            "    \\draw[->, line width=1pt] (B) -- (-2.4,-2.0) node[below] {$x$};\n"
            "    \\draw[->, line width=1pt] (D) -- (4.0,0.3) node[right] {$y$};\n"
            "    \\draw[->, line width=1pt] (E) -- (0,3.6) node[above] {$z$};\n"
            "    \\fill (O) circle (0pt) node {$O$};\n"
            "    \\fill (A) circle (1pt) node[left] {$A$};\n"
            "    \\fill (B) circle (1pt) node[left] {$B$};\n"
            "    \\fill (C) circle (1pt) node[below] {$C$};\n"
            "    \\fill (D) circle (1pt) node[below right] {$D$};\n"
            "    \\fill (E) circle (1pt) node[left] {$E$};\n"
            "    \\fill (F) circle (1pt) node[left] {$F$};\n"
            "    \\fill (G) circle (1pt) node[right] {$G$};\n"
            "    \\fill (H) circle (1pt) node[right] {$H$};\n"
            "    \\fill (I) circle (1pt) node[below] {$I$};\n"
            "    \\fill (K) circle (1pt) node[above] {$K$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = (
            'Một nhà kho được mô hình hoá trong không gian với hệ trục toạ độ $Oxyz$ và hai mái $EFIK$, $HGIK$ có kích thước bằng nhau như hình vẽ.\\\\'
            '%s'
            'Biết rằng chiều cao của nhà kho là $%s\\text{ m}$ và các bức tường của nhà kho tạo thành hình hộp chữ nhật $ABCD.EFGH$ với $AB=%s\\text{ m}$, $AD=%s\\text{ m}$, $AE=%s\\text{ m}$. '
            'Mặt phẳng $(EFIK)$ có phương trình $ax+y+bz+c=0$. Giá trị của $a-b+c$ bằng bao nhiêu?'
            % (tikz_code, latex(h_total), latex(ab), latex(ad), latex(h_wall))
        )

        # Nội dung lời giải
        loigiai = (
            'Chọn hệ trục toạ độ $Oxyz$ như hình vẽ với gốc toạ độ $O$ trùng với điểm $A(0;0;0)$.\\\\ '
            'Tia $Ox$ chứa cạnh $AB$, tia $Oy$ chứa cạnh $AD$ và tia $Oz$ chứa cạnh $AE$.\\\\ '
            'Khi đó, toạ độ các điểm liên quan là:\\\\ '
            '$A(0;0;0)$, $E(0;0;%s)$, $F(%s;0;%s)$.\\\\ '
            'Vì hai mái $EFIK$ và $HGIK$ có kích thước bằng nhau và chiều cao của nhà kho bằng $%s\\text{ m}$ nên đỉnh mái $K$ có cao độ $z_K=%s$ và nằm trên mặt phẳng đối xứng của nhà kho.\\\\ '
            'Điểm $K$ nằm trên bức tường phía sau (mặt phẳng $(ADHE)$ tương ứng với mặt phẳng $Oyz$), do đó hoành độ $x_K=0$.\\\\ '
            'Tung độ của $K$ là trung điểm của cạnh $AD$: $y_K=\\dfrac{AD}{2}=\\dfrac{%s}{2}=%s$.\\\\ '
            'Suy ra toạ độ điểm $K$ là $K\\left(0;%s;%s\\right)$.\\\\ '
            'Ta có:\\\\ '
            '$\\vec{EF}=(%s;0;0)$ suy ra một vectơ cùng phương là $\\vec{u}_1=(1;0;0)$.\\\\ '
            '$\\vec{EK}=\\left(0;%s;%s\\right)$ suy ra một vectơ cùng phương là $\\vec{u}_2=\\left(0;%s;%s\\right)$.\\\\ '
            'Mặt phẳng $(EFIK)$ đi qua điểm $E(0;0;%s)$ và nhận vectơ $\\vec{n}=\\left[\\vec{u}_1,\\vec{u}_2\\right]=\\left(0;%s;%s\\right)$ làm vectơ pháp tuyến.\\\\ '
            'Do đó, phương trình mặt phẳng $(EFIK)$ là:\\\\ '
            '$0\\cdot(x-0)+1\\cdot(y-0)%s\\cdot(z-%s)=0 \\Leftrightarrow %s$.\\\\ '
            'Đối chiếu với phương trình dạng $ax+y+bz+c=0$, ta được:\\\\ '
            '$a=%s$, $b=%s$, $c=%s$.\\\\ '
            'Vậy $a-b+c=%s-%s+%s=%s$.'
            % (
                latex(h_wall), latex(ab), latex(h_wall),
                latex(h_total), latex(h_total),
                latex(ad), latex(Rational(ad, 2)),
                latex(Rational(ad, 2)), latex(h_total),
                latex(ab),
                latex(Rational(ad, 2)), latex(delta_h),
                latex(Rational(ad, 2)), latex(delta_h),
                latex(h_wall),
                latex(-delta_h), latex(Rational(ad, 2)),
                "- " + latex(-val_b) if val_b < 0 else "+ " + latex(val_b),
                latex(h_wall),
                pt_mp,
                latex(val_a), latex(val_b), latex(val_c),
                latex(val_a), latex(val_b), latex(val_c),
                str(kq_str)
            )
        )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = (
        '\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n' +
        str(dapan) +
        '\\loigiai{\n' +
        str(loigiai) + '\n}\n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n' )
    return content

