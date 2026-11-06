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


def bt_dang23_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Bước 1: Khởi tạo các biến số ngẫu nhiên
            # Cho a là một số nguyên ngẫu nhiên từ 2 đến 10 để tính toán sinh động
            a_val = random.randint(2, 9)
            # Cố định hệ số căn 3 để giữ góc 60 độ đẹp như trong đề bài gốc
            he_so_sa = sqrt(3)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thoi cạnh $a = %s$. Cho biết $SA = %s\\sqrt{3}$, $SA \\perp AB, SA \\perp AD$.''' 
                             '\\begin{center}\n'
                             '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n'
                             '\\coordinate (A) at (0,0);\n'
                             '\\coordinate (B) at (-1.2,-1.2);\n'
                             '\\coordinate (D) at (2.5,0);\n'
                             '\\coordinate (C) at ($(B)+(D)-(A)$);\n'
                             '\\coordinate (S) at (0,3);\n'
                             '\\draw (S)--(B)--(C)--(D)--(S)--(C);\n'
                             '\\draw[dashed] (S)--(A)--(B) (A)--(D);\n'
                             '\\node at (A) [above left] {$A$};\n'
                             '\\node at (B) [below left] {$B$};\n'
                             '\\node at (C) [below right] {$C$};\n'
                             '\\node at (D) [right] {$D$};\n'
                             '\\node at (S) [above] {$S$};\n'
                             '\\draw (0,0.2)--(0.2,0.2)--(0.2,0);\n'
                             '\\draw (-0.15,-0.15)--(0.05,-0.35)--(0.2,-0.2);\n'
                             '\\end{tikzpicture}\n'
                             '\\end{center}'
                             %(latex(a_val), latex(a_val)))

            ########################################################################
            # (a) Nhận biết: Góc giữa SA và AB
            ########################################################################
            nb_da_1_d = '\\True $(AB, SA) = 90^\\circ$'
            nb_da_1_s = '$(AB, SA) = 60^\\circ$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Vì $SA \\perp AB$ theo giả thiết nên góc giữa hai đường thẳng $SA$ và $AB$ bằng $90^\\circ$.''')

            ########################################################################
            # (b) Thông hiểu: SA vuông góc với CD
            ########################################################################
            th_da_1_d = '\\True $SA \\perp CD$'
            th_da_1_s = '$SA$ không vuông góc với $CD$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $\\begin{cases} SA \\perp AB \\\\ SA \\perp AD \\end{cases} \\Rightarrow SA \\perp (ABCD)$.\\\\ 
                            Mà $CD \\subset (ABCD)$ nên $SA \\perp CD$.''')

            ########################################################################
            # (c) Vận dụng: So sánh góc (SD, BC) và (SD, CD)
            ########################################################################
            # Trong hình thoi tổng quát, góc (SD, BC) = (SD, AD). 
            # Góc (SD, CD) phụ thuộc vào đường chéo AC, thường không bằng góc SDA.
            vd_da_1_d = '$(SD, BC) = (SD, CD)$'
            vd_da_1_s = '\\True $(SD, BC) \\neq (SD, CD)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $BC \\parallel AD$ nên $(SD, BC) = (SD, AD) = \\widehat{SDA}$.\\\\
                            Trong tam giác vuông $SAD$ tại $A$: $\\tan \\widehat{SDA} = \\frac{SA}{AD} = \\frac{%s\\sqrt{3}}{%s} = \\sqrt{3} \\Rightarrow \\widehat{SDA} = 60^\\circ$.\\\\
                            Góc $(SD, CD)$ phụ thuộc vào độ dài đường chéo $AC$ của hình thoi, nên thông thường $(SD, BC) \\neq (SD, CD)$.'''
                            %(latex(a_val), latex(a_val)))

            ########################################################################
            # (d) Vận dụng cao: Tính góc SDA
            ########################################################################
            vdc_da_1_d = '\\True $\\widehat{SDA} = 60^\\circ$'
            vdc_da_1_s = '$\\widehat{SDA} = 30^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét tam giác $SAD$ vuông tại $A$ (do $SA \\perp AD$).\\\\
                            Ta có $\\tan \\widehat{SDA} = \\frac{SA}{AD} = \\frac{%s\\sqrt{3}}{%s} = \\sqrt{3}$.\\\\
                            Suy ra $\\widehat{SDA} = 60^\\circ$.'''
                             %(latex(a_val), latex(a_val)))

            # --- Phần logic xáo trộn và xuất nội dung ---

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

