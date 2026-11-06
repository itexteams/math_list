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


def bt_dang36_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            # Chuỗi hình vẽ TikZ của hình hộp ABCD.A'B'C'D' với độ dày nét 1pt
            tikz_str = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1.2, line width=1pt]\n'
                '\\coordinate (A) at (0.6, 0.8);\n'
                '\\coordinate (B) at (0, 0);\n'
                '\\coordinate (C) at (2.5, 0);\n'
                '\\coordinate (D) at (3.1, 0.8);\n'
                '\\coordinate (A1) at (0.6, 2.8);\n'
                '\\coordinate (B1) at (0, 2);\n'
                '\\coordinate (C1) at (2.5, 2);\n'
                '\\coordinate (D1) at (3.1, 2.8);\n'
                '\\draw[dashed] (A1)--(A) (A)--(B) (A)--(D);\n'
                '\\draw (B)--(C)--(D)--(D1)--(C1)--(B1)--(B) (B1)--(C1) (C1)--(D1)'
                ' (D1)--(A1)--(B1) (C)--(C1);\n'
                '\\node[left] at (A) {$A$};\n'
                '\\node[below left] at (B) {$B$};\n'
                '\\node[below right] at (C) {$C$};\n'
                '\\node[right] at (D) {$D$};\n'
                '\\node[above left] at (A1) {$A\'$};\n'
                '\\node[left] at (B1) {$B\'$};\n'
                '\\node[right] at (C1) {$C\'$};\n'
                '\\node[above right] at (D1) {$D\'$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            if dang == '1':
              vec_ask = "\\overrightarrow{A'D'}"
              vec_ans = '\\overrightarrow{AD}'
              vec_parallel = 'A\'D\' // AD // BC // B\'C\''
              vec_list = (
                  '\\overrightarrow{AD}, \\overrightarrow{DA}, \\overrightarrow{BC},'
                  ' \\overrightarrow{CB}, \\overrightarrow{B\'C\'}, \\overrightarrow{C\'B\'},'
                  ' \\overrightarrow{A\'D\'}, \\overrightarrow{D\'A\'}'
              )
              da = '$\\overrightarrow{AD}$'
              s = [
                  '$\\overrightarrow{BD}$',
                  '$\\overrightarrow{AB}$',
                  '$\\overrightarrow{AC}$',
                  '$\\overrightarrow{A\'B\'}$',
              ]

            elif dang == '2':
              vec_ask = "\\overrightarrow{A'B'}"
              vec_ans = '\\overrightarrow{AB}'
              vec_parallel = 'A\'B\' // AB // CD // C\'D\''
              vec_list = (
                  '\\overrightarrow{AB}, \\overrightarrow{BA}, \\overrightarrow{CD},'
                  ' \\overrightarrow{DC}, \\overrightarrow{C\'D\'}, \\overrightarrow{D\'C\'},'
                  ' \\overrightarrow{A\'B\'}, \\overrightarrow{B\'A\'}'
              )
              da = '$\\overrightarrow{AB}$'
              s = [
                  '$\\overrightarrow{AC}$',
                  '$\\overrightarrow{AD}$',
                  '$\\overrightarrow{BD}$',
                  '$\\overrightarrow{A\'D\'}$',
              ]

            else:
              vec_ask = '\\overrightarrow{AA\'}'
              vec_ans = '\\overrightarrow{BB\'}'
              vec_parallel = 'AA\' // BB\' // CC\' // DD\''
              vec_list = (
                  '\\overrightarrow{BB\'}, \\overrightarrow{B\'B}, \\overrightarrow{CC\'},'
                  ' \\overrightarrow{C\'C}, \\overrightarrow{DD\'}, \\overrightarrow{D\'D},'
                  ' \\overrightarrow{AA\'}, \\overrightarrow{A\'A}'
              )
              da = '$\\overrightarrow{BB\'}$'
              s = [
                  '$\\overrightarrow{AB}$',
                  '$\\overrightarrow{AD}$',
                  '$\\overrightarrow{AC}$',
                  '$\\overrightarrow{A\'C\'}$',
              ]

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            # Câu hỏi
            noidungcauhoi = (
                'Cho hình hộp $ABCD.A\'B\'C\'D\'$ (xem hình minh họa bên dưới). Vectơ nào'
                ' sau đây cùng phương với vectơ $%s$?\\\\'
                '%s' % (vec_ask, tikz_str)
            )

            # Các đáp án
            da_d = '\\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (
                'Trong hình hộp $ABCD.A\'B\'C\'D\'$, ta có $%s$.\\\\'
                'Do đó, các vectơ $%s$ đều cùng phương với nhau.\\\\'
                'Vậy vectơ cùng phương với vectơ $%s$ trong các phương án là $%s$.'
                % (vec_parallel, vec_list, vec_ask, vec_ans)
            )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

