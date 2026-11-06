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


def bt_dang37_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Thiết lập biến ngẫu nhiên hệ số tỉ lệ: SN/ND = 1/k => SN/SD = 1/(k+1) và AM = AD/(k+1)
        k_val = random.choice([2, 3])
        k_plus_1 = k_val + 1

        # Tạo chuỗi tỉ lệ cho giả thiết
        if k_val == 2:
            str_sn = '\\frac{ND}{2}'
        else:
            str_sn = '\\frac{ND}{%s}' % (k_val)

        str_am = '\\frac{AD}{%s}' % (k_plus_1)
        str_ti_le = '\\frac{1}{%s}' % (k_plus_1)

        # Đáp án đúng và các phương án gây nhiễu (không có dấu chấm ở cuối)
        da = '$NK // (SAB)$'
        s = [
            '$NK // SB$',
            '$NK // SA$',
            '$NK // SC$',
            '$NK // (SCD)$',
            '$NK // (SBC)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Hình vẽ TikZ 100% theo mẫu và phong cách yêu cầu
        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0.5,0.8);
        \\coordinate (B) at (-1.2,-1);
        \\coordinate (C) at (2.8,-1);
        \\coordinate (D) at ($(A)+(C)-(B)$);
        \\coordinate (S) at (0.3,3.5);
        \\coordinate (O) at ($(A)!0.5!(C)$);
        \\coordinate (E) at ($(B)!0.5!(C)$);
        \\coordinate (G) at ($(A)!2/3!(E)$);
        \\coordinate (M) at ($(A)!1/3!(D)$);
        \\coordinate (N) at ($(S)!1/3!(D)$);
        \\coordinate (H) at ($(S)!1/3!(B)$);
        \\coordinate (K) at ($(M)!0.5!(G)$);
        \\fill[color=blue!20, opacity=0.6] (G)--(M)--(N)--(H)--cycle;
        \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D) (H)--(N);
        \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (A)--(E) (G)--(M)--(N) (G)--(H) (M)--(K)--(N);
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (M) circle (1pt) node[below right] {$M$};
        \\fill (N) circle (1pt) node[above right] {$N$};
        \\fill (H) circle (1pt) node[left] {$H$};
        \\fill (G) circle (1pt) node[below] {$G$};
        \\fill (K) circle (1pt) node[right] {$K$};
        \\fill (E) circle (1pt);
        \\fill (O) circle (1pt);
    \\end{tikzpicture}
    \\end{center}''')

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành; điểm $N$ thuộc cạnh $SD$, sao cho $SN = %s$; điểm $M$ thuộc cạnh $AD$, sao cho $AM = %s$; $G$ là trọng tâm của $\\Delta ABC$. Điểm $K$ luôn thuộc đường thẳng $MG$. Mệnh đề nào sau đây đúng?'''
                         % (str_sn, str_am))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''%s
    Gọi $O$ là tâm hình bình hành $ABCD$, khi đó $BO$ là trung tuyến của $\\Delta ABC$.\\\\
    Do $G$ là trọng tâm của $\\Delta ABC$, ta có $\\frac{BG}{BO} = \\frac{2}{3}$.\\\\
    Mặt khác $BD = 2BO$, suy ra:
    $$\\frac{BG}{BD} = \\frac{1}{3}.$$
    Theo giả thiết:
    - Trên cạnh $AD$ ta có:
    $$\\frac{AM}{AD} = %s \\Rightarrow \\frac{DM}{DA} = 1 - %s = \\frac{%s}{%s}.$$
    - Trên đoạn $BD$:
    $$\\frac{DG}{BD} = 1 - \\frac{BG}{BD} = 1 - \\frac{1}{3} = \\frac{2}{3}.$$
    - Từ $SN = %s \\Rightarrow \\frac{SN}{SD} = %s$.\\\\
    Trong tam giác $SBD$, xét tỉ số trên hai cạnh $SB$ và $SD$: lấy điểm $H \\in SB$ sao cho $\\frac{SH}{SB} = \\frac{SN}{SD} = %s$, ta suy ra $HN // BD$.\\\\
    Tương tự, xét quan hệ song song của các đường thẳng trong mặt phẳng $(GMN)$ với mặt phẳng $(SAB)$:\\\\
    Ta có mặt phẳng $(GMN)$ song song với mặt phẳng $(SAB)$, tức là $(GMN) // (SAB)$.\\\\
    Vì $K$ thuộc đường thẳng $MG$ nên $K \\in (GMN)$, từ đó ta có đường thẳng $NK \\subset (GMN)$.\\\\
    Do đó:
    $$(GMN) // (SAB) \\Rightarrow NK // (SAB).$$'''
                   % (hinhve, str_am, str_am, k_val, k_plus_1, str_sn, str_ti_le, str_ti_le))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\choice \n' +
               '{' + str(list_1[0]) + '}\n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

