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


def bt_dang59_p3_b1_c2_hh11(self):
            # Khai báo biến
            # --- BƯỚC 1 & 2: THIẾT LẬP GIÁ TRỊ VÀ TÍNH TOÁN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Giả sử độ dài cạnh tứ diện là a (chọn ngẫu nhiên một số nguyên để minh họa trong lời giải)
                a_val = random.randint(2, 10) 

                # Kết quả cos(AB, DM) trong tứ diện đều luôn là sqrt(3)/6
                kq_sym = Rational(1, 6) * sqrt(3)
                kq_latex = latex(kq_sym)

                # Các phương án nhiễu (sai) thường gặp trong trắc nghiệm hình học
                s = [
                    '$%s$' % latex(Rational(1, 2) * sqrt(3)),  # sqrt(3)/2
                    '$%s$' % latex(Rational(1, 2)),            # 1/2
                    '$%s$' % latex(Rational(1, 2) * sqrt(2)),  # sqrt(2)/2
                    '$%s$' % latex(Rational(1, 3) * sqrt(3)),  # sqrt(3)/3
                    '$%s$' % latex(Rational(1, 4)),            # 1/4
                    '$%s$' % latex(Rational(1, 3))             # 1/3
                ]

                # Chọn ngẫu nhiên 3 đáp án sai
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Đáp án đúng
                da_dung = '$%s$' % kq_latex

                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện đều $ABCD$, $M$ là trung điểm của cạnh $BC$. Giá trị của $\\cos(AB, DM)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).''')

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- BƯỚC 3: HÌNH VẼ TIKZ ---
                # Vẽ tứ diện đều và các điểm M (trung điểm BC), N (trung điểm AC)
                hinhtikz = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line cap=round]
                \\coordinate (A) at (1,3);
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (3,0.5);
                \\coordinate (D) at (1.2,1);
                \\coordinate (M) at ($(B)!0.5!(C)$);
                \\coordinate (N) at ($(A)!0.5!(C)$);
                \\draw[dashed] (B)--(D)--(C) (D)--(A) (D)--(M) (N)--(D);
                \\draw (A)--(B)--(C)--cycle (A)--(C) (N)--(M);
                \\foreach \\p/\\pos in {A/above, B/left, C/right, D/left, M/below, N/right}
                    \\fill (\\p) node[\\pos] {$\\p$};
            \\end{tikzpicture}
            \\end{center}''')

                # --- BƯỚC 4: NỘI DUNG LỜI GIẢI ---
                h1=sqrt(3)/6
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                loigiai = (hinhtikz + '''Giả sử cạnh của tứ diện đều bằng $a$. \\\\
            Gọi $N$ là trung điểm của $AC$. Vì $MN$ là đường trung bình của tam giác $ABC$ nên $MN \\parallel AB$ và $MN = \\frac{AB}{2} = \\frac{a}{2}$. \\\\
            Khi đó: $(AB, DM) = (MN, DM) = \\widehat{NMD}$ (hoặc bù với góc này). \\\\
            Xét tam giác $MND$: \\\\
            $MN = \\frac{a}{2}$. \\\\
            $DM$ là đường cao trong tam giác đều $BCD$ cạnh $a$ nên $DM = \\frac{a\\sqrt{3}}{2}$. \\\\
            $DN$ là đường cao trong tam giác đều $ACD$ cạnh $a$ nên $DN = \\frac{a\\sqrt{3}}{2}$. \\\\
            Áp dụng hệ quả định lý côsin trong tam giác $MND$, ta có: \\\\
            $\\cos \\widehat{NMD} = \\frac{MN^2 + MD^2 - ND^2}{2 \\cdot MN \\cdot MD} = \\frac{\\left(\\frac{a}{2}\\right)^2 + \\left(\\frac{a\\sqrt{3}}{2}\\right)^2 - \\left(\\frac{a\\sqrt{3}}{2}\\right)^2}{2 \\cdot \\frac{a}{2} \\cdot \\frac{a\\sqrt{3}}{2}} = \\frac{\\frac{a^2}{4}}{\\frac{a^2\\sqrt{3}}{2}} = \\frac{1}{2\\sqrt{3}} = \\frac{\\sqrt{3}}{6}$. \\\\
            Vì $\\frac{\\sqrt{3}}{6} > 0$ nên $\\cos(AB, DM) = \\frac{\\sqrt{3}}{6} \\approx %s$.'''%(str(kqz)))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.',','))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

