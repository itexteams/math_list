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


def bt_dang6_p3_b1_c1_hh11(self):
    # Khai báo biến
    # Random bài toán bằng cách yêu cầu các tỉ số khác nhau giữa 3 điểm S, G, O
    # Gán giá trị số học (float) để thuận tiện cho việc làm tròn
    variants = [
        {'ask': '\\frac{SG}{GO}', 'val': 2.0},
        {'ask': '\\frac{GO}{SG}', 'val': 0.5},
        {'ask': '\\frac{SG}{SO}', 'val': 2/3},
        {'ask': '\\frac{SO}{SG}', 'val': 1.5},
        {'ask': '\\frac{GO}{SO}', 'val': 1/3},
        {'ask': '\\frac{SO}{GO}', 'val': 3.0}
    ]

    choice_dict = random.choice(variants)
    yeucau = choice_dict['ask']
    val_kq = choice_dict['val']

    # Quy tròn đến hàng phần 10 và chuyển dấu chấm thành dấu phẩy
    kq_decimal = Decimal(float(val_kq)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    kq = str(kq_decimal).replace('.', ',')

    # Tạo danh sách các giá trị nhiễu tiềm năng
    all_vals = [2.0, 0.5, 2/3, 1.5, 1/3, 3.0, 0.25, 4.0]

    # Áp dụng quy tròn cho tất cả các đáp án nhiễu
    all_options = [str(Decimal(float(v)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',') for v in all_vals]

    # Loại bỏ trùng lặp và loại bỏ đáp án đúng khỏi danh sách nhiễu
    all_options = list(set(all_options))
    if kq in all_options:
        all_options.remove(kq)
    random.shuffle(all_options)

    # Đưa vào format LaTeX
    da = '$%s$' % kq
    das1 = '$%s$' % all_options[0]
    das2 = '$%s$' % all_options[1]
    das3 = '$%s$' % all_options[2]

    # Câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật. Gọi $M, N$ theo thứ tự là trọng tâm $\\Delta SAB; \\Delta SCD$. Gọi $G$ là giao điểm của đường thẳng $MN$ với mặt phẳng $(SAC)$, $O$ là tâm của hình chữ nhật $ABCD$. Khi đó tỉ số $%s$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần mười).''' % (yeucau))

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
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (5,0);
    \\coordinate (A) at (1.5,1.5);
    \\coordinate (D) at ($(A)+(C)-(B)$);
    \\coordinate (S) at (2.5,5);
    \\coordinate (E) at ($(A)!0.5!(B)$);
    \\coordinate (F) at ($(C)!0.5!(D)$);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (M) at ($(S)!2/3!(E)$);
    \\coordinate (N) at ($(S)!2/3!(F)$);
    \\coordinate (G) at ($(S)!2/3!(O)$);
    \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D) (S)--(F);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (S)--(E) (E)--(F) (S)--(O) (M)--(N);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (E) circle (1pt) node[below left] {$E$};
    \\fill (F) circle (1pt) node[below right] {$F$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (M) circle (1pt) node[above left] {$M$};
    \\fill (N) circle (1pt) node[above right] {$N$};
    \\fill (G) circle (1pt) node[below left] {$G$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $E, F$ lần lượt là trung điểm của $AB, CD$. \\\\
    Ta có: $O \\in FE$. Xét hai mặt phẳng $(SEF)$ và $(SAC)$ có: \\\\
    $\\begin{cases} O \\in EF \\subset (SEF) \\\\ O \\in AC \\subset (SAC) \\end{cases} \\Rightarrow O \\in (SEF) \\cap (SAC)$. Mà $S \\in (SEF) \\cap (SAC)$ nên $(SEF) \\cap (SAC) = SO$. \\\\
    Trong mặt phẳng $(SEF)$ ta có: $SO \\cap MN = G \\Rightarrow \\begin{cases} G \\in MN \\\\ G \\in SO \\subset (SAC) \\end{cases} \\Rightarrow MN \\cap (SAC) = \\{G\\}$. \\\\
    Xét tam giác $SFE$ có: $MG // EF \\; (\\text{do } MN // EF) \\Rightarrow \\frac{SG}{SO} = \\frac{SM}{SE} = \\frac{2}{3} \\Rightarrow \\frac{SG}{GO} = 2$. \\\\
    Từ đó suy ra tỉ số $%s \\approx %s$.''' % (yeucau, kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content      

