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


def bt_dang44_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các góc có thể random
            list_goc = [30, 45, 60]
            goc_val = random.choice(list_goc)

            # Tính toán giá trị MN dựa trên góc alpha (góc giữa AB và MN)
            # Trong tam giác cân PMN tại P, góc PNM = alpha.
            # MN = 2 * PN * cos(alpha) = 2 * (a/2) * cos(alpha) = a * cos(alpha)
            a = symbols('a')

            if goc_val == 30:
                kq_sym = sqrt(3)/2 * a
                loigiai_cos = "\\frac{\\sqrt{3}}{2}"
                loigiai_goc_p = "120^\\circ"
            elif goc_val == 45:
                kq_sym = sqrt(2)/2 * a
                loigiai_cos = "\\frac{\\sqrt{2}}{2}"
                loigiai_goc_p = "90^\\circ"
            else: # 60 độ
                kq_sym = a/2
                loigiai_cos = "\\frac{1}{2}"
                loigiai_goc_p = "60^\\circ"

            # Đáp án đúng
            da = '$MN = %s$' % (latex(kq_sym))

            # Tạo danh sách các phương án sai (không trùng đáp án đúng)
            s = [
                '$MN = \\frac{a}{2}$',
                '$MN = \\frac{a\\sqrt{3}}{2}$',
                '$MN = \\frac{a\\sqrt{3}}{3}$',
                '$MN = \\frac{a}{4}$',
                '$MN = \\frac{a\\sqrt{2}}{2}$',
                '$MN = a$'
            ]

            # Loại bỏ đáp án đúng khỏi danh sách nhiễu
            da_test = '$MN = %s$' % (latex(kq_sym))
            if da_test in s:
                s.remove(da_test)

            random.shuffle(s)
            das1, das2, das3 = s[:3]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tứ diện $ABCD$ có $AB = CD = a$. Gọi $M$ và $N$ lần lượt là trung điểm của $AD$ và $BC$. Xác định độ dài đoạn thẳng $MN$ để góc giữa hai đường thẳng $AB$ và $MN$ bằng $%s^\\circ$.'''
                              % (goc_val))

            # Hình vẽ bằng TikZ
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                \\coordinate (A) at (1.5,3.5);
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (2,-1);
                \\coordinate (D) at (4.5,0.5);
                \\coordinate (M) at ($(A)!0.5!(D)$);
                \\coordinate (N) at ($(B)!0.5!(C)$);
                \\coordinate (P) at ($(A)!0.5!(C)$);

                \\draw (A)--(B)--(C)--(A) (A)--(D)--(C) (P)--(N) (M)--(P);
                \\draw[dashed] (B)--(D) (M)--(N) (M)--(N);

                \\fill (A)  node[above] {$A$};
                \\fill (B)  node[left] {$B$};
                \\fill (C)  node[below] {$C$};
                \\fill (D)  node[right] {$D$};
                \\fill (M)  node[above right] {$M$};
                \\fill (N)  node[below left] {$N$};
                \\fill (P)  node[left] {$P$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung lời giải
            loigiai = ('''Gọi $P$ là trung điểm của $AC$. \\\\
            Xét tam giác $ACD$, có $M, P$ lần lượt là trung điểm $AD, AC$ nên $PM$ là đường trung bình, suy ra $PM = \\frac{1}{2}CD = \\frac{a}{2}$ và $PM \\parallel CD$.\\\\
            Xét tam giác $ABC$, có $N, P$ lần lượt là trung điểm $BC, AC$ nên $PN$ là đường trung bình, suy ra $PN = \\frac{1}{2}AB = \\frac{a}{2}$ và $PN \\parallel AB$.\\\\
            Vì $AB = CD = a \\Rightarrow PM = PN = \\frac{a}{2}$. Do đó tam giác $PMN$ cân tại $P$.\\\\
            Vì $PN \\parallel AB$ nên góc giữa $AB$ và $MN$ chính là góc giữa $PN$ và $MN$.\\\\
            Theo giả thiết, góc này bằng $%s^\\circ$, suy ra $\\widehat{PNM} = %s^\\circ$.\\\\
            Vì tam giác $PMN$ cân tại $P$ nên $\\widehat{PMN} = \\widehat{PNM} = %s^\\circ$.\\\\
            Suy ra góc ở đỉnh $\\widehat{MPN} = 180^\\circ - 2 \\cdot %s^\\circ = %s$.\\\\
            Áp dụng định lý côsin trong tam giác $PMN$:\\\\
            $MN^2 = PM^2 + PN^2 - 2PM \\cdot PN \\cdot \\cos(\\widehat{MPN})$\\\\
            $MN^2 = \\left(\\frac{a}{2}\\right)^2 + \\left(\\frac{a}{2}\\right)^2 - 2 \\cdot \\frac{a}{2} \\cdot \\frac{a}{2} \\cdot \\cos(%s)$.\\\\
            Thay số ta được $MN = %s$.''' 
            % (goc_val, goc_val, goc_val, goc_val, loigiai_goc_p, loigiai_goc_p, latex(kq_sym)))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Xuất nội dung (Không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + hinh_ve + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

