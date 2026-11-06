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


def bt_dang34_p3_b2_c1_ds12(self):
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
            # 1. Sinh ngẫu nhiên các giá trị gốc cho bài toán
            # Chọn các giá trị V sao cho nghiệm tính ra đẹp
            V = random.choice([20, 22, 24, 25, 26, 27, 28, 30, 32, 34, 35, 36, 38, 40, 42, 44, 45, 46, 48, 50, 52]) # Thể tích bể
            k = random.choice([S(4) / 3, S(5)/ 3, 2, S(3)/2, S(5)/2, 3, S(7)/2, S(7)/3, S(8)/3, 4]) # Tỉ lệ chiều dài/rộng
            w_max =  3 if V < 27 else 4 if V < 36 else 5 if V < 45 else 5

            # 2. Giải bài toán dựa trên các số đã tạo
            w_opt = (V * (k + 1) / (k**2))**(1/3)

            if w_opt > w_max:
                w_final = w_max
            else:
                w_final = w_opt

            # Từ w_final, tính ra chiều cao tối ưu
            h_final = V / (k * w_final**2)
            w = symbols('w')

            # Làm tròn kết quả để đưa vào bài
            ket_qua = round(h_final, 5)

            noidungcauhoi = f"""Ông Nam cần xây dựng một bể chứa nước có dạng hình hộp chữ nhật không có nắp đậy để phục vụ cho việc tưới cây trong vườn. 
                    Do các điều kiện về diện tích vườn, ông Nam cần bể có thể tích là ${latex(V)}$ m$^3$, đáy bể có chiều dài gấp ${latex(k)}$ lần chiều rộng và chiều rộng không quá ${latex(w_max)}$ m, biết rằng chi phí vật liệu xây dựng mỗi mét vuông diện tích bề mặt là như nhau.
            Hỏi chiều cao bể nước bằng bao nhiêu để tổng chi phí vật liệu là nhỏ nhất? {round_SA(ket_qua)[0]} """
            loigiai = f"""  Gọi chiều rộng của đáy bể là $w$ (m) và chiều cao của bể là $h$ (m).  \\\\
                        Theo đề bài, chiều dài đáy bể là $l = {latex(k)}w$.
                        Điều kiện của chiều rộng là $0 < w \\le {latex(w_max)}$.  \\\\
                        Thể tích của bể là $V = l \\cdot w \\cdot h = \\left({latex(k)}w\\right) \\cdot w \\cdot h = {latex(k)}w^2h$.\\\\
                        Với $V = {V}$ m$^3$, ta có ${latex(k)}w^2h = {V} \\Rightarrow h = \\dfrac{{{V}}}{{{latex(k)}w^2}}$.  \\\\
                        Diện tích vật liệu cần dùng là tổng diện tích đáy và diện tích xung quanh:\\\\
                        $A = A_{{\\text{{đáy}}}} + A_{{xq}} = (l \\cdot w) + 2h(l+w)$\\\\
                        $A(w) = \\left({latex(k)}w \\cdot w\\right) + 2\\left(\\dfrac{{{V}}}{{{latex(k)}w^2}}\\right)\\left({latex(k)}w+w\\right)$\\\\
                        $A(w) = {latex(k)}w^2 + \\dfrac{{2V(k+1)}}{{kw}} = {latex(k)}w^2 + \\dfrac{{2 \\cdot {V} \\cdot {latex(k+1)}}}{{{latex(k)}w}}$\\\\
                        $A(w) = {latex(k)}w^2 + {latex(nsimplify(2*(V*(k+1))/(k *w)))}$  \\\\
                        Để tối ưu chi phí, ta cần tìm giá trị nhỏ nhất của hàm $A(w)$ trên khoảng $(0, {w_max}]$.\\\\
                        Ta có đạo hàm: $A'(w) = {latex(2*k)}w - {latex(nsimplify(2*(V*(k+1))/(k *w**2)))}$. \\\\
                        Giải phương trình $A'(w)=0 \\Leftrightarrow {latex(2*k)}w = {latex(nsimplify(2*(V*(k+1))/(k *w**2)))}$\\\\
                        $ \\Leftrightarrow w^3 = {latex(nsimplify(V*(k+1)/k**2))} $
                        $\\Leftrightarrow w = \\sqrt[3]{{ {latex(nsimplify(V*(k+1) / k**2))} }} \\approx {round_SA(w_opt)[1]}$ m. \\\\
                        Vì ${round_SA(w_opt)[1]} {'\\le' if w_opt <= w_max else '>'} {w_max}$ nên để tối ưu hoá chi phí thì chiều rộng của bể là $w_{{final}} \\approx {w_final:.2f}$ m.  \\\\
                        Chiều cao tương ứng là $h = \\dfrac{{{latex(V)}}}{{{latex(k)}w_{{final}}^2}} = \\dfrac{{{latex(V)}}}{{{latex(k)} \\cdot \\left({w_final:.2f}\\right)^2}} = {latex(ket_qua)} {'' if len(str(ket_qua)) < 5 else f'\\approx {round_SA(ket_qua)[1]}'}$ m.  \\\\
                        Vậy, chiều cao cần tìm là khoảng ${round_SA(ket_qua)[1]}$ m. """
            #Đáp án
            dapan='\\shortans[0]{$%s$}'%(round_SA(ket_qua)[1])              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content

