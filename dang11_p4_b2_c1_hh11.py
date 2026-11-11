
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


def bt_dang11_p4_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1', '2']
    dang=random.choice(lisdang)
    if dang=='1':
        # Dạng 1: Giữ nguyên tên điểm như bài gốc
        I, J, G, M, N, K = 'I', 'J', 'G', 'M', 'N', 'K'
    else:
        # Dạng 2: Đổi tên các điểm ngẫu nhiên để sinh đề mới
        I, J, G, M, N, K = 'E', 'F', 'H', 'P', 'Q', 'L'
    # Nội dung câu hỏi
    noidungcauhoi = ('Cho hình chóp $S.ABCD$, đáy là hình thang với các cạnh đáy là $AB$ và $CD$. Gọi $%s, %s$ lần lượt là trung điểm của $AD$ và $BC$ và $%s$ là trọng tâm tam giác $SAB$.\\\\ \n'
                     'a) Tìm giao tuyến của $(SAB)$ và $(%s%s%s)$. \\\\ \n'
                     'b) Xác định thiết diện của hình chóp với mặt phẳng $(%s%s%s)$. Thiết diện là hình gì? Tìm điều kiện đối với $AB$ và $CD$ để thiết diện là hình bình hành. \n'
                     %(I, J, G, I, J, G, I, J, G))
    # Nội dung lời giải (Chia làm 2 phần TikZ và Text để dễ quản lý biến %s)
    loigiai_tikz = ('\\begin{center}\n'
                   '\\begin{tikzpicture}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.9]\n'
                   '    \\coordinate (A) at (0,0);\n'
                   '    \\coordinate (B) at (6,0);\n'
                   '    \\coordinate (D) at (-2,-2);\n'
                   '    \\coordinate (C) at (4,-2);\n'
                   '    \\coordinate (S) at (1.5,4.5);\n'
                   '    \\coordinate (I) at (-1,-1);\n'
                   '    \\coordinate (J) at (5,-1);\n'
                   '    \\coordinate (K) at (3,0);\n'
                   '    \\coordinate (G) at (2.5,1.5);\n'
                   '    \\coordinate (N) at (0.5,1.5);\n'
                   '    \\coordinate (M) at (4.5,1.5);\n'
                   '    \\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (I)--(J) (I)--(N) (S)--(K) (S)--(G) (M)--(N) ;\n'
                   '    \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (J)--(M);\n'
                   '    \\fill (A) circle (1pt) node[left] {$A$};\n'
                   '    \\fill (B) circle (1pt) node[right] {$B$};\n'
                   '    \\fill (C) circle (1pt) node[below right] {$C$};\n'
                   '    \\fill (D) circle (1pt) node[below left] {$D$};\n'
                   '    \\fill (S) circle (1pt) node[above] {$S$};\n'
                   '    \\fill (I) circle (1pt) node[below left] {$%s$};\n'
                   '    \\fill (J) circle (1pt) node[below right] {$%s$};\n'
                   '    \\fill (K) circle (1pt) node[above right] {$%s$};\n'
                   '    \\fill (G) circle (1pt) node[above right] {$%s$};\n'
                   '    \\fill (M) circle (1pt) node[right] {$%s$};\n'
                   '    \\fill (N) circle (1pt) node[left] {$%s$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n'
                   %(I, J, K, G, M, N))
    loigiai_text = ('\\begin{enumEX}[a)]{1} \n'
                    '\\item Giả sử $(SAB) \\cap (%s%s%s) = %s%s$ với $%s \\in SB$ và $%s \\in SA$. Ba mặt phẳng $(SAB); (%s%s%s)$ và $(ABCD)$ cắt nhau theo ba giao tuyến là các đường thẳng $%s%s, AB$ và $%s%s$ nên chúng song song hoặc đồng quy. \\\\ \n'
                    'Mặt khác $AB // %s%s \\Rightarrow %s%s // AB // %s%s$. \\\\ \n'
                    'Do vậy $(SAB) \\cap (%s%s%s) = %s%s$ với $%s%s$ là đường thẳng qua $%s$ và song song với $AB$. \n'
                    '\\item Thiết diện của hình chóp với mặt phẳng $(%s%s%s)$ là tứ giác $%s%s%s%s$. \\\\ \n'
                    'Ta có: $%s%s%s%s$ là hình bình hành khi $%s%s = %s%s$. \\\\ \n'
                    'Lại có: $\\dfrac{%s%s}{AB} = \\dfrac{S%s}{SA} = \\dfrac{S%s}{S%s} = \\dfrac{2}{3} \\Rightarrow %s%s = \\dfrac{2}{3}AB; %s%s = \\dfrac{AB+CD}{2}$ (Gọi $%s$ là trung điểm $AB$). \\\\ \n'
                    'Do đó: $%s%s = %s%s \\Leftrightarrow \\dfrac{2AB}{3} = \\dfrac{AB+CD}{2} \\Leftrightarrow AB = 3CD$. \\\\ \n'
                    'Vậy $AB = 3CD$ thì thiết diện là hình bình hành. \n'
                    '\\end{enumEX} \n'
                    %(I, J, G, M, N, M, N, I, J, G, M, N, I, J, 
                      I, J, M, N, I, J,
                      I, J, G, M, N, M, N, G,
                      I, J, G, M, N, I, J,
                      M, N, I, J, M, N, I, J,
                      M, N, N, G, K, M, N, I, J, K,
                      M, N, I, J))
    loigiai = loigiai_tikz + loigiai_text
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
