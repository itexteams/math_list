
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


def bt_dang18_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        a_rand = randint(1, 4)
        b_rand = randint(a_rand + 1, 5)
        if a_rand == 2 and b_rand == 3:
            gt_diem = 'Lấy $G_1, G_2, G_3$ lần lượt là trọng tâm của các tam giác $ABC, ACD, ADB$.'
            lg_goi = 'Gọi $M, N, L$ lần lượt là trung điểm của các cạnh $BC, CD, BD$.'
            lg_tiso = '\\dfrac{AG_1}{AM} = \\dfrac{AG_2}{AN} = \\dfrac{AG_3}{AL} = \\dfrac{2}{3}'
        else:
            gt_diem = 'Gọi $M, N, L$ lần lượt là trung điểm của $BC, CD, BD$. Lấy các điểm $G_1, G_2, G_3$ lần lượt thuộc các đoạn $AM, AN, AL$ sao cho $\\dfrac{AG_1}{AM} = \\dfrac{AG_2}{AN} = \\dfrac{AG_3}{AL} = \\dfrac{'+str(a_rand)+'}{'+str(b_rand)+'}$.'
            lg_goi = ''
            lg_tiso = '\\dfrac{AG_1}{AM} = \\dfrac{AG_2}{AN} = \\dfrac{AG_3}{AL} = \\dfrac{'+str(a_rand)+'}{'+str(b_rand)+'}'
        
        noidungcauhoi = ('Cho tứ diện $ABCD$. ' + gt_diem + '\\\\ \n'
                         'a) Chứng minh rằng $(G_1G_2G_3) \\parallel (BCD)$. \\\\ \n'
                         'b) Xác định giao tuyến của mặt phẳng $(G_1G_2G_3)$ với mặt phẳng $(ABC)$. \n'
                         )
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=1, line join=round, line cap=round] \n'
                    '\\coordinate (B) at (0,0); \n'
                    '\\coordinate (C) at (4,-1); \n'
                    '\\coordinate (D) at (-2,-2); \n'
                    '\\coordinate (A) at (1,4); \n'
                    '\\coordinate (M) at ($(B)!0.5!(C)$); \n'
                    '\\coordinate (N) at ($(C)!0.5!(D)$); \n'
                    '\\coordinate (L) at ($(B)!0.5!(D)$); \n'
                    '\\coordinate (G1) at ($(A)!'+str(a_rand)+'/'+str(b_rand)+'!(M)$); \n'
                    '\\coordinate (G2) at ($(A)!'+str(a_rand)+'/'+str(b_rand)+'!(N)$); \n'
                    '\\coordinate (G3) at ($(A)!'+str(a_rand)+'/'+str(b_rand)+'!(L)$); \n'
                    '\\coordinate (Delta_left) at ($(G1) - 0.3*(B) + 0.3*(C)$); \n'
                    '\\coordinate (Delta_right) at ($(G1) + 0.3*(B) - 0.3*(C)$); \n'
                    '\\draw[dashed] (B) -- (C) (A) -- (B) (B) -- (D) (A) -- (L) (A) -- (M) (M) -- (N) (N) -- (L) (L) -- (M) (G1) -- (G2) (G2) -- (G3) (G3) -- (G1); \n'
                    '\\draw (A) -- (C) (A) -- (D) (A) -- (N) (C) -- (D); \n'
                    '\\draw[dashed] (Delta_left) -- (Delta_right) node[right] {$\\Delta$}; \n'
                    '\\fill (A) circle (1.5pt) node[above] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[right] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[left] {$D$}; \n'
                    '\\fill (M) circle (1.5pt) node[below right] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[below] {$N$}; \n'
                    '\\fill (L) circle (1.5pt) node[left] {$L$}; \n'
                    '\\fill (G1) circle (1.5pt) node[below right] {$G_1$}; \n'
                    '\\fill (G2) circle (1.5pt) node[above right] {$G_2$}; \n'
                    '\\fill (G3) circle (1.5pt) node[left] {$G_3$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item Chứng minh rằng $(G_1G_2G_3) \\parallel (BCD)$. \\\\ \n'
                    + lg_goi + ' Ta có $' + lg_tiso + '$ suy ra $\\begin{cases} G_1G_2 \\parallel MN \\\\ G_2G_3 \\parallel NL \\end{cases}$. \\\\ \n'
                    'Mà $\\begin{cases} MN \\subset (BCD) \\\\ NL \\subset (BCD) \\end{cases}$ nên $\\begin{cases} G_1G_2 \\parallel (BCD) \\\\ G_2G_3 \\parallel (BCD) \\end{cases}$ suy ra $(G_1G_2G_3) \\parallel (BCD)$. \n'
                    '\\item Xác định giao tuyến của mặt phẳng $(G_1G_2G_3)$ với mặt phẳng $(ABC)$. \\\\ \n'
                    'Từ $(G_1G_2G_3) \\parallel (BCD)$ suy ra $BC \\parallel (G_1G_2G_3)$. \\\\ \n'
                    'Ta có $\\begin{cases} G_1 \\in (ABC) \\cap (G_1G_2G_3) \\\\ BC \\subset (ABC) \\\\ BC \\parallel (G_1G_2G_3) \\end{cases} \\Rightarrow (ABC) \\cap (G_1G_2G_3) = \\Delta \\parallel BC$ với $\\Delta$ qua $G_1$. \n'
                    '\\end{enumEX} \n'
                    )
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
