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


def bt_dang55_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập thông số ngẫu nhiên
            # Ta sẽ random hệ số 'k' cho cạnh hình vuông 4ka
            k = random.randint(1, 4)
            side = 4 * k # Cạnh hình vuông ABCD là 4ka

            # Các đại lượng tính theo a (coi a = 1 để tính toán)
            ah = k
            bh = 3 * k
            ak = 3 * k
            kd = k

            # SH vuông góc đáy, góc SBH = 30 độ
            # SH = BH * tan(30) = 3k * sqrt(3)/3 = k*sqrt(3)
            sh_val = k * sqrt(3)

            # Tính toán các đoạn thẳng trong mặt đáy (ABCD)
            # CH = sqrt(BC^2 + BH^2) = sqrt((4k)^2 + (3k)^2) = 5k
            ch_val = 5 * k
            # Tam giác HBC vuông tại B, BE là đường cao (do CH vuông BK tại E)
            # HE = BH^2 / CH = (3k)^2 / 5k = 9k/5
            he_val = Rational(9 * k, 5)
            # BE = (BH * BC) / CH = (3k * 4k) / 5k = 12k/5
            be_val = Rational(12 * k, 5)

            # Tính SE, SI, EI (I là hình chiếu của E lên AB)
            # SE = sqrt(SH^2 + HE^2)
            se_sq = sh_val**2 + he_val**2
            se_val = simplify(sqrt(se_sq))

            # Trong tam giác HBE vuông tại E, EI là đường cao
            # HI = HE^2 / HB = (9k/5)^2 / 3k = 27k/25
            hi_val = Rational(27 * k, 25)
            # EI = (HE * BE) / HB = (9k/5 * 12k/5) / 3k = 36k/25
            ei_val = Rational(36 * k, 25)

            # SI = sqrt(SH^2 + HI^2)
            si_sq = sh_val**2 + hi_val**2
            si_val = simplify(sqrt(si_sq))

            # Áp dụng định lý cosin trong tam giác SEI để tìm cos(SE, EI)
            # cos_sei = (SE^2 + EI^2 - SI^2) / (2 * SE * EI)
            num = se_sq + ei_val**2 - si_sq
            den = 2 * se_val * ei_val
            cos_val = simplify(num / den)

            # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
            def generate_wrong_answers(correct):
                wrong = []
                while len(wrong) < 3:
                    # Tạo biến thể bằng cách thay đổi tử số hoặc mẫu số
                    factor = random.choice([Rational(1, 2), Rational(2, 3), Rational(4, 3), 2])
                    w = simplify(correct * factor)
                    if w != correct and w not in wrong:
                        wrong.append(w)
                return wrong

            wrong_ans = generate_wrong_answers(cos_val)

            # Định dạng LaTeX cho các kết quả
            def to_latex(expr):
                return latex(expr)

            # Nội dung bài toán
            noidungcauhoi = ('''Cho hình vuông $ABCD$ cạnh $%sa$, lấy $H, K$ lần lượt trên các cạnh $AB, AD$ sao cho $BH = 3HA, AK = 3KD$. Trên đường thẳng vuông góc với mặt phẳng $(ABCD)$ tại $H$ lấy điểm $S$ sao cho $\\widehat{SBH} = 30^\\circ$. Gọi $E$ là giao điểm của $CH$ và $BK$. Cosin của góc giữa hai đường thẳng $SE$ và $BC$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).''' 
                             % (side if side != 1 else ""))

            # Hình vẽ TikZ
            tikz_code = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (0,2);
                \coordinate (D) at (-1.5,0);
                \coordinate (B) at (5,2);
                \coordinate (C) at (3.5,0);
                \coordinate (H) at ($(A)!0.25!(B)$);
                \coordinate (K) at ($(A)!0.75!(D)$);
                \coordinate (S) at ($(H)+(0,4)$);
                \coordinate (E) at (intersection of C--H and B--K);
                \coordinate (I) at ($(A)!(E)!(B)$);
                \draw[dashed] (S)--(A) (A)--(B) (A)--(D) (H)--(C) (B)--(K) (S)--(H) (S)--(E) (E)--(I) (S)--(I) (D)--(K);
                \draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) ;
                \fill [red] (A) node[left] {$A$};
                \fill [red] (B) node[right] {$B$};
                \fill [red] (C) node[below right] {$C$};
                \fill [red] (D) node[below left] {$D$};
                \fill [red] (S) node[above] {$S$};
                \fill [red] (H) node[above] {$H$};
                \fill [red] (K) node[left] {$K$};
                \fill [red] (E) node[below] {$E$};
                \fill [red] (I) node[above] {$I$};
            \end{tikzpicture}
            \end{center}'''

            # Lời giải chi tiết
            h1=cos_val
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            loigiai = ('''Gọi $I$ là hình chiếu vuông góc của $E$ lên $AB$. \\\\
            Ta có $\\triangle ABK = \\triangle BCH$ (c.g.c) vì $AB=BC, AK=BH, \\widehat{A}=\\widehat{B}=90^\\circ$. \\\\
            $\\Rightarrow \\widehat{ABK} = \\widehat{BCH}$. Mà $\\widehat{ABK} + \\widehat{KBC} = 90^\\circ \\Rightarrow \\widehat{BCH} + \\widehat{KBC} = 90^\\circ \\Rightarrow \\widehat{BEC} = 90^\\circ$. \\\\
            Vậy $CH \\perp BK$ tại $E$. \\\\
            Do $BC \\parallel AD$ và $I$ là hình chiếu của $E$ lên $AB$ nên $EI \\parallel BC$. \\\\
            Khi đó $\\cos(SE; BC) = \\cos(SE; EI) = |\\cos \\widehat{SEI}|$. \\\\
            Tính toán các giá trị: \\\\
            $BH = \\frac{3}{4} AB = %sa$. \\\\
            $SH = BH \\cdot \\tan 30^\\circ = %sa \\cdot \\frac{\\sqrt{3}}{3} = %sa$. \\\\
            Trong tam giác $BCH$ vuông tại $B$, $BE$ là đường cao: \\\\
            $HC = \\sqrt{BC^2 + BH^2} = %sa$. \\\\
            $HE = \\frac{BH^2}{HC} = \\frac{(%sa)^2}{%sa} = %sa$. \\\\
            $SE = \\sqrt{SH^2 + HE^2} = \\sqrt{(%sa)^2 + (%sa)^2} = %s$. \\\\
            Trong tam giác $HBE$ vuông tại $E$, $EI$ là đường cao: \\\\
            $HI = \\frac{HE^2}{HB} = %s$. \\\\
            $EI = \\frac{HE \\cdot BE}{HB} = %s$. \\\\
            $SI = \\sqrt{SH^2 + HI^2} = %s$. \\\\
            Áp dụng định lý cosin cho tam giác $SEI$: \\\\
            $\\cos \\widehat{SEI} = \\frac{SE^2 + EI^2 - SI^2}{2 \\cdot SE \\cdot EI} = %s \\approx %s$.''' 
                       % (to_latex(bh), to_latex(bh), to_latex(sh_val), 
                          to_latex(side), to_latex(bh), to_latex(side), to_latex(he_val),
                          to_latex(sh_val), to_latex(he_val), to_latex(se_val),
                          to_latex(hi_val), to_latex(ei_val), to_latex(si_val), to_latex(cos_val),str(kqz)))

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất câu trắc nghiệm
            da_d = '\\True $' + to_latex(cos_val) + '$'
            list_1 = [da_d] + ['$' + to_latex(w) + '$' for w in wrong_ans]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{'+ tikz_code +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

