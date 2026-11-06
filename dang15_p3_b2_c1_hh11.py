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


def bt_dang15_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random hệ số k_val để đảm bảo kết quả cuối T luôn là số nguyên
        # k_val = 1 tương ứng với bài toán gốc A'A = 1/2 A'S -> SA/SA' = 3/2 -> T = 3
        k_val = random.randint(1, 6)
        T = 2 + k_val

        if k_val % 2 == 0:
            k_num = k_val // 2
            if k_num == 1:
                cond_str = "A'A = A'S"
            else:
                cond_str = "A'A = %s A'S" % k_num
            ratio_str = str(1 + k_num)
        else:
            cond_str = "A'A = \\frac{%s}{2} A'S" % k_val
            ratio_str = "\\frac{%s}{2}" % (2 + k_val)

        # Các đáp án trắc nghiệm
        du = ['$%s$' % T]
        da = du[0]

        # Tạo các phương án sai ngẫu nhiên (đảm bảo là số dương và không trùng đáp án đúng)
        s_list_raw = [T + 1, T + 2, T + 3, abs(T - 1) if T - 1 > 0 else T + 4, abs(T - 2) if T - 2 > 0 else T + 5]
        s_list = []
        for val in s_list_raw:
            s_list.append('$%s$' % val)

        # Loại bỏ các phương án trùng lặp với đáp án đúng
        s_list = list(set(s_list) - set(du))

        das1 = s_list[0]
        das2 = s_list[1]
        das3 = s_list[2]

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $A'$ là điểm trên $SA$ sao cho $%s$. Qua $A'$ kẻ đường thẳng song song với $AC$ cắt $SC$ tại $C'$. Mặt phẳng $(\\alpha)$ chứa $A'C'$ cắt các cạnh $SB, SD$ lần lượt tại $B', D'$. Giá trị của biểu thức $T = \\frac{SB}{SB'} + \\frac{SD}{SD'}$ bằng bao nhiêu?''' 
                         % cond_str)

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (2,1.5);
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (5,0);
            \\coordinate (D) at (7,1.5);
            \\coordinate (S) at (2.5,5.5);
            \\coordinate (O) at ($(A)!0.5!(C)$);
            \\coordinate (A') at ($(S)!0.55!(A)$);
            \\coordinate (C') at ($(S)!0.55!(C)$);
            \\coordinate (I) at (intersection of A'--C' and S--O);
            \\coordinate (B') at ($(S)!0.7!(B)$);
            \\coordinate (D') at (intersection of B'--I and S--D);
            \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D) (B')--(C')--(D');
            \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (A')--(C') (A')--(B') (A')--(D') (B')--(D');
            \\fill (S) circle (1pt) node[above] {$S$};
            \\fill (A) circle (1pt) node[below] {$A$};
            \\fill (B) circle (1pt) node[below left] {$B$};
            \\fill (C) circle (1pt) node[below right] {$C$};
            \\fill (D) circle (1pt) node[right] {$D$};
            \\fill (O) circle (1pt) node[below right] {$O$};
            \\fill (A') circle (1pt) node[above left] {$A'$};
            \\fill (B') circle (1pt) node[left] {$B'$};
            \\fill (C') circle (1pt) node[right] {$C'$};
            \\fill (D') circle (1pt) node[above right] {$D'$};
            \\fill (I) circle (1pt) node[above] {$I$};
           \\end{tikzpicture}
           \\end{center}
           Gọi $O$ là giao của $AC$ và $BD$. Ta có $O$ là trung điểm của đoạn thẳng $AC, BD$.\\\\
           Các đoạn thẳng $SO, A'C', B'D'$ đồng quy tại $I$.\\\\
           Ta có: $S_{SA'I} + S_{SC'I} = S_{SA'C'} \\Leftrightarrow \\frac{S_{SA'I}}{S_{SAC}} + \\frac{S_{SC'I}}{S_{SAC}} = \\frac{S_{SA'C'}}{S_{SAC}} \\Leftrightarrow \\frac{S_{SA'I}}{2S_{SAO}} + \\frac{S_{SC'I}}{2S_{SCO}} = \\frac{S_{SA'C'}}{S_{SAC}}$\\\\
           $\\Leftrightarrow \\frac{SA'}{2SA} \\cdot \\frac{SI}{SO} + \\frac{SC'}{2SC} \\cdot \\frac{SI}{SO} = \\frac{SA'}{SA} \\cdot \\frac{SC'}{SC} \\Leftrightarrow \\frac{SI}{2SO} \\left( \\frac{SA'}{SA} + \\frac{SC'}{SC} \\right) = \\frac{SA'}{SA} \\cdot \\frac{SC'}{SC} \\Leftrightarrow \\frac{SA}{SA'} + \\frac{SC}{SC'} = 2 \\cdot \\frac{SO}{SI}$.\\\\
           Tương tự: $\\frac{SB}{SB'} + \\frac{SD}{SD'} = 2 \\cdot \\frac{SO}{SI}$\\\\
           Ta có: $A'C' // AC \\Rightarrow \\frac{SA}{SA'} = \\frac{SC}{SC'} = %s$.\\\\
           Suy ra: $\\frac{SB}{SB'} + \\frac{SD}{SD'} = \\frac{SA}{SA'} + \\frac{SC}{SC'} = %s + %s = %s$.''' 
                 % (ratio_str, ratio_str, ratio_str, T))
    dapan='\\shortans[0]{$%s$}\n'%(T)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content 

