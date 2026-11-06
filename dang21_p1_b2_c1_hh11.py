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


def bt_dang21_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1', '2', '3']
    dang=random.choice(lisdang)

    td = 'S.ABCD'
    day = 'ABCD'
    hh = 'hình bình hành'

    if dang=='1':
        # Xét mặt phẳng (SAD)
        d1, d2, d3 = 'M', 'N', 'P'
        c1, c2, c3 = 'AB', 'CD', 'SA'
        mp_cat = 'SAD'

        # Đáp án đúng
        gt_dung = 'Đường thẳng đi qua $%s$ và song song $%s$' % (d3, 'AD')

        # Các đáp án sai
        s1 = '$%s$' % ('NP')
        s2 = 'Đường thẳng đi qua $%s$ và song song $%s$' % (d1, 'AC')
        s3 = 'Đường thẳng đi qua $%s$ và song song $%s$' % ('S', 'AD')

        # Text cho lời giải
        lg_mp1 = 'SAD'
        lg_mp2 = 'ABCD'
        lg_giao1 = 'AD'
        lg_mp3 = 'MNP'
        lg_giao2 = 'MN'
        lg_giao3 = 'Px'
        lg_songsong = 'AD'
        lg_diem_gt = 'P'

    elif dang=='2':
        # Xét mặt phẳng (SBC)
        d1, d2, d3 = 'M', 'N', 'P'
        c1, c2, c3 = 'AB', 'CD', 'SB'
        mp_cat = 'SBC'

        gt_dung = 'Đường thẳng đi qua $%s$ và song song $%s$' % (d3, 'BC')

        s1 = '$%s$' % ('NP')
        s2 = 'Đường thẳng đi qua $%s$ và song song $%s$' % (d2, 'BD')
        s3 = 'Đường thẳng đi qua $%s$ và song song $%s$' % ('S', 'BC')

        lg_mp1 = 'SBC'
        lg_mp2 = 'ABCD'
        lg_giao1 = 'BC'
        lg_mp3 = 'MNP'
        lg_giao2 = 'MN'
        lg_giao3 = 'Px'
        lg_songsong = 'BC'
        lg_diem_gt = 'P'

    elif dang=='3':
        # Xét mặt phẳng (SCD)
        d1, d2, d3 = 'M', 'N', 'P'
        c1, c2, c3 = 'AD', 'BC', 'SD'
        mp_cat = 'SCD'

        gt_dung = 'Đường thẳng đi qua $%s$ và song song $%s$' % (d3, 'CD')

        s1 = '$%s$' % ('MP')
        s2 = 'Đường thẳng đi qua $%s$ và song song $%s$' % (d1, 'AC')
        s3 = 'Đường thẳng đi qua $%s$ và song song $%s$' % ('S', 'CD')

        lg_mp1 = 'SCD'
        lg_mp2 = 'ABCD'
        lg_giao1 = 'CD'
        lg_mp3 = 'MNP'
        lg_giao2 = 'MN'
        lg_giao3 = 'Px'
        lg_songsong = 'CD'
        lg_diem_gt = 'P'


    # Câu hỏi
    noidungcauhoi = ('''Cho hình chóp $%s$ có đáy $%s$ là %s. Gọi $%s, %s, %s$ lần lượt là trung điểm của $%s, %s, %s$. Giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ là'''
                     %(td, day, hh, d1, d2, d3, c1, c2, c3, lg_mp3, mp_cat))

    # Các đáp án
    da_d = ('\\True ' + str(gt_dung))
    da_s1 = str(s1)
    da_s2 = str(s2) 
    da_s3 = str(s3) 

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d,da_s1,da_s2,da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai=('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (1.5,1);
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4,0);
    \\coordinate (D) at (5.5,1);
    \\coordinate (S) at (1.5,3.5);
    \\coordinate (M) at ($(A)!0.5!(B)$);
    \\coordinate (N) at ($(C)!0.5!(D)$);
    \\coordinate (P) at ($(S)!0.5!(A)$);
    \\coordinate (I) at ($(S)!0.5!(D)$);
    \\coordinate (Px) at (6.5, 2.25);
    \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D) (I)--(Px);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (M)--(N) (P)--(I);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\fill (N) circle (1pt) node[below right] {$N$};
    \\fill (P) circle (1pt) node[above left] {$P$};
    \\node at (6.5, 2.4) {$x$};
    \\end{tikzpicture}
    \\end{center} Ta có $(%s) \\cap (%s) = %s, (%s) \\cap (%s) = %s, (%s) \\cap (%s) = %s$ \\\\
    mà $%s // %s \\Rightarrow %s // %s // %s$. \\\\
    Vậy giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ đường thẳng đi qua $%s$ và song song $%s$.'''
             %(lg_mp1, lg_mp2, lg_giao1, lg_mp2, lg_mp3, lg_giao2, lg_mp1, lg_mp3, lg_giao3, lg_giao2, lg_giao1, lg_giao2, lg_giao1, lg_giao3, lg_mp3, lg_mp1, lg_diem_gt, lg_songsong))


    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\choice \n'
               '{'+str(list_1[1])+'}\n'
               '{'+str(list_1[2])+'}\n'
               '{'+str(list_1[3])+'}\n'
               '{'+str(list_1[0])+'}\n'
               '\\loigiai{'+str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

