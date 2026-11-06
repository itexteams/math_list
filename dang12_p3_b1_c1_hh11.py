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


def bt_dang12_p3_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tỉ số m (tương ứng với BK = m*KD)
        m = random.randint(2, 6)

        kq = m

        # Các đáp án trắc nghiệm
        du = ['$%s$'%(kq),
              ]
        da= random.choice(du)

        # Tạo các đáp án sai không trùng với đáp án đúng
        s = ['$%s$'%(kq+1),
             '$%s$'%(kq+2),
             '$\\frac{1}{%s}$'%(kq),
             '$\\frac{%s}{2}$'%(kq) if kq % 2 != 0 else '$%s$'%(kq-1),
             '$%s$'%(kq+3)
            ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $I$, $J$ lần lượt là trung điểm của $AC$ và $BC$. Trên cạnh $BD$ lấy điểm $K$ sao cho $BK = %sKD$. Gọi $F$ là giao điểm của $AD$ với mặt phẳng $(IJK)$. Tỉ số $\\frac{FA}{FD}$ bằng bao nhiêu?'''
                         %(m))

        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai=('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (3,-2);
    \\coordinate (D) at (5,0);
    \\coordinate (A) at (1,3);
    \\coordinate (I) at ($(A)!0.5!(C)$);
    \\coordinate (J) at ($(B)!0.5!(C)$);
    \\coordinate (K) at ($(B)!2/3!(D)$);
    \\coordinate (E) at (intersection of J--K and C--D);
    \\coordinate (F) at (intersection of A--D and E--I);
    \\coordinate (D_ext) at ($(D)+(C)-(B)$);
    \\coordinate (H) at (intersection of J--E and D--D_ext);
    \\draw[line width=1pt] (A)--(B)--(C)--(E)--(A)--(C) (A)--(D) (I)--(J) (I)--(E);
    \\draw[line width=1pt, dashed] (B)--(D) (J)--(E) (I)--(K) (D)--(H)--(K);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[below right] {$D$};
    \\fill (E) circle (1pt) node[right] {$E$};
    \\fill (I) circle (1pt) node[above left] {$I$};
    \\fill (J) circle (1pt) node[below left] {$J$};
    \\fill (K) circle (1pt) node[below] {$K$};
    \\fill (F) circle (1pt) node[above] {$F$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\end{tikzpicture}
    \\end{center}
    Trong mặt phẳng $(BCD)$ hai đường thẳng $JK$ và $CD$ không song song nên gọi $E = JK \\cap CD$. Khi đó $E \\in (ACD)$.\\\\
    Suy ra: $(ACD) \\cap (IJK) = EI$.\\\\
    Trong $(ACD)$ gọi $F = EI \\cap AD$. Khi đó $(IJK) \\cap AD = F$.\\\\
    Vẽ $DH \\parallel BC$ và $H \\in JE$. Ta có: $\\frac{BJ}{HD} = \\frac{BK}{KD} = %s \\Rightarrow HD = \\frac{BJ}{%s} \\Rightarrow HD = \\frac{1}{%s}JC$.\\\\
    Suy ra $JC = %s HD$.\\\\
    Xét $\\triangle JCE$ có $DH \\parallel JC$ nên $\\frac{EC}{ED} = \\frac{JC}{HD} = %s$.\\\\
    Áp dụng định lý Menelaus cho $\\triangle ADC$ với cát tuyến $E, F, I$, ta có:\\\\
    $\\frac{FA}{FD} \\cdot \\frac{ED}{EC} \\cdot \\frac{IC}{IA} = 1 \\Leftrightarrow \\frac{FA}{FD} \\cdot \\frac{1}{%s} \\cdot 1 = 1 \\Rightarrow \\frac{FA}{FD} = %s$.\\\\
    Vậy $\\frac{FA}{FD} = %s$.'''
                 %(m, m, m, m, m, m, m, m))
    dapan='\\shortans[0]{$%s$}\n'%(m)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content  

