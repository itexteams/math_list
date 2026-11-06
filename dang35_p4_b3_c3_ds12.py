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


def bt_dang35_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random bài toán bằng cách thay đổi giá trị a để tạo các phương án nhiễu logic
                val_a = randint(2, 8)

                # Tính toán đáp án đúng: V = 5/4 * pi * a^3
                kq_factor = Rational(5, 4)
                da_dung = '$%s\\pi a^3$' % (latex(kq_factor))

                # B4: Tạo các phương án sai không trùng đáp án đúng
                s = []
                list_sai_factors = [Rational(3, 4), Rational(7, 4), Rational(3, 2), Rational(1, 2), Rational(5, 6), Rational(2, 3)]
                for factor in list_sai_factors:
                    if factor != kq_factor:
                        s.append('$%s\\pi a^3$' % (latex(factor)))

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình thang $ABCD$ có $AB$ song song $CD$ và $AB = AD = BC = a$, $CD = 2a$. Tính thể tích khối tròn xoay khi quay hình thang $ABCD$ quanh trục là đường thẳng $AB$.''')

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Mã TikZ để vẽ hình
                tikz_code = (r'''\begin{center}
            \begin{tikzpicture}[scale=2, font=\footnotesize, >=stealth, line join=round, line cap=round,>=stealth,thick]
                \draw[->] (-0.5,0) -- (2.5,0) node[right]{$x$};
                \draw[->] (0,-1.2) -- (0,0.5) node[above]{$y$};
                \draw (0,0) node[above left]{$O$};
                \coordinate (A) at (0.5,0);
                \coordinate (B) at (1.5,0);
                \coordinate (D) at (0,-0.866);
                \coordinate (C) at (2,-0.866);
                \coordinate (H) at (0.5,-0.866);
                \coordinate (E) at (1,-0.866);
                \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
                \draw (A) -- (H);
                \draw (A) -- (E);
                \draw (0,-0.866) -- (2,-0.866);
                \filldraw[] (A) node[above]{$A$};
                \filldraw[] (B) node[above]{$B$};
                \filldraw[] (D) node[below left]{$D$};
                \filldraw[] (C) node[below right]{$C$};
                \filldraw[] (H) node[below]{$H$};
                \filldraw[] (E) node[below]{$E$};
            \end{tikzpicture}
            \end{center}''')

                # Nội dung lời giải (dx thay bằng \text{d}x)
                loigiai = tikz_code + ('''Dễ thấy $ABCE$ là hình bình hành nên $AE = BC = a$. \\\\
                            Suy ra $ADE$ là tam giác đều. \\\\
                            Có $AH = \\frac{a\\sqrt{3}}{2}$. \\\\
                            Xét hệ trục tọa độ $Oxy$ như hình vẽ. Có phương trình $CD: y = -\\frac{a\\sqrt{3}}{2}; x_D = 0, x_C = 2a; A\\left(\\frac{a}{2}; 0\\right)$. \\\\
                            Phương trình $AD: y = \\sqrt{3}x - \\frac{a\\sqrt{3}}{2}$. \\\\
                            Vậy $V = \\pi \\int\\limits_{0}^{2a} \\left(\\frac{a\\sqrt{3}}{2}\\right)^2 \\text{d}x - 2\\pi \\int\\limits_{0}^{\\frac{a}{2}} \\left(\\sqrt{3}x - \\frac{a\\sqrt{3}}{2}\\right)^2 \\text{d}x$ \\\\
                            $= \\frac{3\\pi a^2}{4} \\cdot 2a - 2\\pi \\int\\limits_{0}^{\\frac{a}{2}} \\left(3x^2 - 3ax + \\frac{3a^2}{4}\\right) \\text{d}x$ \\\\
                            $= \\frac{3\\pi a^3}{2} - 2\\pi \\left(x^3 - \\frac{3a}{2}x^2 + \\frac{3a^2}{4}x\\right) \\bigg|_0^{\\frac{a}{2}}$ \\\\
                            $= \\frac{3\\pi a^3}{2} - 2\\pi \\cdot \\frac{a^3}{8} = \\frac{5}{4}\\pi a^3$.''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

