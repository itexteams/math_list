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


def bt_dang38_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số AB = k và SB = m
                k = 2 * randint(2, 4)  # k có thể là 4, 6, 8
                m = k + 2  # m có thể là 6, 8, 10

                # Bước 2: Tính toán các giá trị (không dùng a)
                # AC = BC = AB / sqrt(2)
                ac_val = simplify(k / sqrt(2))
                # S_abc = 1/2 * AC * BC = k^2/4
                s_abc = Rational(k**2, 4)
                # SA = sqrt(SB^2 - AB^2)
                sa_sq = m**2 - k**2
                sa_val = simplify(sqrt(sa_sq))
                # V = 1/3 * S_abc * SA
                v_val = simplify(Rational(1, 3) * s_abc * sa_val)

                # Tỷ số 1 / 3V và làm tròn đến hàng phần chục
                # Ở đây đề bài yêu cầu tỷ số a^3 / 3V, khi bỏ a thì là 1 / 3V
                ty_so_raw = 1 / (3 * v_val)
                ty_so = round(float(ty_so_raw), 2)

                # Đáp án đúng
                da = '$%s$' % (str(ty_so).replace('.', ','))

                # Bước 3: Tạo các phương án sai
                s = []
                while len(s) < 3:
                    # Tạo các giá trị sai quanh kết quả đúng
                    offset = random.choice([-0.2, 0.2, 0.3, -0.3, 0.5, -0.1, 0.1])
                    sai = round(ty_so + offset, 1)
                    sai_str = '$%s$' % (str(sai).replace('.', ','))
                    if sai_str != da and sai_str not in s and sai > 0:
                        s.append(sai_str)

                das1, das2, das3 = s[0], s[1], s[2]

                # Vẽ hình TikZ
                hinh_ve = r'''\begin{center} \begin{tikzpicture}[scale=0.8, line width=1pt, font=\footnotesize]
            \coordinate (A) at (0,0);
            \coordinate (B) at (4,-0.5);
            \coordinate (C) at (2.5,-2);
            \coordinate (S) at (0,3);
            \draw (S)--(C)--(B)--(S) (S)--(A) (A)--(C);
            \draw[dashed] (A)--(B) ;
            \draw (S) node[above]{$S$} (A) node[left]{$A$} (B) node[right]{$B$} (C) node[below]{$C$};
            \end{tikzpicture} \end{center}'''

                # Câu hỏi (Bỏ ký hiệu a)
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy là tam giác vuông cân tại $C$, cạnh bên $SA$ vuông góc với mặt đáy, biết $AB = %s$, $SB = %s$. Thể tích khối chóp $S.ABC$ là $V$. Tỷ số $\\frac{1}{3V}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 % (latex(k), latex(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Bỏ a, chuyển kết quả cuối sang số thập phân)
                loigiai = ('''Ta có: \\\\
                             $\\Delta ABC$ vuông cân tại $C$, $AB = %s$ suy ra \\\\
                             $AC = BC = %s$. \\\\
                             Do đó: $S_{ABC} = \\frac{1}{2} AC \\cdot BC = %s$. \\\\
                             $SA \\perp \\left(ABC\\right) \\Rightarrow SA \\perp AB \\Rightarrow \\Delta SAB$ vuông tại $A$. \\\\
                             $SA = \\sqrt{SB^2 - AB^2} = \\sqrt{%s^2 - %s^2} = %s$. \\\\
                             Khối chóp $S.ABC$ có $SA \\perp \\left(ABC\\right)$ \\\\
                             $\\Rightarrow V = \\frac{1}{3} S_{ABC} \\cdot SA = \\frac{1}{3} \\cdot %s \\cdot %s = %s$. \\\\
                             Vậy tỷ số: $\\frac{1}{3V} = \\frac{1}{3 \\cdot %s} \\approx %s$.'''
                           % (latex(k), latex(ac_val), latex(s_abc),
                              latex(m), latex(k), latex(sa_val),
                              latex(s_abc), latex(sa_val), latex(v_val),
                              latex(v_val), str(ty_so).replace('.', ',')))
                dapan='\\shortans[0]{$%s$}\n'%(str(ty_so).replace('.', ','))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+hinh_ve+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

