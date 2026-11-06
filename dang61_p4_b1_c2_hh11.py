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


def bt_dang61_p4_b1_c2_hh11(self):
            # Khai báo biến
            a_val = random.randint(1, 10) # Độ dài cạnh hình lập phương


            AC_sq = 2 * (a_val**2)
            AP_sq = (a_val**2) / 4 + 2 * (a_val**2)
            PC_sq = (a_val**2) / 4 + (a_val**2)

            # Cosin góc PAC = (AC^2 + AP^2 - PC^2) / (2 * AC * AP)
            cos_val = (AC_sq + AP_sq - PC_sq) / (2 * sqrt(AC_sq) * sqrt(AP_sq))
            angle = 45 # Cố định theo hình học đặc biệt này

            # B4-Điều chỉnh các phương án sai
            answers = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ']
            correct_ans = '45^\\circ'

            # Trộn đáp án
            da_d = '\\True $' + correct_ans + '$'
            wrong_ans = [a for a in answers if a != '45^\\circ']
            random.shuffle(wrong_ans)

            da_s1 = '$' + wrong_ans[0] + '$'
            da_s2 = '$' + wrong_ans[1] + '$'
            da_s3 = '$' + wrong_ans[2] + '$'

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình lập phương $ABCD.A\'B\'C\'D\'$. Gọi $M, N, P$ lần lượt là trung điểm của $AB, BC, C\'D\'$. '
                'Tính góc giữa $MN$ và $AP$.'
            )

            # Hình vẽ TikZ
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1.5, line join=round, line cap=round]\n'
                '   \\coordinate (A) at (0,0); \\coordinate (B) at (2,0); \\coordinate (D) at (0.8,0.7);\n'
                '   \\coordinate (C) at ($(B)+(D)-(A)$); \\coordinate (A1) at (0,2);\n'
                '   \\coordinate (B1) at (2,2); \\coordinate (D1) at (0.8,2.7); \\coordinate (C1) at ($(B1)+(D1)-(A1)$);\n'
                '   \\draw (A1)--(A) (A1)--(B1)--(C1)--(D1)--cycle; \\draw (A)--(B)--(C); \\draw (B1)--(B) (C1)--(C);\n'
                '   \\draw[dashed] (A)--(D)--(C) (D1)--(D);\n'
                '   \\coordinate (M) at ($(A)!0.5!(B)$); \\coordinate (N) at ($(B)!0.5!(C)$); \\coordinate (P) at ($(C1)!0.5!(D1)$);\n'
                '   \\draw[dashed] (M)--(N); \\draw[dashed] (A)--(P);\n'
                '   \\draw[dashed] (A)--(C) (P)--(C);\n'
                '   \\foreach \\p/\\pos in {A/left, B/below, C/right, D/above left, A1/left, B1/above, C1/right, D1/above, M/below, N/right, P/above} \\fill (\\p) node[\\pos] {$\\p$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Lời giải chi tiết
            loigiai = (
                'Ta có $MN$ song song với $AC$ (do $MN$ là đường trung bình của tam giác $ABC$). \\\\\n'
                'Khi đó góc giữa $MN$ và $AP$ chính là góc giữa $AC$ và $AP$, tức là $(MN, AP) = (AC, AP) = \\widehat{PAC}$. \\\\\n'
                'Giả sử hình lập phương $ABCD.A\'B\'C\'D\'$ có độ dài các cạnh bằng ' + str(a_val) + '. \\\\\n'
                'Xét tam giác $APC$, ta tính độ dài các cạnh như sau: \\\\\n'
                '$PC = \\sqrt{C\'C^2 + C\'P^2} = \\sqrt{' + str(a_val) + '^2 + \\left(\\frac{' + str(a_val) + '}{2}\\right)^2} = \\frac{' + str(a_val) + '\\sqrt{5}}{2}$. \\\\\n'
                '$AC = \\sqrt{AB^2 + BC^2} = \\sqrt{' + str(a_val) + '^2 + ' + str(a_val) + '^2} = ' + str(a_val) + '\\sqrt{2}$. \\\\\n'
                '$AP = \\sqrt{AD^2 + DD\'^2 + D\'P^2} = \\sqrt{' + str(a_val) + '^2 + ' + str(a_val) + '^2 + \\left(\\frac{' + str(a_val) + '}{2}\\right)^2} = \\frac{3 \\cdot ' + str(a_val) + '}{2}$. \\\\\n'
                'Theo định lý hàm cos trong tam giác $APC$, ta có: \\\\\n'
                '$\\cos \\widehat{PAC} = \\frac{AC^2 + AP^2 - PC^2}{2 \\cdot AC \\cdot AP} = \\frac{2 \\cdot ' + str(a_val**2) + ' + \\frac{9}{4} ' + str(a_val**2) + ' - \\frac{5}{4} ' + str(a_val**2) + '}{2 \\cdot ' + str(a_val) + '\\sqrt{2} \\cdot \\frac{3}{2} ' + str(a_val) + '} = \\frac{3 ' + str(a_val**2) + '}{3\\sqrt{2} ' + str(a_val**2) + '} = \\frac{1}{\\sqrt{2}}$. \\\\\n'
                'Suy ra $\\widehat{PAC} = 45^\\circ$.'
            )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\loigiai{' + tikz_code+ loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

