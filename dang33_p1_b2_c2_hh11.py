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


def bt_dang33_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Thiết lập các đỉnh (có thể mở rộng random tên đỉnh nếu cần)
                S, A, B, C = 'S', 'A', 'B', 'C'
                M, N = 'M', 'N'

                # Bước 2: Nội dung câu hỏi
                noidungcauhoi = ('''Cho tứ diện $%s.%s%s%s$ có đáy $%s%s%s$ là tam giác vuông tại $%s$ và $%s%s$ vuông góc với mặt phẳng $\\left(%s%s%s\\right)$. Gọi $%s, %s$ lần lượt là hình chiếu vuông góc của $%s$ trên cạnh $%s%s$ và $%s%s$. Khẳng định nào sau đây \\textbf{sai}?'''
                                 % (S, A, B, C, A, B, C, B, S, A, A, B, C, M, N, A, S, B, S, C))



                # Bước 4: Thiết lập đáp án (da_d là khẳng định sai theo yêu cầu đề bài)
                da_d = ('\\True $%s%s \\perp %s%s$' % (A, N, S, B))

                # Các khẳng định đúng (phương án nhiễu)
                da_s1 = ('$%s%s \\perp %s%s$' % (A, M, S, C))
                da_s2 = ('$%s%s \\perp %s%s$' % (A, M, M, N))
                da_s3 = ('$%s%s \\perp %s%s$' % (S, A, B, C))

                # Trộn các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 5: Nội dung lời giải chi tiết
                loigiai = (r'''\begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.73,135.9) -- (259.62,135.17) ;
            	\draw [line width=1]    (103.73,135.9) -- (103.09,24.75) ;
            	\draw [line width=1]    (103.73,135.9) -- (163.76,182.5) ;
            	\draw [line width=1]    (163.76,182.5) -- (259.62,135.17) ;
            	\draw [line width=1]    (103.09,24.75) -- (163.76,182.5) ;
            	\draw [line width=1]    (103.09,24.75) -- (259.62,135.17) ;
            	\draw [line width=1]    (103.73,135.9) -- (123.47,81.4) ;
            	\draw [line width=1]    (181.35,79.96) -- (123.47,81.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.73,135.9) -- (181.35,79.96) ;
            	\draw (95.73,3.03) node [anchor=north west][inner sep=0.75pt]    {$S$};
            	\draw (84.21,122.58) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (263.01,124.65) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (152.87,181.37) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (182.67,58.63) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\draw (102.65,67.37) node [anchor=north west][inner sep=0.75pt]    {$N$};
            \end{tikzpicture}
            		\end{center}'''
                    '''Ta có: $%s%s \\perp \\left(%s%s%s\\right) \\Rightarrow %s%s \\perp %s%s$. \\\\
                             Mà $%s%s \\perp %s%s$ (do tam giác $%s%s%s$ vuông tại $%s$). \\\\
                             Suy ra $%s%s \\perp \\left(%s%s%s\\right)$. \\\\
                             Vì $%s%s \\subset \\left(%s%s%s\\right)$ nên $%s%s \\perp %s%s$. \\\\
                             Xét mặt phẳng $\\left(%s%s%s\\right)$, ta có: \\\\
                             $\\begin{cases} %s%s \\perp %s%s \\text{ (giả thiết)} \\\\ %s%s \\perp %s%s \\text{ (chứng minh trên)} \\end{cases} \\Rightarrow %s%s \\perp \\left(%s%s%s\\right)$. \\\\
                             Từ $%s%s \\perp \\left(%s%s%s\\right)$, ta suy ra: \\\\
                             + $%s%s \\perp %s%s$ (vì $%s%s \\subset \\left(%s%s%s\\right)$). Vậy đáp án $%s%s \\perp %s%s$ đúng. \\\\
                             + $%s%s \\perp %s%s$ (vì $%s%s \\subset \\left(%s%s%s\\right)$). Vậy đáp án $%s%s \\perp %s%s$ đúng. \\\\
                             Mặt khác, $%s%s \\perp \\left(%s%s%s\\right) \\Rightarrow %s%s \\perp %s%s$ nên đáp án $%s%s \\perp %s%s$ đúng. \\\\
                             Vậy khẳng định $%s%s \\perp %s%s$ là sai.'''
                           % (S, A, A, B, C, S, A, B, C,
                              B, C, A, B, A, B, C, B,
                              B, C, S, A, B,
                              A, M, S, A, B, B, C, A, M,
                              S, B, C,
                              A, M, S, B, A, M, B, C, A, M, S, B, C,
                              A, M, S, B, C,
                              A, M, S, C, S, C, S, B, C, A, M, S, C,
                              A, M, M, N, M, N, S, B, C, A, M, M, N,
                              S, A, A, B, C, S, A, B, C, S, A, B, C,
                              A, N, S, B))

            # Xuất câu trắc nghiệm theo đúng cấu trúc template
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

