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


def bt_dang50_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến ký hiệu
            a = symbols('a')

            # B3- Suy nghĩ tìm cách random bài toán
            # Random hệ số k của khoảng cách (trong ảnh k=1, khoảng cách = a)
            k = random.randint(1, 5) 
            dist = k * a

            # Các thông số cố định từ đề bài
            # Góc giữa (SBC) và (ABC) là 30 độ
            # AI = dist / sin(30) = 2 * dist
            ai_val = 2 * dist
            # SA = AI * tan(30) = AI * sqrt(3)/3
            sa_val = ai_val * sqrt(3) / 3
            # Cạnh đáy x: AI = x * sqrt(3)/2 => x = 2*AI / sqrt(3)
            x_val = 2 * ai_val / sqrt(3)
            # Diện tích đáy ABC = x^2 * sqrt(3) / 4
            s_abc = (x_val**2 * sqrt(3)) / 4
            # Thể tích V = 1/3 * S_abc * SA
            v_val = Rational(1, 3) * s_abc * sa_val

            # Rút gọn các biểu thức để hiển thị lời giải
            ai_latex = latex(ai_val)
            sa_latex = latex(sa_val)
            x_latex = latex(x_val)
            s_abc_latex = latex(s_abc)
            v_latex = latex(v_val)

            # B4- Điều chỉnh các phương án sai
            # Đáp án đúng (A trong ảnh gốc)
            da_dung = '$%s$' % v_latex

            # Tạo các đáp án nhiễu dựa trên cấu trúc các phương án B, C, D của ảnh
            ds_sai = [
                '$%s$' % latex(v_val * 3), # Tương ứng phương án B (8a^3/3)
                '$%s$' % latex(Rational(1, 8) * v_val * sqrt(3)), # Tương ứng phương án C (sqrt(3)a^3/12)
                '$%s$' % latex(v_val / 2), # Tương ứng phương án D (4a^3/9)
                '$%s$' % latex(v_val * 2)
            ]

            # Trộn đáp án
            list_da = ['\\True ' + da_dung] + random.sample(ds_sai, 3)
            random.shuffle(list_da)

            # B2- Viết lại nội dung câu hỏi và lời giải theo mẫu
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều, $SA \\perp \\left( ABC \\right)$. Mặt phẳng $\\left( SBC \\right)$ cách $A$ một khoảng bằng $%s$ và hợp với mặt phẳng $\\left( ABC \\right)$ góc $30^\\circ$. Thể tích của khối chóp $S.ABC$ bằng'''
                             % (latex(dist)))

            # Vẽ hình bằng TikZ (độ dày nét 1pt, giống 100% ảnh)
            tikz_code = ('''\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, scale=0.8, line width=1pt]
            \\coordinate (A) at (0,0);
            \\coordinate (S) at (0,4);
            \\coordinate (B) at (1.5,-1.5);
            \\coordinate (C) at (5,0.5);
            \\coordinate (I) at ($(B)!0.5!(C)$);
            \\coordinate (H) at ($(S)!0.65!(I)$);
            \\draw [dashed] (A)--(C) (A)--(I) (A)--(H);
            \\draw (S)--(A)--(B)--(S)--(C)--(B) (S)--(I);
            \\tkzMarkRightAngle(S,A,I)
            \\tkzMarkRightAngle(A,H,I)
            \\tkzMarkRightAngle(A,I,B)
            \\draw (A) node[left]{$A$} (S) node[above]{$S$} (B) node[below]{$B$} (C) node[right]{$C$} (I) node[below right]{$I$} (H) node[above right]{$H$};
            \\tkzMarkAngle[size=0.7](S,I,A)
            \\node at ($(I)+(-0.9,0.4)$){$30^\\circ$};
            \\end{tikzpicture} \\end{center}''')

            loigiai = ('''%s
            Gọi $I$ là trung điểm của $BC$ suy ra góc giữa mp$\\left( SBC \\right)$ và mp$\\left( ABC \\right)$ là $\\widehat{SIA}=30^\\circ$. \\\\
            $H$ là hình chiếu vuông góc của $A$ trên $SI$ suy ra $d\\left( A, \\left( SBC \\right) \\right) = AH = %s$. \\\\
            Xét tam giác $AHI$ vuông tại $H$ suy ra $AI = \\frac{AH}{\\sin 30^\\circ} = %s$. \\\\
            Giả sử tam giác đều $ABC$ có cạnh bằng $x$, mà $AI$ là đường cao suy ra $%s = x \\cdot \\frac{\\sqrt{3}}{2} \\Rightarrow x = %s$. \\\\
            Diện tích tam giác đều $ABC$ là $S_{ABC} = \\frac{\\left( %s \\right)^2 \\sqrt{3}}{4} = %s$. \\\\
            Xét tam giác $SAI$ vuông tại $A$ suy ra $SA = AI \\cdot \\tan 30^\\circ = %s$. \\\\
            Vậy $V_{S.ABC} = \\frac{1}{3} \\cdot S_{ABC} \\cdot SA = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.'''
                       % (tikz_code, latex(dist), ai_latex, ai_latex, x_latex, x_latex, s_abc_latex, sa_latex, s_abc_latex, sa_latex, v_latex))

            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\choice \n'
                       '{' + str(list_da[0]) + '}\n'
                       '{' + str(list_da[1]) + '}\n'
                       '{' + str(list_da[2]) + '}\n'
                       '{' + str(list_da[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

