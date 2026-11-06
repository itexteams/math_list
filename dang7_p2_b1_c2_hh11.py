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


def bt_dang7_p2_b1_c2_hh11(self):
            # Khai báo biến
            # B1: Nghiên cứu đề bài và Randomize
            # Chọn giá trị cụ thể cho a (ví dụ từ 2 đến 6)
            val_a = random.randint(2, 6)
            val_ab = 2 * val_a
            val_ad = val_a
            val_dc = val_a

            # Random hệ số k để tính SA = (k * a * sqrt(3)) / 3
            k = random.choice([1, 2, 3, 4, 6])

            # Tính toán giá trị SA dưới dạng số cụ thể
            # SA = (k * val_a * sqrt(3)) / 3
            tu_so = k * val_a
            mau_so = 3
            common = math.gcd(tu_so, mau_so)
            tu_rut_gon = tu_so // common
            mau_rut_gon = mau_so // common

            if mau_rut_gon == 1:
                if tu_rut_gon == 1:
                    sa_latex = r"\sqrt{3}"
                else:
                    sa_latex = r"%s\sqrt{3}" % tu_rut_gon
            else:
                sa_latex = r"\frac{%s\sqrt{3}}{%s}" % (tu_rut_gon, mau_rut_gon)

            # Tính toán các giá trị phục vụ lời giải
            # tan(SBA) = SA / AB = (k * val_a * sqrt(3) / 3) / (2 * val_a) = k * sqrt(3) / 6
            tan_sba_val = Rational(k, 6) * sqrt(3)

            # Tính góc giữa SD và BC (giá trị này không đổi theo a, chỉ phụ thuộc k)
            cos_val = 1 / (math.sqrt(2) * math.sqrt((3 + k**2) / 3))
            angle_rad = math.acos(cos_val)
            angle_deg = round(math.degrees(angle_rad), 2)

            # Nội dung câu hỏi (thay a bằng số cụ thể)
            noidungcauhoi = (r'''Cho hình chóp $S.ABCD$, có đáy $ABCD$ là hình thang vuông tại $A$ và $D$. Gọi $E$ là trung điểm của $AB$. Biết $AB=%s, AD=DC=%s$, đồng thời $SA \perp AB, SA \perp AD$ và $SA=%s$.''' 
                            % (val_ab, val_a, sa_latex))

            # Hình vẽ TikZ
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round]
            \coordinate (A) at (0,0);
            \coordinate (D) at (1.2,1.2);
            \coordinate (C) at (3.2,1.2);
            \coordinate (B) at (4,0);
            \coordinate (S) at (0,3.5);
            \coordinate (E) at (2,0);
            \draw (S)--(A)--(B)--(C)--(S)--(B);
            \draw[dashed] (S)--(D)--(C);
            \draw[dashed] (A)--(D)--(E);
            \draw[dashed] (D)--(B);
            \foreach \p in {S,A,B,C,D,E} \fill (\p);
            \node[left] at (A) {$A$};
            \node[below] at (B) {$B$};
            \node[right] at (C) {$C$};
            \node[above right] at (D) {$D$};
            \node[above] at (S) {$S$};
            \node[below] at (E) {$E$};
            \end{tikzpicture}
            \end{center}'''

            ########################################################################
            # a) Góc giữa SB và DC
            da_a_d = r'\True $(SB, DC) = \widehat{SBA}$'
            da_a_s = r'$(SB, DC) = \widehat{SDA}$'
            list_da_a = [da_a_d, da_a_s]
            sel_a = random.choice(list_da_a)
            loigiai_a = r'''Vì $ABCD$ là hình thang vuông tại $A, D$ nên $DC \parallel AB$. Khi đó góc giữa hai đường thẳng $SB$ và $DC$ bằng góc giữa $SB$ và $AB$. Do đó $(SB, DC) = \widehat{SBA}$.'''

            ########################################################################
            # b) Tan của góc SBA
            correct_tan = r'$\tan \widehat{SBA} = %s$' % latex(tan_sba_val)
            wrong_tan = r'$\tan \widehat{SBA} = \frac{\sqrt{3}}{2}$'
            da_b_d = r'\True ' + correct_tan
            da_b_s = wrong_tan if k != 3 else r'$\tan \widehat{SBA} = \frac{1}{3}$'
            list_da_b = [da_b_d, da_b_s]
            sel_b = random.choice(list_da_b)
            loigiai_b = r'''Vì $SA \perp AB$ và $SA \perp AD$ nên $SA \perp (ABCD)$, suy ra $SA \perp AB$. Xét tam giác $SAB$ vuông tại $A$, ta có $\tan \widehat{SBA} = \frac{SA}{AB} = \frac{%s}{%s} = %s$.''' % (sa_latex, val_ab, latex(tan_sba_val))

            ########################################################################
            # c) DE song song BC
            da_c_d = r'\True $DE \parallel BC$'
            da_c_s = r'$DE \perp BC$'
            list_da_c = [da_c_d, da_c_s]
            sel_c = random.choice(list_da_c)
            loigiai_c = r'''Ta có $E$ là trung điểm $AB$ nên $AE = EB = \frac{AB}{2} = %s$. Xét tứ giác $EBCD$ có $DC \parallel EB$ (vì $DC \parallel AB$) và $DC = EB = %s$. Do đó $EBCD$ là hình bình hành, suy ra $DE \parallel BC$.''' % (val_a, val_a)

            ########################################################################
            # d) Góc giữa SD và BC
            correct_angle = r'$(SD, BC) \approx %s^\circ$' % str(angle_deg).replace('.', ',')
            wrong_angle = r'$(SD, BC) \approx 52,42^\circ$'
            da_d_d = r'\True ' + correct_angle
            da_d_s = wrong_angle if abs(angle_deg - 52.42) > 0.1 else r'$(SD, BC) \approx 60,00^\circ$'
            list_da_d = [da_d_d, da_d_s]
            sel_d = random.choice(list_da_d)

            # Tính toán các cạnh cụ thể cho lời giải d
            val_de_sq = 2 * (val_a**2)
            val_sd_sq = (Rational(k**2 * val_a**2, 3)) + val_a**2
            val_se_sq = (Rational(k**2 * val_a**2, 3)) + val_a**2

            loigiai_d = r'''Vì $DE \parallel BC$ nên $(SD, BC) = (SD, DE) = \widehat{SDE}$. \\
            Ta có $AD \perp AE$, $AD=%s, AE=%s \Rightarrow DE = %s\sqrt{2}$. \\
            Tam giác $SAD$ vuông tại $A \Rightarrow SD^2 = SA^2 + AD^2 = %s + %s = %s$. \\
            Tam giác $SAE$ vuông tại $A \Rightarrow SE^2 = SA^2 + AE^2 = %s + %s = %s$. \\
            Xét tam giác $SDE$, áp dụng định lý hàm số cos: $\cos \widehat{SDE} = \frac{SD^2 + DE^2 - SE^2}{2 \cdot SD \cdot DE}$. \\
            Thay các giá trị vào ta được $\cos \widehat{SDE} = \frac{%s}{2 \cdot %s \cdot %s\sqrt{2}} \approx %s \Rightarrow \widehat{SDE} \approx %s^\circ$.''' % (
                val_a, val_a, val_a, 
                latex(Rational(k**2 * val_a**2, 3)), val_a**2, latex(val_sd_sq),
                latex(Rational(k**2 * val_a**2, 3)), val_a**2, latex(val_se_sq),
                latex(val_de_sq), latex(sqrt(val_sd_sq)), val_a, round(cos_val, 4), str(angle_deg).replace('.', ',')
            )

            # Lặp chọn bộ đáp án đảm bảo có 1-3 câu đúng
            while True:
                a_final = random.choice(list_da_a)
                b_final = random.choice(list_da_b)
                c_final = random.choice(list_da_c)
                d_final = random.choice(list_da_d)

                true_count = sum('\\True' in ans for ans in [a_final, b_final, c_final, d_final])
                if 1 <= true_count <= 3:
                    break

            # Xuất nội dung (Không dùng tiền tố r ở content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                str(hinh_ve) + '\n' +
                '\\choiceTFn \n'
                '{' + str(a_final) + '}\n'
                '{' + str(b_final) + '}\n'
                '{' + str(c_final) + '}\n'
                '{' + str(d_final) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

