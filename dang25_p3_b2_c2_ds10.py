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


def bt_dang25_p3_b2_c2_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hệ số lợi nhuận (triệu đồng)
        pA = randint(3, 8)
        pB = randint(3, 8)

        # Chọn toạ độ giao điểm mục tiêu A(xA, yA) là số nguyên
        xA = randint(10, 20)
        yA = randint(15, 30)

        # Định mức nguyên vật liệu và giờ công
        a1, b1 = 6, 4
        a2, b2 = 2, 4
        a3, b3 = 8, 4

        # Giới hạn tài nguyên để miền nghiệm tạo thành từ (d2) và (d3)
        c2 = a2 * xA + b2 * yA
        c3 = a3 * xA + b3 * yA
        c1 = a1 * xA + b1 * yA + randint(10, 30)

        # Toạ độ các đỉnh của miền nghiệm OEAC
        # Điểm E: giao điểm của (d3): a3*x + b3*y = c3 với trục hoành Ox (y = 0)
        xE = Rational(c3, a3)
        yE = 0

        # Điểm C: giao điểm của (d2): a2*x + b2*y = c2 với trục tung Oy (x = 0)
        xC = 0
        yC = Rational(c2, b2)

        # Giao điểm của d1 với các trục toạ độ để xác định khung vẽ
        x_d1 = Rational(c1, a1)
        y_d1 = Rational(c1, b1)

        # Tính toán giới hạn khung vẽ
        x_max_val = max(float(xA), float(xE), float(x_d1))
        y_max_val = max(float(yA), float(yC), float(y_d1))

        x_limit = x_max_val + 8.0
        y_limit = y_max_val + 8.0

        # Giá trị hàm mục tiêu tại các đỉnh
        f_O = 0
        f_E = pA * xE
        f_A = pA * xA + pB * yA
        f_C = pB * yC

        max_F = max(f_O, f_E, f_A, f_C)

        number = Decimal(str(float(max_F)))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP) if max_F == int(max_F) else number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Vẽ hình TikZ minh hoạ: chỉ hiển thị tên các điểm (O, E, A, C), không kèm toạ độ
        tikz = ('''\\begin{center}
    \\begin{tikzpicture}[>=stealth, scale=0.18, line width=1pt]
    \\clip (-4,-4) rectangle (%s,%s);
    \\fill[pattern=north east lines, pattern color=black!35] (-4,-4) rectangle (%s,%s);
    \\fill[white] (0,0) -- (%s,0) -- (%s,%s) -- (0,%s) -- cycle;
    \\draw[->] (-4,0) -- (%s,0) node[below] {$x$};
    \\draw[->] (0,-4) -- (0,%s) node[left] {$y$};
    \\node at (0,0) [below left] {$O$};
    \\draw[black, smooth, domain=-4:%s] plot(\\x, {(%s - %s*\\x)/%s});
    \\draw[black, smooth, domain=-4:%s] plot(\\x, {(%s - %s*\\x)/%s});
    \\draw[black, smooth, domain=-4:%s] plot(\\x, {(%s - %s*\\x)/%s});
    \\coordinate (E) at (%s,0);
    \\coordinate (A) at (%s,%s);
    \\coordinate (C) at (0,%s);
    \\fill (0,0) circle (2pt);
    \\fill (E) circle (2pt) node[below] {$E$};
    \\fill (A) circle (2pt) node[above right] {$A$};
    \\fill (C) circle (2pt) node[left] {$C$};
    \\draw[dashed, thin] (%s,0) -- (A) -- (0,%s);
    \\end{tikzpicture}
    \\end{center}'''
                %(x_limit, y_limit,
                  x_limit, y_limit,
                  float(xE), float(xA), float(yA), float(yC),
                  float(x_limit - 1), float(y_limit - 1),
                  float(x_limit - 2), c1, a1, b1,
                  float(x_limit - 2), c2, a2, b2,
                  float(x_limit - 2), c3, a3, b3,
                  float(xE), float(xA), float(yA), float(yC),
                  float(xA), float(yA)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cơ sở đúc đồng mỹ nghệ dự định sản xuất hai loại đỉnh đồng $A$ và $B$. Để sản xuất một chiếc đỉnh đồng loại $A$ cần $%s\\text{ kg}$ đồng thau, $%s\\text{ kg}$ kẽm và $%s$ giờ công chế tác. Để sản xuất một chiếc đỉnh đồng loại $B$ cần $%s\\text{ kg}$ đồng thau, $%s\\text{ kg}$ kẽm và $%s$ giờ công chế tác. Cơ sở hiện có dự trữ $%s\\text{ kg}$ đồng thau, $%s\\text{ kg}$ kẽm và quỹ thời gian công nhân làm việc tối đa là $%s$ giờ. Mỗi chiếc đỉnh đồng loại $A$ mang lại lợi nhuận $%s$ triệu đồng, mỗi chiếc đỉnh đồng loại $B$ mang lại lợi nhuận $%s$ triệu đồng. Hỏi lợi nhuận tối đa mà cơ sở này có thể thu được là bao nhiêu triệu đồng?'''
                         %(a1, a2, a3,
                           b1, b2, b3,
                           c1, c2, c3,
                           pA, pB))

        # Nội dung lời giải
        loigiai = ('''Gọi $x, y$ lần lượt là số chiếc đỉnh đồng loại $A$ và loại $B$ mà cơ sở cần sản xuất ($x, y \\ge 0$).\\\\
    Theo bài ra, ta có hệ bất phương trình biểu thị các điều kiện ràng buộc:\\\\
    $\\begin{cases}
    %sx + %sy \\le %s \\\\
    %sx + %sy \\le %s \\\\
    %sx + %sy \\le %s \\\\
    x \\ge 0 \\\\
    y \\ge 0
    \\end{cases}$\\\\
    Tổng lợi nhuận thu được là $F(x; y) = %sx + %sy$ (triệu đồng).\\\\
    Miền nghiệm của hệ bất phương trình là tứ giác $OEAC$ (phần mặt phẳng không bị gạch chéo trong hình vẽ dưới đây):
    %s
    Toạ độ các đỉnh của tứ giác là:\\\\
    - $O(0; 0)$\\\\
    - $E(%s; 0)$\\\\
    - $A(%s; %s)$ là giao điểm của hai đường thẳng $%sx + %sy = %s$ và $%sx + %sy = %s$\\\\
    - $C(0; %s)$\\\\
    Giá trị của biểu thức $F(x; y)$ tại các đỉnh:\\\\
    - $F(0; 0) = 0$ triệu đồng.\\\\
    - $F(%s; 0) = %s \\cdot %s = %s$ triệu đồng.\\\\
    - $F(%s; %s) = %s \\cdot %s + %s \\cdot %s = %s$ triệu đồng.\\\\
    - $F(0; %s) = %s \\cdot %s = %s$ triệu đồng.\\\\
    So sánh các giá trị trên, ta thấy $F(x; y)$ đạt giá trị lớn nhất bằng $%s$ triệu đồng tại điểm $A(%s; %s)$.\\\\
    Vậy lợi nhuận tối đa cơ sở có thể thu được là $%s$ triệu đồng.'''
                   %(a1, b1, c1,
                     a2, b2, c2,
                     a3, b3, c3,
                     pA, pB,
                     tikz,
                     latex(xE),
                     xA, yA, a3, b3, c3, a2, b2, c2,
                     latex(yC),
                     latex(xE), pA, latex(xE), latex(f_E),
                     xA, yA, pA, xA, pB, yA, latex(f_A),
                     latex(yC), pB, latex(yC), latex(f_C),
                     latex(max_F), xA, yA,
                     str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content

