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


def bt_dang37_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            # Chuỗi hình vẽ TikZ theo chuẩn nét 1pt
            tikz_str = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=0.8, line width=1pt]\n'
                '\\coordinate (A) at (0,0);\n'
                '\\coordinate (B) at (-1,-1.2);\n'
                '\\coordinate (C) at (1.8,-1.2);\n'
                '\\coordinate (D) at (2.8,0);\n'
                '\\coordinate (S) at (0,2.8);\n'
                '\\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D);\n'
                '\\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);\n'
                '\\node[left] at (A) {$A$};\n'
                '\\node[below left] at (B) {$B$};\n'
                '\\node[below right] at (C) {$C$};\n'
                '\\node[right] at (D) {$D$};\n'
                '\\node[above] at (S) {$S$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            if dang == '1':
              line_ask = 'BC'
              da = '$(SAB)$'
              s = ['$(SCD)$', '$(SBC)$', '$(SBD)$']

              das1 = random.choice(s)
              s.remove(das1)
              das2 = random.choice(s)
              s.remove(das2)
              das3 = random.choice(s)

              # Câu hỏi
              noidungcauhoi = (
                  'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA$ vuông góc với'
                  ' $(ABCD)$. Đường thẳng $%s$ vuông góc với mặt phẳng nào trong các mặt'
                  ' phẳng sau đây?\\\\'
                  '%s' % (line_ask, tikz_str)
              )

              # Lời giải
              loigiai = (
                  'Ta có:\\\\'
                  '$\\begin{cases} %s \\perp AB \\text{ (do } ABCD \\text{ là hình vuông)}'
                  ' \\\\ %s \\perp SA \\text{ (do } SA \\perp (ABCD)\\text{)} \\end{cases}'
                  ' \\Rightarrow %s \\perp (SAB)$.' % (line_ask, line_ask, line_ask)
              )

            elif dang == '2':
              line_ask = 'CD'
              da = '$(SAD)$'
              s = ['$(SCD)$', '$(SBC)$', '$(SBD)$']

              das1 = random.choice(s)
              s.remove(das1)
              das2 = random.choice(s)
              s.remove(das2)
              das3 = random.choice(s)

              # Câu hỏi
              noidungcauhoi = (
                  'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA$ vuông góc với'
                  ' $(ABCD)$. Đường thẳng $%s$ vuông góc với mặt phẳng nào trong các mặt'
                  ' phẳng sau đây?\\\\'
                  '%s' % (line_ask, tikz_str)
              )

              # Lời giải
              loigiai = (
                  'Ta có:\\\\'
                  '$\\begin{cases} %s \\perp AD \\text{ (do } ABCD \\text{ là hình vuông)}'
                  ' \\\\ %s \\perp SA \\text{ (do } SA \\perp (ABCD)\\text{)} \\end{cases}'
                  ' \\Rightarrow %s \\perp (SAD)$.' % (line_ask, line_ask, line_ask)
              )

            # Các đáp án
            da_d = '\\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

