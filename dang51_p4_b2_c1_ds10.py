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


def bt_dang51_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến loại câu hỏi
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số liệu bài toán
                # n_TVH là số học sinh thích cả 3 môn (phần giao của 3 tập hợp)
                n_TVH = random.randint(3, 6)

                # Số học sinh thích 2 môn (phải lớn hơn n_TVH)
                n_TV = n_TVH + random.randint(3, 7)
                n_VH = n_TVH + random.randint(2, 5)
                n_TH = n_TVH + random.randint(3, 6)

                # Số học sinh thích từng môn (phải lớn hơn tổng các phần giao liên quan)
                # n_T >= n_TV + n_TH - n_TVH
                n_T = (n_TV + n_TH - n_TVH) + random.randint(5, 12)
                n_V = (n_TV + n_VH - n_TVH) + random.randint(3, 10)
                n_H = (n_TH + n_VH - n_TVH) + random.randint(5, 10)

                # Tính toán đáp án theo công thức bao hàm - loại trừ cho 3 tập hợp:
                # |A u B u C| = |A| + |B| + |C| - (|A n B| + |B n C| + |C n A|) + |A n B n C|
                kq_dung = n_T + n_V + n_H - (n_TV + n_VH + n_TH) + n_TVH

                # Tạo các phương án sai
                s = set()
                while len(s) < 3:
                    # Sai lầm phổ biến: quên cộng phần giao 3 môn
                    sai1 = n_T + n_V + n_H - (n_TV + n_VH + n_TH)
                    # Sai lầm phổ biến: không trừ các phần giao 2 môn
                    sai2 = n_T + n_V + n_H
                    # Sai lầm ngẫu nhiên
                    sai3 = kq_dung + random.choice([-5, -3, 2, 5, 7])

                    for val in [sai1, sai2, sai3]:
                        if val != kq_dung and val > 0:
                            s.add(val)
                    if len(s) < 3:
                        s.add(kq_dung + random.randint(1, 10))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Kết quả khảo sát tại lớp 11A1 có: $%s$ học sinh thích môn Toán; $%s$ học sinh thích Vật lý và $%s$ học sinh thích môn Hóa học. Biết rằng có $%s$ học sinh thích hai môn Toán và Vật lý; $%s$ học sinh thích hai môn Vật lý và Hóa học; $%s$ học sinh thích hai môn Toán và Hóa học; $%s$ học sinh thích cả ba môn. Tìm số học sinh thích ít nhất một trong ba môn Toán, Vật lý và Hóa học.'''
                                 % (latex(n_T), latex(n_V), latex(n_H), 
                                    latex(n_TV), latex(n_VH), latex(n_TH), latex(n_TVH)))

                # Các đáp án
                da_d = ('\\True ' + str(kq_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[thick, set/.style={circle, minimum size=3cm, fill opacity=0.3}]
                \\draw[line width=1pt] (0,0) circle (1.5cm) node[shift={(0,1)}] {$T$};
                \\draw[line width=1pt] (2,0) circle (1.5cm) node[shift={(0,1)}] {$V$};
                \\draw[line width=1pt] (1,-1.5) circle (1.5cm) node[shift={(0,-1)}] {$H$};
                \\node at (1,-0.5) {$%s$};
                \\end{tikzpicture}
                \\end{center}
                Gọi $T, V, H$ lần lượt là tập hợp các học sinh thích môn Toán, Vật lý và Hóa học. \\\\
                             Theo giả thiết, ta có: \\\\
                             $n\\left(T\\right)=%s, n\\left(V\\right)=%s, n\\left(H\\right)=%s$. \\\\
                             $n\\left(T \\cap V\\right)=%s, n\\left(V \\cap H\\right)=%s, n\\left(T \\cap H\\right)=%s$. \\\\
                             $n\\left(T \\cap V \\cap H\\right)=%s$. \\\\
                             Số học sinh thích ít nhất một trong ba môn là số phần tử của tập hợp $T \\cup V \\cup H$. \\\\
                             Áp dụng công thức bao hàm - loại trừ cho ba tập hợp: \\\\
                             $n\\left(T \\cup V \\cup H\\right) = n\\left(T\\right) + n\\left(V\\right) + n\\left(H\\right) - \\left[n\\left(T \\cap V\\right) + n\\left(V \\cap H\\right) + n\\left(T \\cap H\\right)\\right] + n\\left(T \\cap V \\cap H\\right)$ \\\\
                             $n\\left(T \\cup V \\cup H\\right) = %s + %s + %s - \\left(%s + %s + %s\\right) + %s = %s$. \\\\
                             Vậy có $%s$ học sinh thích ít nhất một trong ba môn.'''
                           % (latex(n_TVH),
                               latex(n_T), latex(n_V), latex(n_H),
                              latex(n_TV), latex(n_VH), latex(n_TH),
                              latex(n_TVH),
                              latex(n_T), latex(n_V), latex(n_H),
                              latex(n_TV), latex(n_VH), latex(n_TH),
                              latex(n_TVH), latex(kq_dung),
                              latex(kq_dung)             
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

