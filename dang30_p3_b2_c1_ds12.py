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


def bt_dang30_p3_b2_c1_ds12(self):
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
            r = symbols('r')
            r_opt = 3 * random.choice(list(range(7, 16)))

            # Chọn chi phí sơn và tỉ lệ
            k = random.randint(15, 24) 
            cost_s = random.randint(15, 26)
            cost_c = 12 * cost_s / k
            while cost_c != int(cost_c):
                k = random.randint(15, 24) 
                cost_s = random.randint(15, 26)
                cost_c = 12 * cost_s / k
            cost_c = round(cost_c * 1000)
            cost_s = round(cost_s * 1000)

            # Từ r_opt và chi phí, tính ngược ra Thể tích V/pi để V/pi là số nguyên
            # Công thức gốc: r^3 = (3 * cost_c * V_pi) / (4 * (3*cost_s - 2*cost_c))
            V_pi = (4 * r_opt**3 * (3*cost_s - 2*cost_c)) / (3 * cost_c)
            V_pi = round(V_pi)

            r_max = round(r_opt * 1.3) # Giới hạn bán kính
            hamf = (4*cost_s - S(8*cost_c)/3) * r**2 + (2*cost_c*V_pi)/r
            tikz_code = f"""\\begin{{tikzpicture}}[scale=0.7, every node/.style={{scale=0.9}},line width=1pt]
            \\def\\Radius{{2}} 
            \\def\\Length{{6}} 
            \\shade[bottom color=gray!20!white, opacity=1] 
            (-\\Length/2, -\\Radius) --(\\Length/2, -\\Radius) arc (-90:90:\\Radius) -- 
            (-\\Length/2, \\Radius) arc (90:270:\\Radius)--cycle;
            \\draw[gray!20!white] (-\\Length/2,-\\Radius) arc (270:90:{{.7}} and {{\\Radius}})  ;
            \\draw[gray!80!white] (-\\Length/2,-\\Radius) arc (-90:90:{{.7}} and {{\\Radius}})  ;
            \\draw[gray!20!white] (\\Length/2,-\\Radius) arc (270:90:{{.7}} and {{\\Radius}})   ;
            \\draw[gray!80!white] (\\Length/2,-\\Radius) arc (-90:90:{{.7}} and {{\\Radius}})   ;
            \\draw[gray] 
            (-\\Length/2, -\\Radius) --(\\Length/2, -\\Radius) arc (-90:90:\\Radius) -- 
            (-\\Length/2, \\Radius) arc (90:270:\\Radius)--cycle;
            \\draw[<->, thick, red] (-\\Length/2, \\Radius+0.6) -- (\\Length/2, \\Radius+0.6) node[midway, above] {{$h$}};
            \\draw[->, thick, blue] (-\\Length/2, 0) -- (-\\Length/2, \\Radius) node[midway, right] {{$r$}};
            \\fill[blue] (-\\Length/2, 0) circle (3pt);
            \\draw[red,thick] (-\\Length/2,\\Radius)--(-\\Length/2,1+\\Radius)
            (\\Length/2,\\Radius)--(\\Length/2,1+\\Radius);
            \\end{{tikzpicture}}"""

            # 2. Giải bài toán (kiểm tra lại để chắc chắn)
            # Các bước này để xác nhận lại logic, kết quả chính là r_opt
            ket_qua = r_opt

            noidungcauhoi = f"""\\immini{{  Một thùng chứa nhiên liệu gồm phần ở giữa là một hình trụ có chiều dài $h$ mét ($h > 0$) và hai đầu là các nửa hình cầu bán kính $r$ ($r > 0$).
                    Biết rằng thể tích của thùng chứa là ${V_pi}\\pi$ m$^3$.
                    Để sơn mặt ngoài của phần hình cầu cần ${cost_s}$ đồng cho 1 m$^2$, còn sơn mặt ngoài cho phần hình trụ cần ${cost_c}$ đồng cho 1 m$^2$.
            Bán kính r bằng bao nhiêu để chi phí cho việc sơn diện tích mặt ngoài thùng chứa (bao gồm diện tích xung quanh hình trụ và diện tích hai nửa hình cầu) là nhỏ nhất? Biết rằng bán kính $r$ không được vượt quá {r_max} m. {round_SA(ket_qua)[0]} 
            }}{{{tikz_code}}}"""
            loigiai = f"""  Gọi $r$ là bán kính của hai nửa hình cầu và $h$ là chiều dài phần hình trụ. \\\\
                        - Thể tích khối trụ: $V_{{\\text{{trụ}}}} = \\pi r^2 h$.\\\\
                        - Thể tích hai nửa hình cầu (một hình cầu): $V_{{\\text{{cầu}}}} = \\dfrac{{4}}{{3}}\\pi r^3$.\\\\
                        - Tổng thể tích: $V = V_{{\\text{{trụ}}}} + V_{{\\text{{cầu}}}} = \\pi r^2 h + \\dfrac{{4}}{{3}}\\pi r^3$.  \\\\
                        Theo đề bài, ta có $V = {V_pi}\\pi \\Leftrightarrow \\pi r^2 h + \\dfrac{{4}}{{3}}\\pi r^3 = {V_pi}\\pi \\Leftrightarrow r^2 h + \\dfrac{{4}}{{3}}r^3 = {V_pi}$.\\\\
                        Suy ra: $h = \\dfrac{{{V_pi}}}{{r^2}} - \\dfrac{{4}}{{3}}r$. $\\left(\\text{{Vì }} h>0 \\text{{ nên }} r < \\sqrt[3]{{{latex(S(3*V_pi)/4)}}}\\right)$. \\\\
                        Chi phí sơn thùng chứa được tính bằng tổng chi phí sơn phần cầu và phần trụ:\\\\
                        - Diện tích mặt cầu: $A_{{\\text{{cầu}}}} = 4\\pi r^2$.\\\\
                        - Diện tích xung quanh mặt trụ: $A_{{\\text{{xq trụ}}}} = 2\\pi r h$.            \\\\
                        Hàm tổng chi phí theo $r$:
                        $C(r) = {cost_s} \\cdot A_{{\\text{{cầu}}}} + {cost_c} \\cdot A_{{\\text{{xq trụ}}}} = {cost_s}\\cdot 4\\pi r^2 + {cost_c}\\cdot 2\\pi r h$.  \\\\
                        Thay $h = \\dfrac{{{V_pi}}}{{r^2}} - \\dfrac{{4}}{{3}}r$ vào biểu thức chi phí:\\\\
                        $C(r) = {latex(cost_s)}\\cdot 4\\pi r^2 + {latex(cost_c)}\\cdot 2\\pi r \\left( \\dfrac{{{V_pi}}}{{r^2}} - \\dfrac{{4}}{{3}}r \\right) $\\\\
                        $C(r) = {4*cost_s}\\pi r^2 + \\dfrac{{2\\pi {cost_c} {V_pi}}}{{r}} - \\dfrac{{8\\pi {cost_c}}}{{3}}r^2$\\\\
                        $C(r) = \\pi \\left[ {latex(nsimplify(4*cost_s - S(8*cost_c)/3))} \\cdot r^2 + \\dfrac{{{latex(2*cost_c* V_pi)}}}{{r}} \\right]$. \\\\
                        Để chi phí $C(r)$ nhỏ nhất, ta cần tìm giá trị nhỏ nhất của hàm số $f(r) = {latex(hamf)} $ trên nửa khoảng $(0, {r_max}]$.   \\\\
                        Ta có đạo hàm: $f'(r) = {latex(nsimplify(diff(hamf, r)))} $.  \\\\
                        Giải phương trình $f'(r)=0 \\Leftrightarrow r = {r_opt}$.  \\\\
                        Giá trị $r={r_opt}$ nằm trong khoảng cho phép $(0, {r_max}]$ nên đây là giá trị cần tìm để chi phí là nhỏ nhất.  """
            #Đáp án
            dapan=' \\shortans[0]{$%s$}'%(round_SA(ket_qua)[1])              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content

