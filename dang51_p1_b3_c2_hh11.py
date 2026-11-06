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


def bt_dang51_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số k sao cho SA = k*a. 
                # Trong đề gốc k=2. Ta chọn k từ 2 đến 5 để đảm bảo hình vẽ và tính toán đẹp.
                k = randint(2, 5)

                # Tính toán Cosin của góc BSA: cos = SA / SB = (k*a) / sqrt((k*a)^2 + a^2) = k / sqrt(k^2 + 1)
                tu = k
                mau_binh_phuong = k**2 + 1

                # Kết quả đúng dưới dạng LaTeX
                kq_bieu_thuc = Rational(tu, 1) / sqrt(mau_binh_phuong)
                da_dung = '$' + latex(kq_bieu_thuc) + '$'

                # Tạo các phương án sai (distractors)
                s = []
                # Phương án sai 1: sin của góc (AB/SB)
                s1 = '$' + latex(Rational(1, 1) / sqrt(mau_binh_phuong)) + '$'
                s.append(s1)
                # Phương án sai 2: k/ (k+1)
                s2 = '$' + latex(Rational(k, k+1)) + '$'
                s.append(s2)
                # Phương án sai 3: các giá trị thường gặp 1/2, sqrt(3)/2, 1
                common = ['$1$', '$\\frac{1}{2}$', '$\\frac{\\sqrt{3}}{2}$', '$\\frac{\\sqrt{2}}{2}$']
                s3 = random.choice(common)
                s.append(s3)

                # Đảm bảo các phương án sai không trùng đáp án đúng
                while da_dung in s:
                    s.remove(da_dung)
                    s.append('$\\frac{%s}{%s}$' % (randint(1, 5), randint(6, 10)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Hai mặt phẳng $\\left(SAB\\right)$ và $\\left(SAC\\right)$ cùng vuông góc với đáy $\\left(ABCD\\right)$ và $SA = %sa$. Cosin của góc giữa đường thẳng $SB$ và mặt phẳng $\\left(SAD\\right)$ là'''
                                 %(latex(k) if k != 1 else ''))

                # Vẽ hình bằng TikZ
                tikz_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line width=1pt]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (3,-1.2);
                \\coordinate (C) at (5,0);
                \\coordinate (D) at (2,1.2);
                \\coordinate (S) at (0,4);  
                \\draw [dashed]  (A)--(D) (S)--(D) (C)--(D);
                \\draw (S)--(B) (S)--(A) (A)--(B) (S)--(C)  (B)--(C) ;
                \\node [left] at (A) {$A$};
                \\node [below] at (B) {$B$};
                \\node [right] at (C) {$C$};
                \\node [right] at (D) {$D$};
                \\node [above] at (S) {$S$};
                \\draw (0,0.3) -- (0.3,0.3) -- (0.3,0);
                \\draw (0.2,0.12) -- (0.4,0.24) -- (0.2,0.12); 
            \\end{tikzpicture}
            \\end{center}''')

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có: $\\begin{cases} \\left(SAB\\right) \\perp \\left(ABCD\\right) \\\\ \\left(SAC\\right) \\perp \\left(ABCD\\right) \\\\ \\left(SAB\\right) \\cap \\left(SAC\\right) = SA \\end{cases} \\Rightarrow SA \\perp \\left(ABCD\\right)$.\\\\
                             Vì $ABCD$ là hình vuông nên $AB \\perp AD$.\\\\
                             Mà $SA \\perp \\left(ABCD\\right) \\Rightarrow SA \\perp AB$.\\\\
                             Ta có $\\begin{cases} AB \\perp AD \\\\ AB \\perp SA \\\\ AD \\cap SA = A \\end{cases} \\Rightarrow AB \\perp \\left(SAD\\right)$.\\\\
                             Do đó, hình chiếu vuông góc của đường thẳng $SB$ lên mặt phẳng $\\left(SAD\\right)$ là đường thẳng $SA$.\\\\
                             Suy ra góc giữa đường thẳng $SB$ và mặt phẳng $\\left(SAD\\right)$ là góc giữa hai đường thẳng $SB$ và $SA$, chính là góc $\\widehat{BSA}$.\\\\
                             Xét tam giác $SAB$ vuông tại $A$ (do $SA \\perp AB$), ta có:\\\\
                             $SB = \\sqrt{SA^2 + AB^2} = \\sqrt{\\left(%sa\\right)^2 + a^2} = a\\sqrt{%s}$.\\\\
                             Vậy $\\cos\\left(SB, \\left(SAD\\right)\\right) = \\cos \\widehat{BSA} = \\frac{SA}{SB} = \\frac{%sa}{a\\sqrt{%s}} = %s$.'''
                           %(latex(k), latex(mau_binh_phuong), latex(k), latex(mau_binh_phuong), latex(kq_bieu_thuc)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + tikz_hinh+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

