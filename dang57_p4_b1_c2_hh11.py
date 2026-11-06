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


def bt_dang57_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lis_canh = ['a', 'x', 'm', 'k', 'c']
            canh = random.choice(lis_canh) # Random ký hiệu độ dài cạnh

            # Bước 3: Suy nghĩ tìm cách random bài toán
            # Với hình chóp đều có tất cả các cạnh bằng nhau, góc giữa MN và SC luôn là 90 độ.
            # Ta có thể random các giá trị nhiễu và ký hiệu cạnh để bài toán sinh động.

            kq_dung = '90^\\circ'

            # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            cac_phuong_an_sai = ['$30^\\circ$', '$45^\\circ$', '$60^\\circ$', '$120^\\circ$', '$150^\\circ$']
            random.shuffle(cac_phuong_an_sai)

            da_s1 = cac_phuong_an_sai[0]
            da_s2 = cac_phuong_an_sai[1]
            da_s3 = cac_phuong_an_sai[2]

            # Câu hỏi
            noidungcauhoi = ('''Cho hình chóp đều $S.ABCD$ có tất cả các cạnh đều bằng $%s$. Gọi $M$, $N$ lần lượt là trung điểm của $AD$ và $SD$. Tính góc giữa hai đường thẳng $MN$ và $SC$.'''
                             %(canh))

            # Các đáp án
            da_d = ('\\True $%s$' % (kq_dung))
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (-1.2,-1.5);
                \\coordinate (C) at (2.5,-1.5);
                \\coordinate (D) at (3.7,0);
                \\coordinate (S) at (1.85,3.5);
                \\coordinate (M) at ($(A)!0.5!(D)$);
                \\coordinate (N) at ($(S)!0.5!(D)$);
                \\coordinate (P) at ($(C)!0.5!(D)$);
                \\coordinate (O) at (1.85,-0.75);
                \\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (M)--(N) (M)--(P) (A)--(C) (B)--(D) (S)--(O);
                \\draw (S)--(B)--(C)--(D)--(S)--(C) (N)--(P);
                \\foreach \\p/\\pos in {S/above, A/left, B/below left, C/below right, D/right, M/above left, N/right, P/below right}
                    \\fill (\\p) node[\\pos] {$\\p$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung lời giải chi tiết
            loigiai = ('''Gọi $P$ là trung điểm của $CD$. \\\\
                         Trong tam giác $SCD$, vì $N$ là trung điểm $SD$ và $P$ là trung điểm $CD$ nên $NP$ là đường trung bình của tam giác $SCD$. \\\\
                         Suy ra $NP \\parallel SC \\Rightarrow (MN, SC) = (MN, NP)$. \\\\
                         Xét tam giác $MNP$ có: \\\\
                         $MN = \\frac{SA}{2} = \\frac{%s}{2}$ (do $MN$ là đường trung bình $\\triangle SAD$). \\\\
                         $NP = \\frac{SC}{2} = \\frac{%s}{2}$ (do $NP$ là đường trung bình $\\triangle SCD$). \\\\
                         $MP$ là đường trung bình của hình vuông $ABCD$ (nối trung điểm hai cạnh đối $AD$ và $CD$ không đúng, $MP$ là cạnh của tam giác vuông $MDP$). \\\\
                         Xét tam giác vuông $MDP$ tại $D$ (do $ABCD$ là hình vuông), ta có: \\\\
                         $MP = \\sqrt{MD^2 + DP^2} = \\sqrt{\\left(\\frac{%s}{2}\\right)^2 + \\left(\\frac{%s}{2}\\right)^2} = \\frac{%s\\sqrt{2}}{2}$. \\\\
                         Trong tam giác $MNP$, ta có: \\\\
                         $MN^2 + NP^2 = \\left(\\frac{%s}{2}\\right)^2 + \\left(\\frac{%s}{2}\\right)^2 = \\frac{%s^2}{4} + \\frac{%s^2}{4} = \\frac{%s^2}{2}$. \\\\
                         $MP^2 = \\left(\\frac{%s\\sqrt{2}}{2}\\right)^2 = \\frac{2%s^2}{4} = \\frac{%s^2}{2}$. \\\\
                         Vì $MN^2 + NP^2 = MP^2$ nên tam giác $MNP$ vuông tại $N$ (theo định lý đảo của định lý Pytago). \\\\
                         Suy ra $\\widehat{MNP} = 90^\\circ \\Rightarrow (MN, SC) = (MN, NP) = 90^\\circ$.'''
                         %(canh, canh, canh, canh, canh, canh, canh, canh, canh, canh, canh, canh, canh))

            # Xuất câu trắc nghiệm - Không dùng tiền tố r
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

