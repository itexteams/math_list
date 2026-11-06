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


def bt_dang4_p3_b1_c1_hh11(self):
    # Random hóa bằng cách yêu cầu các tỉ số khác nhau trên cùng một cấu trúc hình
    variants = [
        {'ask': '\\frac{IS}{IG}', 'ans': '3'},
        {'ask': '\\frac{IG}{IS}', 'ans': '\\frac{1}{3}'},
        {'ask': '\\frac{SG}{IG}', 'ans': '4'},
        {'ask': '\\frac{IG}{SG}', 'ans': '\\frac{1}{4}'},
        {'ask': '\\frac{IS}{SG}', 'ans': '\\frac{3}{4}'},
        {'ask': '\\frac{SG}{IS}', 'ans': '\\frac{4}{3}'}
    ]

    choice_dict = random.choice(variants)
    yeucau = choice_dict['ask']
    kq = choice_dict['ans']

    # Các đáp án trắc nghiệm
    all_options = ['3', '\\frac{1}{3}', '4', '\\frac{1}{4}', '\\frac{3}{4}', '\\frac{4}{3}', '2', '\\frac{1}{2}']
    if kq in all_options:
        all_options.remove(kq)
    random.shuffle(all_options)

    da = '$%s$' % kq
    das1 = '$%s$' % all_options[0]
    das2 = '$%s$' % all_options[1]
    das3 = '$%s$' % all_options[2]

    # Câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là tứ giác lồi. Gọi $N$, $P$ lần lượt là trung điểm của $SB$ và $AD$. Gọi $I$ là trung điểm của $NP$ và $G$ là giao điểm của $SI$ với mặt phẳng $(ABCD)$. Tỉ số $%s$ bằng bao nhiêu?''' % (yeucau))

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
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (6,0);
    \\coordinate (D) at (1.8,-1.5);
    \\coordinate (C) at (4.2,-1.2);
    \\coordinate (S) at (2.7,3.5);
    \\coordinate (N) at ($(S)!0.5!(B)$);
    \\coordinate (P) at ($(A)!0.5!(D)$);
    \\coordinate (I) at ($(N)!0.5!(P)$);
    \\coordinate (G) at (intersection of S--I and B--P);
    \\coordinate (H) at ($(B)!0.5!(G)$);
    \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (S)--(B) (A)--(D)--(C)--(B) (S)--(P);
    \\draw[line width=1pt, dashed] (A)--(B) (B)--(P)  (S)--(G) (N)--(P) (N)--(H);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (P) circle (1pt) node[left] {$P$};
    \\fill (I) circle (1pt) node[right] {$I$};
    \\fill (G) circle (1pt) node[below] {$G$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\end{tikzpicture}
    \\end{center}
    Trong mặt phẳng $(SBP)$, gọi $G$ là giao điểm của $SI$ và $BP$. \\\\
    Vì $BP \\subset (ABCD)$ nên $G$ chính là giao điểm của $SI$ và mặt phẳng $(ABCD)$.\\\\
    Qua $N$ dựng đường thẳng song song với $SG$ cắt $BP$ tại $H$. Suy ra $G$ là trung điểm $PH$ và $H$ là trung điểm $BG$. \\\\
    Suy ra $IG = \\frac{1}{2}NH$, $NH = \\frac{1}{2}SG$. \\\\
    Vậy ta có $SG = 2NH = 4IG$. \\\\
    Do $S, I, G$ thẳng hàng nên $SI = SG - IG = 3IG$. \\\\
    Từ đó, ta có tỉ số $\\frac{IS}{IG} = 3$. \\\\
    Suy ra $%s = %s$.''' % (yeucau, kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content      

