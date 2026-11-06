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


def bt_dang49_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến dang để chọn loại bài toán (ở đây mặc định là 1)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các bộ số (k1, k2, k3) tương ứng với các cạnh AB, AD, SA
                # AB = a * sqrt(k1), AD = a * sqrt(k2), SA = a * sqrt(k3)
                # Tan(BSC) = BC / SB = AD / sqrt(SA^2 + AB^2) = sqrt(k2) / sqrt(k3 + k1)

                # Danh sách các bộ số cho ra góc đẹp (30, 45, 60)
                # (k1, k2, k3, ket_qua_goc)
                cac_bo_so = [
                    (1, 3, 2, 45), # Tan = sqrt(3)/sqrt(2+1) = 1 -> 45
                    (1, 9, 2, 60), # Tan = 3/sqrt(2+1) = sqrt(3) -> 60
                    (2, 1, 1, 30), # Tan = 1/sqrt(1+2) = 1/sqrt(3) -> 30
                    (1, 1, 0, 45), # Trường hợp SA=0 không thực tế, bỏ qua
                    (3, 1, 1, 30), # Tan = 1/sqrt(1+3) = 1/2 (không đẹp, bỏ)
                ]

                # Chọn ngẫu nhiên một bộ số từ danh sách hợp lệ
                hop_le = [(1, 3, 2, 45), (1, 9, 2, 60), (2, 1, 1, 30)]
                k1, k2, k3, goc_dung = random.choice(hop_le)

                # Hàm xử lý latex cho căn thức
                def format_can(k):
                    if k == 1: return "a"
                    if sqrt(k).is_integer: return str(int(sqrt(k))) + "a"
                    return "a\\sqrt{" + str(k) + "}"

                val_AB = format_can(k1)
                val_AD = format_can(k2)
                val_SA = format_can(k3)

                # Tính SB = sqrt(SA^2 + AB^2)
                k_SB = k3 + k1
                val_SB = format_can(k_SB)

                # Đáp án đúng
                da = goc_dung

                # Các đáp án sai
                tap_goc = [30, 45, 60, 90]
                tap_goc.remove(da)
                random.shuffle(tap_goc)
                das1, das2, das3 = tap_goc

                # Vẽ hình TikZ
                tikz_code = (
                    "\\begin{center}\n"
                    "\\begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm, line width=1pt]\n"
                    "\\coordinate (A) at (0,0);\n"
                    "\\coordinate (B) at (4,0);\n"
                    "\\coordinate (D) at (1.5,1.2);\n"
                    "\\coordinate (C) at (5.5,1.2);\n"
                    "\\coordinate (S) at (0,4);\n"
                    "\\draw [dashed] (S)--(D) (D)--(A) (D)--(C);\n"
                    "\\draw (S)--(A) (A)--(B) (B)--(C) (S)--(B) (S)--(C) (C)--(B);\n"
                    "\\draw (0.3,0) -- (0.3,0.3) -- (0,0.3);\n"
                    "\\begin{small}\n"
                    "\\draw (A) node[below left] {$A$};\n"
                    "\\draw (B) node[below right] {$B$};\n"
                    "\\draw (C) node[right] {$C$};\n"
                    "\\draw (D) node[above right] {$D$};\n"
                    "\\draw (S) node[above] {$S$};\n"
                    "\\end{small}\n"
                    "\\end{tikzpicture}\n"
                    "\\end{center}"
                )

                # Câu hỏi
                noidungcauhoi = (
                    "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật. "
                    "Biết $AB = %s$, $AD = %s$. Cạnh bên $SA \\perp \\left( ABCD \\right)$ và $SA = %s$. "
                    "Góc giữa đường thẳng $SC$ và mặt phẳng $\\left( SAB \\right)$ là"
                    % (val_AB, val_AD, val_SA)
                )

                # Các đáp án
                da_d = "\\True $%s^\\circ$" % da
                da_s1 = "$%s^\\circ$" % das1
                da_s2 = "$%s^\\circ$" % das2
                da_s3 = "$%s^\\circ$" % das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = (
                    "Ta có $BC \\perp AB$ (do $ABCD$ là hình chữ nhật), "
                    "$BC \\perp SA$ (do $SA \\perp \\left( ABCD \\right)$). "
                    "Suy ra $BC \\perp \\left( SAB \\right)$. \\\\"
                    "Hình chiếu vuông góc của đường thẳng $SC$ lên mặt phẳng $\\left( SAB \\right)$ là $SB$. \\\\"
                    "Suy ra góc giữa đường thẳng $SC$ và mặt phẳng $\\left( SAB \\right)$ là góc $\\widehat{BSC}$. \\\\"
                    "Xét tam giác $\\Delta SAB$ vuông tại $A$, ta có: "
                    "$SB = \\sqrt{SA^2 + AB^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$. \\\\"
                    "Xét tam giác $\\Delta SBC$ vuông tại $B$ (vì $BC \\perp \\left( SAB \\right) \\Rightarrow BC \\perp SB$), ta có: \\\\"
                    "$BC = AD = %s$. \\\\"
                    "Khi đó: $\\tan \\widehat{BSC} = \\frac{BC}{SB} = \\frac{%s}{%s} = %s$. \\\\"
                    "Suy ra $\\widehat{BSC} = %s^\\circ$. \\\\"
                    "Vậy góc giữa đường thẳng $SC$ và mặt phẳng $\\left( SAB \\right)$ bằng $%s^\\circ$."
                    % (val_SA, val_AB, val_SB, val_AD, val_AD, val_SB, latex(sqrt(k2)/sqrt(k_SB)), da, da)
                )

            # Xuất câu trắc nghiệm
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choice \n"
                "{" + str(list_1[0]) + "}\n"
                "{" + str(list_1[1]) + "}\n"
                "{" + str(list_1[2]) + "}\n"
                "{" + str(list_1[3]) + "}\n"
                "\\loigiai{" + str(tikz_code)+ str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

