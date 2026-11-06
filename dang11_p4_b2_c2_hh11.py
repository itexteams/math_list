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


def bt_dang11_p4_b2_c2_hh11(self):
            # Khai báo biến
            # dang = 2: Hình chiếu trên SD -> AM vuông góc (SCD)
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            # Khởi tạo các nhãn điểm để có thể mở rộng ngẫu nhiên nếu cần
            A, B, C, D, S = 'A', 'B', 'C', 'D', 'S'

            if dang == '1':
                M = 'M'
                canh_chieu = 'SB'
                # Đáp án đúng
                da_dung = '$%s%s \\perp (%s%s%s)$ ' % (A, M, S, B, C)

                # Các đáp án sai
                s1 = '$%s%s \\perp %s%s$' % (A, M, S, D)
                s2 = '$%s%s \\perp (%s%s%s)$' % (A, M, S, C, D)
                s3 = '$%s%s \\perp %s%s$' % (A, M, C, D)

                # TikZ code cho trường hợp chiếu lên SB
                hinh_ve = ('''\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]
                            \\coordinate (A) at (0,3);
                            \\coordinate (B) at (-1.5,0);
                            \\coordinate (C) at (1.5,-0.5);
                            \\coordinate (D) at (3,2.5);
                            \\coordinate (S) at (0,7);
                            \\coordinate (M) at (-0.6,4.2);
                            \\draw (S)--(B)--(C)--(D)--(S)--(C);
                            \\draw[dashed] (S)--(A)--(B) (A)--(D) (A)--(M) (B)--(D);
                            \\node at (A) [right] {$A$}; \\node at (B) [below left] {$B$};
                            \\node at (C) [below right] {$C$}; \\node at (D) [right] {$D$};
                            \\node at (S) [above] {$S$}; \\node at (M) [left] {$M$};
                            \\draw (-0.45,4.05)--(-0.35,4.3)--(-0.5,4.45); % Ký hiệu vuông góc tại M
                            \\end{tikzpicture}''')

                loigiai = ('''\\begin{center}
                %s
                \\end{center}
                Do $%s%s \\perp (%s%s%s%s)$ và $%s%s%s%s$ là hình vuông nên $\\begin{cases} %s%s \\perp %s%s \\\\ %s%s \\perp %s%s \\end{cases} \\Rightarrow %s%s \\perp (%s%s%s)$.\\\\
                             Vì $\\begin{cases} %s%s \\perp (%s%s%s) \\\\ %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s%s \\perp %s%s$.\\\\
                             Theo giả thiết, $%s%s \\perp %s%s$.\\\\
                             Như vậy $\\begin{cases} %s%s \\perp %s%s \\\\ %s%s \\perp %s%s \\end{cases} \\Rightarrow %s%s \\perp (%s%s%s)$.'''
                             %(hinh_ve,S, A, A, B, C, D, A, B, C, D, S, A, B, C, A, B, B, C, B, C, S, A, B,
                               B, C, S, A, B, A, M, S, A, B, A, M, B, C,
                               A, M, S, B,
                               A, M, S, B, A, M, B, C, A, M, S, B, C))

            else: # dang == '2'
                M = 'N'
                canh_chieu = 'SD'
                # Đáp án đúng
                da_dung = '$%s%s \\perp (%s%s%s)$' % (A, M, S, C, D)

                # Các đáp án sai
                s1 = '$%s%s \\perp %s%s$' % (A, M, S, B)
                s2 = '$%s%s \\perp (%s%s%s)$' % (A, M, S, B, C)
                s3 = '$%s%s \\perp %s%s$' % (A, M, B, C)

                hinh_ve = ('''\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]
                            \\coordinate (A) at (0,3);
                            \\coordinate (B) at (-1.5,0);
                            \\coordinate (C) at (1.5,-0.5);
                            \\coordinate (D) at (3,2.5);
                            \\coordinate (S) at (0,7);
                            \\coordinate (N) at (1.5,4.75); % Tọa độ xấp xỉ hình chiếu trên SD
                            \\draw (S)--(B)--(C)--(D)--(S)--(C);
                            \\draw[dashed] (S)--(A)--(B) (A)--(D) (A)--(N) (B)--(D);
                            \\node at (A) [left] {$A$}; \\node at (B) [below left] {$B$};
                            \\node at (C) [below right] {$C$}; \\node at (D) [right] {$D$};
                            \\node at (S) [above] {$S$}; \\node at (N) [right] {$N$};
                            \\draw (1.4,4.5)--(1.65,4.6)--(1.75,4.85);
                            \\end{tikzpicture}''')

                loigiai = ('''\\begin{center}
                %s
                \\end{center}
                Do $%s%s \\perp (%s%s%s%s)$ và $%s%s%s%s$ là hình vuông nên $\\begin{cases} %s%s \\perp %s%s \\\\ %s%s \\perp %s%s \\end{cases} \\Rightarrow %s%s \\perp (%s%s%s)$.\\\\
                             Vì $\\begin{cases} %s%s \\perp (%s%s%s) \\\\ %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s%s \\perp %s%s$.\\\\
                             Theo giả thiết, $%s%s \\perp %s%s$.\\\\
                             Như vậy $\\begin{cases} %s%s \\perp %s%s \\\\ %s%s \\perp %s%s \\end{cases} \\Rightarrow %s%s \\perp (%s%s%s)$.'''
                             %(hinh_ve,S, A, A, B, C, D, A, B, C, D, S, A, C, D, A, D, C, D, C, D, S, A, D,
                               C, D, S, A, D, A, M, S, A, D, A, M, C, D,
                               A, M, S, D,
                               A, M, S, D, A, M, C, D, A, M, S, C, D))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $%s.%s%s%s%s$ có đáy $%s%s%s%s$ là hình vuông, $%s%s \\perp (%s%s%s%s)$. Gọi $%s$ là hình chiếu của $%s$ trên $%s$. Chứng minh $%s%s \\perp (%s%s%s)$.'''
                              %(S, A, B, C, D, A, B, C, D, S, A, A, B, C, D, M, A, canh_chieu, A, M, S, C, D))

            # Trộn đáp án
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(s1), str(s2), str(s3)]
            random.shuffle(list_1)

            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

