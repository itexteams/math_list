
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


def bt_dang6_p4_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1', '2']
    dang=random.choice(lisdang)
    if dang=='1':
        # Dạng 1: Giữ nguyên tên điểm như bài gốc
        p_M, p_N, p_P, p_Q, p_K, p_I, p_E, p_F, p_R = 'M', 'N', 'P', 'Q', 'K', 'I', 'E', 'F', 'R'
    else:
        # Dạng 2: Đổi tên các điểm ngẫu nhiên để sinh đề mới
        p_M, p_N, p_P, p_Q, p_K, p_I, p_E, p_F, p_R = 'E', 'F', 'G', 'H', 'U', 'V', 'X', 'Y', 'Z'
    noidungcauhoi = ('Cho hình chóp $S.ABCD$, đáy là hình bình hành. Gọi $%s, %s, %s$ lần lượt là trung điểm của $SB, BC, SD$.\\\\ \n'
                     'a) Tìm giao tuyến của $(SCD)$ và $(%s%s%s)$. \\\\ \n'
                     'b) Tìm giao điểm của $CD$ và $(%s%s%s)$. \\\\ \n'
                     'c) Tìm giao điểm của $AB$ và $(%s%s%s)$. \\\\ \n'
                     'd) Tìm giao tuyến của $(SAC)$ và $(%s%s%s)$ suy ra thiết diện của hình chóp với mặt phẳng $(%s%s%s)$. \n'
                     %(p_M, p_N, p_P, p_M, p_N, p_P, p_M, p_N, p_P, p_M, p_N, p_P, p_M, p_N, p_P, p_M, p_N, p_P))
    # Nội dung lời giải
    loigiai = (    '\\begin{center}\n'
                   '\\begin{tikzpicture}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=1]\n'
                   '    \\coordinate (A) at (0,0);\n'
                   '    \\coordinate (B) at (-2,-2);\n'
                   '    \\coordinate (C) at (3,-2);\n'
                   '    \\coordinate (D) at (5,0);\n'
                   '    \\coordinate (S) at (1,4);\n'
                   '    \\coordinate (M) at (-0.5,1);\n'
                   '    \\coordinate (N) at (0.5,-2);\n'
                   '    \\coordinate (P) at (3,2);\n'
                   '    \\coordinate (Q) at (4,-1);\n'
                   '    \\coordinate (K) at (-3,-3);\n'
                   '    \\coordinate (I) at (1.5,-1);\n'
                   '    \\coordinate (E) at (1.25,1.5);\n'
                   '    \\coordinate (F) at (2.25,-1.5);\n'
                   '    \\coordinate (R) at (0.75,3);\n'
                   '    \\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(I) (M)--(P) (R)--(M) (R)--(P) (N)--(Q) (R)--(F);\n'
                   '    \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (M)--(N) (P)--(Q) (K)--(B) (K)--(N);\n'
                   '    \\fill (A) circle (1.5pt) node[left] {$A$};\n'
                   '    \\fill (B) circle (1.5pt) node[below left] {$B$};\n'
                   '    \\fill (C) circle (1.5pt) node[below right] {$C$};\n'
                   '    \\fill (D) circle (1.5pt) node[right] {$D$};\n'
                   '    \\fill (S) circle (1.5pt) node[above] {$S$};\n'
                   '    \\fill (M) circle (1.5pt) node[left] {$%s$};\n'
                   '    \\fill (N) circle (1.5pt) node[below] {$%s$};\n'
                   '    \\fill (P) circle (1.5pt) node[right] {$%s$};\n'
                   '    \\fill (Q) circle (1.5pt) node[right] {$%s$};\n'
                   '    \\fill (K) circle (1.5pt) node[below] {$%s$};\n'
                   '    \\fill (I) circle (1.5pt) node[below] {$%s$};\n'
                   '    \\fill (E) circle (1.5pt) node[right] {$%s$};\n'
                   '    \\fill (F) circle (1.5pt) node[below left] {$%s$};\n'
                   '    \\fill (R) circle (1.5pt) node[above left] {$%s$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Do $%s%s // SC$ (tính chất đường trung bình) nên giao tuyến của $(SCD)$ và $(%s%s%s)$ phải là $d // %s%s // SC$. \\\\ \n'
                   'Do đó $d$ qua $%s$ và song song với $SC$ nên $d$ là đường trung bình tam giác $(SCD)$. Gọi $%s$ là trung điểm $CD$ thì $%s%s$ là giao tuyến cần tìm. \n'
                   '\\item Ta có $%s \\in CD, %s \\in (%s%s%s)$ \\\\ \n'
                   'Suy ra $%s$ là giao điểm của $CD$ và $(%s%s%s)$. \n'
                   '\\item Trong mp $(ABCD)$, gọi $%s$ là giao điểm của $%s%s$ và $AB$. \\\\ \n'
                   'Ta có $%s \\in AB, %s \\in %s%s \\subset (%s%s%s%s) \\Rightarrow %s \\in (%s%s%s)$ \\\\ \n'
                   'Vậy $%s$ là giao điểm của $AB$ với $(%s%s%s)$. \n'
                   '\\item Gọi $%s$ là giao điểm của $AC$ và $BD$. \\\\ \n'
                   'Trong mp $(SBD)$ có $%s%s$ là đường trung bình tam giác $SBD$. \\\\ \n'
                   'Gọi $%s = %s%s \\cap SI \\Rightarrow (SAC) \\cap (%s%s%s) = %s%s$ \\\\ \n'
                   'Trong mp $(SAC)$, gọi $%s = %s%s \\cap SA \\Rightarrow$ thiết diện của mặt phẳng $(%s%s%s)$ với khối chóp là ngũ giác $%s%s%s%s%s$. \n'
                   '\\end{enumEX} \n'
                   %(p_M, p_N, p_P, p_Q, p_K, p_I, p_E, p_F, p_R,
                     p_M, p_N, p_M, p_N, p_P, p_M, p_N,
                     p_P, p_Q, p_P, p_Q,
                     p_Q, p_Q, p_M, p_N, p_P,
                     p_Q, p_M, p_N, p_P,
                     p_K, p_N, p_Q,
                     p_K, p_K, p_N, p_Q, p_M, p_N, p_P, p_Q, p_K, p_M, p_N, p_P,
                     p_K, p_M, p_N, p_P,
                     p_I,
                     p_M, p_P,
                     p_E, p_M, p_P, p_M, p_N, p_P, p_E, p_F,
                     p_R, p_E, p_F, p_M, p_N, p_P, p_M, p_N, p_Q, p_P, p_R))
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
