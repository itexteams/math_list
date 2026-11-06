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


def bt_dang5_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật và $SA$ vuông góc với mặt phẳng đáy. Gọi $H, K$ theo thứ tự là hình chiếu của $A$ trên các cạnh $SB, SD$.''')

            # TikZ code cho hình vẽ (độ dày 1pt)
            tikz_hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,scale=1, line width=1pt]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (-1.5,-1.5);
                \\coordinate (D) at (3.5,0);
                \\coordinate (C) at (2,-1.5);
                \\coordinate (S) at (0,4);
                \\coordinate (H) at (-0.6,1.8); % Ước lượng vị trí H trên SB
                \\coordinate (K) at (1.5,2.2); % Ước lượng vị trí K trên SD
                \\draw [dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(H) (A)--(K) (H)--(K);
                \\draw (S)--(B) (B)--(C) (C)--(D) (D)--(S) (S)--(C);
                \\tkzMarkRightAngle(S,A,D)
                \\tkzMarkRightAngle(A,H,S)
                \\tkzMarkRightAngle(A,K,S)
                \\tkzLabelPoints[above](S)
                \\tkzLabelPoints[left](H,B)
                \\tkzLabelPoints[right](K,D,C)
                \\tkzLabelPoints[left](A)
            \\end{tikzpicture}
            \\end{center}''')

            ########################################################################
            # Nhận biết - Mệnh đề (a)
            ########################################################################
            nb_da_1_d = r'\True Tam giác $SBC$ vuông'
            nb_da_1_s = r'Tam giác $SBC$ cân tại $S$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có: $\\begin{cases} BC \\perp AB \\\\ BC \\perp SA \\text{ (do } SA \\perp \\left( ABCD \\right) \\text{)} \\end{cases} \\Rightarrow BC \\perp \\left( SAB \\right)$.\\\\
            Vì $\\begin{cases} BC \\perp \\left( SAB \\right) \\\\ SB \\subset \\left( SAB \\right) \\end{cases} \\Rightarrow BC \\perp SB$ hay $\\triangle SBC$ vuông tại $B$.''')

            ########################################################################
            # Thông hiểu - Mệnh đề (b)
            ########################################################################
            th_da_1_d = r'\True Tam giác $SCD$ vuông'
            th_da_1_s = r'Tam giác $SCD$ đều'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có: $\\begin{cases} CD \\perp AD \\\\ CD \\perp SA \\text{ (do } SA \\perp \\left( ABCD \\right) \\text{)} \\end{cases} \\Rightarrow CD \\perp \\left( SAD \\right)$.\\\\
            Vì $\\begin{cases} CD \\perp \\left( SAD \\right) \\\\ SD \\subset \\left( SAD \\right) \\end{cases} \\Rightarrow CD \\perp SD$ hay $\\triangle SCD$ vuông tại $D$.''')

            ########################################################################
            # Vận dụng - Mệnh đề (c)
            ########################################################################
            vd_da_1_d = r'\True $SC \perp \left( AHK \right)$'
            vd_da_1_s = r'$SC \parallel \left( AHK \right)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có: $\\begin{cases} AH \\perp SB \\\\ AH \\perp BC \\text{ (do } BC \\perp \\left( SAB \\right) \\text{)} \\end{cases} \\Rightarrow AH \\perp \\left( SBC \\right) \\Rightarrow AH \\perp SC$ (1).\\\\
            Tương tự: $\\begin{cases} AK \\perp SD \\\\ AK \\perp CD \\text{ (do } CD \\perp \\left( SAD \\right) \\text{)} \\end{cases} \\Rightarrow AK \\perp \\left( SCD \\right) \\Rightarrow AK \\perp SC$ (2).\\\\
            Từ (1) và (2) suy ra $SC \\perp \\left( AHK \\right)$.''')

            ########################################################################
            # Vận dụng cao - Mệnh đề (d)
            ########################################################################
            vdc_da_1_d = r'\True $HK \perp SC$'
            vdc_da_1_s = r'$HK \parallel SC$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Mà $HK \\subset \\left( AHK \\right)$ nên $HK \\perp SC$.''')

            # Lặp để đảm bảo số câu đúng từ 1 đến 3
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Gán lời giải tương ứng (vì bài này logic lời giải cố định cho mệnh đề đúng)
            # Để đơn giản và chính xác, ta chỉ xuất lời giải nếu chọn câu đúng hoặc giải thích tại sao sai.
            # Ở đây tôi giữ nguyên lời giải chi tiết như trong ảnh.

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(d1) + '}\n'
                '{' + str(d2) + '}\n'
                '{' + str(d3) + '}\n'
                '{' + str(d4) + '}\n'
                '\\loigiai{ \n'
                +str(tikz_hinh_ve)+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

