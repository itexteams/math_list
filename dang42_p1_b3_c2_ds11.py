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


def bt_dang42_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng số hạng n của cấp số nhân (để tạo biến thể bài toán)
                n = random.randint(12, 25)
                S = n + 1

                # Chọn các cặp đúng (tổng chỉ số bằng S = n + 1) để làm đáp án nhiễu
                a_cands = list(range(2, n//2 + 1))
                random.shuffle(a_cands)
                a1, a2, a3 = a_cands[:3]
                b1 = S - a1
                b2 = S - a2
                b3 = S - a3

                # Chọn cặp sai (tổng chỉ số khác S) để làm đáp án đúng của câu hỏi "tìm đẳng thức sai"
                c = random.randint(3, n//2)
                offset = random.choice([-1, 1, 2, -2])
                d = S - c + offset

                # Đẳng thức sai (đáp án đúng)
                da_dung = 'u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}' % (n, c, d)

                # Các đẳng thức đúng (đáp án nhiễu)
                das1 = 'u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}' % (n, a1, b1)
                das2 = 'u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}' % (n, a2, b2)
                das3 = 'u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}' % (n, a3, b3)

                du = ['$%s$' % (da_dung)]
                da = random.choice(du)

                # Câu hỏi
                noidungcauhoi = ('''Cho một cấp số nhân có $%s$ số hạng. Đẳng thức nào sau đây là sai?''' % (n))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2
                da_s3 = '$%s$' % das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Giả sử cấp số nhân có số hạng đầu là $u_1$ và công bội là $q$.\\\\
                          Theo công thức số hạng tổng quát của cấp số nhân $u_k = u_1 \\cdot q^{k-1}$, ta có:\\\\
                          $u_k \\cdot u_m = (u_1 \\cdot q^{k-1}) \\cdot (u_1 \\cdot q^{m-1}) = u_1^2 \\cdot q^{k+m-2}$.\\\\
                          Suy ra $u_k \\cdot u_m = u_p \\cdot u_q \\Leftrightarrow k+m = p+q$.\\\\
                          Xét các đẳng thức ở đề bài, vế trái luôn là $u_1 \\cdot u_{%s}$ có tổng các chỉ số là $1 + %s = %s$.\\\\
                          Ta thấy:\\\\
                          - Vì $%s + %s = %s$, do đó $u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}$ là đẳng thức đúng.\\\\
                          - Vì $%s + %s = %s$, do đó $u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}$ là đẳng thức đúng.\\\\
                          - Vì $%s + %s = %s$, do đó $u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}$ là đẳng thức đúng.\\\\
                          - Vì $%s + %s = %s \\neq %s$, do đó $u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}$ là đẳng thức sai.\\\\
                          Vậy đẳng thức sai là $u_1 \\cdot u_{%s} = u_{%s} \\cdot u_{%s}$.'''
                         % (n, n, S,
                            a1, b1, S, n, a1, b1,
                            a2, b2, S, n, a2, b2,
                            a3, b3, S, n, a3, b3,
                            c, d, c+d, S, n, c, d,
                            n, c, d))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

