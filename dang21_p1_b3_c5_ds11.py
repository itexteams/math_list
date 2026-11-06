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


def bt_dang21_p1_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang = ['1','2']
            dang = random.choice(lisdang)

            if dang == '2':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn cơ số a ngẫu nhiên từ 2 đến 5 để đồ thị không quá dốc
                b = random.randint(2, 5)
                a = Rational(1,b)

                # Các đáp án trắc nghiệm
                # Đáp án đúng
                da_dung = '$y=\\left(%s\\right)^x$' % (latex(a))

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = [
                    '$y=%s^x$' % (latex(b)),
                    '$y=\\log_{%s}{x}$' % (latex(a)),
                    '$y=\\log_{\\frac{1}{%s}}{x}$' % (latex(b)),
                    '$y=\\left(%s\\right)^{x+1}$' % (latex(a)),
                    '$y=x^{%s}$' % (latex(a))
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi - Cập nhật TikZ để vẽ đúng đồ thị của a^x
                # Tọa độ dashed line sẽ chạy theo a: (1, 0) -> (1, a) -> (0, a)
                noidungcauhoi = (r'''Đường cong trong hình vẽ sau là đồ thị của hàm số nào dưới đây?
            \begin{center}
            \begin{tikzpicture}[line join=round, line cap=round, >=stealth, thick, scale=0.8]
                \draw[->] (-3.5,0) -- (3.5,0) node[below left] {$x$};
                \draw[->] (0,-0.5) -- (0,5.5) node[below left] {$y$};
                \draw (0,0) node [below left] {$O$};
                \draw[thin] (1,2pt) -- (1,-2pt) node [below] {$1$};
                \draw[thin] (2pt,%s) -- (-2pt,%s) node [left] {$%s$};
                \draw[dashed, thin] (1,0) -- (1,%s) -- (0,%s);
                \begin{scope}
                \clip (-3.5,-0.5) rectangle (3.5,5.2);
                \draw[samples=200, domain=-3.5:2.5, smooth, variable=\x, blue] plot (\x, {%s^(\x)});
                \end{scope}
            \end{tikzpicture}
            \end{center}''' % (a, a, a, a, a, a))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Dựa vào hình vẽ, ta thấy đồ thị hàm số đi qua điểm $(0;1)$ và điểm $\\left(1;\\dfrac{1}{%s} \\right)$. \\\\
                Thay tọa độ $\\left(1;\\dfrac{1}{%s} \\right)$ vào hàm số: \\\\
                Với $y=\\left(\\dfrac{1}{%s} \\right)^x$, khi $x=1 \\Rightarrow y=\\left(\\dfrac{1}{%s} \\right)^1=\\dfrac{1}{%s}$ (thỏa mãn). \\\\
                Hàm số nghịch biến trên $\\mathbb{R}$ nên đây là đồ thị của hàm số mũ cơ số dương nhỏ hơn 1.''' 
                % (b, b, b, b, b))

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn cơ số a ngẫu nhiên từ 2 đến 5 để đồ thị không quá dốc
                a = random.randint(2, 5)

                # Các đáp án trắc nghiệm
                # Đáp án đúng
                da_dung = '$y=%s^x$' % (latex(a))

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = [
                    '$y=\\left(\\frac{1}{%s}\\right)^x$' % (latex(a)),
                    '$y=\\log_{%s}{x}$' % (latex(a)),
                    '$y=\\log_{\\frac{1}{%s}}{x}$' % (latex(a)),
                    '$y=%s^{x+1}$' % (latex(a)),
                    '$y=x^{%s}$' % (latex(a))
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi - Cập nhật TikZ để vẽ đúng đồ thị của a^x
                # Tọa độ dashed line sẽ chạy theo a: (1, 0) -> (1, a) -> (0, a)
                noidungcauhoi = (r'''Đường cong trong hình vẽ sau là đồ thị của hàm số nào dưới đây?
            \begin{center}
            \begin{tikzpicture}[line join=round, line cap=round, >=stealth, thick, scale=0.8]
                \draw[->] (-3.5,0) -- (3.5,0) node[below left] {$x$};
                \draw[->] (0,-0.5) -- (0,5.5) node[below left] {$y$};
                \draw (0,0) node [below left] {$O$};
                \draw[thin] (1,2pt) -- (1,-2pt) node [below] {$1$};
                \draw[thin] (2pt,%s) -- (-2pt,%s) node [left] {$%s$};
                \draw[dashed, thin] (1,0) -- (1,%s) -- (0,%s);
                \begin{scope}
                \clip (-3.5,-0.5) rectangle (3.5,5.2);
                \draw[samples=200, domain=-3.5:2.5, smooth, variable=\x, blue] plot (\x, {%s^(\x)});
                \end{scope}
            \end{tikzpicture}
            \end{center}''' % (a, a, a, a, a, a))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Dựa vào hình vẽ, ta thấy đồ thị hàm số đi qua điểm $(0;1)$ và điểm $(1;%s)$. \\\\
                Thay tọa độ $(1;%s)$ vào các hàm số: \\\\
                Với $y=%s^x$, khi $x=1 \\Rightarrow y=%s^1=%s$ (thỏa mãn). \\\\
                Hàm số đồng biến trên $\\mathbb{R}$ nên đây là đồ thị của hàm số mũ cơ số lớn hơn 1.''' 
                % (a, a, a, a, a))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content

