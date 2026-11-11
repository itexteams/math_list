

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


def bt_dang5_p4_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1', '2']
    dang=random.choice(lisdang)

    if dang=='1':
        # Dạng 1: Giữ nguyên tên điểm như bài gốc
        p1, p2, p3, p4, p5 = 'M', 'N', 'P', 'Q', 'K'
    else:
        # Dạng 2: Đổi tên các điểm ngẫu nhiên để sinh đề mới
        p1, p2, p3, p4, p5 = 'E', 'F', 'G', 'H', 'I'

    # B2: Viết lại y hệt bài toán gồm đề bài và lời giải
    # Nội dung câu hỏi
    noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình bình hành, gọi $%s, %s, %s, %s$ lần lượt nằm trên $BC, SC, SD, AD$ sao cho $%s%s // SB, %s%s // CD, %s%s // CD$.\\\\ \n'
                     'a) Chứng minh rằng: $%s%s // SA$. \\\\ \n'
                     'b) Gọi $%s$ là giao điểm của $%s%s$ và $%s%s$. Chứng minh rằng: $S%s // AD // BC$. \n'
                     %(p1, p2, p3, p4, p1, p2, p2, p3, p1, p4, p3, p4, p5, p1, p2, p3, p4, p5))
        
    # Nội dung lời giải kèm hình vẽ code TikZ (Đã fix lỗi tọa độ thành tọa độ tuyệt đối)
    loigiai = (    '\\begin{center}\n'
                   '\\begin{tikzpicture}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.8]\n'
                   '    \\coordinate (A) at (0,0);\n'
                   '    \\coordinate (B) at (-2,-2);\n'
                   '    \\coordinate (C) at (3,-2);\n'
                   '    \\coordinate (D) at (5,0);\n'
                   '    \\coordinate (S) at (1,4);\n'
                   '    \\coordinate (M) at (0.75,-2);\n'
                   '    \\coordinate (N) at (2.1,0.7);\n'
                   '    \\coordinate (P) at (3.2,1.8);\n'
                   '    \\coordinate (Q) at (2.75,0);\n'
                   '    \\coordinate (K) at (3.75,4);\n'
                   '    \\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (M)--(Q) (P)--(Q);\n'
                   '    \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (M)--(N) (N)--(P) (N)--(K) (P)--(K) (S)--(K);\n'
                   '    \\fill (A) circle (1.5pt) node[left] {$A$};\n'
                   '    \\fill (B) circle (1.5pt) node[below left] {$B$};\n'
                   '    \\fill (C) circle (1.5pt) node[below right] {$C$};\n'
                   '    \\fill (D) circle (1.5pt) node[right] {$D$};\n'
                   '    \\fill (S) circle (1.5pt) node[above] {$S$};\n'
                   '    \\fill (M) circle (1.5pt) node[below] {$%s$};\n'
                   '    \\fill (N) circle (1.5pt) node[left] {$%s$};\n'
                   '    \\fill (P) circle (1.5pt) node[right] {$%s$};\n'
                   '    \\fill (Q) circle (1.5pt) node[right] {$%s$};\n'
                   '    \\fill (K) circle (1.5pt) node[above] {$%s$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Ta có: $%s%s // SB \\Rightarrow \\dfrac{C%s}{SC} = \\dfrac{C%s}{CB} = \\dfrac{D%s}{AD}$ (1) \\\\ \n'
                   'Lại có: $%s%s // CD \\Rightarrow \\dfrac{C%s}{CS} = \\dfrac{D%s}{DS}$ (2). (Định lý Ta-let) \\\\ \n'
                   'Từ (1) và (2) suy ra $\\dfrac{D%s}{DS} = \\dfrac{D%s}{AD} \\Rightarrow SA // %s%s$. \n'
                   '\\item Xét $3$ mặt phẳng $(SAD); (SBC)$ và $(ABCD)$ cắt nhau theo các giao tuyến là $S%s, AD, BC$. \\\\ \n'
                   'Suy ra $S%s, AD, BC$ song song hoặc đồng quy. \\\\ \n'
                   'Mặt khác $AD // BC \\Rightarrow S%s // AD // BC$. \n'
                   '\\end{enumEX} \n'
                   %(p1, p2, p3, p4, p5, p1, p2, p2, p1, p4, p2, p3, p2, p3, p3, p4, p3, p4, p5, p5, p5))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
