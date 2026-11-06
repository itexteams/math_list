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


def bt_dang57_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo các ký hiệu toán học
            x, m = symbols('x m')

            # Bước 1: Random tham số bài toán
            # Để Parabol đẹp, ta chọn a=1, trục đối xứng là số nguyên
            a = 1
            x_i = random.randint(-2, 2)  # Hoành độ đỉnh
            y_i = random.randint(-3, -1) # Tung độ đỉnh (luôn âm để giống hình mẫu)

            # Từ đỉnh I(x_i, y_i) suy ra phương trình y = (x - x_i)^2 + y_i = x^2 - 2*x_i*x + x_i^2 + y_i
            b_val = -2 * x_i
            c_val = x_i**2 + y_i

            # Phương trình đề bài cho: x^2 + bx + m = 0
            # Biến đổi về tương giao: x^2 + bx + c = c - m
            # Vô nghiệm khi c - m < y_i => m > c - y_i
            m_threshold = c_val - y_i

            # --- PHẦN XỬ LÝ ĐÁP ÁN ---
            da_dung = f"$m > {m_threshold}$"
            s = [
                f"$m < {m_threshold}$",
                f"$m > {m_threshold + 1}$",
                f"$m < {m_threshold - 1}$",
                f"$m = {m_threshold}$",
                f"$m \\geq {m_threshold}$",
                f"$m \\leq {m_threshold}$"
            ]
            random.shuffle(s)
            das1, das2, das3 = s[:3]

            # --- NỘI DUNG CÂU HỎI & TIKZ ---
            # Định dạng dấu cho b và c khi in ra chuỗi
            b_str = f"+ {b_val}" if b_val > 0 else f"{b_val}"
            if b_val == 0: b_str = ""
            c_str = f"+ {c_val}" if c_val > 0 else f"{c_val}"

            noidungcauhoi = (r'''Hàm số $y = x^2 %sx %s$ có đồ thị như hình vẽ. Tìm giá trị $m$ để phương trình $x^2 %sx + m = 0$ vô nghiệm.
            \begin{center}
            \begin{tikzpicture}[>=stealth, x=0.8cm, y=0.8cm, scale=0.9]
                \draw[->] (-4,0) -- (4,0) node[below] {$x$};
                \draw[->] (0,-4) -- (0,3) node[left] {$y$};
                \draw[red, thick, smooth, samples=100, domain=%s:%s] plot(\x, {(\x)^2 + %s*\x + %s});
                \node[below left] at (0,0) {$O$};
                \draw[dashed, blue] (%s,0) -- (%s,%s) -- (0,%s);
                \filldraw[black] (%s,%s) circle (1.5pt);
                \node[below] at (%s,0) {$%s$};
                \node[left] at (0,%s) {$%s$};
            \end{tikzpicture}
            \end{center}''' % (
                b_str, c_str, b_str,
                x_i-2.2, x_i+2.2, b_val, c_val, # domain và tham số vẽ hàm
                x_i, x_i, y_i, y_i, # tọa độ vẽ đường dóng
                x_i, y_i, # tọa độ chấm điểm đỉnh
                x_i, x_i, # label x_i
                y_i, y_i  # label y_i
            ))

            # --- NỘI DUNG LỜI GIẢI ---
            # Ta cần truyền đúng số lượng đối số cho các dấu %s trong loigiai
            loigiai = (r'''Ta có phương trình: $x^2 %sx + m = 0 \Leftrightarrow x^2 %sx %s = %s - m \quad (*)$. \\
            Số nghiệm của phương trình $(*)$ chính là số giao điểm của parabol $y = x^2 %sx %s$ và đường thẳng nằm ngang $d \colon y = %s - m$. \\
            Dựa vào đồ thị, đỉnh của parabol có tung độ là $y_I = %s$. \\
            Phương trình vô nghiệm khi và chỉ khi đường thẳng $d$ nằm hoàn toàn phía dưới đỉnh của parabol: \\
            $%s - m < %s \Leftrightarrow -m < %s \Leftrightarrow m > %s$.''' 
            % (
                b_str, b_str, c_str, c_val, # Dòng 1
                b_str, c_str, c_val,         # Dòng 2
                y_i,                         # Dòng 3
                c_val, y_i, (y_i - c_val), m_threshold # Dòng 5 (4 đối số)
            ))

            # --- XUẤT KẾT QUẢ ---
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

