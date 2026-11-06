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


def bt_dang7_p3_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random hệ số mẫu số của AP/AB. Giới hạn random từ 3 đến 6
        k = random.choice([3, 4, 5, 6])

        # Tính các thông số cho lời giải
        k_minus_1 = k - 1

        # Tính kết quả chính xác
        kq_exact = 1 / k

        # Làm tròn đến hàng phần trăm (2 chữ số thập phân) theo yêu cầu
        kq_dec = Decimal(float(kq_exact)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq_dec).replace('.', ',')

        # Tạo các đáp án gây nhiễu (sai)
        choices = [
            Decimal(float(1 / (k - 1))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(float(1 / (k + 1))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(float(2 / k)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(float(1 / (k + 2))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(float(2 / (k + 1))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        ]

        # Lọc ra các đáp án sai không trùng với đáp án đúng
        s = []
        for c in choices:
            c_str = str(c).replace('.', ',')
            if c_str != kq_str and c_str not in s:
                s.append(c_str)

        # Chọn ngẫu nhiên 3 phương án sai
        random.shuffle(s)
        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Các đáp án trắc nghiệm
        da_d = '\\True $%s$' % kq_str
        da_s1 = '$%s$' % das1
        da_s2 = '$%s$' % das2
        da_s3 = '$%s$' % das3

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung câu hỏi và vẽ hình bằng native TikZ (calc library)
        noidungcauhoi = ('''Cho hình chóp $S.ABC$. Gọi $M,N$ lần lượt là trung điểm của $SA,BC$ và $P$ là điểm nằm trên cạnh $AB$ sao cho $AP=\\frac{1}{%s}AB$. Gọi $Q$ là giao điểm của $SC$ và $(MNP)$. Tỉ số $\\frac{SQ}{SC}$ bằng bao nhiêu (kết quả làm tròn đến hàng phần trăm).''' % (k))

        # Nội dung lời giải chi tiết
        loigiai = ('''\\begin{center}
        \\begin{tikzpicture}[scale=0.7, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (2,-3);
        \\coordinate (C) at (7,-0.5);
        \\coordinate (S) at (2.2,4.5);
        \\coordinate (M) at ($(S)!0.5!(A)$);
        \\coordinate (N) at ($(B)!0.5!(C)$);
        \\coordinate (P) at ($(A)!1/%s!(B)$);
        \\coordinate (I) at (intersection of N--P and A--C);
        \\coordinate (Q) at (intersection of M--I and S--C);
        \\coordinate (A_BC) at ($(A)+(C)-(B)$);
        \\coordinate (K) at (intersection of I--N and A--A_BC);
        \\coordinate (A_SC) at ($(A)+(C)-(S)$);
        \\coordinate (E) at (intersection of I--Q and A--A_SC);
        \\draw[line width=1pt] (S)--(A) (S)--(B) (S)--(C) (A)--(B) (B)--(C) (I)--(A) (I)--(M) (I)--(K) (K)--(P) (A)--(E) (A)--(K);
        \\draw[line width=1pt, dashed] (A)--(C) (M)--(Q) (P)--(N);
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (A) circle (1pt) node[above right] {$A$};
        \\fill (B) circle (1pt) node[below] {$B$};
        \\fill (C) circle (1pt) node[right] {$C$};
        \\fill (M) circle (1pt) node[below right] {$M$};
        \\fill (N) circle (1pt) node[below right] {$N$};
        \\fill (P) circle (1pt) node[below] {$P$};
        \\fill (I) circle (1pt) node[left] {$I$};
        \\fill (Q) circle (1pt) node[above right] {$Q$};
        \\fill (K) circle (1pt) node[below] {$K$};
        \\fill (E) circle (1pt) node[above left] {$E$};
        \\end{tikzpicture}
        \\end{center} Gọi $I$ là giao điểm của $NP$ và $AC$. Khi đó $Q$ là giao điểm của $MI$ và $SC$.\\\\
    Từ $A$ kẻ đường thẳng song song với $BC$, cắt $IN$ tại $K$.\\\\
    Khi đó $\\frac{AK}{BN}=\\frac{AP}{BP}=\\frac{1}{%s} \\Rightarrow \\frac{IA}{IC}=\\frac{AK}{CN}=\\frac{1}{%s}$.\\\\
    Từ $A$ kẻ đường thẳng song song với $SC$, cắt $IQ$ tại $E$.\\\\
    Khi đó $\\frac{AE}{SQ}=\\frac{AM}{SM}=1 \\Rightarrow AE=SQ$, $\\frac{AE}{CQ}=\\frac{IA}{IC}=\\frac{1}{%s} \\Rightarrow AE=\\frac{1}{%s}CQ$. Do đó $\\frac{SQ}{SC}=\\frac{1}{%s} \\approx %s$.'''
        % (k, k_minus_1, k_minus_1, k_minus_1, k_minus_1, k, kq_str))
    dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content      

