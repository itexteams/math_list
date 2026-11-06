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


def bt_dang40_p3_b6_c2_hh11(self):
            # Khai báo biến
            # B1 & B3: Thiết lập thông số và logic random
            n = random.randint(2, 6)
            m = random.randint(2, 6)
            if n == m: m += 1 

            list_goc = [30, 45, 60]
            goc_val = random.choice(list_goc)
            goc_rad = goc_val * pi / 180

            # B2: Tính toán lời giải chi tiết (Dạng số thập phân)
            S_day_val = float(n * m)

            # Tính AE = (AB*AD)/sqrt(AB^2 + AD^2)
            mau_AE_sq = n**2 + m**2
            AE_val = float((n * m) / sqrt(mau_AE_sq))

            val_tan = float(tan(goc_rad))
            SA_val = float(AE_val * val_tan)

            V_correct = float((1/3) * SA_val * S_day_val)

            # Hàm hỗ trợ làm tròn và đổi dấu chấm thành phẩy cho chuẩn Tiếng Việt
            def fmt(val):
                return ("{:.1f}".format(round(val, 1))).replace('.', ',')

            # B4: Tạo các phương án sai
            def generate_distractors(correct_val):
                options = set()
                da_str = '$%s$' % fmt(correct_val)
                options.add(da_str)

                # Các sai lầm logic
                wrong1 = SA_val * S_day_val # Quên 1/3
                wrong2 = (1/6) * SA_val * S_day_val # Nhầm công thức
                wrong3 = (1/3) * (AE_val / val_tan) * S_day_val # Nhầm tan thành cot

                candidates = [wrong1, wrong2, wrong3]
                for cand in candidates:
                    cand_str = '$%s$' % fmt(cand)
                    if cand_str not in options:
                        options.add(cand_str)

                while len(options) < 4:
                    extra = correct_val * random.uniform(0.5, 2.0)
                    options.add('$%s$' % fmt(extra))

                res = list(options)
                random.shuffle(res)
                return res, da_str

            options_list, da_dung = generate_distractors(V_correct)

            # Chuẩn bị nội dung TikZ
            tikz_code = '''\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, scale=0.7, line width=1pt]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (-1.5,-1.5);
                \\coordinate (D) at (4,0);
                \\coordinate (C) at (2.5,-1.5);
                \\coordinate (S) at (0,4);
                \\coordinate (E) at (0.6,-0.4); 
                \\draw [dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (A)--(E) (S)--(E);
                \\draw (S)--(B)--(C)--(D)--cycle (S)--(C) ;
                \\draw (A) node[left] {$A$} (B) node[left] {$B$} (C) node[right] {$C$} (D) node[right] {$D$} (S) node[above] {$S$} (E) node[left] {$E$};
            \\end{tikzpicture} \\end{center}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật $AB = %s$, $AD = %s$, cạnh bên $SA$ vuông góc với đáy. Thể tích $V$ của khối chóp $S.ABCD$ biết góc giữa hai mặt phẳng $\\left(SBD\\right)$ và $\\left(ABCD\\right)$ bằng $%s^\\circ$ bằng bao nhiêu? (Làm tròn kết quả đến hàng phần chục).'''
                             %(n, m, goc_val))

            # Nội dung lời giải chi tiết
            loigiai = ('''Kẻ $AE \\perp BD$. Vì $SA \\perp \\left(ABCD\\right)$ nên theo định lý ba đường vuông góc, ta có $SE \\perp BD$. \\\\
                             Khi đó $\\left(\\left(SBD\\right),\\left(ABCD\\right)\\right) = \\widehat{SEA} = %s^\\circ$. \\\\
                             Xét $\\triangle ABD$ vuông tại $A$: \\\\
                             $AE = \\frac{AB \\cdot AD}{\\sqrt{AB^2 + AD^2}} = \\frac{%s \\cdot %s}{\\sqrt{%s^2 + %s^2}} \\approx %s$. \\\\
                             Xét $\\triangle SAE$ vuông tại $A$: \\\\
                             $SA = AE \\cdot \\tan %s^\\circ \\approx %s \\cdot %s \\approx %s$. \\\\
                             Khi đó thể tích $S.ABCD$ là: \\\\
                             $V = \\frac{1}{3} SA \\cdot S_{ABCD} \\approx \\frac{1}{3} \\cdot %s \\cdot %s \\approx %s$.'''
                       %(goc_val, n, m, n, m, fmt(AE_val), 
                         goc_val, fmt(AE_val), fmt(val_tan), fmt(SA_val),
                         fmt(SA_val), fmt(S_day_val), fmt(V_correct)
                        ))
            dapan='\\shortans[0]{$%s$}\n'%(fmt(V_correct))
            # Xử lý các đáp án để đưa vào list_1
            list_1 = []
            for opt in options_list:
                if opt == da_dung:
                    list_1.append('\\True ' + str(opt))
                else:
                    list_1.append(str(opt))

            # Xuất câu trắc nghiệm đúng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+ str(tikz_code)+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

