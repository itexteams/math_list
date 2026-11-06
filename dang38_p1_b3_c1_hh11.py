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


def bt_dang38_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ vẽ đúng như mẫu ảnh
        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (2.2,-1.2);
        \\coordinate (D) at (3.8,0);
        \\coordinate (A) at (1.6,3.6);
        \\coordinate (M) at ($(A)!0.5!(B)$);
        \\coordinate (N) at ($(B)!0.5!(C)$);
        \\coordinate (P) at ($(C)!0.5!(D)$);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A) (A)--(C) (M)--(N)--(P);
        \\draw[line width=1pt, dashed] (B)--(D) (M)--(P);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (M) circle (1pt) node[above left] {$M$};
        \\fill (N) circle (1pt) node[below left] {$N$};
        \\fill (P) circle (1pt) node[below right] {$P$};
    \\end{tikzpicture}
    \\end{center}''')

        # Các mệnh đề đúng:
        # 1. MN là đường trung bình tam giác ABC => MN // AC => AC // (MNP) và MN // (ACD)
        # 2. NP là đường trung bình tam giác BCD => NP // BD => BD // (MNP) và NP // (ABD)
        # 3. Mặt phẳng (MNP) cắt AD tại trung điểm Q của AD, do đó AD cắt (MNP) tại Q nên AD // (MNP) là mệnh đề SAI.

        # Đáp án đúng của câu hỏi (mệnh đề sai)
        da = '$AD // (MNP)$'

        # Các phương án nhiễu (các mệnh đề đúng)
        danh_sach_dung = [
            '$AC // (MNP)$',
            '$NP // (ABD)$',
            '$MN // (ACD)$',
            '$BD // (MNP)$'
        ]
        random.shuffle(danh_sach_dung)

        das1 = danh_sach_dung[0]
        das2 = danh_sach_dung[1]
        das3 = danh_sach_dung[2]

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $M, N, P$ lần lượt là trung điểm của các cạnh $AB, BC, CD$ (tham khảo hình vẽ bên dưới). Mệnh đề nào sau đây sai?%s''' % (hinhve))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Xét từng mệnh đề:\\\\
    - Trong tam giác $ABC$, do $M, N$ lần lượt là trung điểm của $AB, BC$ nên $MN$ là đường trung bình của $\\Delta ABC$.\\\\
    Suy ra $MN // AC$.\\\\
    Vì $\\begin{cases} MN // AC \\\\ MN \\subset (MNP) \\\\ AC \\not\\subset (MNP) \\end{cases} \\Rightarrow AC // (MNP)$. Mệnh đề này đúng.\\\\
    Đồng thời vì $\\begin{cases} MN // AC \\\\ AC \\subset (ACD) \\\\ MN \\not\\subset (ACD) \\end{cases} \\Rightarrow MN // (ACD)$. Mệnh đề này đúng.\\\\
    - Trong tam giác $BCD$, do $N, P$ lần lượt là trung điểm của $BC, CD$ nên $NP$ là đường trung bình của $\\Delta BCD$.\\\\
    Suy ra $NP // BD$.\\\\
    Vì $\\begin{cases} NP // BD \\\\ BD \\subset (ABD) \\\\ NP \\not\\subset (ABD) \\end{cases} \\Rightarrow NP // (ABD)$. Mệnh đề này đúng.\\\\
    - Gọi $Q$ là trung điểm của cạnh $AD$, ta có $MQ$ là đường trung bình của tam giác $ABD$, suy ra $MQ // BD$.\\\\
    Mà $NP // BD$ nên $MQ // NP$, do đó $Q \\in (MNP)$.\\\\
    Vậy đường thẳng $AD$ cắt mặt phẳng $(MNP)$ tại $Q$ nên mệnh đề $%s$ là mệnh đề sai.''' % (da))

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

