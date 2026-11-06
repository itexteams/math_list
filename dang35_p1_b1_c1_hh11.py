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


def bt_dang35_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tên các đỉnh của tứ diện (4 đỉnh)
        dinh = random.sample(['A', 'B', 'C', 'D'], 4)
        v1, v2, v3, v4 = dinh 

        # Random tên trọng tâm và trung điểm (đảm bảo không trùng với các đỉnh)
        tap_diem = [k for k in ['G', 'H', 'K', 'O', 'M', 'N', 'P', 'I', 'J'] if k not in dinh]
        cg = random.choice(tap_diem)
        tap_diem.remove(cg)
        pm = random.choice(tap_diem)

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$. Gọi $%s$ là trọng tâm của tam giác $%s%s%s$. Giao điểm của đường thẳng $%s%s$ và mặt phẳng $({%s%s%s})$ là'''
                         %(v1, v2, v3, v4, cg, v1, v3, v4, v3, v4, v1, v2, cg))

        # Các đáp án trắc nghiệm
        da_d = ('\\True điểm $%s$ (với $%s$ là trung điểm của $%s%s$)' % (pm, pm, v3, v4))
        das1 = 'điểm $%s$' % (v3)
        das2 = 'điểm $%s$' % (v4)
        das3 = 'điểm $%s$' % (cg)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        # Vẽ hình TikZ cho lời giải
        tikz_code = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (V2) at (0,0);
            \\coordinate (V4) at (5,0);
            \\coordinate (V3) at (2,-2);
            \\coordinate (V1) at (2.5,3.5);
            \\coordinate (PM) at ($(V3)!0.5!(V4)$);
            \\coordinate (CG) at ($(V1)!0.67!(PM)$);
            \\draw[line width=1pt] (V1)--(V2) (V1)--(V3) (V1)--(V4) (V2)--(V3)--(V4) (V1)--(PM);
            \\draw[line width=1pt, dashed] (V2)--(V4) (V2)--(CG);
            \\fill (V1) circle (1pt) node[above] {$%s$};
            \\fill (V2) circle (1pt) node[left] {$%s$};
            \\fill (V3) circle (1pt) node[below] {$%s$};
            \\fill (V4) circle (1pt) node[right] {$%s$};
            \\fill (PM) circle (1pt) node[right] {$%s$};
            \\fill (CG) circle (1pt) node[above right] {$%s$};
           \\end{tikzpicture}
           \\end{center}''' % (v1, v2, v3, v4, pm, cg))

        # Nội dung lời giải
        loigiai = ('''%s 
            Trong mặt phẳng $({%s%s%s})$, gọi $%s$ là giao điểm của $%s%s$ và $%s%s$. \\\\
            Do $%s$ là trọng tâm của tam giác $%s%s%s$ nên $%s$ là trung điểm của $%s%s$. \\\\
            Ta có: \\\\
            $\\begin{cases} %s \\in %s%s \\\\ %s \\in %s%s \\subset ({%s%s%s}) \\end{cases} \\Rightarrow ({%s%s%s}) \\cap %s%s = \\{%s\\}$.'''
            %(tikz_code, 
              v1, v3, v4, pm, v1, cg, v3, v4,
              cg, v1, v3, v4, pm, v3, v4,
              pm, v3, v4, pm, v1, cg, v1, v2, cg, v1, v2, cg, v3, v4, pm))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

