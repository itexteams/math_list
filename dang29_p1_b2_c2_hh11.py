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


def bt_dang29_p1_b2_c2_hh11(self):
            # Khai báo biến
            # =================================================================
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Danh sách các bộ nhãn đỉnh để thay đổi đề bài
                list_points = [
                    ('S', 'A', 'B', 'C'),
                ]
                p = random.choice(list_points)
                S, A, B, C = p[0], p[1], p[2], p[3]
                H, K = 'H', 'K'
                M = 'M'

                # =================================================================
                # BƯỚC 2: NỘI DUNG CÂU HỎI
                # =================================================================
                noidungcauhoi = (
                    'Cho hình chóp $%s.%s%s%s$ có $%s%s \\perp \\left( %s%s%s \\right)$. '
                    'Gọi $%s, %s$ lần lượt là trực tâm các tam giác $%s%s%s$ và $%s%s%s$. '
                    'Mệnh đề nào \\textbf{sai} trong các mệnh đề sau?'
                    % (S, A, B, C, S, A, A, B, C, H, K, S, B, C, A, B, C)
                )

                # Các phương án
                # da_d: Là mệnh đề SAI về toán học (đáp án đúng của câu hỏi "tìm câu sai")
                da_d = ('\\True $%s%s \\perp \\left( %s%s%s \\right)$ ' % (B, C, S, A, B))
                da_s1 = ('$%s%s \\perp \\left( %s%s%s \\right)$ ' % (B, C, S, A, H))
                da_s2 = ('$%s%s \\perp \\left( %s%s%s \\right)$ ' % (H, K, S, B, C))
                da_s3 = ('$%s%s, %s%s$ và $%s%s$ đồng quy' % (S, H, A, K, B, C))

                # Trộn ngẫu nhiên các phương án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # =================================================================
                # BƯỚC 2: LỜI GIẢI CHI TIẾT (DÙNG CẤU TRÚC % VÀ KHÔNG DÙNG r-string)
                # =================================================================
                loigiai = (
                    r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.73,135.9) -- (259.62,135.17) ;
            		\draw [line width=1]    (103.73,135.9) -- (103.09,24.75) ;
            		\draw [line width=1]    (103.73,135.9) -- (163.76,182.5) ;
            		\draw [line width=1]    (163.76,182.5) -- (259.62,135.17) ;
            		\draw [line width=1]    (103.09,24.75) -- (163.76,182.5) ;
            		\draw [line width=1]    (103.09,24.75) -- (259.62,135.17) ;
            		\draw [line width=1]    (103.09,24.75) -- (198.95,164.3) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.73,135.9) -- (198.95,164.3) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (163.76,182.5) -- (160.12,135.17) ; 
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (161.94,153.13) -- (181.35,139.79) ;
            		\draw (95.73,3.03) node [anchor=north west][inner sep=0.75pt]    {$S$};
            		\draw (84.21,122.58) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (155.01,184.65) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (260.87,122.37) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (179.67,119.63) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\draw (163.65,155.37) node [anchor=north west][inner sep=0.75pt]    {$K$};
            	\end{tikzpicture}
            \end{center}'''
                    '+ Gọi $%s = %s%s \\cap %s%s$. Vì $%s$ là trực tâm $\\Delta %s%s%s \\Rightarrow %s%s \\perp %s%s$.\\\\\n'
                    '+ Có $%s%s \\perp (%s%s%s) \\Rightarrow %s%s \\perp %s%s$. \\\\\n'
                    'Từ đó suy ra $%s%s \\perp (%s%s%s) \\Rightarrow %s%s \\perp %s%s$.\\\\\n'
                    '+ Vì $%s$ là trực tâm $\\Delta %s%s%s \\Rightarrow %s%s \\perp %s%s$, do đó $%s, %s, %s$ thẳng hàng.\\\\\n'
                    '$\\Rightarrow$ $%s%s, %s%s$ và $%s%s$ đồng quy tại $%s$. Mệnh đề này đúng.\\\\\n'
                    '+ Vì $%s%s \\perp (%s%s%s)$ nên $%s%s \\perp (%s%s%s)$. Mệnh đề này đúng.\\\\\n'
                    '+ Theo tính chất quen thuộc: $%s%s \\perp (%s%s%s)$. Mệnh đề này đúng.\\\\\n'
                    '+ Mệnh đề "$%s%s \\perp (%s%s%s)$" là \\textbf{sai} vì nếu $%s%s \\perp (%s%s%s)$ thì $%s%s \\perp %s%s$, '
                    'tức tam giác $%s%s%s$ phải vuông tại $%s$.'
                    % (M, A, K, B, C, K, A, B, C, A, M, B, C,
                       S, A, A, B, C, S, A, B, C,
                       B, C, S, A, M, B, C, S, M,
                       H, S, B, C, S, H, B, C, S, H, M,
                       S, H, A, K, B, C, M,
                       B, C, S, A, M, B, C, S, A, H,
                       H, K, S, B, C,
                       B, C, S, A, B, B, C, S, A, B, B, C, A, B, A, B, C, B)
                )

                # =================================================================
                # BƯỚC 4: XUẤT NỘI DUNG (THEO MẪU)
                # =================================================================
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

