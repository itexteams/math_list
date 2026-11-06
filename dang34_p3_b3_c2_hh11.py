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


def bt_dang34_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số cho bài toán
                # k là hệ số của a cho cạnh (cạnh đáy = 2ka, OA = ka)
                k = randint(1, 3)
                canh_day = 2 * k
                oa_val = k

                # Chọn ngẫu nhiên đáp án đúng là 30, 45, hoặc 60 độ
                list_goc = [30, 45, 60]
                goc_dung = random.choice(list_goc)

                # Tính toán SA dựa trên góc đã chọn để tan(ASO) = OA/SA
                # SA = OA / tan(goc)
                if goc_dung == 30:
                    # tan(30) = 1/sqrt(3) => SA = OA * sqrt(3)
                    sa_latex = latex(k * sqrt(3)) + 'a'
                    if k == 1: sa_latex = '\\sqrt{3}a'
                    tan_val_latex = '\\frac{1}{\\sqrt{3}}'
                elif goc_dung == 45:
                    # tan(45) = 1 => SA = OA
                    sa_latex = str(k) + 'a'
                    if k == 1: sa_latex = 'a'
                    tan_val_latex = '1'
                else: # 60 độ
                    # tan(60) = sqrt(3) => SA = OA / sqrt(3) = (k*sqrt(3))/3
                    sa_latex = latex(Rational(k, 3) * sqrt(3)) + 'a'
                    tan_val_latex = '\\sqrt{3}'

                # Đáp án đúng
                da = '$%s^\\circ$' % (goc_dung)

                # Các đáp án sai (không trùng đáp án đúng)
                s_full = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ', '15^\\circ']
                s_filtered = [item for item in s_full if item != str(goc_dung) + '^\\circ']
                random.shuffle(s_filtered)

                das1 = '$' + s_filtered[0] + '$'
                das2 = '$' + s_filtered[1] + '$'
                das3 = '$' + s_filtered[2] + '$'

                # Vẽ hình TikZ (độ dày 1pt, đúng các điểm trong đề bài)
                hinh_tikz = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, line width=1pt]\n'
                    '\\coordinate (A) at (0,0);\n'
                    '\\coordinate (B) at (3,0);\n'
                    '\\coordinate (D) at (-1.5,-1.2);\n'
                    '\\coordinate (C) at ($(B)+(D)-(A)$);\n'
                    '\\coordinate (S) at (0,3.5);\n'
                    '\\coordinate (O) at ($(A)!0.5!(C)$);\n'
                    '\\coordinate (H) at ($(S)!0.6!(O)$);\n'
                    '\\draw[dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (A)--(H);\n'
                    '\\draw (S)--(D)--(C)--(B)--(S)--(C);\n'
                    '\\foreach \\p/\\pos in {S/above, A/left, B/right, C/below, D/left, O/below, H/right}\n'
                    '\\fill (\\p) circle (1.5pt) node[\\pos] {$\\p$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Cho hình chóp $S.ABCD$ có đáy là hình thoi cạnh $%sa$, $\\widehat{ABC} = 60^\\circ$, $SA = %s$ và $SA \\perp (ABCD)$. Góc giữa $SA$ và mặt phẳng $(SBD)$ bằng bao nhiêu?'
                    % (latex(canh_day), sa_latex)
                )

                # Nội dung lời giải (viết chi tiết, không viết tắt)
                loigiai = (
                    'Gọi $O$ là tâm của hình thoi $ABCD$, gọi $H$ là hình chiếu vuông góc của $A$ lên $SO$, ta có:\\\\\n'
                    '$\\begin{cases} BD \\perp AC \\\\ BD \\perp SA \\end{cases} \\Rightarrow BD \\perp (SAC) \\Rightarrow BD \\perp AH$.\\\\\n'
                    'Từ $AH \\perp SO, AH \\perp BD$ suy ra $AH \\perp (SBD)$, hay $SH$ là hình chiếu vuông góc của $SA$ lên $(SBD)$.\\\\\n'
                    'Suy ra $\\widehat{\\left(SA, (SBD)\\right)} = \\widehat{\\left(SA, SO\\right)} = \\widehat{ASO}$.\\\\\n'
                    'Ta có $\\triangle ABC$ đều cạnh $%sa$ nên $OA = %sa$.\\\\\n'
                    '$\\triangle SAO$ vuông tại $A$ nên $\\tan \\widehat{ASO} = \\frac{OA}{SA} = \\frac{%sa}{%s} = %s \\Rightarrow \\widehat{ASO} = %s^\\circ$.'
                    % (latex(canh_day), latex(oa_val), latex(oa_val), sa_latex, tan_val_latex, goc_dung)
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(goc_dung)

                # Trộn đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xuất câu trắc nghiệm (không dùng raw string, format dấu phẩy cho số thập phân nếu có)
                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi).replace('.', ',') + '\n'+str(dapan)+
                    '\\loigiai{' + hinh_tikz+ str(loigiai).replace('.', ',') + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n' )
            return content

