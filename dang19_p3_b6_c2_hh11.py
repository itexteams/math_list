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


def bt_dang19_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của cạnh bên (cạnh bên = k, với a = 1)
                k = random.randint(2, 5)

                # Tính toán các thông số (với a = 1)
                # AI = sqrt(3)/2
                # AO = sqrt(3)/3
                # SO = sqrt(k^2 - (sqrt(3)/3)^2) = sqrt(k^2 - 1/3) = sqrt((3k^2 - 1)/3)
                # V = 1/3 * S_day * SO = 1/3 * (sqrt(3)/4) * (sqrt(3k^2 - 1)/sqrt(3)) = sqrt(3k^2 - 1)/12

                inner_val = 3 * k**2 - 1
                v_real = math.sqrt(inner_val) / 12

                # Đáp án đúng: làm tròn đến hàng phần chục
                kq_dung_num = round(v_real, 1)
                kq_dung = str(kq_dung_num)

                # Các đáp án sai (dựa trên logic cũ nhưng chuyển sang số thập phân)
                # Đảm bảo các đáp án sai không trùng với đáp án đúng
                s_list_raw = [
                    round(math.sqrt(inner_val) / 6, 1),
                    round(math.sqrt(inner_val) / 4, 1),
                    round(math.sqrt(3 * k**2 + 1) / 12, 1),
                    round(math.sqrt(k**2 + 2) / 12, 1)
                ]

                # Loại bỏ giá trị trùng với đáp án đúng và lấy 3 giá trị duy nhất
                s_list_unique = list(set([x for x in s_list_raw if x != kq_dung_num]))
                while len(s_list_unique) < 3:
                    s_list_unique.append(round(kq_dung_num + random.uniform(0.1, 0.5), 1))

                random.shuffle(s_list_unique)

                da_d = "\\True " + kq_dung
                da_s1 = str(s_list_unique[0])
                da_s2 = str(s_list_unique[1])
                da_s3 = str(s_list_unique[2])

                # Trộn các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    "Cho khối chóp tam giác đều $S.ABC$ có cạnh đáy bằng $1$ và cạnh bên bằng $%s$. "
                    "Thể tích $V$ của khối chóp $S.ABC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                    % (latex(k))
                )

                # TikZ code giữ nguyên
                tikz_code = (
                    "\\begin{center}\n"
                    "\\begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]\n"
                    "\\coordinate (A) at (-1.5,-1);\n"
                    "\\coordinate (B) at (0,-2);\n"
                    "\\coordinate (C) at (2.5,-1);\n"
                    "\\coordinate (I) at ($(B)!0.5!(C)$);\n"
                    "\\coordinate (O) at ($(A)!2/3!(I)$);\n"
                    "\\coordinate (S) at ($(O)+(0,3.5)$);\n"
                    "\\draw (S)--(A)--(B)--(C)--(S)--(B);\n"
                    "\\draw [dashed] (A)--(C) (S)--(O) (A)--(I) (O)--(B) (O)--(C);\n"
                    "\\node [left] at (A) {$A$};\n"
                    "\\node [below] at (B) {$B$};\n"
                    "\\node [right] at (C) {$C$};\n"
                    "\\node [above] at (S) {$S$};\n"
                    "\\node [below] at (O) {$O$};\n"
                    "\\node [below right] at (I) {$I$};\n"
                    "\\end{tikzpicture}\n"
                    "\\end{center}"
                )

                # Lời giải chi tiết (bỏ tham số a)
                loigiai = (
                    "Do đáy là tam giác đều cạnh bằng $1$ nên gọi $I$ là trung điểm cạnh $BC$, khi đó $AI$ là đường cao của tam giác đáy. "
                    "Ta có $AI = \\frac{\\sqrt{3}}{2}$, và $AO = \\frac{2}{3}AI = \\frac{\\sqrt{3}}{3}$.\\\\ \n"
                    "Trong tam giác $SOA$ vuông tại $O$ ta có $SO = \\sqrt{%s^2 - \\left(\\frac{\\sqrt{3}}{3}\\right)^2} = \\sqrt{%s - \\frac{1}{3}} = \\frac{\\sqrt{%s}}{\\sqrt{3}}$.\\\\ \n"
                    "Diện tích tam giác đáy $ABC$ là $S_{ABC} = \\frac{\\sqrt{3}}{4}$.\\\\ \n"
                    "Vậy thể tích khối chóp $S.ABC$ là $V = \\frac{1}{3} S_{ABC} \\cdot SO = \\frac{1}{3} \\cdot \\frac{\\sqrt{3}}{4} \\cdot \\frac{\\sqrt{%s}}{\\sqrt{3}} = \\frac{\\sqrt{%s}}{12} \\approx %s$."
                    % (latex(k), latex(k**2), latex(3*k**2-1), latex(3*k**2-1), latex(3*k**2-1), kq_dung)
                )
                dapan='\\shortans[0]{$%s$}\n'%(str(kq_dung).replace('.', ','))

            # Xuất câu trắc nghiệm
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + str(noidungcauhoi) + str(dapan)+
                "\\loigiai{" + str(tikz_code)+ str(loigiai) + "}\n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content

