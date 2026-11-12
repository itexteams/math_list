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


def bt_dang29_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dữ liệu các cặp tam giác và đường thẳng song song tương ứng
        ds_cap = [
            {
                'tg1': 'SAB',
                'tg2': 'SBC',
                'canh_chung': 'SB',
                'da_dung': '$AC$',
                'da_sai': ['$BD$', '$AB$', '$BC$', '$CD$', '$AD$']
            }
        ]
        ch = random.choice(ds_cap)
        tg1 = ch['tg1']
        tg2 = ch['tg2']
        canh_chung = ch['canh_chung']

        # Đỉnh còn lại trong 2 tam giác để xét đường trung tuyến
        dinh1 = tg1.replace('S', '').replace(canh_chung.replace('S', ''), '')
        dinh2 = tg2.replace('S', '').replace(canh_chung.replace('S', ''), '')

        # Hình vẽ TikZ
        hinhve = ('''\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (0,0);
            \\coordinate (D) at (-1.8,-0.6);
            \\coordinate (C) at (1.3,-0.6);
            \\coordinate (B) at ($(A)+(C)-(D)$);
            \\coordinate (S) at (0,3);
            \\coordinate (M) at ($(S)!0.5!(B)$);
            \\coordinate (I) at ($(A)!2/3!(M)$);
            \\coordinate (J) at ($(C)!2/3!(M)$);
            \\draw[line width=1pt] (S)--(D)--(C)--(B)--(S) (S)--(C) (C)--(M);
            \\draw[line width=1pt, dashed] (S)--(A) (A)--(D) (A)--(B) (A)--(C) (A)--(M) (I)--(J);
            \\fill (S) circle (1pt) node[above] {$S$};
            \\fill (A) circle (1pt) node[below] {$A$};
            \\fill (B) circle (1pt) node[right] {$B$};
            \\fill (C) circle (1pt) node[below] {$C$};
            \\fill (D) circle (1pt) node[below left] {$D$};
            \\fill (M) circle (1pt) node[above right] {$M$};
            \\fill (I) circle (1pt) node[above left] {$I$};
            \\fill (J) circle (1pt) node[right] {$J$};
        \\end{tikzpicture}
        \\end{center}''')

        # Các đáp án trắc nghiệm
        du = [ch['da_dung']]
        da = random.choice(du)
        s = ch['da_sai'].copy()

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$, có đáy $ABCD$ là hình bình hành. Gọi $I, J$ là trọng tâm các tam giác $%s, %s$. Khi đó đường thẳng $IJ$ song song với đường thẳng nào sau đây?%s'''
                        % (tg1, tg2, hinhve))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Gọi $M$ là trung điểm của $%s$.\\\\
        Vì $I, J$ lần lượt là trọng tâm tam giác $%s$ và $%s$ nên $I \\in M%s$ và $J \\in M%s$.\\\\
        Theo tính chất trọng tâm tam giác, ta có:
        $$\\frac{MI}{M%s} = \\frac{MJ}{M%s} = \\frac{1}{3}.$$
        Xét tam giác $M%s%s$, theo định lí Ta-lét đảo ta suy ra:
        $$IJ // %s%s.$$
        Vậy đường thẳng $IJ$ song song với đường thẳng %s.'''
                % (canh_chung, tg1, tg2, dinh1, dinh2, dinh1, dinh2, dinh1, dinh2, dinh1, dinh2, da))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' +
            str(noidungcauhoi) + '\\choice \n'
            '{' + str(list_1[1]) + '}\n'
            '{' + str(list_1[2]) + '}\n'
            '{' + str(list_1[3]) + '}\n'
            '{' + str(list_1[0]) + '}\n'
            '\\loigiai{' + str(loigiai) + '}\n'
            '\\end{ex}\n \\end{minipage} \n\n')
    return content

