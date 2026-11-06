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


def bt_dang15_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random giá trị cụ thể cho a (ví dụ từ 2 đến 6 để số không quá lớn)
                val_a = randint(2, 6)

                # Các thông số bài toán dựa trên giá trị val_a
                canh_hv = val_a
                sa_val = 2 * val_a
                ah_val = Rational(val_a, 2)

                # Tính SH = sqrt(SA^2 - AH^2)
                sh_sq = sa_val**2 - ah_val**2
                sh = sqrt(sh_sq)

                # Diện tích đáy
                s_abcd = canh_hv**2

                # Thể tích V = 1/3 * SH * S_ABCD
                v_val = Rational(1, 3) * sh * s_abcd

                # Tính toán số thập phân làm tròn đến hàng phần chục
                v_float = round(float(v_val.evalf()), 1)
                v_float_latex = str(v_float).replace('.', ',')

                # Chuyển sang định dạng latex và thay dấu chấm thành dấu phẩy
                v_latex = latex(v_val).replace('.', ',')
                sh_latex = latex(sh).replace('.', ',')
                s_abcd_latex = latex(s_abcd).replace('.', ',')
                sa_latex = latex(sa_val).replace('.', ',')
                ah_latex = latex(ah_val).replace('.', ',')
                canh_hv_latex = latex(canh_hv).replace('.', ',')

                # Đáp án đúng
                da = '$V = %s$' % v_latex

                # Tạo các đáp án sai (nhiễu số học)
                v_sai1 = Rational(1, 2) * sh * s_abcd  # Sai công thức (nhân 1/2)
                v_sai2 = Rational(1, 3) * (sa_val) * s_abcd  # Quên Pitago, lấy SA làm đường cao
                v_sai3 = Rational(1, 3) * sqrt(sa_val**2 + ah_val**2) * s_abcd # Sai dấu trong Pitago

                s = [
                    '$V = %s$' % latex(v_sai1).replace('.', ','),
                    '$V = %s$' % latex(v_sai2).replace('.', ','),
                    '$V = %s$' % latex(v_sai3).replace('.', ','),
                    '$V = %s$' % latex(v_val * 2).replace('.', ','),
                    '$V = %s$' % latex(v_val / 2).replace('.', ','),
                    '$V = %s$' % latex(v_val + 10).replace('.', ',')
                ]

                # Loại bỏ trường hợp trùng với đáp án đúng (nếu có)
                s = [item for item in s if item != da]
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho khối chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $%s$, tam giác $SAB$ cân tại $S$ và nằm trong mặt phẳng vuông góc với đáy, $SA = %s$. Thể tích khối chóp $S.ABCD$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 %(canh_hv_latex, sa_latex))

                # TikZ code
                tikz_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt, x={(1cm,0cm)}, y={(0.5cm,0.5cm)}, z={(0cm,1cm)}]
                \\coordinate (A) at (0,4,0);
                \\coordinate (B) at (0,0,0);
                \\coordinate (C) at (4,0,0);
                \\coordinate (D) at (4,4,0);
                \\coordinate (H) at (0,2,0);
                \\coordinate (S) at (0,2,5);
                \\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (S)--(H);
                \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);
                \\node[left] at (A) {$A$};
                \\node[below left] at (B) {$B$};
                \\node[below right] at (C) {$C$};
                \\node[right] at (D) {$D$};
                \\node[above] at (S) {$S$};
                \\node[left] at (H) {$H$};
                \\draw (H) ++(0,0.3,0) -- ++(0.3,0,0) -- ++(0,-0.3,0);
                \\draw (B) ++(0,0.3,0) -- ++(0.3,0,0) -- ++(0,-0.3,0);
                \\draw (D) ++(0,-0.3,0) -- ++(-0.3,0,0) -- ++(0,0.3,0);
            \\end{tikzpicture} \\end{center}''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hiển thị các lựa chọn (Nếu dùng định dạng trắc nghiệm 4 lựa chọn)
                lua_chon = '\n\\choice{%s}{%s}{%s}{%s}' % (list_1[0], list_1[1], list_1[2], list_1[3])

                # Lời giải chi tiết
                loigiai = ('''Gọi $H$ là trung điểm $AB$.\\\\
            Theo đề, tam giác $SAB$ cân tại $S$ nên suy ra $SH \\perp AB$.\\\\
            Mặt khác, tam giác $SAB$ nằm trong mặt phẳng vuông góc với đáy nên suy ra $SH \\perp \\left(ABCD\\right)$.\\\\
            Xét tam giác $SHA$ vuông tại $H$.\\\\
            Ta có $AH = \\frac{AB}{2} = \\frac{%s}{2} = %s$.\\\\
            $SH = \\sqrt{SA^2 - AH^2} = \\sqrt{\\left(%s\\right)^2 - \\left(%s\\right)^2} = %s$.\\\\
            Diện tích hình vuông là $S_{ABCD} = %s^2 = %s$.\\\\
            Vậy thể tích khối chóp $S.ABCD$ là $V = \\frac{1}{3} \\cdot SH \\cdot S_{ABCD} = \\frac{1}{3} \\cdot %s \\cdot %s = %s \\approx %s$.'''
                           %(canh_hv_latex, ah_latex, sa_latex, ah_latex, sh_latex, canh_hv_latex, s_abcd_latex, sh_latex, s_abcd_latex, v_latex, v_float_latex))

                # Gán giá trị cho kqz để tránh lỗi undefined
                kqz = v_val
                dapan='\\shortans[0]{$%s$}\n'%(str(v_float_latex).replace('.', ','))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{'+ str(tikz_hinh)+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

