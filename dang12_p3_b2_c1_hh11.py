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


def bt_dang12_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    if dang == '1':
        ratio_str = "\\frac{SH}{SC}"
        kq_val = Decimal('0.4')
        final_line = "Vậy $\\frac{SH}{SC} = \\frac{2}{5} = 0,4$."
    elif dang == '2':
        ratio_str = "\\frac{SC}{SH}"
        kq_val = Decimal('2.5')
        final_line = "Từ đó suy ra $\\frac{SC}{SH} = \\frac{5}{2} = 2,5$."
    else:
        ratio_str = "\\frac{HC}{SC}"
        kq_val = Decimal('0.6')
        final_line = "Ta có $SH = 2HJ, SC = 5HJ \\Rightarrow HC = 3HJ$. Vậy $\\frac{HC}{SC} = \\frac{3}{5} = 0,6$."

    # Chuyển đổi kết quả sang chuỗi có dấu phẩy
    s_str = str(kq_val).replace('.', ',')

    # Các đáp án trắc nghiệm
    du = ['$%s$' % s_str]
    da = du[0]

    # Tạo các phương án sai ngẫu nhiên
    s_f = float(kq_val)
    s_list_raw = [
        Decimal(str(s_f + 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP),
        Decimal(str(abs(s_f - 0.1))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP),
        Decimal(str(s_f + 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP),
        Decimal('0.5'),
        Decimal('0.6'),
        Decimal('2.5'),
        Decimal('0.4'),
        Decimal('1.5')
    ]
    s_list = []
    for val in s_list_raw:
        val_str = str(val).replace('.', ',')
        s_list.append('$%s$' % val_str)

    # Loại bỏ các phương án trùng lặp với đáp án đúng
    s_list = list(set(s_list) - set(du))

    das1 = s_list[0]
    das2 = s_list[1]
    das3 = s_list[2]

    # Câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của $AB, AD$ và $G$ là trọng tâm tam giác $SBD$. Mặt phẳng $(MNG)$ cắt $SC$ tại điểm $H$. Tỉ số $%s$ bằng bao nhiêu?'''
                     % (ratio_str))

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
            \\begin{scope}
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (4.5,0);
                \\coordinate (A) at (1.5,1.5);
                \\coordinate (D) at (6,1.5);
                \\coordinate (S) at (2.5,5);
                \\coordinate (O) at ($(A)!0.5!(C)$);
                \\coordinate (M) at ($(A)!0.5!(B)$);
                \\coordinate (N) at ($(A)!0.5!(D)$);
                \\coordinate (E) at (intersection of M--N and A--C);
                \\coordinate (G) at ($(S)!0.666!(O)$);
                \\coordinate (H) at ($(S)!0.4!(C)$);
                \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D);
                \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (M)--(N) (S)--(O) (E)--(H);
                \\fill (S) circle (1pt) node[above] {$S$};
                \\fill (A) circle (1pt) node[above right] {$A$};
                \\fill (B) circle (1pt) node[below left] {$B$};
                \\fill (C) circle (1pt) node[below right] {$C$};
                \\fill (D) circle (1pt) node[right] {$D$};
                \\fill (M) circle (1pt) node[left] {$M$};
                \\fill (N) circle (1pt) node[above right] {$N$};
                \\fill (O) circle (1pt) node[below right] {$O$};
                \\fill (E) circle (1pt) node[below] {$E$};
                \\fill (G) circle (1pt) node[right] {$G$};
                \\fill (H) circle (1pt) node[right] {$H$};
            \\end{scope}
            \\begin{scope}[xshift=7.5cm]
                \\coordinate (A) at (0,0);
                \\coordinate (C) at (5,0);
                \\coordinate (S) at (1.5,4.5);
                \\coordinate (O) at ($(A)!0.5!(C)$);
                \\coordinate (E) at ($(A)!0.25!(C)$);
                \\coordinate (G) at ($(S)!0.666!(O)$);
                \\coordinate (H) at ($(S)!0.4!(C)$);
                \\coordinate (I) at ($(S)!0.5!(G)$);
                \\coordinate (J) at ($(S)!0.5!(H)$);
                \\draw[line width=1pt] (S)--(A)--(C)--(S) (S)--(O) (E)--(H) (A)--(J);
                \\fill (S) circle (1pt) node[above] {$S$};
                \\fill (A) circle (1pt) node[below left] {$A$};
                \\fill (C) circle (1pt) node[below right] {$C$};
                \\fill (E) circle (1pt) node[below] {$E$};
                \\fill (O) circle (1pt) node[below] {$O$};
                \\fill (G) circle (1pt) node[right] {$G$};
                \\fill (H) circle (1pt) node[above right] {$H$};
                \\fill (I) circle (1pt) node[left] {$I$};
                \\fill (J) circle (1pt) node[above right] {$J$};
            \\end{scope}
           \\end{tikzpicture}
           \\end{center}
           Trong mặt phẳng $(ABCD)$, gọi $E = MN \\cap AC$.\\\\
           Trong mặt phẳng $(SAC)$, gọi $H = EG \\cap SC$.\\\\
           Ta có: $\\begin{cases} H \\in EG; EG \\subset (MNG) \\\\ H \\in SC \\end{cases} \\Rightarrow H = SC \\cap (MNG)$.\\\\
           Gọi $I, J$ lần lượt là trung điểm của $SG$ và $SH$.\\\\
           Ta có $\\begin{cases} IJ // HG \\\\ IA // GE \\end{cases} \\Rightarrow A, I, J$ thẳng hàng.\\\\
           Xét $\\triangle ACJ$ có $EH // AJ \\Rightarrow \\frac{CH}{HJ} = \\frac{CE}{EA} = 3 \\Rightarrow CH = 3HJ$.\\\\
           Lại có $SH = 2HJ$ nên $SC = 5HJ$.\\\\
           %s''' % (final_line))
    dapan='\\shortans[0]{$%s$}\n'%(s_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content 

