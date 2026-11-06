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


def bt_dang33_p1_b3_c1_hh11(self):
    # Dạng 2: G là trọng tâm tam giác ABC, M trên BD sao cho MB = 2MD => MG // (ACD)
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        tam_giac = 'ABD'
        canh_chua_M = 'BC'
        dinh_dau = 'B'
        dinh_cuoi = 'C'
        trung_diem_canh = 'AD'
        canh_song_song = 'NC'
        mp_song_song = '(ACD)'

        # Đáp án đúng
        da = '$MG$ song song với $%s$' % (mp_song_song)

        # Tập hợp các phương án gây nhiễu
        s = [
            '$MG$ song song với (ABD)',
            '$MG$ song song với (ACB)',
            '$MG$ song song với (BCD)',
            '$MG$ song song với (ABC)'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$, $G$ là trọng tâm tam giác $%s$. Trên đoạn $%s$ lấy điểm $M$ sao cho $MB = 2MC$. Khẳng định nào sau đây đúng?'''
                         % (tam_giac, canh_chua_M))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải với hình vẽ TikZ đúng 100% hình mẫu
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (1.5,4);
    \\coordinate (D) at (0.2,1.2);
    \\coordinate (B) at (2,-0.2);
    \\coordinate (C) at (4.5,1.2);
    \\coordinate (N) at ($(A)!0.5!(D)$);
    \\coordinate (G) at ($(B)!0.66667!(N)$);
    \\coordinate (M) at ($(B)!0.66667!(C)$);
    \\draw[line width=1pt] (A)--(D)--(B)--(C)--(A)--(B);
    \\draw[line width=1pt, dashed] (D)--(C) (N)--(C) (G)--(M) (B)--(N);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (N) circle (1pt) node[left] {$N$};
    \\fill (G) circle (1pt) node[left] {$G$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $N$ là trung điểm của $%s$.\\\\
    Vì $G$ là trọng tâm $\\Delta %s$ nên $\\frac{BG}{GN} = 2$ (1).\\\\
    mà $MB = 2MC \\Rightarrow \\frac{MB}{MC} = 2$ (2).\\\\
    Từ (1) và (2) suy ra $\\frac{BG}{GN} = \\frac{BM}{MC} \\Rightarrow MG // %s$.\\\\
    Ta có: $\\begin{cases} MG \\not\\subset %s \\\\ MG // %s, %s \\subset %s \\end{cases} \\Rightarrow MG // %s$.'''
                   % (trung_diem_canh, tam_giac, canh_song_song, mp_song_song, canh_song_song, canh_song_song, mp_song_song, mp_song_song))

    elif dang == '2':
        tam_giac = 'ABC'
        canh_chua_M = 'BD'
        dinh_dau = 'B'
        dinh_cuoi = 'D'
        trung_diem_canh = 'AC'
        canh_song_song = 'ND'
        mp_song_song = '(ACD)'

        da = '$MG$ song song với $%s$' % (mp_song_song)

        s = [
            '$MG$ song song với (ABD)',
            '$MG$ song song với (ACB)',
            '$MG$ song song với (BCD)',
            '$MG$ song song với (ABC)'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho tứ diện $ABCD$, $G$ là trọng tâm tam giác $%s$. Trên đoạn $%s$ lấy điểm $M$ sao cho $MB = 2MD$. Khẳng định nào sau đây đúng?'''
                         % (tam_giac, canh_chua_M))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (1.5,4);
    \\coordinate (D) at (0.2,1.2);
    \\coordinate (B) at (2,-0.2);
    \\coordinate (C) at (4.5,1.2);
    \\coordinate (N) at ($(A)!0.5!(D)$);
    \\coordinate (G) at ($(B)!0.66667!(N)$);
    \\coordinate (M) at ($(B)!0.66667!(C)$);
    \\draw[line width=1pt] (A)--(D)--(B)--(C)--(A)--(B) (B)--(N);
    \\draw[line width=1pt, dashed] (D)--(C) (N)--(C) (G)--(M) ;
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (N) circle (1pt) node[left] {$N$};
    \\fill (G) circle (1pt) node[left] {$G$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $N$ là trung điểm của $%s$.\\\\
    Vì $G$ là trọng tâm $\\Delta %s$ nên $\\frac{BG}{GN} = 2$ (1).\\\\
    mà $MB = 2MD \\Rightarrow \\frac{MB}{MD} = 2$ (2).\\\\
    Từ (1) và (2) suy ra $\\frac{BG}{GN} = \\frac{BM}{MD} \\Rightarrow MG // %s$.\\\\
    Ta có: $\\begin{cases} MG \\not\\subset %s \\\\ MG // %s, %s \\subset %s \\end{cases} \\Rightarrow MG // %s$.'''
                   % (trung_diem_canh, tam_giac, canh_song_song, mp_song_song, canh_song_song, canh_song_song, mp_song_song, mp_song_song))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

