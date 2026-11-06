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


def bt_dang27_p3_b3_c1_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        P0 = random.choice([40, 50, 60, 80])
        A = random.choice([10, 15, 20, 25])

        # Kết quả tổng thời gian (giờ)
        ans_t = 16
        number = Decimal(str(ans_t))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hệ thống lưới điện thông minh giám sát lượng điện tiêu thụ của một nhà kính nông nghiệp công nghệ cao. Công suất tiêu thụ điện (tính bằng $\\text{kW}$) tại thời điểm $t$ (giờ) trong một ngày ($0 \\le t \\le 24$) được mô hình hóa bởi hàm số: $P(t) = %s + %s\\cos\\left(\\dfrac{\\pi t}{6}\\right) - %s\\sin\\left(\\dfrac{\\pi t}{12}\\right)$. Để đảm bảo an toàn vận hành và tiết kiệm chi phí, hệ thống sẽ tự động kích hoạt chế độ tiết kiệm điện khi công suất tiêu thụ đạt từ $%s\\text{ kW}$ trở lên. Đồ thị minh họa công suất tiêu thụ điện trong ngày được cho dưới đây:
    \\begin{center}
    \\begin{tikzpicture}[scale=0.38, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[->, line width=1pt] (0,0) -- (26,0) node[below right] {$t\\text{ (h)}$};
        \\draw[->, line width=1pt] (0,0) -- (0,11) node[above] {$P\\text{ (kW)}$};
        \\node[below left] at (0,0) {$0$};
        \\foreach \\x in {2,4,6,8,10,12,14,16,18,20,22,24} {
            \\draw[line width=1pt] (\\x,0.15) -- (\\x,-0.15) node[below] {$\\x$}; }
        \\foreach \\y/\\label in {1/10, 2/20, 3/30, 4/40, 5/50, 6/60, 7/70, 8/80, 9/90, 10/100} {
            \\draw[line width=1pt] (0.2,\\y) -- (-0.2,\\y) node[left] {$\\label$};}
        \\draw[line width=1pt, dashed] (0,5) -- (25,5) node[right] {$%s\\text{ kW}$};
        \\draw[line width=1pt, red, smooth, samples=120, domain=0:24] plot (\\x, {5 + 2*cos(30*\\x) - 2*sin(15*\\x)});
        \\fill (2,5) circle (1pt) node[above right] {$(2;%s)$};
        \\fill (10,5) circle (1pt) node[below] {$(10;%s)$};
        \\fill (18,5) circle (1pt) node[below] {$(18;%s)$};
    \\end{tikzpicture}
    \\end{center} Hỏi trong một ngày ($24$ giờ), tổng thời gian (tính bằng giờ) mà nhà kính này hoạt động ở chế độ tiết kiệm điện là bao nhiêu?'''
                         % (latex(P0), latex(A), latex(A), latex(P0),
                            latex(P0), latex(P0), latex(P0), latex(P0)))

        # Nội dung lời giải
        loigiai = ('''Hệ thống kích hoạt chế độ tiết kiệm điện khi công suất $P(t) \\ge %s$. \\\\
    Ta có bất phương trình: \\\\
    $%s + %s\\cos\\left(\\dfrac{\\pi t}{6}\\right) - %s\\sin\\left(\\dfrac{\\pi t}{12}\\right) \\ge %s$ \\\\
    $\\Leftrightarrow %s\\left[\\cos\\left(\\dfrac{\\pi t}{6}\\right) - \\sin\\left(\\dfrac{\\pi t}{12}\\right)\\right] \\ge 0$ \\\\
    $\\Leftrightarrow \\cos\\left(\\dfrac{\\pi t}{6}\\right) - \\sin\\left(\\dfrac{\\pi t}{12}\\right) \\ge 0$. \\\\
    Áp dụng công thức nhân đôi $\\cos(2\\alpha) = 1 - 2\\sin^2(\\alpha)$ với $\\alpha = \\dfrac{\\pi t}{12}$: \\\\
    $1 - 2\\sin^2\\left(\\dfrac{\\pi t}{12}\\right) - \\sin\\left(\\dfrac{\\pi t}{12}\\right) \\ge 0$ \\\\
    $\\Leftrightarrow 2\\sin^2\\left(\\dfrac{\\pi t}{12}\\right) + \\sin\\left(\\dfrac{\\pi t}{12}\\right) - 1 \\le 0$ \\\\
    $\\Leftrightarrow \\left(2\\sin\\left(\\dfrac{\\pi t}{12}\\right) - 1\\right)\\left(\\sin\\left(\\dfrac{\\pi t}{12}\\right) + 1\\right) \\le 0$ \\\\
    $\\Leftrightarrow -1 \\le \\sin\\left(\\dfrac{\\pi t}{12}\\right) \\le \\dfrac{1}{2}$. \\\\
    Vì $0 \\le t \\le 24$ nên $0 \\le \\dfrac{\\pi t}{12} \\le 2\\pi$. \\\\
    Do đó, $\\sin\\left(\\dfrac{\\pi t}{12}\\right) \\le \\dfrac{1}{2}$ khi và chỉ khi: \\\\
    $\\left[ \\begin{array}{l} 0 \\le \\dfrac{\\pi t}{12} \\le \\dfrac{\\pi}{6} \\\\ \\dfrac{5\\pi}{6} \\le \\dfrac{\\pi t}{12} \\le 2\\pi \\end{array} \\right. \\Leftrightarrow \\left[ \\begin{array}{l} 0 \\le t \\le 2 \\\\ 10 \\le t \\le 24. \\end{array} \\right.$ \\\\
    Thời gian nhà kính hoạt động ở chế độ tiết kiệm điện trong các khoảng là: \\\\
    - Khoảng thứ nhất: $2 - 0 = 2$ giờ. \\\\
    - Khoảng thứ hai: $24 - 10 = 14$ giờ. \\\\
    Tổng thời gian nhà kính hoạt động ở chế độ tiết kiệm điện trong một ngày là: \\\\
    $2 + 14 = %s$ (giờ).'''
                   % (latex(P0),
                      latex(P0), latex(A), latex(A), latex(P0),
                      latex(A),
                      str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content

