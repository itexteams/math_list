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


def bt_dang12_p3_b1_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random tỷ lệ BM = k * MC và CN = m * NA
        # Để nghiệm x, y và các hệ số đẹp, chọn k và m là các số nguyên dương từ 2 đến 4
        k = random.choice([2, 3, 4])
        m = random.choice([2, 3, 4])


        mau = 1 + k * m + k
        x_val = Rational(1, mau)
        y_val = Rational(k, mau)


        heso_x = mau
        heso_y = mau * random.choice([1, 2])
        gia_tri_T = heso_x * x_val + heso_y * y_val

        # Đáp án đúng
        da = '$%s$' % (latex(gia_tri_T))

        # Các phương án nhiễu
        s = [
            '$%s$' % (latex(gia_tri_T + 1)),
            '$%s$' % (latex(gia_tri_T - 1 if gia_tri_T > 1 else gia_tri_T + 4)),
            '$%s$' % (latex(gia_tri_T + 2)),
            '$%s$' % (latex(gia_tri_T - 2 if gia_tri_T > 2 else gia_tri_T + 3)),
            '$%s$' % (latex(gia_tri_T + 3)),
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung hình vẽ TikZ
        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (1.5,3.5);
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (5.5,0);
        \\coordinate (M) at ($(B)!%s!(C)$);
        \\coordinate (N) at ($(C)!%s!(A)$);
        \\coordinate (I) at (intersection of A--M and B--N);
        \\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(M) (B)--(N);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (M) circle (1pt) node[below] {$M$};
        \\fill (N) circle (1pt) node[above right] {$N$};
        \\fill (I) circle (1pt) node[left] {$I$};
    \\end{tikzpicture}
    \\end{center}''' % (str(float(k / (k + 1))), str(float(m / (m + 1)))))

        # Câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$. Điểm $M$ thuộc cạnh $BC$ sao cho $BM = %s MC$, điểm $N$ thuộc cạnh $CA$ sao cho $CN = %s NA$. Gọi $I$ là giao điểm của $AM$ và $BN$. Phân tích vectơ $\\vec{AI} = x\\vec{AB} + y\\vec{AC}$. Giá trị của tổng $%sx + %sy$ bằng bao nhiêu?'''
                         % (latex(k), latex(m), latex(heso_x), latex(heso_y)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''%s
    Vì $M$ thuộc cạnh $BC$ sao cho $BM = %s MC$ nên $\\vec{BM} = \\dfrac{%s}{%s}\\vec{BC}$.\\\\
    Ta có:
    \\begin{align*}
    \\vec{AM} &= \\vec{AB} + \\vec{BM} = \\vec{AB} + \\dfrac{%s}{%s}\\vec{BC} = \\vec{AB} + \\dfrac{%s}{%s}(\\vec{AC} - \\vec{AB}) \\\\
    &= \\dfrac{1}{%s}\\vec{AB} + \\dfrac{%s}{%s}\\vec{AC}.
    \\end{align*}
    Vì $N$ thuộc cạnh $CA$ sao cho $CN = %s NA$ nên $\\vec{AN} = \\dfrac{1}{%s}\\vec{AC}$.\\\\
    Do $I$ thuộc đoạn $AM$, giả sử $\\vec{AI} = k_0\\vec{AM}$, với $k_0 \\in (0; 1)$, ta có:
    \\[
    \\vec{AI} = \\dfrac{k_0}{%s}\\vec{AB} + \\dfrac{%s k_0}{%s}\\vec{AC}.
    \\]
    Mặt khác, $I$ thuộc đường thẳng $BN$ nên ba điểm $B, I, N$ thẳng hàng. Biểu diễn $\\vec{AI}$ qua $\\vec{AB}$ và $\\vec{AN}$:
    \\[
    \\vec{AI} = \\dfrac{k_0}{%s}\\vec{AB} + \\dfrac{%s k_0(%s)}{%s}\\vec{AN}.
    \\]
    Điều kiện để $B, I, N$ thẳng hàng là tổng hai hệ số bằng $1$:
    \\[
    \\dfrac{k_0}{%s} + \\dfrac{%s}{%s}k_0 = 1 \\iff \\dfrac{%s}{%s}k_0 = 1 \\iff k_0 = \\dfrac{%s}{%s}.
    \\]
    Thay $k_0 = \\dfrac{%s}{%s}$ vào biểu thức của $\\vec{AI}$, ta được:
    \\[
    \\vec{AI} = \\dfrac{1}{%s}\\vec{AB} + \\dfrac{%s}{%s}\\vec{AC}.
    \\]
    Suy ra $x = %s$, $y = %s$.\\\\
    Do đó, giá trị của tổng $%sx + %sy$ bằng:
    \\[
    %s \\cdot %s + %s \\cdot %s = %s.
    \\]'''
                   % (
                       hinh_tikz,
                       latex(k), latex(k), latex(k + 1),
                       latex(k), latex(k + 1), latex(k), latex(k + 1),
                       latex(k + 1), latex(k), latex(k + 1),
                       latex(m), latex(m + 1),
                       latex(k + 1), latex(k), latex(k + 1),
                       latex(k + 1), latex(k), latex(m + 1), latex(k + 1),
                       latex(k + 1), latex(k * (m + 1)), latex(k + 1),
                       latex(1 + k * (m + 1)), latex(k + 1), latex(k + 1), latex(1 + k * (m + 1)),
                       latex(k + 1), latex(1 + k * (m + 1)),
                       latex(mau), latex(k), latex(mau),
                       latex(x_val), latex(y_val),
                       latex(heso_x), latex(heso_y),
                       latex(heso_x), latex(x_val), latex(heso_y), latex(y_val), latex(gia_tri_T)
                   ))
    dapan='\\shortans[0]{$%s$}\n'%(latex(gia_tri_T))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n\\end{minipage}\n\n')
    return content

