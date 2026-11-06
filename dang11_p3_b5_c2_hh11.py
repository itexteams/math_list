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


def bt_dang11_p3_b5_c2_hh11(self):
            # Khai báo biến
            def round_SA(a): 
                # Kiểm tra nếu a là số nguyên
                if a == int(a):
                    return "", int(a)

                # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                # Xác định cách làm tròn
                if len(integer_part) > 2:
                    number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng đơn vị)."
                elif len(integer_part) == 2 and len(decimal_part) > 1:
                    number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần chục)."
                elif len(decimal_part) <= 2:
                    number = str_a  # Không cần làm tròn thêm
                    cirle = ""
                else:
                    number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần trăm)."

                # Chuyển dấu chấm thành dấu phẩy (nếu có)
                return cirle, str(number).replace('.', ',')

            # ------------------------------------------------------------------------------BÀI TOÁN
            # Khởi tạo các giá trị ngẫu nhiên
            AB, SH = random.sample(
                [sqrt(2), sqrt(3), sqrt(5), sqrt(6), sqrt(8), sqrt(10), sqrt(12), sqrt(18), sqrt(20), sqrt(24), sqrt(32), sqrt(45), sqrt(50)] + list(range(1, 12)), 2)
            while SH * 3 < AB or SH > AB * 3:
                AB, SH = random.sample(
                    [sqrt(2), sqrt(3), sqrt(5), sqrt(6), sqrt(8), sqrt(10), sqrt(12), sqrt(18), sqrt(20), sqrt(24), sqrt(32), sqrt(45), sqrt(50)] + list(range(1, 12)), 2)

            A, B, C, D = random.choice([('A', 'B', 'C', 'D'), ('B', 'C', 'D', 'A'), ('C', 'D', 'A', 'B'), ('D', 'A', 'B', 'C')])
            O, H, K, N = 'O', 'H', 'K', 'N'
            mat_day, BD = random.choice([
                (f" thoi tâm ${O}$ với $\\widehat{{{A}{B}{C}}} = 60^\\circ $ và $AB = {latex(AB)}$", AB * sqrt(3)),
                (f" vuông tâm ${O}$ và $AB = {latex(AB)}$", AB * sqrt(2))
            ])
            vi_tri_H, HD, ti_le = random.choice([
                (f" trọng tâm ${H}$ của tam giác ${A}{B}{C}$", 2 * BD / 3, 1/3),
                (f" trung điểm ${H}$ của ${B}{O}$", 3 * BD / 4, 1/4),
                (f" trọng tâm ${H}$ của tam giác ${A}{D}{C}$", BD / 3, 2/3),
                (f" trung điểm ${H}$ của ${D}{O}$", BD / 4, 3/4)
            ])
            HN = simplify(SH * HD / sqrt(SH**2 + HD**2))
            tile_K = 3/4 if ti_le == 1/3 else 2/3 if ti_le == 1/4 else 3/2 if ti_le == 2/3 else 2
            SD = sqrt(SH**2 + HD**2)
            tile_N = round((HD / SD)**2, 2)
            OK = 3 * HN / 4 if f"${A}{B}{C}$" in vi_tri_H else 2 * HN / 3 if f"${B}{O}$" in vi_tri_H else 3 * HN / 2 if f"${A}{D}{C}$" in vi_tri_H else 2 * HN

            tikz_latex = f'''\\begin{{tikzpicture}}[scale=.7, >=stealth,line width=1pt,line join=round,line cap=round,font=\\footnotesize]
                \\path (0:0) coordinate ({A})
                ({-130 if ti_le < 1/2 else -105} :3) coordinate ({B})
                ({B})--++(0:7) coordinate ({C})
                ($({A})+({C})-({B})$) coordinate ({D})
                ($({B})!{ti_le}!({D})$) coordinate ({H})
                ({H}) --++(90:5) coordinate (S)
                ($({A})!1/2!({C})$) coordinate ({O})
                ($({D})!{tile_N if ti_le < 1/2 else 1/4}!(S)$) coordinate ({N})
                ($({D})!{tile_K}!({N})$) coordinate ({K}) ;
                \\draw (S) -- ({B})--({C})--({D})--cycle
                    (S)--({C})
                    pic[draw,angle radius=2mm]{{right angle={A}--{O}--{B}}}
                    pic[draw,angle radius=2mm]{{right angle=S--{H}--{B}}}
                    pic[draw,angle radius=2mm]{{right angle={H}--{N}--{D}}}
                    pic[draw,angle radius=2mm]{{right angle={O}--{K}--{D}}} ; 
                \\draw[dashed] ({B})--({D})
                ({C})--({A}) 
                (S)--({H})--({N})
                ({O})--({K})
                ({A})--({D}) ;
                \\draw[{"dashed" if ti_le < 1/2 else ""}] (S)--({A})--({B});
                \\foreach \\x/\\g in {{{A}/165,{B}/-135,{C}/-45,{D}/45,S/90,{O}/-100,{H}/-65,{N}/40,{K}/40}} \\draw[fill=black] (\\x) circle (1pt) node[shift={{(\\g:.2)}}] {{$\\x$}} ;
            \\end{{tikzpicture}}'''
            ket_qua = round_SA(OK)[1]

            noidungcauhoi = f"""Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình {mat_day}.
                    Biết rằng hình chiếu vuông góc của $S$ trên mặt phẳng $\\left( ABCD \\right)$ là {vi_tri_H} và $S{H} = {latex(SH)}$.             
                    Khoảng cách giữa hai đường thẳng ${A}{C}$ và ${S}{D}$ bằng bao nhiêu? {round_SA(OK)[0]} """
            loigiai = f""" \\immini{{ Do ${A}{C} \\perp {B}{D}$ và ${A}{C} \\perp S{H}$ nên ${A}{C} \\perp (S{B}{D})$.\\\\
                        Gọi ${K}$ là hình chiếu vuông góc của ${O}$ trên $S{D}$ thì \\text{{${O}{K} = \\mathrm{{d}}\\left({A}{C}, S{D}\\right)$}}.\\\\
                        Gọi ${N}$ là hình chiếu vuông góc của ${H}$ trên $S{D}$.\\\\
                        Ta có \\text{{${B}{D} = AB \\cdot \\sqrt{{{3 if 'thoi' in mat_day else 2}}} = {latex(BD)}$}}\\\\ 
                        và \\text{{${H}{D} = {latex(S(2)/3) if f"${A}{B}{C}$" in vi_tri_H else latex(S(1)/3) if f"${A}{D}{C}$" in vi_tri_H else latex(S(3)/4) if f"${B}{O}$" in vi_tri_H else latex(S(1)/4)}{B}{D} = {latex(HD)}$}}.\\\\
                        Khi đó ${H}{N} = \\dfrac{{{H}S \\cdot {H}{D}}}{{\\sqrt{{{H}S^2 + {H}{D}^2}}}} = {latex(HN)}$.\\\\
                        Vậy \\text{{${O}{K} = {latex(S(3)/4) if f"${A}{B}{C}$" in vi_tri_H else latex(S(3)/2) if f"${A}{D}{C}$" in vi_tri_H else latex(S(2)/3) if f"${B}{O}$" in vi_tri_H else latex(2)}{H}{N} = {latex(OK)} {f"\\approx {round_SA(OK)[1]}" if len(str(OK)) > 4 else ""}  $}}.
            }}{{{tikz_latex}}}"""
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(ket_qua))              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content

