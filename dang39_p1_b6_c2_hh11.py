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


def bt_dang39_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random số liệu (AD = CD = a*sqrt(k), AA' = q*a)
                # Để kết quả đẹp, chọn k sao cho 3*k*q chia hết cho 2 hoặc để dạng phân số
                k = random.choice([2, 4, 6, 8]) 
                q = random.choice([2, 3, 4, 5])

                # Tính toán diện tích đáy và thể tích
                # S = (AB + CD)*AD / 2 = (2*sqrt(k) + sqrt(k))*sqrt(k) / 2 = 3k/2
                dt_day_num = Rational(3 * k, 2)
                the_tich_num = dt_day_num * q

                # Định dạng hiển thị số (Thay . thành ,)
                val_k_str = latex(sqrt(k)).replace('.', ',')
                val_q_str = str(q).replace('.', ',')
                val_dt_day = latex(dt_day_num).replace('.', ',')
                val_the_tich = latex(the_tich_num).replace('.', ',')

                # Đáp án đúng
                da_dung = '$%s a^3$' % val_the_tich

                # Bước 2: Tạo các đáp án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = random.choice([the_tich_num * 2, the_tich_num + 2, the_tich_num / 2, the_tich_num + 4, Rational(1, 2) * the_tich_num])
                    sai_str = '$%s a^3$' % latex(sai).replace('.', ',')
                    if sai_str != da_dung:
                        s.add(sai_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                val_ad_cd = 'a\\sqrt{%s}' % k if k != 4 else '2a'
                noidungcauhoi = ('''Cho hình lăng trụ đứng $ABCD.A'B'C'D'$, đáy là hình thang vuông tại $A$ và $D$, có $AB = 2CD, AD = CD = %s, AA' = %sa$. Thể tích khối lăng trụ đã cho bằng'''
                                 %(val_ad_cd, val_q_str))

                # Bước 3: Vẽ hình TikZ (Độ dày 1pt, nét đứt chính xác)
                # Ghi chú: %% dùng để Python không nhầm lẫn với biến format
                hinh_ve = '''\\begin{center}
            \\begin{tikzpicture}[line join=round, line cap=round, font=\\footnotesize, scale=0.8, line width=1pt]
                \\coordinate (D) at (0,0);
                \\coordinate (C) at (2.5,0);
                \\coordinate (A) at (1.2,1.3);
                \\coordinate (B) at (6.2,1.3);
                \\coordinate (D1) at (0,4);
                \\coordinate (C1) at (2.5,4);
                \\coordinate (A1) at (1.2,5.3);
                \\coordinate (B1) at (6.2,5.3);
                \\draw (D1)--(C1)--(B1)--(A1)--cycle;
                \\draw (D1)--(D)--(C)--(C1);
                \\draw (B1)--(B)--(C);
                \\draw[dashed] (A1)--(A)--(D);
                \\draw[dashed] (A)--(B);
                \\node[left] at (D) {$D$}; \\node[right] at (C) {$C$};
                \\node[above left] at (A) {$A$}; \\node[right] at (B) {$B$};
                \\node[left] at (D1) {$D'$}; \\node[right] at (C1) {$C'$};
                \\node[above] at (A1) {$A'$}; \\node[right] at (B1) {$B'$};
                \\node[left] at (0.6, 0.65) {$%s$};
                \\node[below] at (1.25, 0) {$%s$};
                \\node[left] at (1.2, 3.3) {$%sa$};
                \\draw (0.3,0)--(0.3,0.3)--(0,0.3);
                \\draw[dashed] (1.2,1.6)--(1.5,1.6)--(1.5,1.3);
            \\end{tikzpicture}
            \\end{center}''' % (val_ad_cd, val_ad_cd, val_q_str)

                # Bước 4: Nội dung lời giải chi tiết
                loigiai = ('''Diện tích hình thang $ABCD$ là:
                $$S_{ABCD} = \\frac{\\left(AB + CD\\right) \\cdot AD}{2} = \\frac{\\left(2CD + CD\\right) \\cdot AD}{2} = \\frac{3CD \\cdot AD}{2} = \\frac{3 \\cdot %s \\cdot %s}{2} = %s a^2.$$
                Thể tích khối lăng trụ đã cho là:
                $$V = S_{ABCD} \\cdot AA' = %s a^2 \\cdot %s a = %s a^3.$$'''
                % (val_ad_cd, val_ad_cd, val_dt_day, val_dt_day, val_q_str, val_the_tich))

                # Sắp xếp đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Không dùng tiền tố r ở content theo yêu cầu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

