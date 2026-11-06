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


def bt_dang22_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Giữ nguyên cấu trúc bài gốc trong ảnh
        tam_giac_g = "ABD"
        canh_chua_e = "BC"
        he_so_e = random.choice([
            ("EB = 2EC", "\\frac{BE}{BC} = \\frac{2}{3}"),
            ("BE = 2EC", "\\frac{BE}{BC} = \\frac{2}{3}"),
            ("BC = 3EC", "\\frac{BE}{BC} = \\frac{2}{3}")
        ])
        dieu_kien_e = he_so_e[0]
        ti_le_e = he_so_e[1]

        mp_dung = "EG // (ACD)"

        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3.2);
    \\coordinate (B) at (-1.8,0.2);
    \\coordinate (C) at (-0.1,-1.5);
    \\coordinate (D) at (3,0.3);
    \\coordinate (F) at ($(A)!0.5!(D)$);
    \\coordinate (G) at ($(B)!0.6667!(F)$);
    \\coordinate (E) at ($(B)!0.6667!(C)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (C)--(F);
    \\draw[line width=1pt, dashed] (B)--(D) (B)--(F) (E)--(G);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (F) circle (1pt) node[above right] {$F$};
    \\fill (G) circle (1pt) node[above] {$G$};
    \\fill (E) circle (1pt) node[below left] {$E$};
    \\end{tikzpicture}
    \\end{center}''')

        da = '$%s$' % (mp_dung)

        s = [
            '$EG // (ABC)$',
            '$EG // (BCD)$',
            '$EG // (ABD)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $G$ là trọng tâm tam giác $%s$, $E$ là điểm thuộc cạnh $%s$ sao cho $%s$. Mệnh đề nào sau đây đúng?'''
                         % (tam_giac_g, canh_chua_e, dieu_kien_e))

        loigiai = ('''%s
    Gọi $F$ là trung điểm của $AD$. \\\\
    Vì $G$ là trọng tâm tam giác $ABD$ nên $\\frac{BG}{BF} = \\frac{2}{3}$. \\\\
    Theo giả thiết ta có $%s \\Rightarrow %s$. \\\\
    Trong tam giác $BCF$ có $\\frac{BG}{BF} = %s \\Rightarrow GE // CF$. \\\\
    Mà $CF \\subset (ACD), EG \\not\\subset (ACD)$. \\\\
    Suy ra $EG // (ACD)$.'''
                   % (hinh_tikz, dieu_kien_e, ti_le_e, ti_le_e))

    elif dang == '2':
        # Dạng 2: G là trọng tâm tam giác ABC, E thuộc cạnh BD sao cho EB = 2ED
        tam_giac_g = "ABC"
        canh_chua_e = "BD"
        he_so_e = random.choice([
            ("EB = 2ED", "\\frac{BE}{BD} = \\frac{2}{3}"),
            ("BE = 2ED", "\\frac{BE}{BD} = \\frac{2}{3}"),
            ("BD = 3ED", "\\frac{BE}{BD} = \\frac{2}{3}")
        ])
        dieu_kien_e = he_so_e[0]
        ti_le_e = he_so_e[1]

        mp_dung = "EG // (ACD)"

        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3.2);
    \\coordinate (B) at (-1.8,0.2);
    \\coordinate (C) at (-0.1,-1.5);
    \\coordinate (D) at (3,0.3);
    \\coordinate (F) at ($(A)!0.5!(C)$);
    \\coordinate (G) at ($(B)!0.6667!(F)$);
    \\coordinate (E) at ($(B)!0.6667!(D)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (B)--(F) (D)--(F);
    \\draw[line width=1pt, dashed] (B)--(D) (E)--(G);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (F) circle (1pt) node[right] {$F$};
    \\fill (G) circle (1pt) node[above] {$G$};
    \\fill (E) circle (1pt) node[below] {$E$};
    \\end{tikzpicture}
    \\end{center}''')

        da = '$%s$' % (mp_dung)

        s = [
            '$EG // (ABC)$',
            '$EG // (BCD)$',
            '$EG // (ABD)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $G$ là trọng tâm tam giác $%s$, $E$ là điểm thuộc cạnh $%s$ sao cho $%s$. Mệnh đề nào sau đây đúng?'''
                         % (tam_giac_g, canh_chua_e, dieu_kien_e))

        loigiai = ('''%s
    Gọi $F$ là trung điểm của $AC$. \\\\
    Vì $G$ là trọng tâm tam giác $ABC$ nên $\\frac{BG}{BF} = \\frac{2}{3}$. \\\\
    Theo giả thiết ta có $%s \\Rightarrow %s$. \\\\
    Trong tam giác $BDF$ có $\\frac{BG}{BF} = %s \\Rightarrow GE // DF$. \\\\
    Mà $DF \\subset (ACD), EG \\not\\subset (ACD)$. \\\\
    Suy ra $EG // (ACD)$.'''
                   % (hinh_tikz, dieu_kien_e, ti_le_e, ti_le_e))

    # Các đáp án trắc nghiệm
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)

    # Đưa các đáp án vào danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

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

