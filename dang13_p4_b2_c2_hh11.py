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


def bt_dang13_p4_b2_c2_hh11(self):
            # Khai báo biến
            # --- KHAI BÁO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các giá trị ngẫu nhiên
                a_val = random.randint(2, 6)  # Cạnh đáy
                h_val = random.randint(3, 7)  # Chiều cao SA

                # Đáp án đúng
                dap_an_dung = 'AN \\perp (SDO)'

                # Các phương án sai (đảm bảo không trùng đáp án đúng)
                s = [
                    'AC \\perp (SDO)',
                    'AM \\perp (SDO)',
                    'SA \\perp (SDO)',
                    'AB \\perp (SDO)',
                    'SD \\perp (SAC)',
                    'SO \\perp (ABCD)'
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- CÂU HỎI ---
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông tâm $O$ và vuông góc với mặt phẳng đáy. Gọi $N$ là hình chiếu vuông góc của $A$ trên $SO$. Chứng minh $AN \\perp (SDO)$.''')


                # --- CÁC ĐÁP ÁN ---
                da_d = ('\\True $' + str(dap_an_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI ---
                # Sử dụng r''' để tránh lỗi các ký tự đặc biệt của TikZ và LaTeX
                loigiai = (r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, line width=1pt]
                \coordinate (A) at (0,0);
                \coordinate (B) at (-1.5,-1.5);
                \coordinate (D) at (4,0);
                \coordinate (C) at ($(B)+(D)-(A)$);
                \coordinate (S) at (0,3.5);
                \coordinate (O) at ($(A)!0.5!(C)$);
                \coordinate (N) at ($(S)!0.4!(O)$);
                \draw (S)--(B)--(C)--(D)--(S)--(C);
                \draw[dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (A)--(N);
                \foreach \p/\pos in {S/above, A/left, B/below left, C/below, D/right, O/below, N/right}
                    \fill (\p) circle (1.5pt) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}
            Ta có: $BD \perp AC$ (do $ABCD$ là hình vuông) và $BD \perp SA$ (do $SA \perp (ABCD)$). \\
            Suy ra $BD \perp (SAC)$. \\
            Mà $AN \subset (SAC)$, nên $BD \perp AN$ (1). \\
            Theo giả thiết: $AN \perp SO$ (2). \\
            Từ (1) và (2), ta có $AN$ vuông góc với hai đường thẳng cắt nhau $BD$ và $SO$ cùng nằm trong mặt phẳng $(SDO)$. \\
            Vậy $AN \perp (SDO)$.''')

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

