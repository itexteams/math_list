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


def bt_dang24_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Khai báo các tham số để dùng %s
        mp_day = 'ABCD'
        tam = 'O'
        diem1 = 'M'
        diem2 = 'N'
        canh1 = 'SA'
        canh2 = 'SD'

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.%s$ có đáy $%s$ là hình bình hành tâm $%s$. Gọi $%s, %s$ lần lượt là trung điểm của $%s$ và $%s$. Trong các khẳng định sau, khẳng định nào sai?'''
                         % (mp_day, mp_day, tam, diem1, diem2, canh1, canh2))

        # Các đáp án
        da_d = '\\True $ON // SC$'
        da_s1 = '$MN // BC$'
        da_s2 = '$ON // SB$'
        da_s3 = '$OM // SC$'

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (2,1.5);
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (4.5,0);
        \\coordinate (D) at (6.5,1.5);
        \\coordinate (S) at (1,4);
        \\coordinate (O) at ($(A)!0.5!(C)$);
        \\coordinate (M) at ($(S)!0.5!(A)$);
        \\coordinate (N) at ($(S)!0.5!(D)$);
        \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D);
        \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (M)--(N) (O)--(M) (O)--(N);
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[below] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (S) circle (1pt) node[above right] {$S$};
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (M) circle (1pt) node[left] {$M$};
        \\fill (N) circle (1pt) node[right] {$N$};
        \\end{tikzpicture}
        \\end{center} Ta có: $%s%s$ là đường trung bình của tam giác $SAD$. Suy ra, $%s%s // AD$ mà $AD // BC$ nên $%s%s // BC$. \\\\
    Xét tam giác $SBD$ có $ON$ là đường trung bình. Suy ra, $ON // SB$. \\\\
    Xét tam giác $SAC$ có $OM$ là đường trung bình. Suy ra, $OM // SC$. \\\\
    Vậy khẳng định $ON // SC$ là sai.''' % (diem1, diem2, diem1, diem2, diem1, diem2))

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

