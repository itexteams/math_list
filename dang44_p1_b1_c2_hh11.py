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


def bt_dang44_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến danh mục
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Thiết lập các bộ dữ liệu ngẫu nhiên (SA_latex, tan_alpha, ket_qua)
                # Các bộ này đảm bảo góc giữa SD và BC là các góc đặc biệt 30, 45, 60
                data_random = [
                    ('a\\sqrt{3}', '\\sqrt{3}', '60^\\circ'),
                    ('a', '1', '45^\\circ'),
                    ('\\frac{a\\sqrt{3}}{3}', '\\frac{\\sqrt{3}}{3}', '30^\\circ')
                ]

                selected = random.choice(data_random)
                sa_val = selected[0]
                tan_val = selected[1]
                kq_dung = selected[2]

                # Bước 2: Tạo danh sách các phương án sai (không trùng đáp án đúng)
                cac_phuong_an = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ']
                if kq_dung in cac_phuong_an:
                    cac_phuong_an.remove(kq_dung)

                random.shuffle(cac_phuong_an)
                da_s1 = '$' + cac_phuong_an[0] + '$'
                da_s2 = '$' + cac_phuong_an[1] + '$'
                da_s3 = '$' + cac_phuong_an[2] + '$'
                da_d = '\\True $' + kq_dung + '$'

                # Trộn các phương án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 3: Vẽ hình bằng TikZ
                tikz_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (3,0);
            \\coordinate (D) at (-1.2,-1.1);
            \\coordinate (C) at ($(B)+(D)-(A)$);
            \\coordinate (S) at (0,3);
            \\draw [dashed] (S)--(A)--(B) (A)--(D);
            \\draw (S)--(D)--(C)--(B)--(S)--(C);
            \\draw [dashed] (B)--(A);
            \\node [above] at (S) {$S$};
            \\node [left] at (A) {$A$};
            \\node [right] at (B) {$B$};
            \\node [below] at (C) {$C$};
            \\node [below left] at (D) {$D$};
            \\tkzMarkRightAngle(S,A,D)
            \\end{tikzpicture}
            \\end{center}''')

                # Bước 4: Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thoi cạnh $a$, $SA = %s$ và $SA \\perp BC$. Góc giữa hai đường thẳng $SD$ và $BC$ bằng'''
                                 % (sa_val))

                # Bước 5: Nội dung lời giải chi tiết
                loigiai = (tikz_hinh + '''Vì $ABCD$ là hình thoi nên $AD // BC$.\\\\
            Ta có: $AD // BC, SA \\perp BC \\Rightarrow SA \\perp AD$ hay $\\triangle SAD$ vuông tại $A$.\\\\
            Do $AD // BC$ nên góc giữa $SD$ và $BC$ là:
            $(SD, BC) = (SD, AD) = \\widehat{SDA}$.\\\\
            Trong tam giác $SAD$ vuông tại $A$, ta có:
            $\\tan \\widehat{SDA} = \\frac{SA}{AD} = \\frac{%s}{a} = %s \\Rightarrow \\widehat{SDA} = %s$.\\\\
            Vậy góc giữa hai đường thẳng $SD$ và $BC$ bằng $%s$.''' 
                            % (sa_val, tan_val, kq_dung, kq_dung))

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

