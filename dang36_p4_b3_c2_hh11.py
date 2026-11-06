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


def bt_dang36_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang=='1':
                # Random hóa hệ số k để thay đổi độ dài các cạnh
                k = random.randint(1, 4)
                a_sym = symbols('a')

                # Cố định cấu trúc tam giác ABC vuông tại B có AC = 2*BC (tạo góc 60-30 ở đáy)
                bc_len = k * a_sym
                ac_len = 2 * k * a_sym
                ab_len = k * sqrt(3) * a_sym

                # Chọn ngẫu nhiên góc kết quả mong muốn (30, 45, 60) để tính ngược ra SB
                goc_list = [30, 45, 60]
                kq_goc = random.choice(goc_list)

                if kq_goc == 30:
                    sb_len = 2 * ab_len # sin(30) = AB/SB = 1/2
                elif kq_goc == 45:
                    sb_len = sqrt(2) * ab_len # sin(45) = AB/SB = 1/sqrt(2)
                else: # 60
                    sb_len = (2 * ab_len) / sqrt(3) # sin(60) = AB/SB = sqrt(3)/2 -> SB = 2*AB/sqrt(3)

                # Đáp án đúng
                da = str(kq_goc) + '^\\circ'

                # Tạo các đáp án sai
                s = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ', '15^\\circ', '75^\\circ']
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Cho khối chóp $S.ABC$ có $SA \\perp \\left( ABC \\right)$, tam giác $ABC$ vuông tại $B$, $AC = %s$, $BC = %s$, $SB = %s$. Tính góc giữa $SA$ và mặt phẳng $\\left( SBC \\right)$.'
                                 %(latex(ac_len), latex(bc_len), latex(sb_len)))

                # Các đáp án
                da_d = ('\\True $' + str(da) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ
                hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.2,-1.2);
                \\coordinate (C) at (4,0);
                \\coordinate (S) at (0,3.5);
                \\coordinate (H) at (0.5,1.4); % Điểm H tương đối trên SB
                \\draw[line width=1pt, dashed] (A)--(C);
                \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B);
                \\draw[line width=1pt] (A)--(H);
                \\draw[line width=0.6pt] (0,0.2)--(0.2,0.2)--(0.2,0); % Vuông tại A (SA vuông đáy)
                \\draw[line width=0.6pt] (0.9,-1.05)--(1.05,-0.9)--(1.2,-1.05); % Vuông tại B
                \\node at (A) [left] {$A$};
                \\node at (B) [below] {$B$};
                \\node at (C) [right] {$C$};
                \\node at (S) [above] {$S$};
                \\node at (H) [right] {$H$};
            \\end{tikzpicture}
            \\end{center}''')

                # Nội dung lời giải
                loigiai = ('''Trong mặt phẳng $\\left( SAB \\right)$ kẻ $AH \\perp SB$ tại $H$ $\\left( H \\in SB \\right)$. \\\\
                             Vì $\\begin{cases} SA \\perp BC \\\\ AB \\perp BC \\end{cases} \\Rightarrow BC \\perp \\left( SAB \\right) \\Rightarrow BC \\perp AH$. \\\\
                             Mà $SB \\perp AH$ do cách dựng nên $AH \\perp \\left( SBC \\right)$, hay $H$ là hình chiếu của $A$ lên mặt phẳng $\\left( SBC \\right)$. \\\\
                             Suy ra góc giữa đường thẳng $SA$ và mặt phẳng $\\left( SBC \\right)$ là góc $\\widehat{ASH}$ hay góc $\\widehat{ASB}$. \\\\
                             Tam giác $ABC$ vuông ở $B$ nên $AB = \\sqrt{AC^2 - BC^2} = \\sqrt{\\left( %s \\right)^2 - \\left( %s \\right)^2} = %s$. \\\\
                             Tam giác $SAB$ vuông ở $A$ nên $\\sin \\widehat{ASB} = \\frac{AB}{SB} = \\frac{%s}{%s} = %s$. \\\\
                             Vậy $\\widehat{ASB} = %s$.'''
                             %(latex(ac_len), latex(bc_len), latex(ab_len), 
                               latex(ab_len), latex(sb_len), latex(ab_len/sb_len), da))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'  
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

