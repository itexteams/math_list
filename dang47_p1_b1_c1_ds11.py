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


def bt_dang47_p1_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập random bài toán
                # Có 2 trường hợp chính để random cho mút cuối là L,N hoặc M,P
                case = random.choice([1, 2])

                if case == 1:
                    angle_latex = "-\\frac{3\\pi}{4}"
                    ans_text = "$L$ hoặc $N$"
                    wrong_options = ["$L$ hoặc $P$", "$M$ hoặc $P$", "$M$ hoặc $N$"]
                    # Giải thích: k=0 -> -135 độ (N), k=1 -> 45 độ (L)
                    explanation = "Với $k=0$, ta có $\\alpha = -\\frac{3\\pi}{4} \\equiv -135^\\circ$ (điểm $N$). \\\\ Với $k=1$, ta có $\\alpha = -\\frac{3\\pi}{4} + \\pi = \\frac{\\pi}{4} \\equiv 45^\\circ$ (điểm $L$)."
                else:
                    angle_latex = "-\\frac{\\pi}{4}"
                    ans_text = "$M$ hoặc $P$"
                    wrong_options = ["$L$ hoặc $N$", "$L$ hoặc $P$", "$M$ hoặc $N$"]
                    # Giải thích: k=0 -> -45 độ (P), k=1 -> 135 độ (M)
                    explanation = "Với $k=0$, ta có $\\alpha = -\\frac{\\pi}{4} \\equiv -45^\\circ$ (điểm $P$). \\\\ Với $k=1$, ta có $\\alpha = -\\frac{\\pi}{4} + \\pi = \\frac{3\\pi}{4} \\equiv 135^\\circ$ (điểm $M$)."

                # Đáp án
                da = '%s' % ans_text

                # B4: Điều chỉnh các phương án sai
                s = [wrong_options[0], wrong_options[1], wrong_options[2]]
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $L, M, N, P$ lần lượt là điểm chính giữa các cung $AB, BC, CD, DA$. Cung $\\alpha$ có mút đầu trùng với $A$ và số đo $\\alpha = %s + k\\pi$. Mút cuối của $\\alpha$ ở đâu? \\\\'''% (angle_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center} \\begin{tikzpicture}[scale=1.5, line width=1pt]
                \\draw (0,0) circle (1);
                \\coordinate (A) at (1,0); \\node at (1.2,0) {$A$};
                \\coordinate (B) at (0,1); \\node at (0,1.2) {$B$};
                \\coordinate (C) at (-1,0); \\node at (-1.2,0) {$C$};
                \\coordinate (D) at (0,-1); \\node at (0,-1.2) {$D$};
                \\coordinate (L) at (0.707,0.707); \\node at (0.9,0.9) {$L$};
                \\coordinate (M) at (-0.707,0.707); \\node at (-0.9,0.9) {$M$};
                \\coordinate (N) at (-0.707,-0.707); \\node at (-0.9,-0.9) {$N$};
                \\coordinate (P) at (0.707,-0.707); \\node at (0.9,-0.9) {$P$};
                \\end{tikzpicture} \\end{center} Các điểm $L, M, N, P$ là điểm chính giữa các cung phần tư. Ta có tọa độ góc tương ứng trên đường tròn lượng giác là: $L \\equiv 45^\\circ, M \\equiv 135^\\circ, N \\equiv 225^\\circ (\\equiv -135^\\circ), P \\equiv 315^\\circ (\\equiv -45^\\circ)$. \\\\
            Số đo cung $\\alpha = %s + k\\pi$. \\\\
            %s \\\\
            Vậy mút cuối của cung $\\alpha$ trùng với %s.'''
                           % (angle_latex, explanation, ans_text))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

