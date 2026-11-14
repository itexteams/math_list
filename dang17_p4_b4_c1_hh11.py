
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


def bt_dang17_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k = 2
        if k == 2:
            gt_diem = "Gọi $M, N, M'$ lần lượt là trung điểm các cạnh $AB, AC$ và $A'B'$."
            loigiai_a = 'Ta có: $\\begin{cases} MM\' \\parallel BB\' \\\\ MN \\parallel BC \\\\ MM\', MN \\subset (MNM\') \\\\ BB\', BC \\subset (BCC\'B\') \\\\ MN \\cap MM\' = M \\end{cases} \\Rightarrow (MNM\') \\parallel (BCC\'B\').$ \n'
            gt_MphayNphay = "$M'N'$ là đường trung bình tam giác $A'B'C' \\Rightarrow M'N' = \\dfrac{1}{2} B'C'$"
            gt_MN_bang = "$MN$ là đường trung bình tam giác $ABC$ nên $MN \\parallel BC$ và $MN = \\dfrac{1}{2} BC$"
        noidungcauhoi = ('Cho hình lăng trụ $ABC.A\'B\'C\'.$ ' + gt_diem + '\\\\ \n'
                         'a) Chứng minh $(MNM\') \\parallel (BCC\'B\')$. \\\\ \n'
                         'b) Tìm giao điểm $N\'$ của $A\'C\'$ và $(MNM\').$ Tứ giác $MNN\'M\'$ là hình gì? \n')
        tikz_str = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (0,0); \n'
                    '\\coordinate (B) at (2,-2); \n'
                    '\\coordinate (C) at (5,0); \n'
                    '\\coordinate (A\') at (1.5,4); \n'
                    '\\coordinate (B\') at ($(B)+(A\')-(A)$); \n'
                    '\\coordinate (C\') at ($(C)+(A\')-(A)$); \n'
                    '\\coordinate (M) at ($(A)!1/'+str(k)+'!(B)$); \n'
                    '\\coordinate (N) at ($(A)!1/'+str(k)+'!(C)$); \n'
                    '\\coordinate (M\') at ($(A\')!1/'+str(k)+'!(B\')$); \n'
                    '\\coordinate (N\') at ($(A\')!1/'+str(k)+'!(C\')$); \n'
                    '\\draw[dashed] (A) -- (C) (M) -- (N) (M\') -- (N) (N) -- (N\'); \n'
                    '\\draw (A\') -- (B\') -- (C\') -- cycle; \n'
                    '\\draw (A) -- (A\') (B) -- (B\') (C) -- (C\'); \n'
                    '\\draw (A) -- (B) -- (C); \n'
                    '\\draw (M) -- (M\') (M\') -- (N\'); \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[right] {$C$}; \n'
                    '\\fill (A\') circle (1.5pt) node[above] {$A\'$}; \n'
                    '\\fill (B\') circle (1.5pt) node[below right] {$B\'$}; \n'
                    '\\fill (C\') circle (1.5pt) node[right] {$C\'$}; \n'
                    '\\fill (M) circle (1.5pt) node[left] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[above left] {$N$}; \n'
                    '\\fill (M\') circle (1.5pt) node[left] {$M\'$}; \n'
                    '\\fill (N\') circle (1.5pt) node[above] {$N\'$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n')
        loigiai = ( tikz_str +
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item Chứng minh $(MNM\') \\parallel (BCC\'B\')$. \\\\ \n'
                    + loigiai_a +
                    '\\item Tìm giao điểm $N\'$ của $A\'C\'$ và $(MNM\').$ Tứ giác $MNN\'M\'$ là hình gì? \\\\ \n'
                    'Ta có $\\begin{cases} (MNM\') \\parallel (BCC\'B\') \\\\ (A\'B\'C\') \\cap (BCC\'B\') = B\'C\' \\\\ M\' \\in (A\'B\'C\') \\cap (MNM\') \\end{cases} \\Rightarrow (A\'B\'C\') \\cap (MNM\') = x\'M\'x \\parallel B\'C\'.$ \\\\ \n'
                    'Trong $(A\'B\'C\'),$ gọi $N\' = A\'C\' \\cap x\'M\'x \\\\ \\Rightarrow \\begin{cases} N\' \\in A\'C\' \\\\ N\' \\in x\'M\'x \\subset (MNM\') \\end{cases} \\Rightarrow N\' = A\'C\' \\cap (MNM\').$ \\\\ \n'
                    'Suy ra ' + gt_MphayNphay + '. \\\\ \n'
                    'Mà ' + gt_MN_bang + '. \\\\ \n'
                    'Lại do $BC \\parallel B\'C\'$ và $BC = B\'C\'$ nên $MN \\parallel M\'N\'$ và $MN = M\'N\'.$ \\\\ \n'
                    'Vậy tứ giác $MNN\'M\'$ là hình bình hành. \n'
                    '\\end{enumEX} \n' )
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
