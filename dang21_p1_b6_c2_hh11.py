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


def bt_dang21_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1- Thiết lập các giá trị ngẫu nhiên
                a_val = randint(1, 6)

                # Tính toán các thông số hình học
                # Cạnh đáy = a_val * sqrt(2)
                val_canh_day = a_val * sqrt(2)
                # Diện tích đáy = (a_val * sqrt(2))^2 = 2 * a_val^2
                s_day = 2 * a_val**2
                # Đường chéo AC = cạnh * sqrt(2) = a_val * 2
                ac_val = 2 * a_val
                # SA = AC * cos(60) = ac_val * 1/2
                sa_val = Rational(ac_val, 2)
                # SH = SA * sin(60) = sa_val * sqrt(3)/2
                sh_val = Rational(sa_val, 2) * sqrt(3)
                # Thể tích V = 1/3 * S_day * SH
                v_val = Rational(1, 3) * s_day * sh_val

                # Đáp án đúng
                kq = latex(v_val) + " a^3"
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Các đáp án trắc nghiệm sai (B4: Điều chỉnh không trùng đáp án đúng)
                s = [
                    '$%s a^3$' % latex(Rational(a_val**3, 12) * sqrt(3)),
                    '$%s a^3$' % latex(Rational(a_val**3, 12) * sqrt(6)),
                    '$%s a^3$' % latex(Rational(a_val**3, 12) * sqrt(2)),
                    '$%s a^3$' % latex(Rational(a_val**3, 6) * sqrt(3)),
                    '$%s a^3$' % latex(Rational(a_val**3, 4) * sqrt(3)),
                    '$%s a^3$' % latex(v_val * 2),
                ]

                # Loại bỏ giá trị đúng nếu lỡ trùng trong danh sách sai
                if '$%s$' % kq in s:
                    s.remove('$%s$' % kq)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho khối chóp $S.ABCD$ có đáy là hình vuông cạnh $%s a$, tam giác $SAC$ vuông tại $S$ và nằm trong mặt phẳng vuông góc với đáy, cạnh bên $SA$ tạo với đáy góc $60^\\circ$. Thể tích $V$ của khối chóp $S.ABCD$ bằng'''
                                 % (latex(val_canh_day)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ
                tikz_code = """\\begin{center}
            \\begin{tikzpicture}[scale=0.7, line width=1pt, line join=round, line cap=round]
                \\coordinate (A) at (1,2);
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (4,0);
                \\coordinate (D) at (5,2);
                \\coordinate (H) at (1.75,2); 
                \\coordinate (S) at (1.75,5);
                \\draw [dashed] (A)--(D) (A)--(B) (A)--(C) (S)--(H) (A)--(S);
                \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);
                \\draw (S) node[above] {$S$};
                \\draw (A) node[left] {$A$};
                \\draw (B) node[below left] {$B$};
                \\draw (C) node[below right] {$C$};
                \\draw (D) node[right] {$D$};
                \\draw (H) node[below] {$H$};
            \\end{tikzpicture}
            \\end{center}"""

                # Nội dung lời giải
                loigiai = (tikz_code + '''Gọi $H$ là hình chiếu của $S$ lên $AC$. Vì $(SAC) \\perp (ABCD)$ nên $SH \\perp (ABCD)$.\\\\ 
                             Đáy $ABCD$ là hình vuông cạnh $%s a$ nên $S_{ABCD} = (%s a)^2 = %s a^2$.\\\\ 
                             Đường chéo $AC = %s a \\cdot \\sqrt{2} = %s a$.\\\\ 
                             Trong tam giác $SAC$ vuông tại $S$ có $\\widehat{SAC} = 60^\\circ$: \\\\ 
                             $SA = AC \\cdot \\cos 60^\\circ = %s a \\cdot \\frac{1}{2} = %s a$.\\\\ 
                             Đường cao $SH = SA \\cdot \\sin 60^\\circ = %s a \\cdot \\frac{\\sqrt{3}}{2} = %s a$.\\\\ 
                             Thể tích khối chóp là: $V = \\frac{1}{3} S_{ABCD} \\cdot SH = \\frac{1}{3} \\cdot %s a^2 \\cdot %s a = %s a^3$.'''
                           % (latex(val_canh_day), latex(val_canh_day), latex(s_day),
                              latex(val_canh_day), latex(ac_val),
                              latex(ac_val), latex(sa_val),
                              latex(sa_val), latex(sh_val),
                              latex(s_day), latex(sh_val), latex(v_val)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

