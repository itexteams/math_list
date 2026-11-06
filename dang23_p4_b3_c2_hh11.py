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


def bt_dang23_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo các dạng toán (ở đây tập trung vào bài toán hình chóp có góc ADC = 60 độ)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của cạnh hình thoi (m*a) và chiều cao SO (h*a)
                # Để ra góc đẹp, ta chọn các bộ số đặc biệt
                # TH1: SO = a, Side = 2a -> tan = 1/sqrt(3) -> 30 độ
                # TH2: SO = a*sqrt(3), Side = 2a -> tan = 1 -> 45 độ
                # TH3: SO = 3a, Side = 2a -> tan = sqrt(3) -> 60 độ

                scenarios = [
                    {'so_val': 'a', 'so_tex': 'a', 'tan_val': '1/\\sqrt{3}', 'ans': '30^\\circ'},
                    {'so_val': 'a\\sqrt{3}', 'so_tex': 'a\\sqrt{3}', 'tan_val': '1', 'ans': '45^\\circ'},
                    {'so_val': '3a', 'so_tex': '3a', 'tan_val': '\\sqrt{3}', 'ans': '60^\\circ'}
                ]

                sel = random.choice(scenarios)
                so_text = sel['so_tex']
                tan_text = sel['tan_val']
                dap_an_dung = sel['ans']

                # Các phương án nhiễu
                cac_goc = ['30^\\circ', '45^\\circ', '60^\\circ', '75^\\circ', '15^\\circ', '90^\\circ']
                cac_goc.remove(dap_an_dung)
                random.shuffle(cac_goc)

                da_s1 = '$' + cac_goc[0] + '$'
                da_s2 = '$' + cac_goc[1] + '$'
                da_s3 = '$' + cac_goc[2] + '$'
                da_d = '\\True $' + dap_an_dung + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # TikZ Drawing
                # Lưu ý: Thay đổi nét vẽ 1pt và không dùng raw string (dùng \\)
                hinh_ve = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, line width=1pt, font=\\footnotesize]\n'
                    '\\coordinate (D) at (0,0);\n'
                    '\\coordinate (C) at (3,0);\n'
                    '\\coordinate (A) at (1.5,1.2);\n'
                    '\\coordinate (B) at (4.5,1.2);\n'
                    '\\coordinate (O) at (2.25,0.6);\n'
                    '\\coordinate (S) at (2.25,3.5);\n'
                    '\\draw [dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(C) (B)--(D) (S)--(O);\n'
                    '\\draw (S)--(D)--(C)--(B)--cycle (S)--(C);\n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$};\n'
                    '\\fill (B) circle (1.5pt) node[right] {$B$};\n'
                    '\\fill (C) circle (1.5pt) node[below right] {$C$};\n'
                    '\\fill (D) circle (1.5pt) node[below left] {$D$};\n'
                    '\\fill (O) circle (1.5pt) node[below] {$O$};\n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                noidungcauhoi = (
                    'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi cạnh $2a$, $\\widehat{ADC} = 60^\\circ$. '
                    'Gọi $O$ là giao điểm của $AC$ và $BD$, $SO \\perp \\left( ABCD \\right)$ và $SO = ' + so_text + '$. '
                    'Tính góc giữa đường thẳng $SD$ và mặt phẳng $\\left( ABCD \\right)$.'
                )

                loigiai = (
                    'Ta có $ABCD$ là hình thoi cạnh $2a$, và $\\widehat{ADC} = 60^\\circ$ nên $\\triangle ACD$ đều. '
                    'Khi đó $O$ là trung điểm của $AC$ và $BD$, đồng thời $DO$ là đường cao của tam giác đều $ACD$ cạnh $2a$. \\\\'
                    'Suy ra $DO = \\frac{2a \\cdot \\sqrt{3}}{2} = a\\sqrt{3}$. \\\\'
                    'Vì $SO \\perp \\left( ABCD \\right)$ nên $O$ là hình chiếu của $S$ lên mặt phẳng $\\left( ABCD \\right)$. \\\\'
                    'Do đó, góc giữa đường thẳng $SD$ và mặt phẳng $\\left( ABCD \\right)$ là góc $\\widehat{SDO}$. \\\\'
                    'Trong tam giác vuông $SOD$, ta có: \\\\'
                    '$\\tan \\widehat{SDO} = \\frac{SO}{DO} = \\frac{' + so_text + '}{a\\sqrt{3}} = ' + tan_text + '$. \\\\'
                    'Suy ra $\\widehat{SDO} = ' + dap_an_dung + '$.'
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

