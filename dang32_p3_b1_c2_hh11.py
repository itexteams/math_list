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


def bt_dang32_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hóa thông số: AB = n*a (n chẵn để DM là số đẹp), SA = k*a
                # Trong đề gốc: n=2, k=1
                n = random.choice([2, 4, 6])
                k = random.choice([1, 2, 3])

                a = symbols('a')

                # Tính độ dài AM: AM^2 = AD^2 + DM^2 = (na)^2 + (na/2)^2 = 5n^2/4 * a^2
                am_sq_val = Rational(5 * n**2, 4)
                am_val = sqrt(am_sq_val)
                am_tex = latex(am_val) + 'a'

                # Tính độ dài SB: SB^2 = SA^2 + AB^2 = (ka)^2 + (na)^2 = (k^2 + n^2)a^2
                sb_sq_val = k**2 + n**2
                sb_val = sqrt(sb_sq_val)
                sb_tex = latex(sb_val) + 'a'

                # Tích vô hướng: AM.SB = DM.AB = (n/2 * a) * (n * a) = (n^2 / 2) * a^2
                dot_prod_val = Rational(n**2, 2)

                # cos(alpha) = dot_prod / (AM * SB)
                cos_val = simplify(dot_prod_val / (am_val * sb_val))
                da = '$' + latex(cos_val) + '$'

                # Tạo các phương án sai
                s = set()
                while len(s) < 3:
                    # Tạo các phân số ngẫu nhiên hoặc các biến thể của đáp án đúng
                    p_num = randint(1, 5)
                    p_den = randint(2, 7)
                    wrong_val = Rational(p_num, p_den)
                    if wrong_val != cos_val:
                        s.add('$' + latex(wrong_val) + '$')

                list_wrong = list(s)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp tứ giác $S.ABCD$ có đáy là hình vuông cạnh $%sa$; cạnh $SA = %sa$ và vuông góc với đáy. Gọi $M$ là trung điểm $CD$. Giá trị $\\cos\\alpha$ với $\\alpha$ là góc tạo bởi $SB$ và $AM$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 %(latex(n), latex(k) if k != 1 else ""))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                h1=cos_val
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                loigiai = ('''Ta có $AM = \\sqrt{AD^2 + DM^2} = \\sqrt{(%sa)^2 + (%sa)^2} = %s$. \\\\
                             $SB = \\sqrt{SA^2 + AB^2} = \\sqrt{(%sa)^2 + (%sa)^2} = %s$. \\\\
                             Xét tích vô hướng: \\\\
                             $\\vec{AM} \\cdot \\vec{SB} = (\\vec{AD} + \\vec{DM}) \\cdot (\\vec{SA} + \\vec{AB})$ \\\\
                             $= \\vec{AD} \\cdot \\vec{SA} + \\vec{AD} \\cdot \\vec{AB} + \\vec{DM} \\cdot \\vec{SA} + \\vec{DM} \\cdot \\vec{AB}$ \\\\
                             Vì $SA \\perp (ABCD)$ nên $\\vec{AD} \\cdot \\vec{SA} = 0$ và $\\vec{DM} \\cdot \\vec{SA} = 0$. \\\\
                             Vì $ABCD$ là hình vuông nên $\\vec{AD} \\cdot \\vec{AB} = 0$. \\\\
                             Do đó $\\vec{AM} \\cdot \\vec{SB} = \\vec{DM} \\cdot \\vec{AB} = DM \\cdot AB = %sa \\cdot %sa = %sa^2$. \\\\
                             Mặt khác $\\vec{AM} \\cdot \\vec{SB} = AM \\cdot SB \\cdot \\cos(\\vec{AM}, \\vec{SB})$ \\\\
                             $= %s \\cdot %s \\cdot \\cos(\\vec{AM}, \\vec{SB}) = %sa^2 \\cdot \\cos(\\vec{AM}, \\vec{SB})$. \\\\
                             $\\Rightarrow %sa^2 = %sa^2 \\cdot \\cos(\\vec{AM}, \\vec{SB}) \\Leftrightarrow \\cos(\\vec{AM}, \\vec{SB}) = %s$. \\\\
                             Suy ra $\\cos\\alpha = %s \\approx %s$.'''
                           %(latex(n), latex(Rational(n, 2)), am_tex,
                             latex(k), latex(n), sb_tex,
                             latex(Rational(n, 2)), latex(n), latex(dot_prod_val),
                             am_tex, sb_tex, latex(simplify(am_val * sb_val)),
                             latex(dot_prod_val), latex(simplify(am_val * sb_val)),
                             latex(cos_val), latex(cos_val),str(kqz)
                            ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.',','))

            # Hình vẽ TikZ
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (4,-1);
                \\coordinate (D) at (1.5,1.2);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (S) at (0,4);
                \\coordinate (M) at ($(C)!0.5!(D)$);
                \\draw [dashed] (S)--(B) (A)--(D)--(C) (A)--(M) (S)--(D);
                \\draw (S)--(C) (S)--(B)--(C) (S)--(A)--(B);
                \\foreach \\p/\\pos in {A/left, B/below right, C/right, D/above left, S/above, M/below}
                    \\fill (\\p) node [\\pos] {$\\p$};
                \\draw (0,0.3)--(0.3,0.3)--(0.3,0);
            \\end{tikzpicture}
            \\end{center}''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'  + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + tikz_code + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

