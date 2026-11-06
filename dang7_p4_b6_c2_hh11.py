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


def bt_dang7_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            val_a = randint(2, 9)  # Random a là một số cụ thể từ 2 đến 9
            list_k = [2, 3, 5, 6, 10]
            k = random.choice(list_k)

            # Tính toán các giá trị bằng sympy
            sa_val = val_a * sqrt(k)
            s_day = val_a**2
            # Thể tích V = (1/3) * a^2 * a*sqrt(k) = (a^3 * sqrt(k)) / 3
            v_tu_so = (val_a**3) * sqrt(k)
            v_mau_so = 3

            # Hàm hỗ trợ định dạng phân số LaTeX cho thể tích
            def format_volume(tu, mau):
                if tu % mau == 0:
                    return latex(tu // mau)
                return '\\frac{' + latex(tu) + '}{' + str(mau) + '}'

            # Đáp án đúng
            da_dung_str = '$V = ' + format_volume(v_tu_so, v_mau_so)+'$'

            # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            s1 = '$V = ' + format_volume(v_tu_so, 6)+'$'
            s2 = '$V = ' + format_volume(v_tu_so, 2)+'$'
            s3 = '$V = ' + latex(v_tu_so)+'$'

            # Đảm bảo các đáp án sai không trùng đáp án đúng (trong trường hợp rút gọn)
            answers_set = {da_dung_str, s1, s2, s3}
            while len(answers_set) < 4:
                extra = 'V = ' + format_volume(v_tu_so, randint(4, 9))
                answers_set.add(extra)

            # Câu hỏi
            noidungcauhoi = ('''Cho hình chóp tứ giác $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $%s$, cạnh bên $SA$ vuông góc với mặt phẳng đáy và $SA = %s$. Tính thể tích $V$ của khối chóp $S.ABCD$.'''
                             % (latex(val_a), latex(sa_val)))

            # Các đáp án
            da_d = ('\\True ' + da_dung_str)
            list_sai = list(answers_set)
            list_sai.remove(da_dung_str)

            da_s1 = list_sai[0]
            da_s2 = list_sai[1]
            da_s3 = list_sai[2]

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết (B2)
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=0.8]
                \\coordinate (A) at (0,3);
                \\coordinate (B) at (4,3);
                \\coordinate (C) at (5,1);
                \\coordinate (D) at (1,1);
                \\coordinate (S) at (0,6.5);
                \\draw [dashed]  (A)--(B) ;
                \\draw (S)--(A) (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (A)--(D);
                \\node at (S) [above] {$S$};
                \\node at (A) [left] {$A$};
                \\node at (B) [right] {$B$};
                \\node at (C) [right] {$C$};
                \\node at (D) [left] {$D$};
            \\end{tikzpicture}
            \\end{center}''')

            loigiai = ('''Ta có $SA \\perp \\left( ABCD \\right) \\Rightarrow SA$ là đường cao của hình chóp.\\\\
                         Diện tích đáy hình vuông $ABCD$ là: $S_{ABCD} = %s^2 = %s$.\\\\
                         Thể tích khối chóp $S.ABCD$ là: \\\\
                         $V = \\frac{1}{3} \\cdot SA \\cdot S_{ABCD} = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.'''
                       % (latex(val_a), latex(s_day), latex(sa_val), latex(s_day), format_volume(v_tu_so, v_mau_so)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{\n' + hinh_ve + '\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

