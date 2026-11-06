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


def bt_dang17_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến và danh sách góc ngẫu nhiên cho góc CAB
            lis_goc = [30, 45, 90, 120]
            goc_alpha = random.choice(lis_goc)

            # Giả sử độ dài cạnh a = 1 để tính toán tỉ số cosin
            # Tính toán tích vô hướng AB.SC = AB.(SA + AC) = AB.SA + AB.AC
            # Vì SA = SB = AB = a nên tam giác SAB đều => góc (AB, AS) = 60 độ => góc (AB, SA) = 120 độ
            # Góc (AB, AC) = goc_alpha

            cos_120 = Rational(-1, 2)
            cos_alpha_val = simplify(cos(goc_alpha * pi / 180))

            # Tích vô hướng: AB.SC = a*a*cos(120) + a*a*cos(alpha)
            tich_vo_huong = cos_120 + cos_alpha_val
            kq_chinh_xac = abs(tich_vo_huong)

            # Chuyển sang số thập phân và làm tròn 2 chữ số
            kq_float = float(kq_chinh_xac)
            kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_decimal).replace('.', ',')

            # Tạo các phương án sai
            s = []
            while len(s) < 3:
                sai = Decimal(str(random.uniform(0.1, 0.9))).quantize(Decimal('0.02'), rounding=ROUND_HALF_UP)
                sai_str = str(sai).replace('.', ',')
                if sai_str != kq_str and sai_str not in s:
                    s.append(sai_str)

            da_d = '\\True ' + kq_str
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ cho hình chóp
            tikz_code = r"""\begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round]
            \coordinate (A) at (0,0);
            \coordinate (B) at (1.2,-1.2);
            \coordinate (C) at (4.5,0);
            \coordinate (S) at (2.2,3.5);
            \draw (S)--(A)--(B)--(C)--(S)--(B);
            \draw[dashed] (A)--(C);
            \node[left] at (A) {$A$};
            \node[below] at (B) {$B$};
            \node[right] at (C) {$C$};
            \node[above] at (S) {$S$};
            \node[left] at (1.1,1.8) {$a$};
            \node[above] at (3.5,1.7) {$a$};
            \node[above] at (2.2,0) {$a$};
            \node[below left] at (0.6,-0.6) {$a$};
            \node[below right] at (1.9,1.2) {$a$};
            \end{tikzpicture}"""

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có $SA = SB = SC = AB = AC = a$ và góc $\\widehat{CAB} = %d^\\circ$. '
                'Côsin góc tạo bởi hai đường thẳng $AB$ và $SC$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).' % goc_alpha
            )

            # Nội dung lời giải chi tiết
            val_cos_alpha_tex = latex(cos_alpha_val)
            h1=kq_decimal
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            loigiai = (
                'Ta có: $\\overrightarrow{AB} \\cdot \\overrightarrow{SC} = \\overrightarrow{AB}(\\overrightarrow{SA} + \\overrightarrow{AC}) '
                '= \\overrightarrow{AB} \\cdot \\overrightarrow{SA} + \\overrightarrow{AB} \\cdot \\overrightarrow{AC}$. \\\\'
                'Vì tam giác $SAB$ có $SA=SB=AB=a$ nên là tam giác đều, suy ra $\\widehat{SAB}=60^\\circ$. \\\\'
                'Do đó $(\\overrightarrow{AB}, \\overrightarrow{SA}) = 180^\\circ - 60^\\circ = 120^\\circ$. \\\\'
                'Ta có: $\\overrightarrow{AB} \\cdot \\overrightarrow{SA} + \\overrightarrow{AB} \\cdot \\overrightarrow{AC} = '
                'a \\cdot a \\cdot \\cos 120^\\circ + a \\cdot a \\cdot \\cos %d^\\circ$. \\\\'
                '$\\Rightarrow \\overrightarrow{AB} \\cdot \\overrightarrow{SC} = -\\frac{a^2}{2} + %s a^2$. \\\\'
                'Do đó: $\\cos(AB, SC) = \\frac{|\\overrightarrow{AB} \\cdot \\overrightarrow{SC}|}{AB \\cdot SC} = '
                '\\frac{|-\\frac{1}{2} + %s|}{1} \\approx %s$.'
                % (goc_alpha, val_cos_alpha_tex, val_cos_alpha_tex, str(kqz))
            )

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\begin{center}\n'
                + tikz_code + '\n'
                '\\end{center}\n'+str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

