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


def bt_dang78_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Thể tích kho hàng V: chọn k nguyên dương sao cho V = 2 * k^3
        k = randint(2, 6)
        V_val = 2 * (k**3)

        # Kích thước tối ưu: x = y = 2k, h = k
        x_opt = 2 * k
        y_opt = 2 * k
        h_opt = k
        tong = x_opt + y_opt + h_opt

        kq_str = str(tong)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một mô hình kho hàng có dạng khối lăng trụ đứng $ABC.A'B'C'$ với đáy $ABC$ là tam giác vuông tại $A$. Gọi $AB = x\\text{ (m)}$, $AC = y\\text{ (m)}$ là độ dài hai cạnh góc vuông của đáy và $h\\text{ (m)}$ là chiều cao của lăng trụ ($x, y, h > 0$). Biết rằng thể tích của kho hàng là $V = %s\\text{ m}^3$. Chi phí sơn $1\\text{ m}^2$ cho hai mặt đáy (sàn và trần) là $100$ nghìn đồng; chi phí sơn $1\\text{ m}^2$ cho hai mặt bên vuông góc $(ABB'A')$ và $(ACC'A')$ là $100$ nghìn đồng; chi phí sơn $1\\text{ m}^2$ cho mặt bên vát $(BCC'B')$ là $100\\sqrt{2}$ nghìn đồng. Để tổng chi phí sơn toàn bộ các mặt của kho hàng đạt giá trị nhỏ nhất thì tổng $x + y + h$ bằng bao nhiêu mét?'''
                         % (latex(V_val)))

        # Nội dung lời giải kèm hình lăng trụ TikZ và bảng biến thiên an toàn
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (3.5,0);
        \\coordinate (C) at (1.2,-1.5);
        \\coordinate (A1) at (0,3.5);
        \\coordinate (B1) at (3.5,3.5);
        \\coordinate (C1) at (1.2,2);
        \\draw[line width=1pt] (A1)--(B1)--(C1)--cycle (A1)--(A) (B1)--(B) (C1)--(C) (A)--(C)--(B);
        \\draw[line width=1pt, dashed] (A)--(B);
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[right] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (A1) circle (1pt) node[above left] {$A'$};
        \\fill (B1) circle (1pt) node[above right] {$B'$};
        \\fill (C1) circle (1pt) node[above] {$C'$};
    \\end{tikzpicture}
    \\end{center}
    Đáy $ABC$ là tam giác vuông tại $A$ nên $BC = \\sqrt{x^2 + y^2}$. \\\\
    Diện tích hai mặt đáy (sàn và trần) là: \\\\
    $S_{\\text{đáy}} = 2 \\cdot S_{ABC} = 2 \\cdot \\frac{1}{2}xy = xy\\text{ (m}^2\\text{)}$. \\\\
    Diện tích hai mặt bên vuông góc $(ABB'A')$ và $(ACC'A')$ là: \\\\
    $S_1 = (x + y)h\\text{ (m}^2\\text{)}$. \\\\
    Diện tích mặt bên $(BCC'B')$ là: \\\\
    $S_2 = BC \\cdot h = h\\sqrt{x^2 + y^2}\\text{ (m}^2\\text{)}$. \\\\
    Thể tích của khối lăng trụ: \\\\
    $V = \\frac{1}{2}xyh = %s \\Leftrightarrow h = \\frac{%s}{xy}$. \\\\
    Tổng chi phí sơn các mặt (đơn vị: $100$ nghìn đồng) là: \\\\
    $T = 1 \\cdot S_{\\text{đáy}} + 1 \\cdot S_1 + \\sqrt{2} \\cdot S_2 = xy + (x + y)h + h\\sqrt{2(x^2 + y^2)}$. \\\\
    Áp dụng bất đẳng thức Cauchy-Schwarz ta có $\\sqrt{2(x^2 + y^2)} \\ge x + y$, dấu đẳng thức xảy ra khi $x = y$. \\\\
    Khi đó, chi phí sơn đạt giá trị nhỏ nhất khi $x = y$. \\\\
    Thay $y = x$ và $h = \\frac{%s}{x^2}$ vào biểu thức tính chi phí, ta xét hàm số theo biến $x > 0$: \\\\
    $f(x) = x^2 + 2x \\cdot \\frac{%s}{x^2} + 2x \\cdot \\frac{%s}{x^2} = x^2 + \\frac{%s}{x}$. \\\\
    Xét hàm số $f(x) = x^2 + \\frac{%s}{x}$ trên khoảng $(0; +\\infty)$: \\\\
    Ta có $f'(x) = 2x - \\frac{%s}{x^2} = \\frac{2x^3 - %s}{x^2}$. \\\\
    $f'(x) = 0 \\Leftrightarrow 2x^3 - %s = 0 \\Leftrightarrow x^3 = %s \\Leftrightarrow x = %s$. \\\\
    Bảng biến thiên của hàm số $f(x)$: \\\\
    \\begin{center}
    \\renewcommand{\\arraystretch}{1.3}
    $\\begin{array}{|c|lcccr|}
    \\hline
    x & 0 & & %s & & +\\infty \\\\
    \\hline
    f'(x) & \\| & - & 0 & + & \\\\
    \\hline
    & +\\infty & & & & +\\infty \\\\
    f(x) & & \\searrow & & \\nearrow & \\\\
    & & & f(%s) & & \\\\
    \\hline
    \\end{array}$
    \\end{center}
    Căn cứ vào bảng biến thiên, hàm số $f(x)$ đạt giá trị nhỏ nhất tại $x = %s$. \\\\
    Khi đó: \\\\
    $x = y = %s\\text{ (m)}$, $h = \\frac{%s}{%s^2} = %s\\text{ (m)}$. \\\\
    Vậy tổng $x + y + h = %s + %s + %s = %s\\text{ m}$.'''
                   % (latex(V_val),
                      latex(2 * V_val),
                      latex(2 * V_val),
                      latex(2 * V_val),
                      latex(2 * V_val),
                      latex(8 * V_val),
                      latex(8 * V_val),
                      latex(8 * V_val),
                      latex(8 * V_val),
                      latex(8 * V_val),
                      latex(4 * V_val),
                      latex(x_opt),
                      latex(x_opt),
                      latex(x_opt),
                      latex(x_opt),
                      latex(x_opt),
                      latex(2 * V_val),
                      latex(x_opt),
                      latex(h_opt),
                      latex(x_opt),
                      latex(y_opt),
                      latex(h_opt),
                      str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

